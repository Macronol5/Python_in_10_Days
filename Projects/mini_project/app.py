from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy data for bank accounts
accounts = []

class Account:
    def __init__(self, account_number, customer_name, balance):
        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_customer_name(self):
        return self._customer_name

    def set_customer_name(self, customer_name):
        self._customer_name = customer_name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        account_number = request.form['account_number']
        customer_name = request.form['customer_name']
        balance = float(request.form['balance'])
        account = Account(account_number, customer_name, balance)
        accounts.append(account)
        return redirect('/view_customers')
    return render_template('create_account.html')

@app.route('/perform_transaction', methods=['GET', 'POST'])
def perform_transaction():
    if request.method == 'POST':
        account_number = request.form['account_number']
        amount = float(request.form['amount'])
        transaction_type = request.form['transaction_type']
        for account in accounts:
            if account.get_account_number() == account_number:
                if transaction_type == 'Deposit':
                    account.set_balance(account.get_balance() + amount)
                else:
                    account.set_balance(account.get_balance() - amount)
                return redirect('/view_customers')
        return redirect('/view_customers')
    return render_template('perform_transaction.html')

@app.route('/update_account', methods=['GET', 'POST'])
def update_account():
    if request.method == 'POST':
        account_number = request.form['account_number']
        customer_name = request.form['customer_name']
        balance = float(request.form['balance'])
        for account in accounts:
            if account.get_account_number() == account_number:
                account.set_customer_name(customer_name)
                account.set_balance(balance)
                return redirect('/view_customers')
        return redirect('/view_customers')
    return render_template('update_account.html')

@app.route('/delete_account', methods=['GET', 'POST'])
def delete_account():
    if request.method == 'POST':
        account_number = request.form['account_number']
        for account in accounts:
            if account.get_account_number() == account_number:
                accounts.remove(account)
                return redirect('/view_customers')
        return redirect('/view_customers')
    return render_template('delete_account.html')

@app.route('/search_account', methods=['GET', 'POST'])
def search_account():
    if request.method == 'POST':
        account_number = request.form['account_number']
        for account in accounts:
            if account.get_account_number() == account_number:
                return render_template('search_account.html', account=account)
        return redirect('/view_customers')
    return render_template('search_account.html')

@app.route('/view_customers')
def view_customers():
    return render_template('view_customers.html', accounts=accounts)

@app.route('/exit')
def exit_system():
    return 'Thank you for using our banking system. Goodbye!'

if __name__ == '__main__':
    app.run()