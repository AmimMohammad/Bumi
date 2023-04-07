import ccxt

#The aim of this code is to identify trading pairs that have a profitable arbitrage opportunity.
# The code uses the CCXT library to connect to ten different exchanges: Binance, Kraken, Bitget, Bitmart, Bybit, Gate, Huobi, Kucoin, MEXC, and OKEx.
# CCXT provides a uniform API for trading across various exchanges.

binance = ccxt.binance()
kraken = ccxt.kraken()
bitget = ccxt.bitget()
bitmart = ccxt.bitmart()
bybit  = ccxt.bybit()
gate  = ccxt.gate()
huobi  = ccxt.huobi()
kucoin  = ccxt.kucoin()
mexc  = ccxt.mexc()
okx  = ccxt.okx()

exchanges = [binance,kraken, bitget, bitmart, bybit, gate, huobi, kucoin, mexc, okx]
exchange=[]

#The first step is to extract a list of common trading pairs that are traded on all ten exchanges.
# A set of common symbols is created by getting the intersection of symbols that are traded on each exchange.
# The common symbols are then stored in a list to be used later in the code.

for enum in exchanges:
    exchange.append(enum.load_markets())


common_symbol_pairs = set.intersection(*[set(e.keys()) for e in exchange])

common_symbol_pairs = list(common_symbol_pairs)
# Common Pairs from all 8 exchanges have been extracted. The next step is to perform interexchange arbitrage.
# For each symbol in the common symbol list, the code checks each exchange to see if the trading pair is available.
# If the trading pair is available, the code fetches the current ask and bid prices for the trading pair.


for symbol in common_symbol_pairs:
    # Each symbol is common across 10 exchanges.
    # Perform interexchange arbitrage here.

    min_ask = float('inf')
    max_bid = float('-inf')
    best_ask_exchange = None
    best_bid_exchange = None


    # The code uses a try-except block to handle rate limit errors that may be returned by the exchange. If a rate limit error is returned, the code prints a message indicating that the exchange has reached its rate limit and then moves on to the next exchange.
    #
    # After getting the current ask and bid prices for the trading pair on each exchange, the code checks if there is a profitable arbitrage opportunity.
    # If there is a profitable arbitrage opportunity, the code calculates the profit margin, prints the current volume of the trading pair,
    # and provides information on where to buy and sell the trading pair to make the most profit.
    # The code uses a loop to go through each trading pair in the common symbol list and check for profitable arbitrage opportunities.
    # If there are no profitable arbitrage opportunities for a particular trading pair, the code moves on to the next trading pair.


    # Check each exchange for the symbol pair
    for enum in exchanges:
        # Check if symbol is traded on the exchange
        if symbol in exchange[exchanges.index(enum)]:
            # Get current ask and bid prices for the symbol pair
            try:
                ticker = enum.fetch_ticker(symbol)
            except ccxt.BaseError as e:
                print(f"\n{enum.id} rate limit exceeded for {symbol}, skipping...\n")
                print("\n\n")
                continue

            current_ask = ticker['ask']
            current_bid = ticker['bid']
            volume = ticker['baseVolume']

            # Check if current ask is lower than current minimum ask
            if current_ask < min_ask:
                min_ask = current_ask
                best_ask_exchange = enum
                ask_volume = volume

            # Check if current bid is higher than current maximum bid
            if current_bid > max_bid:
                max_bid = current_bid
                best_bid_exchange = enum
                bid_volume = volume

    # Check if there is a profitable arbitrage opportunity
    if max_bid > min_ask:
        # Calculate profit margin and print information about arbitrage opportunity
        margin = (max_bid - min_ask) / min_ask * 100
        print(f"Arbitrage opportunity found for {symbol}!")
        print(
            f"Buy {ask_volume} {symbol.split('/')[0]} at {best_ask_exchange.id} for {min_ask} and sell at {best_bid_exchange.id} for {max_bid}")
        print(f"Potential profit margin: {margin:.2f}%")
        print("\n\n")

    else:
        print(f"No profitable arbitrage opportunity found for {symbol}")




# The OUTPUT : #

