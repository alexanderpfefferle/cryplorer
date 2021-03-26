from cryplorer_eth_backend import *

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def use_template():
    net_info = get_net_info()
    return render_template('main.html', net_info=net_info)

@app.route('/eth/address/<address>')
def use_eth_template(address):
    address=Web3.toChecksumAddress(address)
    accinfo, transactions = get_eth_acc_info(address)
    return render_template('template_eth_address.html', address=address, transactions=transactions, accinfo=accinfo)

@app.route('/eth/tx/<tx_hash>')
def use_eth_tx_template(tx_hash):
    exists, tx_info = get_eth_tx_info(tx_hash)
    if exists:
        return render_template('template_eth_tx.html', tx_hash=tx_hash, tx_info=tx_info)
    else:
        return redirect('/')

app.run(debug=True)