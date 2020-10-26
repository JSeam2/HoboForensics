# HOBO FORENSICS
This is a pretty informal forensics repo of interesting smart contracts that do not have source code provided and are used in economic attacks

## Harvest Finance (26/Oct/2020)
Some guy did an economic exploit on curve stablecoin yvaults and repeatedly deposit, swap, withdraw, etc. and earned from mispricing on the harvest finance USDT, USDC vaults. 


Strategy 1 exploited USDT, this was executed
Strategy 2 was supposed to exploit WETH, USDC, USDT, and uses uniswap instead. Unipools were potentially not safe. This was not executed as I believe it might have been much more complicated
Strategy 3 exploited USDC, this was executed