# Arbitrage opportunity found for ETH/BTC!
# Buy 3811.9901411 ETH at kucoin for 0.06684 and sell at bybit for 0.066859
# Potential profit margin: 0.03%
#
#
#
# Arbitrage opportunity found for LINK/USDT!
# Buy 218400.47324144 LINK at gate for 7.1948 and sell at bybit for 7.1971
# Potential profit margin: 0.03%
#
#
#
# Arbitrage opportunity found for XRP/USDT!
# Buy 32204835.6285 XRP at bitget for 0.49982 and sell at kucoin for 0.49995
# Potential profit margin: 0.03%
#
#
#
# Arbitrage opportunity found for ATOM/USDT!
# Buy 134833.8581002056 ATOM at huobi for 11.2888 and sell at mexc for 11.294
# Potential profit margin: 0.05%
#
#
#
# Arbitrage opportunity found for LTC/USDT!
# Buy 55196.16553942 LTC at kucoin for 91.081 and sell at bybit for 91.1
# Potential profit margin: 0.02%
#
#
#
# Arbitrage opportunity found for BTC/USDT!
# Buy 37462.31152 BTC at binance for 28048.43 and sell at gate for 28053.9
# Potential profit margin: 0.02%
#
#
#
# No profitable arbitrage opportunity found for MANA/USDT
# Arbitrage opportunity found for AVAX/USDT!
# Buy 1405667.96 AVAX at binance for 18.08 and sell at huobi for 18.0831
# Potential profit margin: 0.02%
#
#
#
# Arbitrage opportunity found for ADA/USDT!
# Buy 4185486.6230081 ADA at gate for 0.38137 and sell at kucoin for 0.381608
# Potential profit margin: 0.06%
#
#
#
# Arbitrage opportunity found for DOGE/USDT!
# Buy 166704907.23 DOGE at mexc for 0.08532 and sell at kucoin for 0.08537
# Potential profit margin: 0.06%
#
#
#
# Arbitrage opportunity found for DOT/USDT!
# Buy 581753.7154047055 DOT at huobi for 6.2818 and sell at kucoin for 6.283
# Potential profit margin: 0.02%
#
#
#
#
# bitmart rate limit exceeded for SHIB/USDT, skipping...
#
#
#
#
# Arbitrage opportunity found for SHIB/USDT!
# Buy 363433836072.61 SHIB at gate for 1.09519e-05 and sell at bybit for 1.09544e-05
# Potential profit margin: 0.02%
#
#
#
# Arbitrage opportunity found for BCH/USDT!
# Buy 5935.514534007971 BCH at huobi for 125.87 and sell at gate for 125.9
# Potential profit margin: 0.02%
#
#
#
# Arbitrage opportunity found for USDC/USDT!
# Buy 566603.9 USDC at bitmart for 0.99946 and sell at gate for 0.9995
# Potential profit margin: 0.00%
#
#
#
#
# bitmart rate limit exceeded for EOS/USDT, skipping...
#
#
#
#
# Arbitrage opportunity found for EOS/USDT!
# Buy 1740112.63470917 EOS at kucoin for 1.2187 and sell at gate for 1.2191
# Potential profit margin: 0.03%
#
#
#
# Arbitrage opportunity found for APE/USDT!
# Buy 145142.85 APE at bybit for 4.2374 and sell at kucoin for 4.2378
# Potential profit margin: 0.01%
#
#
#
#
# bitmart rate limit exceeded for SOL/USDT, skipping...
#
#
#
#
# Arbitrage opportunity found for SOL/USDT!
# Buy 351548.298718 SOL at okx for 20.649 and sell at kucoin for 20.652
# Potential profit margin: 0.01%
#
#
#
# Arbitrage opportunity found for MATIC/USDT!
# Buy 1810781.439914146 MATIC at huobi for 1.114948 and sell at kraken for 1.1153
# Potential profit margin: 0.03%
#
#
#
# Arbitrage opportunity found for ETH/USDT!
# Buy 20678.841084211985 ETH at huobi for 1875.13 and sell at gate for 1875.62
# Potential profit margin: 0.03%
