# PENCARIAN SISWA

# keterangan:
# low = index awal
# up = index akhir
# m = median

# Data array
arr_name = ['Andi', 'Akbar', 'Bela', 'Ceko', 'Dede', 'Ega', 'Fazar']
arr_name.sort()

# Nama yang dicari
key = input('Name : ')

# Proses
low = 0
up = len(arr_name) - 1
for i in range(len(arr_name)):
  i += 1
  m = int((low + up)/2)
  if key == arr_name[m]:
    print('{} ditemukan pada index ke {} dan percobaan ke {}'.format(key, m, i))
    break
  else:
    if key > arr_name[m]:
      low = m + 1
    else:
      up = m - 1
