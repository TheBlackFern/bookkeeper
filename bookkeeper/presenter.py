from bookkeeper.view.app import MainWindow
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from bookkeeper.models.budget import Budget
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category

if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = MainWindow()
    db_name = "databases/sql.db"
    cat_repo = SQLiteRepository[Category](db_name, Category)
    exp_repo = SQLiteRepository[Expense](db_name, Expense)
    budget_repo = BudgetTable(DB_NAME, Budget)
    window = ExpensePresenter(model, view, cat_repo, exp_repo, budget_repo)
    window.show()
    app.exec()
