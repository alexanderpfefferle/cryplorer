from cryplorer_eth_backend import *

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/eth/address/<address>')
def use_eth_template(address):
    address=Web3.toChecksumAddress(address)
    accinfo, transactions = get_eth_acc_info(address)
    return render_template('template_eth_address.html', address=address, transactions=transactions, accinfo=accinfo)

app.run(debug=True)