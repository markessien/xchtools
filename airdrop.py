import sys, subprocess, time, csv


def airdrop(chia_exe, args):
    print("Airdropping Tokens")

    if args.source:
        source_file = args.source
    else:
        print("Please specify the airdrop CSV to read from using the -s argument")
        sys.exit()

    if args.wallet:
        wallet_id = args.wallet
    else:
        print("Please specify the wallet you want to send from. Use the 'wallets' command to get the list")
        sys.exit()

    if args.amount:
        amount = args.amount
    else:
        print("Please specify the amount for the airdrop using the -a parameter")
        sys.exit()

    if args.memo:
        memo = args.memo
    else:
        print("Please specify the memo for the airdrop using the -m parameter. This is a small note included in the send")
        sys.exit()

    if args.fee:
        fee = args.fee
    else:
        fee = 0.0000001

    target_address_list= set()
    try:

        # Load all the addresses
        with open(source_file, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
     
            for row in csv_reader:
  
                for column in row:
                    if column.startswith("xch"):
                        target_address_list.add(column)
                        break

            print('Found ' + str(len(target_address_list)) + " unique XCH addresses")


        # Start sending
        print("Starting Airdrop")

        for c, addr in enumerate(target_address_list):
            process = subprocess.run([chia_exe, "wallet", "send", 
                                                "-i", str(wallet_id), 
                                                "-a", str(amount),
                                                "-e", memo,
                                                "-m", str(fee),
                                                "-t", addr], stdout=subprocess.PIPE, universal_newlines=True)
            print(process.stdout)
            print("Airdropped to " + str(c+1))

            break
            time.sleep(35)

    except IOError:
        print("Count not open the airdrop file. Please provide a valid CSV file with airdrop targets")