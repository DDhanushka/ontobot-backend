import json
from flask import Flask, jsonify, request

from ontobot.services.subkind import Subkind
from ontobot.services.factory import ODPFactory
from ontobot.services.owl import OWL

from ontobot.model.expense import Expense, ExpenseSchema
from ontobot.model.income import Income, IncomeSchema
from ontobot.model.transaction_type import TransactionType

app = Flask(__name__)

# transactions = [
#     Income('Salary', 5000),
#     Income('Dividends', 200),
#     Expense('pizza', 50),
#     Expense('Rock Concert', 100)
# ]

data = {}

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
    owl_res = OWL(data)
    # print(owl_res.get_taxonomy_json())
    return jsonify(owl_res.get_taxonomy_json())


@app.route('/onto', methods=['POST'])
def add_ontos():
    global data
    data = request.get_json()
    return "", 204


if __name__ == "__main__":
    app.run()