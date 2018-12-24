import json

def main():
    languages = set(map(lambda x: x.strip(), """A# .NET
    A# 
    Axiom
    A-0 System
    A+
    A++
    ABAP
    ABC
    ABC ALGOL
    ABSET
    ABSYS
    ACC
    Accent
    Ace DASL 
    Distributed Application Specification Language
    ACL2
    ACT-III
    Action!
    ActionScript
    Actor
    Ada
    Adenine
    Agda
    Agilent VEE
    Agora
    AIMMS
    Aldor
    Alef
    ALF
    ALGOL 58
    ALGOL 60
    ALGOL 68
    ALGOL W
    Alice
    Alma-0
    AmbientTalk
    Amiga E
    AMOS
    AMPL
    AngelScript
    Apex
    APL
    App Inventor for Android's visual block language
    AppleScript
    APT
    Arc
    ARexx
    Argus
    AspectJ
    Assembly language
    ATS
    Ateji PX
    AutoHotkey
    Autocoder
    AutoIt
    AutoLISP
    Visual LISP
    Averest
    AWK
    Axum
    Active Server Pages
    B
    Babbage
    Ballerina
    Bash
    BASIC
    bc
    BCPL
    BeanShell
    Batch file
    Bertrand
    BETA
    BLISS
    Blockly
    BlooP
    Boo
    Boomerang
    Bourne shell 
    bash
    ksh
    BPEL
    Business Basic
    C
    C--
    C++
    C*
    C# 
    C/AL
    Caché ObjectScript
    C Shell 
    csh
    Caml
    Cayenne
    CDuce
    Cecil
    Cesil
    Céu
    Ceylon
    CFEngine
    Cg
    Ch
    Chapel
    Charity
    Charm
    CHILL
    CHIP-8
    chomski
    ChucK
    Cilk
    Citrine
    CL (IBM)
    Claire
    Clarion
    Clean
    Clipper
    CLIPS
    CLIST
    Clojure
    CLU
    CMS-2
    COBOL
    CobolScript
    COBOL Scripting language
    Cobra
    CoffeeScript
    ColdFusion
    COMAL
    Combined Programming Language
    CPL
    COMIT
    Common Intermediate Language 
    CIL
    Common Lisp 
    CL
    COMPASS
    Component Pascal
    Constraint Handling Rules 
    CHR
    COMTRAN
    Cool
    Coq
    Coral 66
    CorVision
    COWSEL
    CPL
    Cryptol
    Crystal
    Csound
    CSP
    CUDA
    Cuneiform
    Curl
    Curry
    Cybil
    Cyclone
    Cython
    D
    DASL 
    Datapoint's Advanced Systems Language
    Dart
    Darwin
    DataFlex
    Datalog
    DATATRIEVE
    dBase
    dc
    DCL
    Delphi
    DinkC
    DIBOL
    Dog
    Draco
    DRAKON
    Dylan
    DYNAMO
    DAX 
    Data Analysis Expressions
    E
    Ease
    Easy PL/I
    EASYTRIEVE PLUS
    eC
    ECMAScript
    Edinburgh IMP
    EGL
    Eiffel
    ELAN
    Elixir
    Elm
    Emacs Lisp
    Emerald
    Epigram
    EPL 
    Easy Programming Language
    EPL 
    Eltron Programming Language
    Erlang
    es
    Escher
    ESPOL
    Esterel
    Etoys
    Euclid
    Euler
    Euphoria
    EusLisp Robot Programming Language
    CMS EXEC 
    EXEC
    EXEC 2
    Executable UML
    F
    F#
    F*
    Factor
    Fantom
    FAUST
    FFP
    Fjölnir
    FL
    Flavors
    Flex
    FlooP
    FLOW-MATIC
    FOCAL
    FOCUS
    FOIL
    FORMAC
    @Formula
    Forth
    Fortran
    Fortress
    FoxBase
    FoxPro
    FP
    Franz Lisp
    F-Script
    G
    Game Maker Language
    GameMonkey Script
    GAMS
    GAP
    G-code
    GDScript
    Genie
    GDL
    GJ
    GEORGE
    GLSL
    GNU E
    GM
    Go
    Go!
    GOAL
    Gödel
    Golo
    GOM 
    Good Old Mad
    Google Apps Script
    Gosu
    GOTRAN
    GPSS
    GraphTalk
    GRASS
    Groovy
    Hack
    HAGGIS
    HAL/S
    Halide 
    Hamilton C shell
    Harbour
    Hartmann pipelines
    Haskell
    Haxe
    Hermes
    High Level Assembly
    HLSL
    HolyC
    Hop
    Hopscotch
    Hope
    Hugo
    Hume
    HyperTalk
    Hexa
    Io
    Icon 
    IBM Basic assembly language
    IBM BASICA
    IBM HAScript
    IBM Informix-4GL
    IBM RPG
    IDL
    Idris
    J
    J#
    J++
    JADE
    JAL
    Janus 
    concurrent constraint programming language
    Janus 
    time-reversible computing programming language
    JASS
    Java
    JavaFX Script
    JavaScript
    JCL
    JEAN
    Join Java
    JOSS
    Joule
    JOVIAL
    Joy
    JScript
    JScript .NET
    JSON
    jq
    Julia
    Jython
    K
    Kaleidoscope
    Karel
    Karel++
    KEE
    Kixtart
    Klerer-May System
    KIF
    Kojo
    Kotlin
    KRC
    KRL
    KRL 
    KUKA Robot Language
    KRYPTON
    Korn shell (ksh)
    Kodu
    Kv
    LabVIEW
    Ladder
    LANSA
    Lasso
    LaTeX
    Lava
    LC-3
    Leda
    Legoscript
    LIL
    LilyPond
    Limbo
    Limnor
    LINC
    Lingo
    LINQ
    LIS
    LISA
    Lisp
    Lite-C
    Lithe
    Little b
    LLL
    Logo
    Logtalk
    LotusScript
    LPC
    LSE
    LSL
    LiveCode
    LiveScript
    Lua
    Lucid
    Lustre
    LYaPAS
    Lynx
    M
    M2001
    M4
    M#
    Machine code
    MAD 
    Michigan Algorithm Decoder
    MAD/I
    Magik
    Magma
    Maude system
    Maple
    MAPPER (now part of BIS)
    MARK-IV (now VISION:BUILDER)
    Mary
    MASM Microsoft Assembly x86
    MATH-MATIC
    Mathematica
    MATLAB
    Maxima 
    Macsyma
    Max (Max Msp – Graphical Programming Environment)
    MaxScript internal language 3D Studio Max
    Maya 
    MEL
    MDL
    Mercury
    Mesa
    Metafont
    MetaQuotes Language
    MQL4
    MQL5
    MHEG-5 
    Microcode
    MicroScript
    MIIS
    Milk 
    MIMIC
    Mirah
    Miranda
    MIVA Script
    ML
    Model 204
    Modelica
    Modula
    Modula-2
    Modula-3
    Mohol
    MOO
    Mortran
    Mouse
    MPD
    Mathcad
    MSIL – deprecated name for CIL
    MSL
    MUMPS
    MuPAD
    Mutan
    Mystic Programming Language 
    MPL
    NASM
    Napier88
    Neko
    Nemerle
    nesC
    NESL
    Net.Data
    NetLogo
    NetRexx
    NewLISP
    NEWP
    Newspeak
    NewtonScript
    Nial
    Nice
    Nickle (NITIN)
    Nim
    NPL
    Not eXactly C (NXC)
    Not Quite C (NQC)
    NSIS
    Nu
    NWScript
    NXT-G
    o:XML
    Oak
    Oberon
    OBJ2
    Object Lisp
    ObjectLOGO
    Object REXX
    Object Pascal
    Objective-C
    Objective-J
    Obliq
    OCaml
    occam
    occam-π
    Octave
    OmniMark
    Onyx
    Opa
    Opal
    OpenCL
    OpenEdge ABL
    OPL
    OpenVera
    OPS5
    OptimJ
    Orc
    ORCA/Modula-2
    Oriel
    Orwell
    Oxygene
    Oz
    P
    P4
    P′′
    ParaSail 
    PARI/GP
    Pascal
    PCASTL
    PCF
    PEARL
    PeopleCode
    Perl
    PDL
    Perl 6
    Pharo
    PHP
    Pico
    Picolisp
    Pict
    Pig (programming tool)
    Pike
    PIKT
    PILOT
    Pipelines
    Pizza
    PL-11
    PL/0
    PL/B
    PL/C
    PL/I
    PL/M
    PL/P
    PL/SQL
    PL360
    PLANC
    Plankalkül
    Planner
    PLEX
    PLEXIL
    Plus
    POP-11
    POP-2
    PostScript
    PortablE
    Powerhouse
    PowerBuilder – 4GL GUI application generator from Sybase
    PowerShell
    PPL
    Processing
    Processing.js
    Prograph
    PROIV
    Prolog
    PROMAL
    Promela
    PROSE modeling language
    PROTEL
    ProvideX
    Pro*C
    Pure
    PureBasic
    Pure Data
    Python
    Q
    equational programming language
    Q 
    programming language from Kx Systems
    Q# 
    Microsoft programming language
    Qalb
    QtScript
    QuakeC
    QPL
    R
    R++
    Racket
    RAPID
    Rapira
    Ratfiv
    Ratfor
    rc
    REBOL
    Red
    Redcode
    REFAL
    Reia
    REXX
    Ring
    Rlab
    ROOP
    RPG
    RPL
    RSL
    RTL/2
    Ruby
    RuneScript
    Rust
    S
    S2
    S3
    S-Lang
    S-PLUS
    SA-C
    SabreTalk
    SAIL
    SALSA
    SAM76
    SAS
    SASL
    Sather
    Sawzall
    SBL
    Scala
    Scheme
    Scilab
    Script.NET
    Sed
    Seed7
    Self
    SenseTalk
    SequenceL
    Serpent
    SETL
    SIMPOL
    SIGNAL
    SiMPLE
    SIMSCRIPT
    Simula
    Simulink
    Singularity
    SISAL
    SLIP
    SMALL
    Scratch
    Smalltalk
    SML
    Strongtalk
    Snap!
    SNOBOL (SPITBOL)
    Snowball
    SOL
    Solidity
    SOPHAEROS
    SPARK
    Speedcode
    SPIN
    SP/k
    SPS
    SQL
    SQR
    Squeak
    Squirrel
    SR
    S/SL
    Starlogo
    Strand
    Stata
    Stateflow
    Subtext
    SuperCollider
    SuperTalk
    Swift 
    Apple programming language
    Swift 
    SYMPL
    SystemVerilog
    T
    TACL
    TACPOL
    TADS
    TAL
    Tcl
    Tea
    TECO
    TELCOMP
    TeX
    TEX
    TIE
    TMG, compiler-compiler
    Tom
    TOM
    Toi
    Topspeed
    TPU
    Trac
    TTM
    T-SQL
    Transcript
    TTCN
    Turing
    TUTOR
    TXL
    TypeScript
    Tynker
    Ubercode
    UCSD Pascal
    Umple
    Unicon
    Uniface
    UNITY
    Unix shell
    UnrealScript
    Vala
    Verilog
    VHDL
    Vim script
    Viper
    Visual Basic
    Visual Basic .NET
    Visual DataFlex
    Visual DialogScript
    Visual Fortran
    Visual FoxPro
    Visual J++
    Visual J#
    Visual LISP
    Visual Objects
    Visual Prolog
    VSXu
    WATFIV, WATFOR
    WebAssembly
    WebDNA
    Whiley
    Winbatch
    Wolfram Language
    Wyvern
    X++
    X10
    xBase
    xBase++
    XBL
    XC 
    xHarbour
    XL
    Xojo
    XOTcl
    XOD 
    XPath
    XPL
    XPL0
    XQuery
    XSB
    XSharp
    XSLT
    Xtend
    Yorick
    YQL
    Yoix
    Z notation
    Zebra, ZPL, ZPL2
    Zeno
    ZetaLisp
    ZOPL
    Zsh
    ZPL
    Z++""".split('\n')))

    with open('./data/languages_wiki.json', 'w') as f:
        json.dump(list(languages), f)
        
    print('file saved to {}'.format('./data/languages_wiki.json'))
    
if __name__ == '__main__':
    main()    