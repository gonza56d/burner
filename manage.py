"""
Handle scripts with execution command lines.
"""

# Python
from enum import Enum
import sys

# App
from app.utils.exceptions import CommandExecutionException
from app.pages import FalabellaPage, SodimacPage


class SubCommand:

    HELP_COMMAND = '--help'

    class Pages(Enum):
        FALABELLA = 'falabella'
        SODIMAC = 'sodimac'

    class Tasks(Enum):
        COLLECTCATEGORIES = 'collectcategories'
        COLLECTPRODUCTS = 'collectproducts'

    @staticmethod
    def page_to_class(page: str) -> str:
        return page.title() + 'Page'

    def __init__(self, argv) -> None:
        SubCommand.check_if_called_help(argv)
        try:
            self.page = argv[1]
            self.task = argv[2]
        except IndexError:
            raise CommandExecutionException(
                f'Usage: manage.py $PAGE $TASK | ' +
                'See manage.py {SubCommand.HELP_COMMAND}'
            )

        if self.page.upper() not in SubCommand.Pages.__members__:
            raise CommandExecutionException(
                f'Page not found, options: {SubCommand.get_pages_pretty()}'
            )

        if self.task.upper() not in SubCommand.Tasks.__members__:
            raise CommandExecutionException(
                f'Task not found, options: {SubCommand.get_tasks_pretty()}'
            )

    @classmethod
    def check_if_called_help(cls, argv):
        try:
            if argv[2] is cls.HELP_COMMAND:
                print('Usage: python3 manage.py $PAGE $TASK')
                print(f'$PAGE options: {cls.get_pages_pretty}')
                print(f'$TASK options: {cls.get_tasks_pretty}')
        except IndexError:
            pass

    @classmethod
    def get_pages_pretty(cls) -> str:
        return f'{[member.value for member in cls.Pages]}'

    @classmethod
    def get_tasks_pretty(cls) -> str:
        return f'{[member.value for member in cls.Tasks]}'


def main():
    sub_command = SubCommand(sys.argv)
    page = SubCommand.page_to_class(sub_command.page)
    method = ''
    if sub_command.task.lower() == SubCommand.Tasks.COLLECTCATEGORIES.value:
        method = 'store_categories()'
    elif sub_command.task.lower() == SubCommand.Tasks.COLLECTPRODUCTS.value:
        method = 'store_products()'
    eval(f'{page}().{method}')

if __name__ == '__main__':
    main()
