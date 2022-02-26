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
    target_address_list_already_sent= set()
    try:

        try:
            with open(source_file + ".sent.csv", mode="r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
        
                for row in csv_reader:
                    target_address_list_already_sent.add(row[0])
        except:
            pass
        
        print(str(len(target_address_list_already_sent)) + " addresses already sent")

        # Load all the addresses
        with open(source_file, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
     
            for row in csv_reader:
  
                for column in row:
                    if column.startswith("xch") and not column in target_address_list_already_sent:
                        target_address_list.add(column)
                        break

            print('Found ' + str(len(target_address_list)) + " unique XCH addresses for airdrop")


        # Start sending
        print("Starting Airdrop")

        # Create a file where we write everything sent already so we can stop and start
        # sending
        try:
            fsent = open(source_file + ".sent.csv", "w")

            for sent_addr in target_address_list_already_sent:
                fsent.write(sent_addr + ",\n")
                fsent.flush()

        except IOError:
            print("Could not open file to write sent airdrops")
            sys.exit()
        
        for c, addr in enumerate(target_address_list):
            process = subprocess.run([chia_exe, "wallet", "send", 
                                                "-i", str(wallet_id), 
                                                "-a", str(amount),
                                                "-e", memo,
                                                "-m", str(fee),
                                                "-t", addr], stdout=subprocess.PIPE, universal_newlines=True)
            print(process.stdout)
            print("Airdropped to " + str(c+1))
            fsent.write(addr + ",\n")
            fsent.flush()

            if c == 5:
                break
            time.sleep(10)
        
        fsent.close()

    except IOError:
        print("Count not open the airdrop file. Please provide a valid CSV file with airdrop targets")