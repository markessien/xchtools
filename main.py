import os
import subprocess

from airdrop import airdrop
from splitcoins import splitcoins
from argparse import ArgumentParser

from dotenv import load_dotenv

load_dotenv()

CHIA_EXE = os.getenv('CHIA_EXE')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("command", type=str,
                    help="the command you want to run. info or split-coins")

    parser.add_argument("-d", "--destination", dest="destination",
                        help="destination address")

    parser.add_argument("-s", "--source",
                        help="the source file to read from")

    parser.add_argument("-a", "--amount",
                        help="amount for each coin")

    parser.add_argument("-m", "--memo",
                        help="memo for the send (optional)")

    parser.add_argument("-f", "--fee",
                        help="fee for the send (optional)")

    parser.add_argument("-i", "--iterations",
                        help="number of times to iterate the send")

    parser.add_argument("-w", "--wallet",
                        help="the wallet you want to send from. Get list of wallets using the 'wallet' command")

    parser.add_argument("--start",
                        help="what position should airdrop start")

    parser.add_argument("--stop",
                        help="what position should airdrop stop")


    args = parser.parse_args()

    if args.command == "info":
        process = subprocess.run([CHIA_EXE, "version"], stdout=subprocess.PIPE, universal_newlines=True)
        print(process.stdout)

    if args.command == "wallets":
        process = subprocess.run([CHIA_EXE, "wallet", "show"], stdout=subprocess.PIPE, universal_newlines=True)
        print(process.stdout)

    # You can use this to split the coin into smaller coins
    if args.command == "split-coins":
        splitcoins(CHIA_EXE, args)

    if args.command == "airdrop":
        airdrop(CHIA_EXE, args)

    

