
import sys, subprocess, time

def splitcoins(chia_exe, args):
    
    if args.wallet:
        wallet_id = args.wallet
    else:
        print("Please specify the wallet you want to send from. Use the 'wallets' command to get the list")
        sys.exit()

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

    # Added a tiny increment in the amount to be split. This is to avoid it just using
    # existing coins instead of taking the big one
    for x in range(iterations):
        amnt = str(float(amount) + (fee*(x+1)))
        print("Sending " + amnt + " to " + destination)
        
        process = subprocess.run([chia_exe, "wallet", "send", 
                                            "-i", str(wallet_id), 
                                            "-a", amnt,
                                            "-e", memo,
                                            "-m", str(fee),
                                            "-t", destination], stdout=subprocess.PIPE, universal_newlines=True)
        print(process.stdout)

        if x < iterations:
            time.sleep(35)