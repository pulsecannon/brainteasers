class PriceSize(object):

  def __init__(self, price, size):
    self.price = int(float(price + 0.005) * 100) / 100.0
    self.size = int(float(size) * 100) / 100.0

  def __eq__(self, other):
    if self.price != other.price or self.size != other.size:
      return False
    return True

  def __ne__(self, other):
    return not(self.__eq__(other))

  def __str__(self):
    return "%f, %f" % (self.price, self.size)


class Prices(list):

  def __init__(self, *args):
    #noinspection PyTypeChecker
    list.__init__(self, *args)

  def __eq__(self, others):
    return len(self) == len(others) and all(
      map(lambda x: x[0] == x[1], zip(self, others)))

  def __getitem__(self, item):
    """
    @param item:
    @return: Price
    """
    return super(Prices, self).__getitem__(item)

  def append(self, p_object):
    assert(isinstance(p_object, PriceSize))
    super(Prices, self).append(p_object)

  @property
  def bestprice(self):
    """
    @return: float
    """
    if len(self) > 0:
      return self[0].price
    return None


class SelectionPrice(object):

  def __init__(self):
    self.selectionid = 0
    self.selectionstatus = 'ACTIVE'
    self.bestbacks = Prices()
    self.bestlays = Prices()
    self.totalmatched = 0
    self.reductionfactor = 0

  def __eq__(self, other):
    return self.bestbacks == other.bestbacks and self.bestlays == other.bestlays

class SelectionPrices(list):

  def __init__(self, *args):
    #noinspection PyTypeChecker
    list.__init__(self, *args)

  def __eq__(self, others):
    return len(self) == len(others) and all(
      map(lambda x: x[0] == x[1], zip(self, others)))

  def __getitem__(self, item):
    """

    @rtype : SelectionPrice
    """
    return super(SelectionPrices, self).__getitem__(item)

  def append(self, p_object):
    assert(isinstance(p_object, SelectionPrice))
    super(SelectionPrices, self).append(p_object)


class MarketPrice:

  def __init__(self):
    self.marketid = None
    self.selectionprices = SelectionPrices()
    self.totalmatched = 0
    self.marketstatus = None
    self.isinplay = False

  def __eq__(self, other):
    return self.selectionprices == other.selectionprices and self.totalmatched == other.totalmatched


m1  = MarketPrice()
m2 = MarketPrice()


print m1 == m2

sp = SelectionPrice()
sp.bestbacks.append(PriceSize(0.01, 0.02))
m1.selectionprices.append(sp)
m1.totalmatched = 10

print m1 == m2

m2.totalmatched = 20
m2.selectionprices.append(sp)

print m1 == m2
