#!/usr/bin/env python
import argparse
import itertools
import xml.etree.ElementTree as ET


class DataTable(object):
  COLUMNS = {'name':0, 'gender': 1, 'age': 2, 'location': 3}

  def __init__(self, filename):
    self.OUTFORMATS = {'html': self.toTable, 'csv': self.toCSV}
    inputObj = open(filename, 'r')
    self.data = [line.split() for line in inputObj.readlines()]
    self.groupedData = {}

  def groupby(self, columns):
    sortedData = sorted(self.data,
      key=lambda x: [x[self.COLUMNS[column]] for column in columns])
    self.groupedData[tuple(columns)] = itertools.groupby(
      sortedData, lambda x: [x[self.COLUMNS[column]] for column in columns])

  def getFormatedData(self):
    columns = [key for key in self.groupedData.keys()[0]]
    columns.append('count')
    rows = []
    for k, v in self.groupedData.values()[0]:
      k.append(str(len(list(v))))
      rows.append(k)
    return columns, rows

  def __str__(self):
    columns, rows  = self.getFormatedData()
    outCols = '|'.join(columns)
    outRows = '\n'.join('|'.join(row) for row in rows)
    return '%s\n%s' % (outCols, outRows)

  def toTable(self):
    columns, rows = self.getFormatedData()
    table = ET.Element('table')
    coltr = ET.SubElement(table, 'tr')
    for col in columns:
      coltd = ET.SubElement(coltr, 'td')
      coltd.text = col
    for row in rows:
      tr = ET.SubElement(table, 'tr')
      for cell in row:
        td = ET.SubElement(tr, 'td')
        td.text = cell
    return ET.tostring(table)

  def toCSV(self):
    csvString = ''
    columns, rows = self.getFormatedData()
    csvString = '%s\n' % ','.join(columns)
    for row in rows:
      csvString  += '%s\n' % ','.join(row)
    return csvString


def parseArguments():
  argParse = argparse.ArgumentParser(description='Pivot program arguments.')
  argParse.add_argument('filename',
    help='The input file format expected,\
    name <string>, gender <char>, age <number>, location <string>', type=str)
  argParse.add_argument('-o', help='csv or html', type=str)
  argParse.add_argument(
    '-by', action='append', help='pivot by.', type=str)
  return argParse.parse_args()


def main():
  args = parseArguments()
  d = DataTable(args.filename)
  d.groupby(args.by)
  out =  d.OUTFORMATS.get(args.o)
  if out:
    print out()
  else:
    print d

if __name__ == '__main__':
  main()
