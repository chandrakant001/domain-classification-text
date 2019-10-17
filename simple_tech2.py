
% Default to the notebook output style

    


% Inherit from the specified cell style.




    
\documentclass[11pt]{article}

    
    
    \usepackage[T1]{fontenc}
    % Nicer default font (+ math font) than Computer Modern for most use cases
    \usepackage{mathpazo}

    % Basic figure setup, for now with no caption control since it's done
    % automatically by Pandoc (which extracts ![](path) syntax from Markdown).
    \usepackage{graphicx}
    % We will generate all images so they have a width \maxwidth. This means
    % that they will get their normal width if they fit onto the page, but
    % are scaled down if they would overflow the margins.
    \makeatletter
    \def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth
    \else\Gin@nat@width\fi}
    \makeatother
    \let\Oldincludegraphics\includegraphics
    % Set max figure width to be 80% of text width, for now hardcoded.
    \renewcommand{\includegraphics}[1]{\Oldincludegraphics[width=.8\maxwidth]{#1}}
    % Ensure that by default, figures have no caption (until we provide a
    % proper Figure object with a Caption API and a way to capture that
    % in the conversion process - todo).
    \usepackage{caption}
    \DeclareCaptionLabelFormat{nolabel}{}
    \captionsetup{labelformat=nolabel}

    \usepackage{adjustbox} % Used to constrain images to a maximum size 
    \usepackage{xcolor} % Allow colors to be defined
    \usepackage{enumerate} % Needed for markdown enumerations to work
    \usepackage{geometry} % Used to adjust the document margins
    \usepackage{amsmath} % Equations
    \usepackage{amssymb} % Equations
    \usepackage{textcomp} % defines textquotesingle
    % Hack from http://tex.stackexchange.com/a/47451/13684:
    \AtBeginDocument{%
        \def\PYZsq{\textquotesingle}% Upright quotes in Pygmentized code
    }
    \usepackage{upquote} % Upright quotes for verbatim code
    \usepackage{eurosym} % defines \euro
    \usepackage[mathletters]{ucs} % Extended unicode (utf-8) support
    \usepackage[utf8x]{inputenc} % Allow utf-8 characters in the tex document
    \usepackage{fancyvrb} % verbatim replacement that allows latex
    \usepackage{grffile} % extends the file name processing of package graphics 
                         % to support a larger range 
    % The hyperref package gives us a pdf with properly built
    % internal navigation ('pdf bookmarks' for the table of contents,
    % internal cross-reference links, web links for URLs, etc.)
    \usepackage{hyperref}
    \usepackage{longtable} % longtable support required by pandoc >1.10
    \usepackage{booktabs}  % table support for pandoc > 1.12.2
    \usepackage[inline]{enumitem} % IRkernel/repr support (it uses the enumerate* environment)
    \usepackage[normalem]{ulem} % ulem is needed to support strikethroughs (\sout)
                                % normalem makes italics be italics, not underlines
    

    
    
    % Colors for the hyperref package
    \definecolor{urlcolor}{rgb}{0,.145,.698}
    \definecolor{linkcolor}{rgb}{.71,0.21,0.01}
    \definecolor{citecolor}{rgb}{.12,.54,.11}

    % ANSI colors
    \definecolor{ansi-black}{HTML}{3E424D}
    \definecolor{ansi-black-intense}{HTML}{282C36}
    \definecolor{ansi-red}{HTML}{E75C58}
    \definecolor{ansi-red-intense}{HTML}{B22B31}
    \definecolor{ansi-green}{HTML}{00A250}
    \definecolor{ansi-green-intense}{HTML}{007427}
    \definecolor{ansi-yellow}{HTML}{DDB62B}
    \definecolor{ansi-yellow-intense}{HTML}{B27D12}
    \definecolor{ansi-blue}{HTML}{208FFB}
    \definecolor{ansi-blue-intense}{HTML}{0065CA}
    \definecolor{ansi-magenta}{HTML}{D160C4}
    \definecolor{ansi-magenta-intense}{HTML}{A03196}
    \definecolor{ansi-cyan}{HTML}{60C6C8}
    \definecolor{ansi-cyan-intense}{HTML}{258F8F}
    \definecolor{ansi-white}{HTML}{C5C1B4}
    \definecolor{ansi-white-intense}{HTML}{A1A6B2}

    % commands and environments needed by pandoc snippets
    % extracted from the output of `pandoc -s`
    \providecommand{\tightlist}{%
      \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
    \DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\}}
    % Add ',fontsize=\small' for more characters per line
    \newenvironment{Shaded}{}{}
    \newcommand{\KeywordTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{\textbf{{#1}}}}
    \newcommand{\DataTypeTok}[1]{\textcolor[rgb]{0.56,0.13,0.00}{{#1}}}
    \newcommand{\DecValTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
    \newcommand{\BaseNTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
    \newcommand{\FloatTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
    \newcommand{\CharTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
    \newcommand{\StringTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
    \newcommand{\CommentTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textit{{#1}}}}
    \newcommand{\OtherTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{{#1}}}
    \newcommand{\AlertTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{{#1}}}}
    \newcommand{\FunctionTok}[1]{\textcolor[rgb]{0.02,0.16,0.49}{{#1}}}
    \newcommand{\RegionMarkerTok}[1]{{#1}}
    \newcommand{\ErrorTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{{#1}}}}
    \newcommand{\NormalTok}[1]{{#1}}
    
    % Additional commands for more recent versions of Pandoc
    \newcommand{\ConstantTok}[1]{\textcolor[rgb]{0.53,0.00,0.00}{{#1}}}
    \newcommand{\SpecialCharTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
    \newcommand{\VerbatimStringTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
    \newcommand{\SpecialStringTok}[1]{\textcolor[rgb]{0.73,0.40,0.53}{{#1}}}
    \newcommand{\ImportTok}[1]{{#1}}
    \newcommand{\DocumentationTok}[1]{\textcolor[rgb]{0.73,0.13,0.13}{\textit{{#1}}}}
    \newcommand{\AnnotationTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
    \newcommand{\CommentVarTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
    \newcommand{\VariableTok}[1]{\textcolor[rgb]{0.10,0.09,0.49}{{#1}}}
    \newcommand{\ControlFlowTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{\textbf{{#1}}}}
    \newcommand{\OperatorTok}[1]{\textcolor[rgb]{0.40,0.40,0.40}{{#1}}}
    \newcommand{\BuiltInTok}[1]{{#1}}
    \newcommand{\ExtensionTok}[1]{{#1}}
    \newcommand{\PreprocessorTok}[1]{\textcolor[rgb]{0.74,0.48,0.00}{{#1}}}
    \newcommand{\AttributeTok}[1]{\textcolor[rgb]{0.49,0.56,0.16}{{#1}}}
    \newcommand{\InformationTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
    \newcommand{\WarningTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textbf{\textit{{#1}}}}}
    
    
    % Define a nice break command that doesn't care if a line doesn't already
    % exist.
    \def\br{\hspace*{\fill} \\* }
    % Math Jax compatability definitions
    \def\gt{>}
    \def\lt{<}
    % Document parameters
    \title{simple\_tech2}
    
    
    

    % Pygments definitions
    
\makeatletter
\def\PY@reset{\let\PY@it=\relax \let\PY@bf=\relax%
    \let\PY@ul=\relax \let\PY@tc=\relax%
    \let\PY@bc=\relax \let\PY@ff=\relax}
\def\PY@tok#1{\csname PY@tok@#1\endcsname}
\def\PY@toks#1+{\ifx\relax#1\empty\else%
    \PY@tok{#1}\expandafter\PY@toks\fi}
\def\PY@do#1{\PY@bc{\PY@tc{\PY@ul{%
    \PY@it{\PY@bf{\PY@ff{#1}}}}}}}
\def\PY#1#2{\PY@reset\PY@toks#1+\relax+\PY@do{#2}}

\expandafter\def\csname PY@tok@w\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.73,0.73}{##1}}}
\expandafter\def\csname PY@tok@c\endcsname{\let\PY@it=\textit\def\PY@tc##1{\textcolor[rgb]{0.25,0.50,0.50}{##1}}}
\expandafter\def\csname PY@tok@cp\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.74,0.48,0.00}{##1}}}
\expandafter\def\csname PY@tok@k\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@kp\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@kt\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.69,0.00,0.25}{##1}}}
\expandafter\def\csname PY@tok@o\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@ow\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.67,0.13,1.00}{##1}}}
\expandafter\def\csname PY@tok@nb\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@nf\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.00,1.00}{##1}}}
\expandafter\def\csname PY@tok@nc\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.00,1.00}{##1}}}
\expandafter\def\csname PY@tok@nn\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.00,1.00}{##1}}}
\expandafter\def\csname PY@tok@ne\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.82,0.25,0.23}{##1}}}
\expandafter\def\csname PY@tok@nv\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.10,0.09,0.49}{##1}}}
\expandafter\def\csname PY@tok@no\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.53,0.00,0.00}{##1}}}
\expandafter\def\csname PY@tok@nl\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.63,0.63,0.00}{##1}}}
\expandafter\def\csname PY@tok@ni\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.60,0.60,0.60}{##1}}}
\expandafter\def\csname PY@tok@na\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.49,0.56,0.16}{##1}}}
\expandafter\def\csname PY@tok@nt\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@nd\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.67,0.13,1.00}{##1}}}
\expandafter\def\csname PY@tok@s\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@sd\endcsname{\let\PY@it=\textit\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@si\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.73,0.40,0.53}{##1}}}
\expandafter\def\csname PY@tok@se\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.73,0.40,0.13}{##1}}}
\expandafter\def\csname PY@tok@sr\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.40,0.53}{##1}}}
\expandafter\def\csname PY@tok@ss\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.10,0.09,0.49}{##1}}}
\expandafter\def\csname PY@tok@sx\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@m\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@gh\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.00,0.50}{##1}}}
\expandafter\def\csname PY@tok@gu\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.50,0.00,0.50}{##1}}}
\expandafter\def\csname PY@tok@gd\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.63,0.00,0.00}{##1}}}
\expandafter\def\csname PY@tok@gi\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.63,0.00}{##1}}}
\expandafter\def\csname PY@tok@gr\endcsname{\def\PY@tc##1{\textcolor[rgb]{1.00,0.00,0.00}{##1}}}
\expandafter\def\csname PY@tok@ge\endcsname{\let\PY@it=\textit}
\expandafter\def\csname PY@tok@gs\endcsname{\let\PY@bf=\textbf}
\expandafter\def\csname PY@tok@gp\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.00,0.50}{##1}}}
\expandafter\def\csname PY@tok@go\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.53,0.53,0.53}{##1}}}
\expandafter\def\csname PY@tok@gt\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.27,0.87}{##1}}}
\expandafter\def\csname PY@tok@err\endcsname{\def\PY@bc##1{\setlength{\fboxsep}{0pt}\fcolorbox[rgb]{1.00,0.00,0.00}{1,1,1}{\strut ##1}}}
\expandafter\def\csname PY@tok@kc\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@kd\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@kn\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@kr\endcsname{\let\PY@bf=\textbf\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@bp\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.50,0.00}{##1}}}
\expandafter\def\csname PY@tok@fm\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.00,0.00,1.00}{##1}}}
\expandafter\def\csname PY@tok@vc\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.10,0.09,0.49}{##1}}}
\expandafter\def\csname PY@tok@vg\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.10,0.09,0.49}{##1}}}
\expandafter\def\csname PY@tok@vi\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.10,0.09,0.49}{##1}}}
\expandafter\def\csname PY@tok@vm\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.10,0.09,0.49}{##1}}}
\expandafter\def\csname PY@tok@sa\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@sb\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@sc\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@dl\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@s2\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@sh\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@s1\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.73,0.13,0.13}{##1}}}
\expandafter\def\csname PY@tok@mb\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@mf\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@mh\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@mi\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@il\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@mo\endcsname{\def\PY@tc##1{\textcolor[rgb]{0.40,0.40,0.40}{##1}}}
\expandafter\def\csname PY@tok@ch\endcsname{\let\PY@it=\textit\def\PY@tc##1{\textcolor[rgb]{0.25,0.50,0.50}{##1}}}
\expandafter\def\csname PY@tok@cm\endcsname{\let\PY@it=\textit\def\PY@tc##1{\textcolor[rgb]{0.25,0.50,0.50}{##1}}}
\expandafter\def\csname PY@tok@cpf\endcsname{\let\PY@it=\textit\def\PY@tc##1{\textcolor[rgb]{0.25,0.50,0.50}{##1}}}
\expandafter\def\csname PY@tok@c1\endcsname{\let\PY@it=\textit\def\PY@tc##1{\textcolor[rgb]{0.25,0.50,0.50}{##1}}}
\expandafter\def\csname PY@tok@cs\endcsname{\let\PY@it=\textit\def\PY@tc##1{\textcolor[rgb]{0.25,0.50,0.50}{##1}}}

\def\PYZbs{\char`\\}
\def\PYZus{\char`\_}
\def\PYZob{\char`\{}
\def\PYZcb{\char`\}}
\def\PYZca{\char`\^}
\def\PYZam{\char`\&}
\def\PYZlt{\char`\<}
\def\PYZgt{\char`\>}
\def\PYZsh{\char`\#}
\def\PYZpc{\char`\%}
\def\PYZdl{\char`\$}
\def\PYZhy{\char`\-}
\def\PYZsq{\char`\'}
\def\PYZdq{\char`\"}
\def\PYZti{\char`\~}
% for compatibility with earlier versions
\def\PYZat{@}
\def\PYZlb{[}
\def\PYZrb{]}
\makeatother


    % Exact colors from NB
    \definecolor{incolor}{rgb}{0.0, 0.0, 0.5}
    \definecolor{outcolor}{rgb}{0.545, 0.0, 0.0}



    
    % Prevent overflowing lines due to hard-to-break entities
    \sloppy 
    % Setup hyperref package
    \hypersetup{
      breaklinks=true,  % so long urls are correctly broken across lines
      colorlinks=true,
      urlcolor=urlcolor,
      linkcolor=linkcolor,
      citecolor=citecolor,
      }
    % Slightly bigger margins than the latex defaults
    
    \geometry{verbose,tmargin=1in,bmargin=1in,lmargin=1in,rmargin=1in}
    
    

    \begin{document}
    
    
    \maketitle
    
    

    
    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}10}]:} \PY{c+c1}{\PYZsh{} !pip3 install opencv\PYZhy{}contrib\PYZhy{}python}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}4}]:} \PY{k+kn}{from} \PY{n+nn}{imutils}\PY{n+nn}{.}\PY{n+nn}{object\PYZus{}detection} \PY{k}{import} \PY{n}{non\PYZus{}max\PYZus{}suppression}
        \PY{k+kn}{import} \PY{n+nn}{numpy} \PY{k}{as} \PY{n+nn}{np}
        \PY{k+kn}{import} \PY{n+nn}{pytesseract}
        \PY{k+kn}{import} \PY{n+nn}{argparse}
        \PY{k+kn}{import} \PY{n+nn}{cv2}
        \PY{n}{img} \PY{o}{=}\PY{n}{cv2}\PY{o}{.}\PY{n}{imread}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{/home/nextjob/bill1.jpg}\PY{l+s+s1}{\PYZsq{}}\PY{p}{)}
        \PY{c+c1}{\PYZsh{} figure}
        \PY{c+c1}{\PYZsh{} \PYZsh{} cv2.imread(path) }
        \PY{c+c1}{\PYZsh{} cv2.imshow(\PYZsq{}img\PYZsq{},img)}
        \PY{c+c1}{\PYZsh{} \PYZsh{} title(\PYZsq{}Original Image\PYZsq{})}
        \PY{c+c1}{\PYZsh{} cv2.waitKey(0) }
        \PY{c+c1}{\PYZsh{} cv2.destroyAllWindows()}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor} }]:} \PY{k+kn}{import} \PY{n+nn}{numpy} \PY{k}{as} \PY{n+nn}{np}
        \PY{c+c1}{\PYZsh{} image = np.array(img, dtype=np.uint8)}
        \PY{n}{grayscaled} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{cvtColor}\PY{p}{(}\PY{n}{img}\PY{p}{,}\PY{n}{cv2}\PY{o}{.}\PY{n}{COLOR\PYZus{}BGR2GRAY}\PY{p}{)}
        \PY{c+c1}{\PYZsh{} retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH\PYZus{}BINARY)}
        \PY{n}{th} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{adaptiveThreshold}\PY{p}{(}\PY{n}{grayscaled}\PY{p}{,} \PY{l+m+mi}{255}\PY{p}{,} \PY{n}{cv2}\PY{o}{.}\PY{n}{ADAPTIVE\PYZus{}THRESH\PYZus{}GAUSSIAN\PYZus{}C}\PY{p}{,} \PY{n}{cv2}\PY{o}{.}\PY{n}{THRESH\PYZus{}BINARY}\PY{p}{,} \PY{l+m+mi}{115}\PY{p}{,} \PY{l+m+mi}{3}\PY{p}{)}
        
        \PY{n}{cv2}\PY{o}{.}\PY{n}{imshow}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{original}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{n}{img}\PY{p}{)}
        \PY{n}{cv2}\PY{o}{.}\PY{n}{imshow}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{threshold}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{n}{th}\PY{p}{)}
        \PY{n}{cv2}\PY{o}{.}\PY{n}{waitKey}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{)}
        \PY{n}{cv2}\PY{o}{.}\PY{n}{destroyAllWindows}\PY{p}{(}\PY{p}{)}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}1}]:} \PY{n}{BW} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{imbinarize}\PY{p}{(}\PY{n}{img}\PY{p}{,}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{adaptive}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{ForegroundPolarity}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{dark}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{Sensitivity}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{l+m+mf}{0.4}\PY{p}{)}\PY{p}{;}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]

        ---------------------------------------------------------------------------

        NameError                                 Traceback (most recent call last)

        <ipython-input-1-a175d5bb0e46> in <module>()
    ----> 1 BW = cv2.imbinarize(I,'adaptive','ForegroundPolarity','dark','Sensitivity',0.4);
    

        NameError: name 'cv2' is not defined

    \end{Verbatim}

    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}4}]:} \PY{n}{cv2}\PY{o}{.}\PY{n}{imshow}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{img}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{n}{BW}\PY{p}{)}
        \PY{c+c1}{\PYZsh{} title(\PYZsq{}Original Image\PYZsq{})}
        \PY{n}{cv2}\PY{o}{.}\PY{n}{waitKey}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{)} 
        \PY{n}{cv2}\PY{o}{.}\PY{n}{destoryAllWindows}\PY{p}{(}\PY{p}{)}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]

        ---------------------------------------------------------------------------

        NameError                                 Traceback (most recent call last)

        <ipython-input-4-c8a30a852c38> in <module>()
    ----> 1 cv2.imshow('img',BW)
          2 \# title('Original Image')
          3 cv2.waitKey(0)
          4 cv2.destoryAllWindows()


        NameError: name 'BW' is not defined

    \end{Verbatim}

    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}37}]:} \PY{k}{def} \PY{n+nf}{kmeans}\PY{p}{(}\PY{n}{input\PYZus{}img}\PY{p}{,} \PY{n}{k}\PY{p}{,} \PY{n}{i\PYZus{}val}\PY{p}{)}\PY{p}{:}
             \PY{n}{hist} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{calcHist}\PY{p}{(}\PY{p}{[}\PY{n}{input\PYZus{}img}\PY{p}{]}\PY{p}{,}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{]}\PY{p}{,}\PY{k+kc}{None}\PY{p}{,}\PY{p}{[}\PY{l+m+mi}{256}\PY{p}{]}\PY{p}{,}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{,}\PY{l+m+mi}{256}\PY{p}{]}\PY{p}{)}
             \PY{n}{img} \PY{o}{=} \PY{n}{input\PYZus{}img}\PY{o}{.}\PY{n}{ravel}\PY{p}{(}\PY{p}{)}
             \PY{n}{img} \PY{o}{=} \PY{n}{np}\PY{o}{.}\PY{n}{reshape}\PY{p}{(}\PY{n}{img}\PY{p}{,} \PY{p}{(}\PY{o}{\PYZhy{}}\PY{l+m+mi}{1}\PY{p}{,} \PY{l+m+mi}{1}\PY{p}{)}\PY{p}{)}
             \PY{n}{img} \PY{o}{=} \PY{n}{img}\PY{o}{.}\PY{n}{astype}\PY{p}{(}\PY{n}{np}\PY{o}{.}\PY{n}{float32}\PY{p}{)}
         
             \PY{n}{criteria} \PY{o}{=} \PY{p}{(}\PY{n}{cv2}\PY{o}{.}\PY{n}{TERM\PYZus{}CRITERIA\PYZus{}EPS} \PY{o}{+} \PY{n}{cv2}\PY{o}{.}\PY{n}{TERM\PYZus{}CRITERIA\PYZus{}MAX\PYZus{}ITER}\PY{p}{,} \PY{l+m+mi}{10}\PY{p}{,} \PY{l+m+mf}{1.0}\PY{p}{)}
             \PY{n}{flags} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{KMEANS\PYZus{}RANDOM\PYZus{}CENTERS}
             \PY{n}{compactness}\PY{p}{,}\PY{n}{labels}\PY{p}{,}\PY{n}{centers} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{kmeans}\PY{p}{(}\PY{n}{img}\PY{p}{,}\PY{n}{k}\PY{p}{,}\PY{k+kc}{None}\PY{p}{,}\PY{n}{criteria}\PY{p}{,}\PY{l+m+mi}{10}\PY{p}{,}\PY{n}{flags}\PY{p}{)}
             \PY{n}{centers} \PY{o}{=} \PY{n}{np}\PY{o}{.}\PY{n}{sort}\PY{p}{(}\PY{n}{centers}\PY{p}{,} \PY{n}{axis}\PY{o}{=}\PY{l+m+mi}{0}\PY{p}{)}
         
             \PY{k}{return} \PY{n}{centers}\PY{p}{[}\PY{n}{i\PYZus{}val}\PY{p}{]}\PY{o}{.}\PY{n}{astype}\PY{p}{(}\PY{n+nb}{int}\PY{p}{)}\PY{p}{,} \PY{n}{centers}\PY{p}{,} \PY{n}{hist}
         
         \PY{n}{img} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{imread}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{/home/nextjob/Create\PYZus{}Online.jpg}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,} \PY{l+m+mi}{0}\PY{p}{)}
         \PY{n}{\PYZus{}}\PY{p}{,} \PY{n}{thresh} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{threshold}\PY{p}{(}\PY{n}{img}\PY{p}{,} \PY{n}{kmeans}\PY{p}{(}\PY{n}{input\PYZus{}img}\PY{o}{=}\PY{n}{img}\PY{p}{,} \PY{n}{k}\PY{o}{=}\PY{l+m+mi}{8}\PY{p}{,} \PY{n}{i\PYZus{}val}\PY{o}{=}\PY{l+m+mi}{2}\PY{p}{)}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{]}\PY{p}{,} \PY{l+m+mi}{255}\PY{p}{,} \PY{n}{cv2}\PY{o}{.}\PY{n}{THRESH\PYZus{}BINARY}\PY{p}{)}
         \PY{n}{cv2}\PY{o}{.}\PY{n}{imwrite}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{text.png}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{n}{thresh}\PY{p}{)}
         \PY{n}{cv2}\PY{o}{.}\PY{n}{imshow}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{threshold}\PY{l+s+s1}{\PYZsq{}}\PY{p}{,}\PY{n}{thresh}\PY{p}{)}
         \PY{n}{cv2}\PY{o}{.}\PY{n}{waitKey}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{)}
         \PY{n}{cv2}\PY{o}{.}\PY{n}{destroyAllWindows}\PY{p}{(}\PY{p}{)}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}34}]:} \PY{c+c1}{\PYZsh{} remove\PYZus{}noise\PYZus{}and\PYZus{}smooth(\PYZsq{}/home/nextjob/bill1.jpg\PYZsq{})}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}35}]:} \PY{n}{text}\PY{o}{=}\PY{n}{pytesseract}\PY{o}{.}\PY{n}{image\PYZus{}to\PYZus{}string}\PY{p}{(}\PY{n}{img}\PY{p}{,}\PY{n}{lang}\PY{o}{=}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{eng}\PY{l+s+s1}{\PYZsq{}}\PY{p}{)}
         \PY{n}{text}
\end{Verbatim}


\begin{Verbatim}[commandchars=\\\{\}]
{\color{outcolor}Out[{\color{outcolor}35}]:} 'Brand Name Inc.\textbackslash{}n\textbackslash{}nA Message From Your Company\textbackslash{}n\textbackslash{}nFull Name\textbackslash{}nMain Title\textbackslash{}n\textbackslash{}n122 Main Street\textbackslash{}nCity, STATE, a013\textbackslash{}n\textbackslash{}n \textbackslash{}n\textbackslash{}ntel. (206) 555.\textbackslash{}nyou@emaiy\textbackslash{}n\textbackslash{}n1689\textbackslash{}nladdress.com'
\end{Verbatim}
            
    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}9}]:} \PY{k+kn}{from} \PY{n+nn}{imutils}\PY{n+nn}{.}\PY{n+nn}{object\PYZus{}detection} \PY{k}{import} \PY{n}{non\PYZus{}max\PYZus{}suppression}
        \PY{k+kn}{import} \PY{n+nn}{numpy} \PY{k}{as} \PY{n+nn}{np}
        \PY{k+kn}{import} \PY{n+nn}{pytesseract}
        \PY{k+kn}{import} \PY{n+nn}{argparse}
        \PY{k+kn}{import} \PY{n+nn}{cv2}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}10}]:} \PY{k}{def} \PY{n+nf}{decode\PYZus{}predictions}\PY{p}{(}\PY{n}{scores}\PY{p}{,} \PY{n}{geometry}\PY{p}{)}\PY{p}{:}
         	\PY{c+c1}{\PYZsh{} grab the number of rows and columns from the scores volume, then}
         	\PY{c+c1}{\PYZsh{} initialize our set of bounding box rectangles and corresponding}
         	\PY{c+c1}{\PYZsh{} confidence scores}
         	\PY{p}{(}\PY{n}{numRows}\PY{p}{,} \PY{n}{numCols}\PY{p}{)} \PY{o}{=} \PY{n}{scores}\PY{o}{.}\PY{n}{shape}\PY{p}{[}\PY{l+m+mi}{2}\PY{p}{:}\PY{l+m+mi}{4}\PY{p}{]}
         	\PY{n}{rects} \PY{o}{=} \PY{p}{[}\PY{p}{]}
         	\PY{n}{confidences} \PY{o}{=} \PY{p}{[}\PY{p}{]}
          
         	\PY{c+c1}{\PYZsh{} loop over the number of rows}
         	\PY{k}{for} \PY{n}{y} \PY{o+ow}{in} \PY{n+nb}{range}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{,} \PY{n}{numRows}\PY{p}{)}\PY{p}{:}
         		\PY{c+c1}{\PYZsh{} extract the scores (probabilities), followed by the}
         		\PY{c+c1}{\PYZsh{} geometrical data used to derive potential bounding box}
         		\PY{c+c1}{\PYZsh{} coordinates that surround text}
         		\PY{n}{scoresData} \PY{o}{=} \PY{n}{scores}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{0}\PY{p}{,} \PY{n}{y}\PY{p}{]}
         		\PY{n}{xData0} \PY{o}{=} \PY{n}{geometry}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{0}\PY{p}{,} \PY{n}{y}\PY{p}{]}
         		\PY{n}{xData1} \PY{o}{=} \PY{n}{geometry}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{1}\PY{p}{,} \PY{n}{y}\PY{p}{]}
         		\PY{n}{xData2} \PY{o}{=} \PY{n}{geometry}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{2}\PY{p}{,} \PY{n}{y}\PY{p}{]}
         		\PY{n}{xData3} \PY{o}{=} \PY{n}{geometry}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{3}\PY{p}{,} \PY{n}{y}\PY{p}{]}
         		\PY{n}{anglesData} \PY{o}{=} \PY{n}{geometry}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{4}\PY{p}{,} \PY{n}{y}\PY{p}{]}
          
         		\PY{c+c1}{\PYZsh{} loop over the number of columns}
         		\PY{k}{for} \PY{n}{x} \PY{o+ow}{in} \PY{n+nb}{range}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{,} \PY{n}{numCols}\PY{p}{)}\PY{p}{:}
         			\PY{c+c1}{\PYZsh{} if our score does not have sufficient probability,}
         			\PY{c+c1}{\PYZsh{} ignore it}
         			\PY{k}{if} \PY{n}{scoresData}\PY{p}{[}\PY{n}{x}\PY{p}{]} \PY{o}{\PYZlt{}} \PY{n}{args}\PY{p}{[}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{min\PYZus{}confidence}\PY{l+s+s2}{\PYZdq{}}\PY{p}{]}\PY{p}{:}
         				\PY{k}{continue}
          
         			\PY{c+c1}{\PYZsh{} compute the offset factor as our resulting feature}
         			\PY{c+c1}{\PYZsh{} maps will be 4x smaller than the input image}
         			\PY{p}{(}\PY{n}{offsetX}\PY{p}{,} \PY{n}{offsetY}\PY{p}{)} \PY{o}{=} \PY{p}{(}\PY{n}{x} \PY{o}{*} \PY{l+m+mf}{4.0}\PY{p}{,} \PY{n}{y} \PY{o}{*} \PY{l+m+mf}{4.0}\PY{p}{)}
          
         			\PY{c+c1}{\PYZsh{} extract the rotation angle for the prediction and}
         			\PY{c+c1}{\PYZsh{} then compute the sin and cosine}
         			\PY{n}{angle} \PY{o}{=} \PY{n}{anglesData}\PY{p}{[}\PY{n}{x}\PY{p}{]}
         			\PY{n}{cos} \PY{o}{=} \PY{n}{np}\PY{o}{.}\PY{n}{cos}\PY{p}{(}\PY{n}{angle}\PY{p}{)}
         			\PY{n}{sin} \PY{o}{=} \PY{n}{np}\PY{o}{.}\PY{n}{sin}\PY{p}{(}\PY{n}{angle}\PY{p}{)}
          
         			\PY{c+c1}{\PYZsh{} use the geometry volume to derive the width and height}
         			\PY{c+c1}{\PYZsh{} of the bounding box}
         			\PY{n}{h} \PY{o}{=} \PY{n}{xData0}\PY{p}{[}\PY{n}{x}\PY{p}{]} \PY{o}{+} \PY{n}{xData2}\PY{p}{[}\PY{n}{x}\PY{p}{]}
         			\PY{n}{w} \PY{o}{=} \PY{n}{xData1}\PY{p}{[}\PY{n}{x}\PY{p}{]} \PY{o}{+} \PY{n}{xData3}\PY{p}{[}\PY{n}{x}\PY{p}{]}
          
         			\PY{c+c1}{\PYZsh{} compute both the starting and ending (x, y)\PYZhy{}coordinates}
         			\PY{c+c1}{\PYZsh{} for the text prediction bounding box}
         			\PY{n}{endX} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{offsetX} \PY{o}{+} \PY{p}{(}\PY{n}{cos} \PY{o}{*} \PY{n}{xData1}\PY{p}{[}\PY{n}{x}\PY{p}{]}\PY{p}{)} \PY{o}{+} \PY{p}{(}\PY{n}{sin} \PY{o}{*} \PY{n}{xData2}\PY{p}{[}\PY{n}{x}\PY{p}{]}\PY{p}{)}\PY{p}{)}
         			\PY{n}{endY} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{offsetY} \PY{o}{\PYZhy{}} \PY{p}{(}\PY{n}{sin} \PY{o}{*} \PY{n}{xData1}\PY{p}{[}\PY{n}{x}\PY{p}{]}\PY{p}{)} \PY{o}{+} \PY{p}{(}\PY{n}{cos} \PY{o}{*} \PY{n}{xData2}\PY{p}{[}\PY{n}{x}\PY{p}{]}\PY{p}{)}\PY{p}{)}
         			\PY{n}{startX} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{endX} \PY{o}{\PYZhy{}} \PY{n}{w}\PY{p}{)}
         			\PY{n}{startY} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{endY} \PY{o}{\PYZhy{}} \PY{n}{h}\PY{p}{)}
          
         			\PY{c+c1}{\PYZsh{} add the bounding box coordinates and probability score}
         			\PY{c+c1}{\PYZsh{} to our respective lists}
         			\PY{n}{rects}\PY{o}{.}\PY{n}{append}\PY{p}{(}\PY{p}{(}\PY{n}{startX}\PY{p}{,} \PY{n}{startY}\PY{p}{,} \PY{n}{endX}\PY{p}{,} \PY{n}{endY}\PY{p}{)}\PY{p}{)}
         			\PY{n}{confidences}\PY{o}{.}\PY{n}{append}\PY{p}{(}\PY{n}{scoresData}\PY{p}{[}\PY{n}{x}\PY{p}{]}\PY{p}{)}
          
         	\PY{c+c1}{\PYZsh{} return a tuple of the bounding boxes and associated confidences}
         	\PY{k}{return} \PY{p}{(}\PY{n}{rects}\PY{p}{,} \PY{n}{confidences}\PY{p}{)}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}12}]:} \PY{c+c1}{\PYZsh{} \PYZsh{} construct the argument parser and parse the arguments}
         \PY{c+c1}{\PYZsh{} ap = argparse.ArgumentParser()}
         \PY{c+c1}{\PYZsh{} ap.add\PYZus{}argument(\PYZdq{}\PYZhy{}i\PYZdq{}, \PYZdq{}\PYZhy{}\PYZhy{}image\PYZdq{}, type=str,help=\PYZdq{}path to input image\PYZdq{})}
         \PY{c+c1}{\PYZsh{} ap.add\PYZus{}argument(\PYZdq{}\PYZhy{}east\PYZdq{}, \PYZdq{}\PYZhy{}\PYZhy{}east\PYZdq{}, type=str,help=\PYZdq{}path to input EAST text detector\PYZdq{})}
         \PY{c+c1}{\PYZsh{} ap.add\PYZus{}argument(\PYZdq{}\PYZhy{}c\PYZdq{}, \PYZdq{}\PYZhy{}\PYZhy{}min\PYZhy{}confidence\PYZdq{}, type=float, default=0.5,help=\PYZdq{}minimum probability required to inspect a region\PYZdq{})}
         \PY{c+c1}{\PYZsh{} ap.add\PYZus{}argument(\PYZdq{}\PYZhy{}w\PYZdq{}, \PYZdq{}\PYZhy{}\PYZhy{}width\PYZdq{}, type=int, default=320,help=\PYZdq{}nearest multiple of 32 for resized width\PYZdq{})}
         \PY{c+c1}{\PYZsh{} ap.add\PYZus{}argument(\PYZdq{}\PYZhy{}e\PYZdq{}, \PYZdq{}\PYZhy{}\PYZhy{}height\PYZdq{}, type=int, default=320,help=\PYZdq{}nearest multiple of 32 for resized height\PYZdq{})}
         \PY{c+c1}{\PYZsh{} ap.add\PYZus{}argument(\PYZdq{}\PYZhy{}p\PYZdq{}, \PYZdq{}\PYZhy{}\PYZhy{}padding\PYZdq{}, type=float, default=0.0,help=\PYZdq{}amount of padding to add to each border of ROI\PYZdq{})}
         \PY{c+c1}{\PYZsh{} args = vars(ap.parse\PYZus{}args())}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
usage: ipykernel\_launcher.py [-h] [-i IMAGE] [-east EAST] [-c MIN\_CONFIDENCE]
                             [-w WIDTH] [-e HEIGHT] [-p PADDING]
ipykernel\_launcher.py: error: unrecognized arguments: -f /run/user/1000/jupyter/kernel-22105565-b251-446f-a1c3-ba5e8f09000c.json

    \end{Verbatim}

    \begin{Verbatim}[commandchars=\\\{\}]

        An exception has occurred, use \%tb to see the full traceback.


        SystemExit: 2


    \end{Verbatim}

    \begin{Verbatim}[commandchars=\\\{\}]
/home/nextjob/anaconda3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2870: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
  warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)

    \end{Verbatim}

    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}14}]:} \PY{c+c1}{\PYZsh{} load the input image and grab the image dimensions}
         \PY{n}{image} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{imread}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{/home/nextjob/bill1.jpg}\PY{l+s+s1}{\PYZsq{}}\PY{p}{)}
         \PY{n}{orig} \PY{o}{=} \PY{n}{image}\PY{o}{.}\PY{n}{copy}\PY{p}{(}\PY{p}{)}
         \PY{p}{(}\PY{n}{origH}\PY{p}{,} \PY{n}{origW}\PY{p}{)} \PY{o}{=} \PY{n}{image}\PY{o}{.}\PY{n}{shape}\PY{p}{[}\PY{p}{:}\PY{l+m+mi}{2}\PY{p}{]}
          
         \PY{c+c1}{\PYZsh{} set the new width and height and then determine the ratio in change}
         \PY{c+c1}{\PYZsh{} for both the width and height}
         \PY{p}{(}\PY{n}{newW}\PY{p}{,} \PY{n}{newH}\PY{p}{)} \PY{o}{=} \PY{p}{(}\PY{l+m+mi}{60}\PY{p}{,}\PY{l+m+mi}{60}\PY{p}{)}
         \PY{n}{rW} \PY{o}{=} \PY{n}{origW} \PY{o}{/} \PY{n+nb}{float}\PY{p}{(}\PY{n}{newW}\PY{p}{)}
         \PY{n}{rH} \PY{o}{=} \PY{n}{origH} \PY{o}{/} \PY{n+nb}{float}\PY{p}{(}\PY{n}{newH}\PY{p}{)}
          
         \PY{c+c1}{\PYZsh{} resize the image and grab the new image dimensions}
         \PY{n}{image} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{resize}\PY{p}{(}\PY{n}{image}\PY{p}{,} \PY{p}{(}\PY{n}{newW}\PY{p}{,} \PY{n}{newH}\PY{p}{)}\PY{p}{)}
         \PY{p}{(}\PY{n}{H}\PY{p}{,} \PY{n}{W}\PY{p}{)} \PY{o}{=} \PY{n}{image}\PY{o}{.}\PY{n}{shape}\PY{p}{[}\PY{p}{:}\PY{l+m+mi}{2}\PY{p}{]}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}15}]:} \PY{n}{layerNames} \PY{o}{=} \PY{p}{[}
         	\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{feature\PYZus{}fusion/Conv\PYZus{}7/Sigmoid}\PY{l+s+s2}{\PYZdq{}}\PY{p}{,}
         	\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{feature\PYZus{}fusion/concat\PYZus{}3}\PY{l+s+s2}{\PYZdq{}}\PY{p}{]}
          
         \PY{c+c1}{\PYZsh{} load the pre\PYZhy{}trained EAST text detector}
         \PY{n+nb}{print}\PY{p}{(}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{[INFO] loading EAST text detector...}\PY{l+s+s2}{\PYZdq{}}\PY{p}{)}
         \PY{n}{net} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{dnn}\PY{o}{.}\PY{n}{readNet}\PY{p}{(}\PY{l+s+s1}{\PYZsq{}}\PY{l+s+s1}{/home/nextjob/frozen\PYZus{}east\PYZus{}text\PYZus{}detection.pb}\PY{l+s+s1}{\PYZsq{}}\PY{p}{)}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
[INFO] loading EAST text detector{\ldots}

    \end{Verbatim}

    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor}16}]:} \PY{c+c1}{\PYZsh{} construct a blob from the image and then perform a forward pass of}
         \PY{c+c1}{\PYZsh{} the model to obtain the two output layer sets}
         \PY{n}{blob} \PY{o}{=} \PY{n}{cv2}\PY{o}{.}\PY{n}{dnn}\PY{o}{.}\PY{n}{blobFromImage}\PY{p}{(}\PY{n}{image}\PY{p}{,} \PY{l+m+mf}{1.0}\PY{p}{,} \PY{p}{(}\PY{n}{W}\PY{p}{,} \PY{n}{H}\PY{p}{)}\PY{p}{,}
         	\PY{p}{(}\PY{l+m+mf}{123.68}\PY{p}{,} \PY{l+m+mf}{116.78}\PY{p}{,} \PY{l+m+mf}{103.94}\PY{p}{)}\PY{p}{,} \PY{n}{swapRB}\PY{o}{=}\PY{k+kc}{True}\PY{p}{,} \PY{n}{crop}\PY{o}{=}\PY{k+kc}{False}\PY{p}{)}
         \PY{n}{net}\PY{o}{.}\PY{n}{setInput}\PY{p}{(}\PY{n}{blob}\PY{p}{)}
         \PY{p}{(}\PY{n}{scores}\PY{p}{,} \PY{n}{geometry}\PY{p}{)} \PY{o}{=} \PY{n}{net}\PY{o}{.}\PY{n}{forward}\PY{p}{(}\PY{n}{layerNames}\PY{p}{)}
          
         \PY{c+c1}{\PYZsh{} decode the predictions, then  apply non\PYZhy{}maxima suppression to}
         \PY{c+c1}{\PYZsh{} suppress weak, overlapping bounding boxes}
         \PY{p}{(}\PY{n}{rects}\PY{p}{,} \PY{n}{confidences}\PY{p}{)} \PY{o}{=} \PY{n}{decode\PYZus{}predictions}\PY{p}{(}\PY{n}{scores}\PY{p}{,} \PY{n}{geometry}\PY{p}{)}
         \PY{n}{boxes} \PY{o}{=} \PY{n}{non\PYZus{}max\PYZus{}suppression}\PY{p}{(}\PY{n}{np}\PY{o}{.}\PY{n}{array}\PY{p}{(}\PY{n}{rects}\PY{p}{)}\PY{p}{,} \PY{n}{probs}\PY{o}{=}\PY{n}{confidences}\PY{p}{)}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]

        ---------------------------------------------------------------------------

        error                                     Traceback (most recent call last)

        <ipython-input-16-89b7d3710983> in <module>()
          5 	(123.68, 116.78, 103.94), swapRB=True, crop=False)
          6 net.setInput(blob)
    ----> 7 (scores, geometry) = net.forward(layerNames)
          8 
          9 \# decode the predictions, then  apply non-maxima suppression to


        error: OpenCV(4.1.1) /io/opencv/modules/dnn/src/layers/concat\_layer.cpp:95: error: (-201:Incorrect size of input array) Inconsistent shape for ConcatLayer in function 'getMemoryShapes'


    \end{Verbatim}

    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor} }]:} \PY{n}{results} \PY{o}{=} \PY{p}{[}\PY{p}{]}
         
        \PY{c+c1}{\PYZsh{} loop over the bounding boxes}
        \PY{k}{for} \PY{p}{(}\PY{n}{startX}\PY{p}{,} \PY{n}{startY}\PY{p}{,} \PY{n}{endX}\PY{p}{,} \PY{n}{endY}\PY{p}{)} \PY{o+ow}{in} \PY{n}{boxes}\PY{p}{:}
        	\PY{c+c1}{\PYZsh{} scale the bounding box coordinates based on the respective}
        	\PY{c+c1}{\PYZsh{} ratios}
        	\PY{n}{startX} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{startX} \PY{o}{*} \PY{n}{rW}\PY{p}{)}
        	\PY{n}{startY} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{startY} \PY{o}{*} \PY{n}{rH}\PY{p}{)}
        	\PY{n}{endX} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{endX} \PY{o}{*} \PY{n}{rW}\PY{p}{)}
        	\PY{n}{endY} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{n}{endY} \PY{o}{*} \PY{n}{rH}\PY{p}{)}
         
        	\PY{c+c1}{\PYZsh{} in order to obtain a better OCR of the text we can potentially}
        	\PY{c+c1}{\PYZsh{} apply a bit of padding surrounding the bounding box \PYZhy{}\PYZhy{} here we}
        	\PY{c+c1}{\PYZsh{} are computing the deltas in both the x and y directions}
        	\PY{n}{dX} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{p}{(}\PY{n}{endX} \PY{o}{\PYZhy{}} \PY{n}{startX}\PY{p}{)} \PY{o}{*} \PY{n}{args}\PY{p}{[}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{padding}\PY{l+s+s2}{\PYZdq{}}\PY{p}{]}\PY{p}{)}
        	\PY{n}{dY} \PY{o}{=} \PY{n+nb}{int}\PY{p}{(}\PY{p}{(}\PY{n}{endY} \PY{o}{\PYZhy{}} \PY{n}{startY}\PY{p}{)} \PY{o}{*} \PY{n}{args}\PY{p}{[}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{padding}\PY{l+s+s2}{\PYZdq{}}\PY{p}{]}\PY{p}{)}
         
        	\PY{c+c1}{\PYZsh{} apply padding to each side of the bounding box, respectively}
        	\PY{n}{startX} \PY{o}{=} \PY{n+nb}{max}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{,} \PY{n}{startX} \PY{o}{\PYZhy{}} \PY{n}{dX}\PY{p}{)}
        	\PY{n}{startY} \PY{o}{=} \PY{n+nb}{max}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{,} \PY{n}{startY} \PY{o}{\PYZhy{}} \PY{n}{dY}\PY{p}{)}
        	\PY{n}{endX} \PY{o}{=} \PY{n+nb}{min}\PY{p}{(}\PY{n}{origW}\PY{p}{,} \PY{n}{endX} \PY{o}{+} \PY{p}{(}\PY{n}{dX} \PY{o}{*} \PY{l+m+mi}{2}\PY{p}{)}\PY{p}{)}
        	\PY{n}{endY} \PY{o}{=} \PY{n+nb}{min}\PY{p}{(}\PY{n}{origH}\PY{p}{,} \PY{n}{endY} \PY{o}{+} \PY{p}{(}\PY{n}{dY} \PY{o}{*} \PY{l+m+mi}{2}\PY{p}{)}\PY{p}{)}
         
        	\PY{c+c1}{\PYZsh{} extract the actual padded ROI}
        	\PY{n}{roi} \PY{o}{=} \PY{n}{orig}\PY{p}{[}\PY{n}{startY}\PY{p}{:}\PY{n}{endY}\PY{p}{,} \PY{n}{startX}\PY{p}{:}\PY{n}{endX}\PY{p}{]}
            \PY{n}{config} \PY{o}{=} \PY{p}{(}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{\PYZhy{}l eng \PYZhy{}\PYZhy{}oem 1 \PYZhy{}\PYZhy{}psm 7}\PY{l+s+s2}{\PYZdq{}}\PY{p}{)}
        	\PY{n}{text} \PY{o}{=} \PY{n}{pytesseract}\PY{o}{.}\PY{n}{image\PYZus{}to\PYZus{}string}\PY{p}{(}\PY{n}{roi}\PY{p}{,} \PY{n}{config}\PY{o}{=}\PY{n}{config}\PY{p}{)}
         
        	\PY{c+c1}{\PYZsh{} add the bounding box coordinates and OCR\PYZsq{}d text to the list}
        	\PY{c+c1}{\PYZsh{} of results}
        	\PY{n}{results}\PY{o}{.}\PY{n}{append}\PY{p}{(}\PY{p}{(}\PY{p}{(}\PY{n}{startX}\PY{p}{,} \PY{n}{startY}\PY{p}{,} \PY{n}{endX}\PY{p}{,} \PY{n}{endY}\PY{p}{)}\PY{p}{,} \PY{n}{text}\PY{p}{)}\PY{p}{)}
\end{Verbatim}


    \begin{Verbatim}[commandchars=\\\{\}]
{\color{incolor}In [{\color{incolor} }]:} \PY{c+c1}{\PYZsh{} sort the results bounding box coordinates from top to bottom}
        \PY{n}{results} \PY{o}{=} \PY{n+nb}{sorted}\PY{p}{(}\PY{n}{results}\PY{p}{,} \PY{n}{key}\PY{o}{=}\PY{k}{lambda} \PY{n}{r}\PY{p}{:}\PY{n}{r}\PY{p}{[}\PY{l+m+mi}{0}\PY{p}{]}\PY{p}{[}\PY{l+m+mi}{1}\PY{p}{]}\PY{p}{)}
         
        \PY{c+c1}{\PYZsh{} loop over the results}
        \PY{k}{for} \PY{p}{(}\PY{p}{(}\PY{n}{startX}\PY{p}{,} \PY{n}{startY}\PY{p}{,} \PY{n}{endX}\PY{p}{,} \PY{n}{endY}\PY{p}{)}\PY{p}{,} \PY{n}{text}\PY{p}{)} \PY{o+ow}{in} \PY{n}{results}\PY{p}{:}
        	\PY{c+c1}{\PYZsh{} display the text OCR\PYZsq{}d by Tesseract}
        	\PY{n+nb}{print}\PY{p}{(}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{OCR TEXT}\PY{l+s+s2}{\PYZdq{}}\PY{p}{)}
        	\PY{n+nb}{print}\PY{p}{(}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{========}\PY{l+s+s2}{\PYZdq{}}\PY{p}{)}
        	\PY{n+nb}{print}\PY{p}{(}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+si}{\PYZob{}\PYZcb{}}\PY{l+s+se}{\PYZbs{}n}\PY{l+s+s2}{\PYZdq{}}\PY{o}{.}\PY{n}{format}\PY{p}{(}\PY{n}{text}\PY{p}{)}\PY{p}{)}
         
        	\PY{c+c1}{\PYZsh{} strip out non\PYZhy{}ASCII text so we can draw the text on the image}
        	\PY{c+c1}{\PYZsh{} using OpenCV, then draw the text and a bounding box surrounding}
        	\PY{c+c1}{\PYZsh{} the text region of the input image}
        	\PY{n}{text} \PY{o}{=} \PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{\PYZdq{}}\PY{o}{.}\PY{n}{join}\PY{p}{(}\PY{p}{[}\PY{n}{c} \PY{k}{if} \PY{n+nb}{ord}\PY{p}{(}\PY{n}{c}\PY{p}{)} \PY{o}{\PYZlt{}} \PY{l+m+mi}{128} \PY{k}{else} \PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{\PYZdq{}} \PY{k}{for} \PY{n}{c} \PY{o+ow}{in} \PY{n}{text}\PY{p}{]}\PY{p}{)}\PY{o}{.}\PY{n}{strip}\PY{p}{(}\PY{p}{)}
        	\PY{n}{output} \PY{o}{=} \PY{n}{orig}\PY{o}{.}\PY{n}{copy}\PY{p}{(}\PY{p}{)}
        	\PY{n}{cv2}\PY{o}{.}\PY{n}{rectangle}\PY{p}{(}\PY{n}{output}\PY{p}{,} \PY{p}{(}\PY{n}{startX}\PY{p}{,} \PY{n}{startY}\PY{p}{)}\PY{p}{,} \PY{p}{(}\PY{n}{endX}\PY{p}{,} \PY{n}{endY}\PY{p}{)}\PY{p}{,}
        		\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{255}\PY{p}{)}\PY{p}{,} \PY{l+m+mi}{2}\PY{p}{)}
        	\PY{n}{cv2}\PY{o}{.}\PY{n}{putText}\PY{p}{(}\PY{n}{output}\PY{p}{,} \PY{n}{text}\PY{p}{,} \PY{p}{(}\PY{n}{startX}\PY{p}{,} \PY{n}{startY} \PY{o}{\PYZhy{}} \PY{l+m+mi}{20}\PY{p}{)}\PY{p}{,}
        		\PY{n}{cv2}\PY{o}{.}\PY{n}{FONT\PYZus{}HERSHEY\PYZus{}SIMPLEX}\PY{p}{,} \PY{l+m+mf}{1.2}\PY{p}{,} \PY{p}{(}\PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{0}\PY{p}{,} \PY{l+m+mi}{255}\PY{p}{)}\PY{p}{,} \PY{l+m+mi}{3}\PY{p}{)}
         
        	\PY{c+c1}{\PYZsh{} show the output image}
        	\PY{n}{cv2}\PY{o}{.}\PY{n}{imshow}\PY{p}{(}\PY{l+s+s2}{\PYZdq{}}\PY{l+s+s2}{Text Detection}\PY{l+s+s2}{\PYZdq{}}\PY{p}{,} \PY{n}{output}\PY{p}{)}
        	\PY{n}{cv2}\PY{o}{.}\PY{n}{waitKey}\PY{p}{(}\PY{l+m+mi}{0}\PY{p}{)}
\end{Verbatim}



    % Add a bibliography block to the postdoc
    
    
    
    \end{document}
