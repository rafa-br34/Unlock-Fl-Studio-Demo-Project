import sys
import os



#                                                                                  XX Separator 0xC7                                                          
#                Header 1                                  Header 2                || XX Signature Version
#                XX XX XX XX XX                            XX XX XX XX             || ||                                                       XX Byte Is Zero
# Free Save:     46 4C 68 64 06 00 00 00 00 00 04 00 60 00 46 4C 64 74 65 D3 01 00 C7 0C 32 30 2E 39 2E 32 2E 32 39 36 33 00 9F 93 0B 00 00 1C 00 25 01 C8

# Premium Save4: 46 4C 68 64 06 00 00 00 00 00 2C 00 60 00 46 4C 64 74 D6 60 0C 00 C7 0C 32 30 2E 37 2E 30 2E 31 36 38 39 00 9F 99 06 00 00 1C 01 25 01 C8
# Premium Save7: 46 4C 68 64 06 00 00 00 00 00 90 00 48 00 46 4C 64 74 14 16 12 00 C7 0C 32 30 2E 38 2E 30 2E 31 33 37 37 00 9F 61 05 00 00 1C 01 25 02 C8
# Premium Save6: 46 4C 68 64 06 00 00 00 00 00 4A 00 60 00 46 4C 64 74 4F 29 06 00 C7 0B 32 30 2E 30 2E 33 2E 35 33 32 00 9F 14 02 00 00 1C 03 25 01 C8
# Premium Save3: 46 4C 68 64 06 00 00 00 00 00 49 00 60 00 46 4C 64 74 A8 82 0B 00 C7 05 32 30 2E 30 00 9F 00 00 00 00 1C 03 25 01 C8
# Premium Save5: 46 4C 68 64 06 00 00 00 00 00 46 00 60 00 46 4C 64 74 09 76 03 00 C7 0B 31 32 2E 39 2E 32 2E 32 36 39 00 1C 03 C8
# Premium Save9: 46 4C 68 64 06 00 00 00 00 00 15 00 60 00 46 4C 64 74 7D 03 06 00 C7 0A 31 32 2E 35 2E 30 2E 35 39 00 1C 03 C8
# Premium Save0: 46 4C 68 64 06 00 00 00 00 00 1F 00 60 00 46 4C 64 74 1E E2 04 00 C7 0A 31 32 2E 33 2E 30 2E 36 32 00 1C 03 C8
# Premium Save1: 46 4C 68 64 06 00 00 00 00 00 1C 00 60 00 46 4C 64 74 07 F5 25 00 C7 08 31 31 2E 35 2E 31 34 00 1C 03 C8
# Premium Save8: 46 4C 68 64 06 00 00 00 00 00 2B 00 60 00 46 4C 64 74 09 DD 07 00 C7 07 31 30 2E 30 2E 30 00 1C 03 C8
# Premium Save2: 46 4C 68 64 06 00 00 00 00 00 28 00 60 00 46 4C 64 74 FF B1 05 00 C7 06 38 2E 35 2E 30 00 1C 04 C8

def GetArg(Index):
	return (len(sys.argv) >= Index + 1 and sys.argv[Index]) or None


def ForgeSignature(Version="11.5.5"):
	pass
							# b"F   L   h   d   x06 ?   ?   ?   ?   ?   ?   ?   x60 x00 F   L   d   t   ?   ?   ?   ?   xC7 ?"
	#FL_FileSignatureFlags	= " -   -   -   -   -   x   x   x   x   x   x   x   -   -   -   -   -   -   x   x   x   x   -   x"
	#FL_FileSignature 		= b"\x46\x4C\x68\x64\x06\x00\x00\x00\x00\x00\x00\x00\x60\x00\x46\x4C\x64\x74\x00\x00\x00\x00\xC7\x00"

	
def FindSig(Data):
	Start = False
	Last = 0
	for Byte in range(len(Data)):
		if Data[Byte] == 0x1C:
			Start = not Start
			Last = Byte
		if Data[Byte] == 0xC8 and Start:
			return Last


def main():
	InputFile = GetArg(1) or False
	if not InputFile:
		print("Specify Input File")
		return
	print("Input \"{}\"".format(InputFile))

	with open(InputFile, "rb") as File:
		Data = bytearray(File.read())
		if len(Data) <= 0:
			print("File Is Empty")
			return
		with open(InputFile + ".bak", "wb") as Backup:
			Backup.write(Data)
			Backup.close()
		
		SigPos = FindSig(Data)
		if not SigPos:
			File.close()
			print("Error Finding Signature")
			return
		print("Sig At {}".format(SigPos))
		I = 0
		while Data[SigPos + I] != 0xC8:
			if Data[SigPos + I] <= 0:
				Data[SigPos + I] = 0x01
				break
		File.close()

		with open(InputFile, "wb") as File:
			File.write(Data)
			File.close()






if __name__ == '__main__':
	main()