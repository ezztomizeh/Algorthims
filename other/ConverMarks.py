def Convert(df):
  col = list(df.columns)
  for i in range(len(col)):
    y = df[col[i]]
    x = list(y)
    for j in range(len(x)):
      if x[j] >= 90 : x[j] = 'A'
      else : x[j] = 'F'
    df[col[i]] = x
  
  return df
