"""
Handle scripts with execution command lines.
"""

# Python
from enum import Enum
from multiprocessing import Process
import sys
from typing import List

# App
from pages import FalabellaPage, SodimacPage
from utils.decorators import timer
from utils.exceptions import CommandExecutionException


class SubCommand:
    """Handle subcommands logic.
    """

    USAGE = " * Usage: manage.py --pages='$PAGE_1 $PAGE_2 $PAGE_N' --tasks='$TASK_1 $TASK_2 $TASK_N'"
    HELP_COMMAND = '-help'

    class Pages(Enum):
        """Enum with pages options to execute tasks from.
        """
        FALABELLA = 'falabella'
        SODIMAC = 'sodimac'

    class Tasks(Enum):
        """Enum with available tasks to execute from any page. 
        """
        COLLECTCATEGORIES = 'collectcategories'
        COLLECTPRODUCTS = 'collectproducts'

    @staticmethod
    def tasks_to_page_methods(tasks: List[str]) -> List[str]:
        """Convert tasks passed as subcommand into the corresponding
        page method name.

        Parameters
        ----------
        tasks : List[str]
            Tasks to convert to the corresponding page method expression.
        
        Return
        ------
        List[str] : Collection of method expressions.
        """

        return [
            'store_products' if task.lower() == SubCommand.Tasks.COLLECTPRODUCTS.value
            else
            'store_categories' if task.lower() == SubCommand.Tasks.COLLECTCATEGORIES.value
            else None
            for task in tasks
        ]

    @staticmethod
    def pages_to_page_objects(pages: List[str]) -> List[str]:
        """Convert pages passed as subcommand into the corresponding
        page object name.

        Parameters
        ----------
        pages : List[str]
            Pages to convert to the corresponding page class expression.

        Return
        ------
        List[str] : Collection of page class expressions.
        """
        return [page.title() + 'Page' for page in pages]

    def __init__(self, argv: List[str]) -> None:
        """Constructor.

        Parameters
        ----------
        argv : List[str]
            Command line arguments.
        """
        self.called_help = SubCommand.check_if_called_help(argv)
        if self.called_help:
            return
        self.pages = None
        self.tasks = None
        arguments = self.validate_arguments(argv)
        self.set_pages_and_tasks(arguments)
        if self.pages is None or self.tasks is None:
            self.throw_common_exception()
        self.validate_data()

    def validate_arguments(self, argv: List[str]) -> str:
        """Validate that all the parts of the command are present and return
        them concatenated in a single string to handle later in set_pages_and_tasks().

        Parameters
        ----------
        argv : List[str]
            Command line arguments.
        
        Return
        ------
        str : Concatenated argv values.
        """
        try:
            first_arg = argv[1]
            second_arg = argv[2]
        except IndexError:
            self.throw_common_exception()
        return first_arg + second_arg

    def validate_data(self) -> None:
        """Validate that pages and tasks sent as subcommands are valid.
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
        """Raise a common exception when command was sent with an error.
        """
        raise CommandExecutionException(
            f"\n{self.USAGE}\n"
            f" * Heads up: Each page is executed asynchronously, running their sent tasks in order.\n"
            f" * See manage.py {self.HELP_COMMAND}"
        )

    def set_pages_and_tasks(self, arguments: str) -> None:
        """Handle arguments to compose the pages and tasks intended to run.

        Parameters
        ----------
        arguments : str
            Options sent in the command line.
        """
        splitted = arguments.split('--')
        for val in splitted:
            if val.startswith('pages='):
                self.pages = val.replace('pages=', '').strip().split(' ')
            if val.startswith('tasks='):
                self.tasks = val.replace('tasks=', '').strip().split(' ')

    @classmethod
    def check_if_called_help(cls, argv: List[str]) -> bool:
        """Check if user called help command and print instructions if true.

        Parameters
        ----------
        argv : List[str]
            Options sent in the command line to check if help was called.

        Return
        ------
        bool : True if help command has been sent.
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


@timer
def run(pages: List[str], methods: List[str]) -> None:
    """Execute pages with their own tasks in the order sent by user.

    Parameters
    ----------
    pages : List[str]
        Expressions of page classes to execute tasks from.

    methods : List[str]
        Expressions of page methods to run.
    """
    for method in methods:
        if method:
            this_iteration = []
            for page in pages:
                this_iteration.append(f'{page}().{method}')  # E.G. FalabellaPage().store_products
            processes = []
            for process in this_iteration:  # Gather the results in a List[Process]
                processes.append(Process(target=eval(process)))
            for process in processes:
                process.start()
            for process in processes:
                process.join()


def main() -> None:
    """Handle how to execute tasks from command line.
    """

    sub_command = SubCommand(sys.argv)
    if sub_command.called_help:
        return
    pages = SubCommand.pages_to_page_objects(sub_command.pages)
    methods = SubCommand.tasks_to_page_methods(sub_command.tasks)
    run(pages, methods)


if __name__ == '__main__':
    main()
