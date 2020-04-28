from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
from datetime import datetime, timedelta
from calendar import monthrange
app= Flask(__name__)


@app.route("/")
def hello():
    return "hello pops !!!"


@app.route("/calci",methods=['POST', 'GET'])
def calci(msg):
    maths = msg
    ans=''
    if maths.find('+')!=-1:
        numbers=maths.split('+')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        ans=str(num1+num2)
    elif maths.find('-')!=-1:
        numbers=maths.split('-')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        ans=str(num1-num2)
    elif maths.find('*')!=-1:
        numbers=maths.split('*')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        ans=str(num1*num2)
    elif maths.find('/')!=-1:
        numbers=maths.split('/')
        num1=int(numbers[0].strip())
        num2=int(numbers[1].strip())
        if num2==0:
            ans="DBZ error"
        else:
            ans=str(num1/num2)
    else:
        ans='invalid input!!'
    print(ans)
    return ans


def calender_f1():
    date=''
    now = datetime.now()
    date=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')
    print(date)
    return date

def calender_f2():
    presentday = datetime.now()
    tomorrow = presentday + timedelta(1)
    date1=tomorrow.strftime('%A, %B the %dth, %Y')
    print(date1)
    return date1


def calendar_f3(msg):
    year=int(msg[-4:])
    res=''
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                res="{0} is a leap year".format(year)
            else:
                res="{0} is not a leap year".format(year)
        else:
            res="{0} is a leap year".format(year)
    else:
        res="{0} is not a leap year".format(year)
    print(res)
    return res


def calendar_f4(msg):
    segments = msg.split()
    year = int(segments[len(segments) - 1])
    month = int(segments[len(segments) - 2])
    days=''
    days=str(monthrange(year, month)[1]) + " days"
    print(days)
    return days


def calendar_f5(msg):
    ref_year = 2020
    ref_year_islamic = 1441
    year = int(msg[-4:])
    islamic_year = (year - ref_year) + ref_year_islamic
    print(islamic_year)
    if(str(islamic_year))[-1] == '1':
        return str(year) + " is " + str(islamic_year) + "st islamic year"
    if(str(islamic_year))[-1] == '2':
        return str(year) + " is " + str(islamic_year) + "nd islamic year"
    if(str(islamic_year))[-1] == '3':
        return str(year) + " is " + str(islamic_year) + "rd islamic year"
    return str(year) + " is the " + str(islamic_year) + "th islamic year"

def bmi_f15(msg):
    segments = msg.split()
    height = int(segments[len(segments) - 1])
    weight = int(segments[len(segments) - 2])
    bmic=''
    bmi = weight/(((height)/100)**2)
    print(bmi)
    if ( bmi < 16):
        bmic="severely underweight"
    elif ( bmi >= 16 and bmi < 18.5):
        bmic="underweight"
    elif ( bmi >= 18.5 and bmi < 25):
        bmic="Healthy"
    elif ( bmi >= 25 and bmi < 30):
        bmic="overweight"
    elif ( bmi >=30):
        bmic="severely overweight"
    return "your BMI is:" + "{:.2f}".format(bmi) + " and you are :" + str(bmic)


