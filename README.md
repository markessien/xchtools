# xchtools
My tools for doing Chia things

# How to use
- Rename .env.sample to .env and customize the variables
- Run pip install -r requirements.txt
- Use python main.py wallets to see all your wallets and get the wallet IDs. Your CATs are in different wallets from xch
- Run python main.py split-coins to split coins
- Run python main.py airdrop <filename> to airdrop tokens

Take note: if you want to airdrop, it's best to split your CAT coins into multiple smaller coins first.

# Airdropping XCH or Chia Tokens
- Add a file called .airdrop.whatever.csv (this format will be git ignored)
- One of the columns should contain the xch address. This will be detected automatically. The first address with xch is the airdrop target


# Example

Run it like this to split your coins

#### XCH splitting example
python main.py split-coins -d xch13379wurwsnkq35qdqyaz8gyvae2q8zuvxxzpschzstkedpsu3paqdxewlw -a 0.1 -i 10

#### Token Splitting Example
python main.py split-coins -d xch1pwrce750mycjaxf39p0yr682gzcjzmlsaxx65x0ue88r50vunq8sfs9e0z -a 110 -i 100


-d = destination address, which should be yours

-a = amount

-i = number of iterations

You can also add_

-m for memo

-f for fee 

Not yet implemented is:

wallet_id, which allows you switch to a CAT wallet