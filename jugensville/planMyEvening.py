#!/usr/bin/env python
import argparse
import csv
import collections
import itertools

class Restaurant(object):

  def __init__(self, restid, priceItems):
    self.restId = restid
    self.priceItems = priceItems
    self.uniqItems = set()
    for item in priceItems:
      self.uniqItems = self.uniqItems | set(item['items'])

  def getCombiMeals(self, choices):
    itemsFromChoice = []
    choiceSet = set(choices)
    for item in choiceSet:
      subItem = []
      for priceItem in self.priceItems:
        if item in priceItem['items']:
          subItem.append(priceItem)
      itemsFromChoice.append(subItem)
    return itertools.product(*itemsFromChoice)

  def getBestChoice(self, choices):
    bestChoice = []
    for combiMeal in self.getCombiMeals(choices):
      combiItems = set([(cm['price'], tuple(cm['items'])) for cm in combiMeal])
      combiPrice = sum([ci[0] for ci in combiItems])
      bestChoice.append(combiPrice)
    return min(bestChoice)

  def serves(self, choices):
    uniqChoices = set(choices)
    return uniqChoices <= self.uniqItems


def handelArguments():
  argParse = argparse.ArgumentParser(description='User plans for the evening.')
  argParse.add_argument(
    'menuFile', help='The consolidated csv menu.', type=str)
  argParse.add_argument('choices', nargs='*', help='Users choices.', type=str)
  args = argParse.parse_args()
  return args.menuFile, args.choices

def readCsvAndFormatData(menuFile):
  menuFileObj = open(menuFile, 'rb')
  menuReader = csv.reader(menuFileObj, skipinitialspace=True)
  formatedData = []
  for row in menuReader:
    if row:
      formatedData.append(
        {'restId': row[0], 'price': float(row[1]), 'items': row[2:]})
  return formatedData

def getMenuByRestId(formatedData):
  menuByRestId = collections.defaultdict(list)
  for data in formatedData:
    menuByRestId[data['restId']].append(data)
  return menuByRestId

def getRestaurants(menuByRestId):
  restaurants = []
  for restId, menu in menuByRestId.items():
    restaurants.append(Restaurant(restId, menu))
  return restaurants

def getResturantAdvice(restaurants, choices):
  possibleChoices = []
  for rest in restaurants:
    if rest.serves(choices):
      possibleChoices.append((rest.getBestChoice(choices), rest.restId))

  if possibleChoices:
    bestChoice = min(possibleChoices)
    return '%s, %s' % (bestChoice[1], bestChoice[0])
  else:
    return "D'oh, no restaurants found!"

def main():
  menuFile, choices = handelArguments()
  formatedData = readCsvAndFormatData(menuFile)
  menuByRestId = getMenuByRestId(formatedData)
  restaurants = getRestaurants(menuByRestId)
  print getResturantAdvice(restaurants, choices)

if __name__ == '__main__':
  main()
