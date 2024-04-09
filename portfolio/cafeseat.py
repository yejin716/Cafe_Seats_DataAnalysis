# -*- coding: utf-8 -*-
"""cafeseat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XZ3bxk55dKZQcTjViBGckn2b1Iys6lJG
"""

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import pandas as pd

df = pd.read_excel('/content/drive/MyDrive/csv/cafe.xlsx')
df

act = df.groupby('행동').count()
pd.DataFrame(act['인원'])

#sex = df['성별'].value_counts()
#pd.DataFrame(sex)

sex = df.groupby('성별').count()
pd.DataFrame(sex['인원'])

old = df.groupby('나이').count()
pd.DataFrame(old['인원'])

bakery = df.groupby('베이커리 유무').count()
pd.DataFrame(bakery['인원'])

seat = df.groupby('좌석').count()
pd.DataFrame(seat['인원'])

ag = df.groupby('연령대').count()
pd.DataFrame(ag['인원'])

!pip install koreanize-matplotlib

import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(3, 3))
piesex = df['성별'].value_counts()
piesex.plot(kind='pie', label='', autopct='%.1f%%', shadow=False, cmap='coolwarm', counterclock=False, startangle=180, fontsize=10, labeldistance=0.9)

plt.title('[성별]', fontsize=12)
plt.show()

import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(5, 5))
pieold = df['나이'].value_counts()
pieold.plot(kind='pie', label='', autopct='%.1f%%', shadow=False, cmap='Spectral',counterclock=False, startangle=180, fontsize=10, labeldistance=0.9)
plt.title('[나이]', fontsize=12)
plt.show()

import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(5, 5))
newseat = df['좌석'].value_counts()
newseat.plot(kind='pie', label='', autopct='%.1f%%', shadow=False, cmap='Pastel2', counterclock=False, startangle=180, fontsize=10, labeldistance=0.9)
plt.title('[좌석]', fontsize=12)
plt.show()

import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(5, 5))
newact = df['행동'].value_counts()
newact.plot(kind='pie', label='', autopct='%.1f%%', shadow=False, cmap='Pastel2', counterclock=False, startangle=180, fontsize=10, labeldistance=0.9)
plt.title('[행동]', fontsize=12)
plt.show()

import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(5, 5))
newbakery = df['베이커리 유무'].value_counts()
newbakery.plot(kind='pie', label='', autopct='%.1f%%', shadow=False, cmap='Pastel2', counterclock=False, startangle=180, fontsize=10, labeldistance=0.9)
plt.title('[베이커리 유무]', fontsize=12)
plt.show()

import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(3, 3))
newac = df['인원'].value_counts()
newac.plot(kind='pie', label='', autopct='%.1f%%', shadow=False, cmap='Pastel2', counterclock=False, startangle=180, fontsize=10, labeldistance=1.1)
plt.title('[인원]', fontsize=12)
plt.show()

import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(3, 3))
newag = df['연령대'].value_counts()
newag.plot(kind='pie', label='', autopct='%.1f%%', shadow=False, cmap='Pastel2', counterclock=False, startangle=180, fontsize=10, labeldistance=1.1)
plt.title('[연령대]', fontsize=12)
plt.show()

df.sort_values(['연령대','행동'],ascending=False).head(300)

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  from matplotlib import pyplot as plt
  import seaborn as sns
  palette = list(sns.palettes.mpl_palette('Dark2'))
  counted = (series['날짜']
                .value_counts()
              .reset_index(name='counts')
              .rename({'index': '날짜'}, axis=1)
              .sort_values('날짜', ascending=True))
  xs = counted['날짜']
  ys = counted['counts']
  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = _df_6.sort_values('날짜', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('행동')):
  _plot_series(series, series_name, i)
  fig.legend(title='행동', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('날짜')
_ = plt.ylabel('count()')

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  from matplotlib import pyplot as plt
  import seaborn as sns
  palette = list(sns.palettes.mpl_palette('Dark2'))
  counted = (series['날짜']
                .value_counts()
              .reset_index(name='counts')
              .rename({'index': '날짜'}, axis=1)
              .sort_values('날짜', ascending=True))
  xs = counted['날짜']
  ys = counted['counts']
  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = _df_4.sort_values('날짜', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('성별')):
  _plot_series(series, series_name, i)
  fig.legend(title='성별', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('날짜')
_ = plt.ylabel('count()')

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['행동'].value_counts()
    for x_label, grp in _df_9.groupby('나이')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('나이')
_ = plt.ylabel('행동')

from matplotlib import pyplot as plt
import seaborn as sns
_df_2.groupby('행동').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
_df_1.groupby('나이').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)