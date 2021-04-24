"""
Handle scripts with execution command lines.
"""

# Python
from enum import Enum
import sys
from typing import List

# AsyncIO
import asyncio

# App
from pages import FalabellaPage, SodimacPage
from utils.exceptions import CommandExecutionException


class SubCommand:
    """
    Handle subcommands logic.
    """

    USAGE = " * Usage: manage.py --pages='$PAGE_1 $PAGE_2 $PAGE_N' --tasks='$TASK_1 $TASK_2 $TASK_N'"
    HELP_COMMAND = '-help'

    class Pages(Enum):
        """
        Pages options to execute tasks from.
        """
        FALABELLA = 'falabella'
        SODIMAC = 'sodimac'

    class Tasks(Enum):
        """
        Available tasks to execute from any page. 
        """
        COLLECTCATEGORIES = 'collectcategories'
        COLLECTPRODUCTS = 'collectproducts'

    @staticmethod
    def tasks_to_page_methods(tasks: List[str]) -> List[str]:
        """
        Convert tasks passed as subcommand into the corresponding
        page method name.
        """
        page_methods = []
        for task in tasks:
            if task.lower() == SubCommand.Tasks.COLLECTCATEGORIES.value:
                page_methods.append('store_categories()')
            elif task.lower() == SubCommand.Tasks.COLLECTPRODUCTS.value:
                page_methods.append('store_products()')
        return page_methods

    @staticmethod
    def pages_to_page_objects(pages: List[str]) -> List[str]:
        """
        Convert pages passed as subcommand into the corresponding
        page object name.
        """
        return [page.title() + 'Page' for page in pages]

    def __init__(self, argv: List[str]) -> None:
        self.called_help = SubCommand.check_if_called_help(argv)
        if self.called_help:
            return
        self.pages = None
        self.tasks = None
        arguments = self.validate_arguments(argv)
        self.get_pages_and_tasks(arguments)
        if self.pages is None or self.tasks is None:
            self.throw_common_exception()
        self.validate_data()

    def validate_arguments(self, argv: List[str]) -> str:
        """
        Validate that all the parts of the command are present and return them
        in a single string to handle later in get_pages_and_tasks().
        """
        try:
            first_arg = argv[1]
            second_arg = argv[2]
        except IndexError:
            self.throw_common_exception()
        return first_arg + second_arg

    def validate_data(self) -> None:
        """
        Validate that pages and tasks sent as subcommands are valid.
        """
        for page in self.pages:
            if page.upper() not in SubCommand.Pages.__members__:
                raise CommandExecutionException(
                    f'Page {page} not found, options: '
                    f'{SubCommand.get_pages_pretty()}'
                )
        for task in self.tasks:
            if task.upper() not in SubCommand.Tasks.__members__:
                raise CommandExecutionException(
                    f'Task {task} not found, options: '
                    f'{SubCommand.get_tasks_pretty()}'
                )

    def throw_common_exception(self):
        raise CommandExecutionException(
            f"\n{self.USAGE}\n"
            f" * Heads up: Each page is executed asynchronously, running their sent tasks in order.\n"
            f" * See manage.py {self.HELP_COMMAND}"
        )

    def get_pages_and_tasks(self, arguments: str) -> None:
        """
        Handle commandline to compose the pages and tasks intended to run.
        """
        splitted = arguments.split('--')
        for val in splitted:
            if val.startswith('pages='):
                self.pages = val.replace('pages=', '').strip().split(' ')
            if val.startswith('tasks='):
                self.tasks = val.replace('tasks=', '').strip().split(' ')

    @classmethod
    def check_if_called_help(cls, argv: List[str]) -> bool:
        """
        Check if user called help command and print instructions if true.
        """
        try:
            if argv[1] == cls.HELP_COMMAND:
                print(
                    f'{cls.USAGE}\n'
                    f'--pages options: {cls.get_pages_pretty()}\n'
                    f'--tasks options: {cls.get_tasks_pretty()}'
                )
                return True
        except IndexError:
            pass
        return False

    @classmethod
    def get_pages_pretty(cls) -> str:
        return f'{[member.value for member in cls.Pages]}'

    @classmethod
    def get_tasks_pretty(cls) -> str:
        return f'{[member.value for member in cls.Tasks]}'


async def run(pages: List[str], methods: List[str]) -> None:
    """
    Execute pages asynchronously with their own tasks in the order sent by user.
    """
    for method in methods:
        thread_run = []
        for page in pages:
            thread_run.append(f'{page}().{method}')
        await asyncio.gather(*[eval(_run) for _run in thread_run])


async def main() -> None:
    """
    Handle how to execute tasks from command line.
    """

    sub_command = SubCommand(sys.argv)
    if sub_command.called_help:
        return
    pages = SubCommand.pages_to_page_objects(sub_command.pages)
    methods = SubCommand.tasks_to_page_methods(sub_command.tasks)
    await run(pages, methods)


if __name__ == '__main__':
    asyncio.run(main())
