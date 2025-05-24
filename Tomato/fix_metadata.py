import nbformat

path = "F:\Coding Camp By DBS Foundation\Tanamind-Tomato\Tomato\Tanamind_Tomato .ipynb"
nb = nbformat.read(path, as_version=4)

# Hapus metadata widgets jika ada
if 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']

# Simpan kembali
nbformat.write(nb, path)
print("Metadata widgets berhasil dihapus.")