# -*- mode: python -*-

block_cipher = None

added_files = [
	  ( 'database.json', '.' ),
	
	  ]


a = Analysis(['user_interface.py', 'savebackup.py', 'insert_in_html.py', 'database.py', 'classes.py'],
             pathex=['C:\\Users\\Hallow\\Documents\\Alex\\Github\\GameSaveBackups'],
             binaries=[],
             datas=[('C:\\Python27\\lib\\site-packages\\eel\\eel.js', 'eel'), ('web', 'web'), ('database.json', '.')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='user_interface',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='user_interface')
