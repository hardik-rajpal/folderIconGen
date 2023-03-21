from subprocess import Popen
import argparse
db = 'rgb(250, 187, 25)'
df = 'rgb(255, 218, 114)'
def genIcon(args):
    color1 = args.ffill
    color2 = args.bfill
    mainfile = args.clipart
    outname = args.name
        
    cmd1 = ['convert','front.png','-fill',f"{color1}","-colorize","100","front1.png"]
    cmd2 = ['convert','back.png','-fill',f"{color2}",'-colorize',"100","back1.png"]
    overlaycmd = 'convert front1.png back1.png -gravity center -composite merge1.png'.split()
    copier = f'convert {mainfile} out.png'.split()
    trimmer = f'convert out.png -trim out.png'.split()
    resizer = f'convert out.png -resize 160x160 out.png'.split()
    extent = f'convert out.png -background none -gravity center -extent 256x256 out.png'.split()
    
    overlaycmd2 = f'convert merge1.png out.png -gravity center -geometry -0+10 -composite {outname}'.split()
    cleaner = 'rm front1.png back1.png out.png merge1.png'.split()
    for cmd in [cmd1,cmd2,overlaycmd]:
        Popen(cmd).wait()
    if(len(mainfile)>0):
        Popen(copier).wait()
        if(args.trim):
            Popen(trimmer).wait()
        Popen(resizer).wait()
        # Popen(extent).wait()
        Popen(overlaycmd2).wait()
    else:
        Popen(f'convert merge1.png {outname}'.split())
    Popen(cleaner).wait()
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ffill',help="front fill",type=str,default=df)
    parser.add_argument('--bfill',help="back fill",type=str,default=db)
    parser.add_argument('--clipart',help='Clipart put on front',type=str,default='')
    parser.add_argument('--trim',help="Trim the transparent padding around the clipart",action='store_true')
    parser.add_argument('--name',help="Name of output file",type=str,default='final.ico')
    args = parser.parse_args()
    genIcon(args)