import sys, subprocess, time

from argparse import ArgumentParser

# Change this to the location of your binary
chia_exe = "C:/Users/Mark/AppData/Local/chia-blockchain/app-1.2.12284/resources/app.asar.unpacked/daemon/chia.exe"

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("cmd", type=str,
                    help="the command you want to run. info or split-coins")

    parser.add_argument("-d", "--destination", dest="destination",
                        help="destination address")

    parser.add_argument("-a", "--amount",
                        help="amount for each coin")

    parser.add_argument("-m", "--memo",
                        help="memo for the send (optional)")

    parser.add_argument("-f", "--fee",
                        help="fee for the send (optional)")

    parser.add_argument("-i", "--iterations",
                        help="number of times to iterate the send")

    args = parser.parse_args()

    if args.cmd == "info":
        process = subprocess.run([chia_exe, "version"], stdout=subprocess.PIPE, universal_newlines=True)
        print(process.stdout)

    # You can use this to split the coin into smaller coins
    if args.cmd == "split-coins":
        wallet_id = 1

        if args.amount:
            amount = args.amount
        else:
            print("Please specify the amount you want each coin split to")
            sys.exit()

        if args.memo:
            memo = args.memo
        else:
            memo = "splitcoins"

        if args.fee:
            fee = args.fee
        else:
            fee = 0.0000001

        if args.destination:
            destination = args.destination
        else:
            print("No destination provided")
            sys.exit()

        if args.iterations:
            iterations = int(args.iterations)
        else:
            iterations = 1

        print("sending coins to : " + args.destination)

        for x in range(iterations):
            process = subprocess.run([chia_exe, "wallet", "send", 
                                                "-i", str(wallet_id), 
                                                "-a", str(amount),
                                                "-e", memo,
                                                "-m", str(fee),
                                                "-t", destination], stdout=subprocess.PIPE, universal_newlines=True)
            print(process.stdout)

            if x < iterations:
                time.sleep(30)

    

