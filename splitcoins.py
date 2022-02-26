
import sys, subprocess, time

def splitcoins(chia_exe, args):
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
            time.sleep(35)