def syllabus_f2(subject):
    # what's the issue...no reply...i 
    print(subject)
    if subject.find('ss')!=-1:
        sub="""Module-1Introduction to System Software \n Introduction to System Software, Machine Architecture of SIC and SIC/XE.\n
            Assemblers: Basic assembler functions, machine dependent assembler features, machine independent assembler features, assembler design options \n
            Macroprocessors: Basicmacro processor functions\n
            Module-2Loaders and Linkers\n 
            Loaders and Linkers:\n
            Basic Loader Functions, Machine Dependent Loader Features, Machine Independent Loader Features, Loader Design Options, Implementation Examples.\n
            Module-3 Introduction \n
            Introduction:
            Language Processors, The structure of a compiler, The evaluation of programming languages, The science of building compiler, Applications of compiler technology, Programming language basics \n
            Lexical Analysis:\n
            The role of lexical analyzer, Input buffering, Specifications of token, recognition of tokens, lexical analyzer generator, Finite automate.\n
            Module-4Syntax Analysis \n
            Syntax Analysis:
            Introduction, Role Of Parsers, Context Free Grammars, Writing a grammar, Top Down Parsers, Bottom-Up Parsers, Operator-Precedence Parsing \n
            Module-5Syntax Directed Translation \n
            Syntax Directed Translation, Intermediate code generation, Code generation"""
    elif subject.find('os')!=-1:
        sub="""Module-1Introduction  \n
            Introduction - Cyber Attacks, Defence Strategies and Techniques, Guiding Principles, Mathematical Background for Cryptography - Modulo Arithmetic’s, The Greatest Comma Divisor, Useful Algebraic Structures, Chinese Remainder Theorem, Basics of Cryptography - Preliminaries, Elementary Substitution Ciphers, Elementary Transport Ciphers, Other Cipher Properties, Secret Key Cryptography – Product Ciphers, DES Construction. \n
            Module-2Public Key Cryptography and RSA \n
            Public Key Cryptography and RSA – RSA Operations, Why Does RSA Work?, Performance, Applications, Practical Issues, Public Key Cryptography Standard (PKCS), Cryptographic Hash - Introduction, Properties, Construction, Applications and Performance, The Birthday Attack, Discrete Logarithm and its Applications - Introduction, Diffie-Hellman Key Exchange, Other Applications. \n
            Module-3Key Management \n
            Key Management - Introduction, Digital Certificates, Public Key Infrastructure, Identity–based Encryption, Authentication–I - One way Authentication, Mutual Authentication, Dictionary Attacks, Authentication – II – Centalised Authentication, The Needham-Schroeder Protocol, Kerberos, Biometrics, IPSec- Security at the Network Layer – Security at Different layers: Pros and Cons, IPSec in Action, Internet Key Exchange (IKE) Protocol, Security Policy and IPSEC, Virtual Private Networks, Security at the Transport Layer - Introduction, SSL Handshake Protocol, SSL Record Layer Protocol, OpenSSL. \n
            Module-4IEEE 802.11 Wireless LAN Security \n
            IEEE 802.11 Wireless LAN Security - Background, Authentication, Confidentiality and Integrity, Viruses, Worms, and Other Malware, Firewalls – Basics, Practical Issues, Intrusion Prevention and Detection - Introduction, Prevention Versus Detection, Types of Instruction Detection Systems, DDoS Attacks Prevention/Detection, Web Service Security – Motivation, Technologies for Web Services, WS- Security, SAML, Other Standards. \n
            Module-5IT act aim and objectives \n
            IT act aim and objectives, Scope of the act, Major Concepts, Important provisions, Attribution, acknowledgement, and dispatch of electronic records, Secure electronic records and secure digital signatures, Regulation of certifying authorities: Appointment of Controller and Other officers, Digital Signature certificates, Duties of Subscribers, Penalties and adjudication, The cyber regulations appellate tribunal, Offences, Network service providers not to be liable in certain cases, Miscellaneous Provisions. \n"""
    elif subject.find('cg')!=-1:
        sub="""Module-1 Overview: Computer Graphics and OpenGL \n
              Overview: Computer Graphics and OpenGL:
              Computer Graphics:Basics of computer graphics, Application of Computer Graphics, Video Display Devices: Random Scan and Raster Scan displays, color CRT monitors, Flat panel displays. Raster-scan systems: video controller, raster scan Display processor, graphics workstations and viewing systems, Input devices, graphics networks, graphics on the internet, graphics software. OpenGL: Introduction to OpenGL ,coordinate reference frames, specifying two-dimensional world coordinate reference frames in OpenGL, OpenGL point functions, OpenGL line functions, point attributes, line attributes, curve attributes, OpenGL point attribute functions, OpenGL line attribute functions, Line drawing algorithms(DDA, Bresenham’s), circle generation algorithms(Bresenham’s). \n
              Module-2 Fill area Primitives, 2D Geometric Transformations and 2D viewing \n
              Fill area Primitives, 2D Geometric Transformations and 2D viewing:
              Fill area Primitives: Polygon fill-areas, OpenGL polygon fill area functions, fill area attributes, general scan line polygon fill algorithm, OpenGL fill-area attribute functions. 2DGeometric Transformations: Basic 2D Geometric Transformations, matrix representations and homogeneous coordinates. Inverse transformations, 2DComposite transformations, other 2D transformations, raster methods for geometric transformations, OpenGL raster transformations, OpenGL geometric transformations function, 2D viewing: 2D viewing pipeline, OpenGL 2D viewing functions. \n
              Module-3 Clipping,3D Geometric Transformations, Color and Illumination Models \n
              Clipping,3D Geometric Transformations, Color and Illumination Models:
              Clipping: clipping window, normalization and viewport transformations, clipping algorithms,2D point clipping, 2D line clipping algorithms: cohen-sutherland line clipping only -polygon fill area clipping: Sutherland-Hodgeman polygon clipping algorithm only.3DGeometric Transformations: 3D translation, rotation, scaling, composite 3D transformations, other 3D transformations, affine transformations, OpenGL geometric transformations functions. Color Models: Properties of light, color models, RGB and CMY color models. Illumination Models: Light sources, basic illumination models-Ambient light, diffuse reflection, specular and phong model, Corresponding openGL functions. \n
              Module-4 3D Viewing and Visible Surface Detection \n
              3D Viewing and Visible Surface Detection:
              3DViewing:3D viewing concepts, 3D viewing pipeline, 3D viewing coordinate parameters , Transformation fromworld to viewing coordinates, Projection transformation, orthogonal projections, perspective projections, The viewport transformation and 3D screen coordinates. OpenGL 3D viewing functions. Visible Surface Detection Methods: Classification of visible surface Detection algorithms, back face detection, depth buffer method and OpenGL visibility detection functions. \n
              Module-5 Input& interaction, Curves and Computer Animation \n
              Input& interaction, Curves and Computer Animation:
              Input and Interaction: Input devices, clients and servers, Display Lists, Display Lists and Modelling, Programming Event Driven Input, Menus Picking, Building Interactive Models, Animating Interactive programs, Design of Interactive programs, Logic operations .Curved surfaces, quadric surfaces, OpenGL Quadric-Surface and Cubic-Surface Functions, Bezier Spline Curves, Bezier surfaces, OpenGL curve functions. Corresponding openGL functions. \n"""
    print(sub)
    return sub
    

