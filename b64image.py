import base64
import zlib

def b64encode(data):
    encoded = base64.encodebytes(data)
    return encoded

def b64decode(data, filename):
    decoded = base64.decodebytes(data)
    image = open(filename, 'wb')
    image.write(decoded)

def gzip64encode(file):
    data = b64encode(file)
    compressed = zlib.compress(data)
    return compressed

def gzip64decode(data):
    decompressed = zlib.decompress(data)
    b64decode(decompressed, 'gzip_image.png')

if __name__ == "__main__":
    image = open('sample_image.png', 'rb')
    data = image.read()
    print("IMAGE size:       ", len(data))
    enc = b64encode(data)
    print("B64 encoded:      ", len(enc))
    b64decode(enc, 'decoded_image.png')

    cenc = gzip64encode(data)
    print("GZIP-B64 encoded: ", len(cenc))
    gzip64decode(cenc)
    gcomp = ((len(enc)-len(cenc))*100/len(enc))
    fcomp = ((len(cenc)-len(data))*100/len(data))
    print(f"Gzip Compression: {gcomp:.2f}%")
    print(f"File Inflation:   {fcomp:.2f}%")


