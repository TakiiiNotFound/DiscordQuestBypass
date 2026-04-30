import time
import sys

# Frame data hardcoded from source 1-30 [cite: 1-30]
frame1 = r"""
                                               d1v                                                                    
                                             idvv1                                                                    
                                           m0r   vd                                                                   
                                          iiv r   N                                                                   
                                        vdm  01m   d1m                                                                
                                       vdm  660Wv  E 0i                   md00irv                                     
                                      vir0R0061Ev v0  ir                 vdr   vd0dm                                  
                                      md mm    r1dd1  rW   vmmmrrrmiim    i0       vWi                                
                                     r1   0d       W   mvd1i          d   vmr         1m                              
                                   01   v  00r                  vr   vW rr mi          dm                             
                                   Ir6v1IRi                 vr1R66   R  r60E6          r1                             
                                   R v6r vir                i0d0Nv  W   r6             v6v                            
                                   R 06          riiv       i60Nr  6v   vm             v6r                            
       vv                          dd   01      6v  mI            1     ir             v6r                            
      rW16i                       mrmivdA1           rI          Rv    r1             v1W1E1mvdNIm                    
       idd66r                    vW 1          RAE   rEr     dmWm      r0             mr        mi                    
       vdm d1dv                   vvi  dRr     NA0   vNr     vWm    v1d1             rW        ddv                    
        idv  160                    vRd v        m    v        dr   6vv            vIIv      idv                      
         di   vRd1                    vd0         mdr     r0W1iv   d1           iWiv Nv      mdv rWNWR                
         mmv    mRi0           rdRdi     m6WR1ddd       m0rmriWNRNN6      vr6ERm rmiRNr       iWi     ri1m            
          0i      iRR0      idiv    vid060dWRWWWWIW    r1                       mimm0RR        di        vdi          
          vdr      vWdm    dmriv v1     v m0IAIm   iW r0v                                       6m        vir         
           dm       i00    0mmr   I  m    vdRWm   6 vdm                                         m6v    rid1d          
           v0r      v6dd   vi6I1ii1Edmi60mdi     Wv                                              W0iiR0d60i           
            ii       m1iv rmmiiiid iNir  vm06dri1v                                               Wm   mmv             
             06v      iWWiddd66m mRd rm                   d0             vv                      r6v                  
              v6i     r00m     iNi  id                   mR6            rd16didiirrv     rm   ridd0R                  
                i0r    i1i     r0  rW  rv                d0vi666666661dmr       vvrmrrrrrmri0m0m                      
                  i0v  vdWi     6mr6Wdd0r               r0i                                  mm                       
                    div m0dr          dWWWWR6irmimmmm  rmddv                                                          
                     r0m 0Wirvvrrrrrrrrm06r     d0ivrWrW v                                                            
                       md00W0iiiiiimmrmiiimrvrvvvvmRI61                                                               
                         rmiWNWWWWWNNNRRNNNNNNW666661r      
working on your quest...""" 

# Frame data hardcoded from source 31-61 [cite: 31-61]
frame2 = r"""
                                               m6v                                                                    
                                             ddrm6                                                                    
                                           m0r   0v                                                                   
                                          iiv ir  I                                                                   
                                        vim  066  i 0r                                                                
                                        dd  d60Rv  Wvid                                                               
                                       i0rdi601Wdv I  ri           mmddmrv                                            
            i1dv                      r0  dm     mWW  r6     rmimi6rrim  i6ir                                         
            W66WR                     mv  riv      r   vri61iv        W    vd0v                                       
            0601m                  IWv     v0dr                vmv   mi       dr                                      
             iv                   vR m                      vrW1Nv   N         dv                                     
                                  vR                        06d1i   I          dm                                     
                                   N                         6Nd   E            i      vmdWRR6r                       
      mR1r                         1 iAAAA0                      vNE            1r rIm        dm                      
      v166d                       N 0ii                         Rr  R           0v N         d0v                      
       idi1Rm            6d      m  W           EAv           1i    I          vr  1v      d0v                        
        di mWNr         m6Wm      rrmdv11        rIAAEN       1m  mrv          1m   1     m1v                         
        miv  i1W                     i0 v                     m1v  1          im    Iv    r6d                         
         di    dWRv                   v06v       vvri   r66N0mv   6          mdmWWr Wr     rdv                        
         rdr    v011                     m1R11RR1m     vm  rrdWRdrm       vm00v    rm       id                        
          di      m1I6                   mWRWWWWNI6m   m6                    vmrd1dv        vim                       
          v0r      v1im      d6iimmmd10v0Wdidd6Wr  v6 d0                           vimi110000W10000WW60v              
           dm       m10    m0r        iW        rdd  dv                                                rid0r          
           v6r      v0dd  v0mir v    v6v          d0                                                       rd0m       
            miv      r6dii6iv6rv6    m0  00  r      00                                                       id       
             i1v      iR10600W01v   vRdr 0R6dR0id0    r   vr                                     vid06  vv rd1i       
               0d     r00i     r60d6RR0mmv i0rvv         vmddr          riiidr               v  0dv   0iddid16v       
                v1i    i1i        06Ndm616W1m0d          d1  rmd0111600rr    rmd00dddddd010mi000dv      vd66dv        
                  v1m   iWd         mWWirr060dr6i        i0                                m0r                        
                    m0v md0m          r6r     idd1ir   vmm6d                                                          
                      idv01irrrrrrrrrmrrdR0     v1mWm  i0v                                                            
                       r060R6mmmmmmmimiiiiiiiiiiiid1Amdm                                                              
                           v011WWWW6WWW1WWW10iiiiimrrr    
working on your quest...""" 

# Mapped ANSI indices based on your Catppuccin Mocha config:
# Red: 1, Yellow: 3, Green: 2, Cyan: 6, Blue: 4, Purple: 5
CATPPUCCIN_PALETTE = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]

def apply_static_theme(text):
    lines = text.splitlines()
    colored_output = ""
    for i, line in enumerate(lines):
        # Apply theme color based on line index
        color_idx = CATPPUCCIN_PALETTE[i % len(CATPPUCCIN_PALETTE)]
        colored_output += f"\033[3{color_idx}m{line}\033[0m\n"
    return colored_output

def animate():
    # Pre-color frames
    colored_frames = [apply_static_theme(frame1), apply_static_theme(frame2)]
    
    # ANSI Escapes
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    HOME = "\033[H"
    CLEAR = "\033[2J"

    # Initial Clear
    sys.stdout.write(CLEAR)
    sys.stdout.write(HIDE_CURSOR)
    
    try:
        while True:
            for frame in colored_frames:
                # HOME resets cursor to top-left to avoid ghosting/flicker
                sys.stdout.write(HOME)
                sys.stdout.write(frame)
                sys.stdout.flush()
                time.sleep(0.5)
    except KeyboardInterrupt:
        sys.stdout.write(SHOW_CURSOR)
        print("\nAnimation stopped.")

if __name__ == "__main__":
    animate()