def syllabus_m(subject,module):
    modwise=''
    syb={"ss":{'1':""" Module-1 Introduction to System Software, Introduction to System Software, Machine Architecture of SIC n SIC/XE. Assemblers: Basic assembler functions, machine dependent assembler features, machine independent assembler features, assembler design options 
        Macroprocessors: Basicmacro processor functions""",'2':"""Module 2 :Fill area Primitives, 2D Geometric Transformations and 2D viewing \n
        Fill area Primitives, 2D Geometric Transformations and 2D viewing:
        Fill area Primitives: Polygon fill-areas, OpenGL polygon fill area functions, fill area attributes, general scan line polygon fill algorithm, OpenGL fill-area attribute functions. 2DGeometric Transformations: Basic 2D Geometric Transformations, matrix representations and homogeneous coordinates. Inverse transformations, 2DComposite transformations, other 2D transformations, raster methods for geometric transformations, OpenGL raster transformations, OpenGL geometric transformations function, 2D viewing: 2D viewing pipeline, OpenGL 2D viewing functions. """,'3':""" Module 3 :Introduction:
        Language Processors, The structure of a compiler, The evaluation of programming languages, The science of building compiler, Applications of compiler technology, Programming language basics \n
        Lexical Analysis:\n
        The role of lexical analyzer, Input buffering, Specifications of token, recognition of tokens, lexical analyzer generator, Finite automate.""",'4':"""Module 4: 3D Viewing and Visible Surface Detection \n
        3D Viewing and Visible Surface Detection:
        3DViewing:3D viewing concepts, 3D viewing pipeline, 3D viewing coordinate parameters , Transformation fromworld to viewing coordinates, Projection transformation, orthogonal projections, perspective projections, The viewport transformation and 3D screen coordinates. OpenGL 3D viewing functions. Visible Surface Detection Methods: Classification of visible surface Detection algorithms, back face detection, depth buffer method and OpenGL visibility detection functions.""",'5':"""Module 5: Input& interaction, Curves and Computer Animation \n
        Input& interaction, Curves and Computer Animation:
        Input and Interaction: Input devices, clients and servers, Display Lists, Display Lists and Modelling, Programming Event Driven Input, Menus Picking, Building Interactive Models, Animating Interactive programs, Design of Interactive programs, Logic operations .Curved surfaces, quadric surfaces, OpenGL Quadric-Surface and Cubic-Surface Functions, Bezier Spline Curves, Bezier surfaces, OpenGL curve functions. Corresponding openGL functions."""
        },
        "os":{'1':"""MODULE 1:Introduction to operating systems, System structures: What operating systems
        do; Computer System organization; Computer System architecture; Operating
        System structure; Operating System operations; Process management; Memory
        management; Storage management; Protection and Security; Distributed system;
        Special-purpose systems; Computing environments. Operating System Services;
        User - Operating System interface; System calls; Types of system calls; System
        programs; Operating system design and implementation; Operating System
        structure; Virtual machines; Operating System generation; System boot. Process
        Management Process concept; Process scheduling; Operations on processes;
        Inter process communication
        """,'2':"""MODULE 2:Multi-threaded Programming: Overview; Multithreading models; Thread
        Libraries; Threading issues. Process Scheduling: Basic concepts; Scheduling
        Criteria; Scheduling Algorithms; Multiple-processor scheduling; Thread
        scheduling. Process Synchronization: Synchronization: The critical section
        problem; Peterson’s solution; Synchronization hardware; Semaphores; Classical
        problems of synchronization; Monitors. """,'3':"""MODULE 3:Deadlocks : Deadlocks; System model; Deadlock characterization; Methods for
        handling deadlocks; Deadlock prevention; Deadlock avoidance; Deadlock
        detection and recovery from deadlock. Memory Management: Memory
        management strategies: Background; Swapping; Contiguous memory allocation;
        Paging; Structure of page table; Segmentation. """,'4':"""MODULE 4:Virtual Memory Management: Background; Demand paging; Copy-on-write;
        Page replacement; Allocation of frames; Thrashing. File System,
        Implementation of File System: File system: File concept; Access methods;
        Directory structure; File system mounting; File sharing; Protection:
        Implementing File system: File system structure; File system implementation;
        Directory implementation; Allocation methods; Free space management. """,'5':"""MODULE 5:Secondary Storage Structures, Protection: Mass storage structures; Disk
        structure; Disk attachment; Disk scheduling; Disk management; Swap space
        management. Protection: Goals of protection, Principles of protection, Domain of
        protection, Access matrix, Implementation of access matrix, Access control,
        Revocation of access rights, Capability- Based systems. Case Study: The Linux
        Operating System: Linux history; Design principles; Kernel modules; Process
        management; Scheduling; Memory Management; File systems, Input and output;"""},
        "cg":{'1':"""MODULE 1:Overview: Computer Graphics and OpenGL: Computer Graphics:Basics of
        computer graphics, Application of Computer Graphics, Video Display Devices:
        Random Scan and Raster Scan displays, color CRT monitors, Flat panel displays.
        Raster-scan systems: video controller, raster scan Display processor, graphics
        workstations and viewing systems, Input devices, graphics networks, graphics on
        the internet, graphics software. OpenGL: Introduction to OpenGL ,coordinate
        reference frames, specifying two-dimensional world coordinate reference frames
        in OpenGL, OpenGL point functions, OpenGL line functions, point attributes,
        line attributes, curve attributes, OpenGL point attribute functions, OpenGL line
        attribute functions, Line drawing algorithms(DDA, Bresenham’s), circle
        generation algorithms(Bresenham’s).""",'2':"""MODULE 2:Fill area Primitives, 2D Geometric Transformations and 2D viewing: Fill
        area Primitives: Polygon fill-areas, OpenGL polygon fill area functions, fill area
        attributes, general scan line polygon fill algorithm, OpenGL fill-area attribute
        functions. 2DGeometric Transformations: Basic 2D Geometric Transformations,
        matrix representations and homogeneous coordinates. Inverse transformations,
        2DComposite transformations, other 2D transformations, raster methods for
        geometric transformations, OpenGL raster transformations, OpenGL geometric
        transformations function, 2D viewing: 2D viewing pipeline, OpenGL 2D viewing
        functions """,'3':"""MODULE 3:Clipping,3D Geometric Transformations, Color and Illumination Models:
        Clipping: clipping window, normalization and viewport transformations, clipping
        algorithms,2D point clipping, 2D line clipping algorithms: cohen-sutherland line
        clipping only -polygon fill area clipping: Sutherland-Hodgeman polygon clipping
        algorithm only.3DGeometric Transformations: 3D translation, rotation, scaling,
        composite 3D transformations, other 3D transformations, affine transformations,
        OpenGL geometric transformations functions. Color Models: Properties of light,
        color models, RGB and CMY color models. Illumination Models: Light sources,
        basic illumination models-Ambient light, diffuse reflection, specular and phong
        model, Corresponding openGL functions. """,'4':"""MODULE 4:3D Viewing and Visible Surface Detection: 3DViewing:3D viewing concepts,
        3D viewing pipeline, 3D viewing coordinate parameters , Transformation from
        10 Hours
        world to viewing coordinates, Projection transformation, orthogonal projections,
        perspective projections, The viewport transformation and 3D screen coordinates.
        OpenGL 3D viewing functions. Visible Surface Detection Methods:
        Classification of visible surface Detection algorithms, back face detection, depth
        buffer method and OpenGL visibility detection functions. 
        """,'5':"""MODULE 5:Input& interaction, Curves and Computer Animation: Input and Interaction:
        Input devices, clients and servers, Display Lists, Display Lists and Modelling,
        Programming Event Driven Input, Menus Picking, Building Interactive Models,
        Animating Interactive programs, Design of Interactive programs, Logic
        operations .Curved surfaces, quadric surfaces, OpenGL Quadric-Surface and
        Cubic-Surface Functions, Bezier Spline Curves, Bezier surfaces, OpenGL curve
        functions. Corresponding openGL functions. 
        """}}
    modwise=syb[subject][module]
    print(modwise)
    return modwise


