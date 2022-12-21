import json

from ontobot.services.subkind import Subkind
from ontobot.services.factory import ODPFactory
from flask import Flask, jsonify, request

from ontobot.model.expense import Expense, ExpenseSchema
from ontobot.model.income import Income, IncomeSchema
from ontobot.model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]


data = {
    "taxonomies": [
        {
            "name": "Organization",
            "stereotype": "kind",
            "subclasses": [
                {
                    "name": "School",
                    "stereotype": "subkind"
                }
            ]
        },
        {
            "name": "Person",
            "stereotype": "kind",
            "disjoint": [["Child", "Teen", "Adult"], ["Man", "Women"]],
            "subclasses": [
                {
                    "name": "Child",
                    "stereotype": "phase"
                },
                {
                    "name": "Teen",
                    "stereotype": "phase"
                },
                {
                    "name": "Adult",
                    "stereotype": "phase"
                },
                {
                    "name": "Student",
                    "stereotype": "role"
                },
                {
                    "name": "Man",
                    "stereotype": "subkind",
                    "subclasses": [
                        {
                            "name": "Husband",
                            "stereotype": "role"
                        }
                    ]
                },
                {
                    "name": "Women",
                    "stereotype": "subkind",
                    "subclasses": [
                        {
                            "name": "Wife",
                            "stereotype": "role"
                        }
                    ]
                }
            ]
        }

    ]
}

newb = []


@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return "", 204


@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 204


# ONTO --------------------------------
@app.route('/onto')
def get_ontos():
    # parsed_json = json.loads(data)
    sk: Subkind = ODPFactory.get_ontouml_odp(
        'subkind', data)
    sk.check_subkind()
    return jsonify(sk.get_subkind_list())

    # schema = ExpenseSchema(many=True)
    # expenses = schema.dump(
    #     filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    # )
    # return jsonify(expenses)

@app.route('/onto', methods=['POST'])
def add_ontos():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 204

if __name__ == "__main__":
    app.run()
