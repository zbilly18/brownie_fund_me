from brownie import FundMe
from scripts.helpful_scripts import get_account
import scripts.deploy


def fund():
    fund_me =   FundMe[-1]# scripts.deploy.deploy_fund_me()
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value" : entrance_fee})

def withdraw():
    fund_me = FundMe[-1] #scripts.deploy.deploy_fund_me()
    account = get_account()
    fund_me.withdraw({"from": account})



def main():
    fund()
    withdraw()
    