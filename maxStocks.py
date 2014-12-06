def getInvestmentAdvice(stocks):
  profit = 0
  buy = stocks[0]
  buyindex = 0
  sellindex = 0
  for i in range(1, len(stocks)):
    if buy > stocks[i]:
      buy = stocks[i]
      buyindex = i

    currentmax = stocks[i] - buy
    if currentmax > profit:
      profit = currentmax
      sellindex = i
  print profit, 'buy at %s sell at %s' % (stocks[buyindex], stocks[sellindex])


if __name__ == '__main__':
  getInvestmentAdvice([5,6,2,7,1,8,9,2])

