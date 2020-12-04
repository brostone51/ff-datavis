""" Contains a simple input class
"""
import re

import pandas as pd


class InputData:
  """Simple class for storing information and data about the input files passed
  in by the caller

  Example uses:

  """
  def __init__(self, file_name: str):
    self.file_name = file_name
    self.df = pd.read_csv('./qb_data/' + self.file_name)
    regexp = r'^(?P<year>\d+)(?P<position>\w+)[.]csv$'
    matches = re.search(regexp, self._file_name)
    self.year = matches.group('year')
    self.position = matches.group('position')

  @property
  def file_name(self):
    return self._get_file_name()

  @file_name.setter
  def file_name(self, file_name):
    self._set_file_name(file_name)

  def _get_file_name(self):
    return self._file_name

  def _set_file_name(self, file_name):
    self._file_name = file_name

  @property
  def year(self):
    return self._get_year()

  @year.setter
  def year(self, year):
    self._set_year(year)

  def _get_year(self):
    return self._year

  def _set_year(self, year):
    self._year = year

  @property
  def position(self):
    return self._get_position()

  @position.setter
  def position(self, position):
    self._set_position(position)

  def _get_position(self):
    return self._position

  def _set_position(self, position):
    self._position = position

  @property
  def df(self):
    return self._get_df()

  @df.setter
  def df(self, df):
    self._set_df(df)

  def _get_df(self):
    return self._df

  def _set_df(self, df):
    self._df = df

  def pretty_name(self) -> str:
    return self.year + ' ' + self.position.upper()