@app.route("/sms",methods=['POST'])
def sms_reply():
    msg=request.form.get('Body')
    if msg.find('+') != -1 or msg.find('-')!= -1 or msg.find('*')!= -1 or msg.find('/') !=-1:
        ans = calci(msg)
        print(ans)
        resp=MessagingResponse()
        resp.message("{}".format(ans))
        return str(resp)
    
    elif msg[0:2] == "@5":
        # to check if user wants feature 1
        if msg.find("today's date") != -1:
            print("f1")
            date=calender_f1()
            print(date)
            resp=MessagingResponse()
            resp.message("{}".format(date))
            return str(resp)

        # to check if user wants feature 2
        elif msg.find("tomorrow's date") != -1:
            date1=calender_f2()
            print(date1)
            resp=MessagingResponse()
            resp.message("{}".format(date1))
            return str(resp)

        # to check if user wants feature 3
        elif msg.find("isleap") != -1:
            res=calendar_f3(msg)
            print(res)
            resp=MessagingResponse()
            resp.message("{}".format(res@2))
            return str(resp)

        elif msg.find("days in the month of year") != -1:
            days=calendar_f4(msg)
            print(days)
            resp=MessagingResponse()
            resp.message("{}".format(days))
            return str(resp)
        elif msg.find("islamic year") != -1:
            days=calendar_f5(msg)
            print(days)
            resp=MessagingResponse()
            resp.message("{}".format(days))
            return str(resp)

    elif msg[0:3] == "@15":
        bmic = bmi_f15(msg)
        print(bmic)
        resp=MessagingResponse()
        resp.message("{}".format(bmic))
        return str(resp)

    elif msg[0:2] == "@2":
        segments = msg.split()
        
        if len(segments) == 3:
            subject=segments[1]
            module=segments[2]
            modwise=syllabus_m(subject,module)
            print(modwise)
            resp=MessagingResponse()
            resp.message("{}".format(modwise))
            return str(resp)
            
        else:    
            subject=segments[1] # you dont need module here .. so no need of segments[2].. this way you avoid error        
            sub=syllabus_f2(subject)
            print(sub)
            resp=MessagingResponse()
            resp.message("{}".format(sub))
            return str(resp)        

    return ""


# start ngrok... and update new url in twilio ...haan
if __name__=="__main__":
    app.run(debug=True)

# calendar features
# we'll assume user will send in the message as : "@5 today's date" or something like that
# features :
# 1) @5 today's date
# 2) @5 tomorrow's date
# 3) @5 isleap 2020
# 4) @5 days in the month of year 2 2020
# 5) @5 muslim year
