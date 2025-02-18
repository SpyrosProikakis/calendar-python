import calendar,datetime
from os.path import exists
arxeio=exists('events.csv')  #Ελέγχω αν το αρχείο events.csv υπάρχει. Αν υπάρχει η μεταβλητή αρχείο παίρνει τιμή True αλλίως False
def minas(y,m):

    #Η συνάρτηση minas δέχεται σαν παραμέτρους τη χρονία και το μήνα και εμφανίζει το αντίστοιχο ημερολόγιο.Ακόμη εμγανίζει το κύριο μενού επιλογών.

    print('________________________________________________________\n')
    print('  ',onomata[m-1],'  ',y)
    print('________________________________________________________\n\n')
    print('   ΔΕΥ  |  ΤΡΙ  |  ΤΕΤ  |  ΠΕΜ  |  ΠΑΡ  |  ΣΑΒ  |  ΚΥΡ   \n')
    tm_meres = calendar.monthcalendar(y,m) # λιστα που περιεχει υπολιστες με τις εβδομαδες του μηνα δλδ της μορφης [[0,1,2,3,4,5,][6,7,8]]
    if m==1:
        pm=calendar.monthrange(y-1,12)#ΠΡΟΗΓΟΥΜΕΝΟΣ ΜΗΝΑΣ tuple με δυο στοιχεια πρωτο στοιχειο αριθμος 1ης μερας 2ο στοιχειο συνολικος αριθμος ημερων μηνα
        tm=calendar.monthrange(y,m)#τωρινος μηνας με ακριβως τα ιδια πραγματα    
    else:
        pm=calendar.monthrange(y,m-1)# περιπτωση που ο μηνας δεν ειναι 1
        tm=calendar.monthrange(y,m)
    meresProigoumenou=pm[1]#συνολικος αριθμος ημερων προηγουμενου μηνα
    epomenos=1#τη χρησιμοποιουμε για να εμφανισουμε στο καλνεταρ τις μερες του επομενου μηνα οι οποιοιες ειναι εκτος του τωρινου μηνα 
    k=0#ποσα στοιχεια μερες βαζω στη σειρα
    for evdomada in tm_meres:#φορ στις υπολιστες
        str_evdomada=''
        for d in evdomada:#τα στοιχεια που περιεχει η υπολιστα
            if k==7:#μερες που εχουμε εκτυπωσει στη σειρα ειναι ισες με 7 αλλαξε σειρα και κανε 0 το κ για να ξεκινησει νεα εβδομαδα 
                print("\n")
                k=0
            k+=1#αυξανω το κ κατα 1 γιατι ειμαστε σε νεα εβδομαδα
            asteri=asteraki(y,'0'+str(m) if m<10 else m,'0'+str(d) if d<10 else d)#λογικη μεταβλητη τρου φολς της συναρτησης αστερακι μας λεει αν υπαρχει γεγονος εκεινη τη μερα,στην αστερακι βαζουμε σα παραμετρους το year.
            if asteri==True:#an uparxei gegonos ekeinh th mera
                if k==1:#αν εκτυπωνουμε πρωτη μερα εβδομαδας δεν εχει καθετη διπλα
                    if d==0:#αν η μερα ειναι 0 σημαινει οτι ειμαστε εκτος οριου μηνα οποτε πρεπει να εμφανισουμε μερες προηγουμενου μηνα,επομενου μηνα αν βρισκομαστε στη πρωτη ή στη τελευταια εβδομαδα αντιστοιχα εμφανιζεται μονο εκει
                        if tm_meres.index(evdomada) == 0:#αν ειμαστε στη πρωτη εβδομαδα 
                            meresProigoumenou+=1#αυξανουμε τη τελευταια μερα προηγουμενου κατα 1
                            data =meresProigoumenou - tm[0]#περιεχει αριθμο ημερας κενα καθετους(7 δατα σε καθε σειρα για αυτο πηραμε κ = 7) σε αυτη τη περιπτωση εμφανιζει τις προηγουμενες ημερες πχ 28,29,#
                            print("    "+str(data)+" ",end=" ")#ενδ για να τα εκτυπωνει το ενα διπλα στο αλλο  
                        elif d == 0:#βρισκομαστε στη τελευταια εβδομαδα και εμφανιζουμε στοχεια επομενου
                            data=epomenos
                            epomenos += 1#αυξανουμε τις μερες του επομενου μηνα που πρεπει να εμφανισουμε
                            print("     "+str(data)+"  ",end="")
                    else:
                        data=d#περιπτωση που ειμαστε εντος του μηνα d διαφορο του μηδενος
                        if int(data)<10:#ειναι για τα κενα
                            print(" [ *"+str(data)+"] ",end=" ")
                        else:
                            print(" [*"+str(data)+"] ",end=" ")
                else:#ειμαστε στη περιπτωση που το κ δεν ειναι 1 και βαζουμε καθετη
                    if d==0:#κανει ακριβως το ιδιο με τον απο πανω αντιστοιχο κωδικα απλα με καθετο
                        if tm_meres.index(evdomada) == 0:
                            meresProigoumenou+=1
                            data =meresProigoumenou - tm[0] 
                            print("|   "+str(data)+" ",end=" ")  
                        elif d == 0:
                            data=epomenos
                            epomenos += 1
                            print("|    "+str(data)+"  ",end="")
                    else:
                        data=d
                        if int(data)<10:
                            print("|[ *"+str(data)+"] ",end=" ")
                        else:
                            print("|[*"+str(data)+"] ",end=" ")
            else:#περιπτωση που δεν υπαρχει γεγονος τη συγκεκριμενη μερα αρα δεν εχουμε αστερακια
                if k==1:#το παρακατω μπλοκ ειναι ιδιο απλα αναφερεται στη περιπτωση που δεν υπαρχει γεγονος τη συγκεκιρμνεη μερα
                    if d==0:
                        if tm_meres.index(evdomada) == 0:
                            meresProigoumenou+=1
                            data =meresProigoumenou - tm[0]
                            print("    "+str(data)+" ",end=" ")  
                        elif d == 0:
                            data=epomenos
                            epomenos += 1
                            print("     "+str(data)+"  ",end="")
                    else:
                        data=d
                        if int(data)<10:
                            print(" [  "+str(data)+"] ",end=" ")
                        else:
                            print(" [ "+str(data)+"] ",end=" ")
                else:
                    if d==0:
                        if tm_meres.index(evdomada) == 0:
                            meresProigoumenou+=1
                            data =meresProigoumenou - tm[0] 
                            print("|   "+str(data)+" ",end=" ")  
                        elif d == 0:
                            data=epomenos
                            epomenos += 1
                            print("|    "+str(data)+"  ",end="")
                    else:
                        data=d
                        if int(data)<10:
                            print("|[  "+str(data)+"] ",end=" ")
                        else:
                            print("|[ "+str(data)+"] ",end=" ")

    print('\n')
    print('________________________________________________________\n\n')
    print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:')
    print('     "-" για πλοήγηση στον προηγούμενο μήνα')
    print('     "+" για διαχείριση των γεγονότων του ημερολογίου')
    print('     "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')


#ΟΙ ΑΚΟΛΟΥΘΕΣ ΣΥΝΑΡΤΗΣΕΙΣ ΕΝΕΡΓΟΠΟΙΟΥΝΤΑΙ ΣΤΗΝ ΠΕΡΙΠΤΩΣΗ ΠΟΥ ΥΠΑΡΧΕΙ ΤΟ ΑΡΧΕΙΟ events.csv

def asteraki(y,m,d):

    '''''
    Η συνάρτηση αστεράκι χρησιμοποιείται για να καταλαβαίνει ο υπολογιστής πότε θα εμφανίζει αστεράκι στο ημερολόγιο και πότε όχι.
    Διαβάζοντας το αρχείο events.csv, δημιουργεί λίστα με τις γραμμές,λίστα τα events η οποία έχει τη μορφή 
    [[date1,oraArxis1,duration1,title1],[date2,oraArxis2,duration2,title2]....] 
    όπου κάθε υπολίστα αναπαριστά ένα γεγονός και λίστα τις ημερομηνίες των events η οποία έχει μορφή [[year1,month1,day1],[year2,month2,day2]....] ,
    όπου κάθε υπολίστα περιέχει την ημερομηνία κάθε γεγονότος. Ακόμη, αρχικοποιεί μια μεταβλητή x με False, δηλαδή αρχικά κάνουμε την υπόθεση πως σε 
    αυτή την συγκεκριμένη μέρα, δεν υπάρχει γεγονός. Ανοίγουμε μια for η οποία τρέχει απο 0 έως και το μέγεθος της λίστας με τις ημερομινίες 
    των γεγονότων και αν βρούμε μέσα στη λίστα με τις ημερομηνίες κάποια που να είναι ίδια με την ημερομηνία που 
    έχει δωθεί στις παραμέτρους της συνάρτησης τότε κάνουμε την μεταβλητή x=True. Τέλος, επιστρέφουμε την μεταβλητή x
    '''
    with open("events.csv","r") as file:#ανοιγω το αρχειο με ριντ
        lines=file.readlines()#η λαινς περιεχει strings οπου καθε string περιεχομενο γραμμης αρχειου
    row=[]#η row περιεχει υπολιστες πρωτο στοιχειο καθε υπολιστας τα δεδομενα του event δευτερο στοιχειο /n.
    for line in lines:
        row.append(line.split("\n"))
    events=[]#περιεχει μονο τα πρωτα στοιχεια καθε υπολιστας της row δλδ τα δεδομενα του γεγονοτος(events)
    for i in range(0,len(row)):
        s=row[i][0]
        events.append(s.split(','))#απομονωνουμε τα δεδομενα 
    hmerominies=[]#λιστα με υπολιστες οπου καθε υπολιστα περιεχει στοιχεια ημερομηνιας γεγονοτων χρονια μηνας ημερα
    for i in range(0,len(events)):
        hm=events[i][0]
        hmerominies.append(hm.split('-'))
    x=False#υποθετω οτι η συγκεκριμενη μερα δεν εχει ιβεντς
    for i in range(len(hmerominies)):
        if hmerominies[i][0]==str(y) and hmerominies[i][1]==str(m) and hmerominies[i][2]==str(d):#αν και τα τρια ειναι ιδια τοτε σημαινει οτι υπαρχει γεγονος εκεινη τη μερα 
            x=True#υπαρχει γεγονος κανω το χ τρου
    return x


def events_Ola():

    # Η συνάρτηση events_ola() διαβάζει το αρχείο και επιστρέφει μια λίστα με όλα τα events που είναι αποθηκευμένα σε αυτό
    # Η λιστα events είναι της μορφής [[date1,oraArxis1,duration1,title1],[date2,oraArxis2,duration2,title2]....] όπου κάθε υπολίστα αναπαριστά ένα γεγονός

    with open("events.csv","r") as file:
        lines=file.readlines()
        row=[]
        for line in lines:
            row.append(line.split("\n"))
        events=[]
        for i in range(len(row)):
            s=row[i][0]
            events.append(s.split(','))
    return events

def pros8eto_event(date,oraArxis,dur,title):

    # Η συνάρτηση pros8eto_event δέχεται σαν παραμέτρους την ημερομινια ,την ώρα αρχής του γεγονότος 
    # την διάρκειά του και τον τίτλο του και τα προσθέτει με αυτή τη σειρά στο αρχείο events.csv
    with open("events.csv","a") as file:#προσθετω γραμμη στο τελος του αρχειου
        file.write(str(date)+','+str(oraArxis)+','+str(dur)+','+str(title)+'\n')



def diagrafi(gegonota_ola,gegonota_mina,c):

    # Η συνάτηση diagrafi δέχεται σαν παραμέτρους μια λίστα με όλα τα γεγονότα,μια λίστα με τα γεγονότα του μήνα 
    # και τη μεταβλητή c που έχει αποθηκευμένο τον αριθμό του γεγονότος που θέλει να διαγράψει ο χρήστης
    # Η συνάτηση ανοίγει το αρχείο csv με w,τρέχει μια επανάληψη απο 0 μέχρι το len της λίστας με όλα τα γεγονότα και 
    #  ξανά όλα τα γεγονότα εκτός από αυτό που έχει επιέξει ο χρήστης προς διαφραφή
    
    with open("events.csv","w") as file:
        for i in range(len(gegonota_ola)):
            if gegonota_ola[i]!=gegonota_mina[c]:
                file.write(gegonota_ola[i][0]+','+gegonota_ola[i][1]+','+gegonota_ola[i][2]+','+gegonota_ola[i][3]+'\n') 


def anazitisi():
    '''''
        Η συνάτηση anazitisi ψάχνει μέσα στο αρχείο events.csv τα γεγονότα του μήνα της 
    συγκεκριμένης χρονιάς που δίνει ο χρήστης και τα εμφανίζει με τον τρόπο που υποδεικνύει 
    η άσκηση και επιπλέον τα προσθέτει σε μια λίστα με όνομα gegonota_mina και επιστρέφει αυτή τη λίστα
    Γι'αυτό το σκοπό διαβαζει το αρχειο events.csv αποθηκεύει στη λίστα row τις γραμμές του αρχείου,αποθηκευει στη λίστα events ολα τα γεγονότα και έχει μορφή
    [[date1,oraArxis1,duration1,title1],[date2,oraArxis2,duration2,title2]....] όπου κάθε υπολίστα αναπαριστά ένα γεγονός. Ακόμη, 
    αποθηκεύει στη λίστα hmerominies όλες τις ημερομηνίες των γεγονότων και έχει μορφή [[year1,month1,day1],[year2,month2,day2]....] ,όπου κάθε υπολίστα περιέχει 
    την ημερομηνία κάθε γεγονότος. Ύστερα, αρχικοποιούμε έναν μετρητή k που θα είναι ο Α/Α της λίστας με τα γεγονότα που θα εμφανίζουμε. Ανοίγουμε μια 
    επανάληψη που θα τρέχει απο 0 έως και το len της λίστας με τις ημερομηνίες και αν το έτος και ο μήνας που έδωσε ο χρήστης είναι ίδια με το έτος και τον μήνα
    κάποιου γεγονότος να το εμφανίζει αυξάνει μετρητή και προσθέτει τα στοιχεία του γεγονότος στη λίστα gegonota_mina.

    ''' 
    print('===Aναζήτηση Γεγονότων===\n')
    y=int(input('Εισάγετε έτος:'))
    while y<=2022:
        y=int(input('Εισάγετε έτος:'))
    m=int(input('Εισάγετε μήνα:'))
    while m<1 or m>12:
        m=int(input('Εισάγετε μήνα:'))
    with open("events.csv","r") as file:
        lines=file.readlines()
    row=[]
    for line in lines:
        row.append(line.split("\n"))
    events=[]
    for i in range(len(row)):
        s=row[i][0]
        events.append(s.split(','))
    hmerominies=[]
    for i in range(0,len(events)):
        hm=events[i][0]
        hmerominies.append(hm.split('-'))
    k=0#πληθος γεγονοτων
    gegonota_mina=[]
    for i in range(0,len(events)):
        if events[i][0]=='Date':
            continue#σκιπ για να μη μπερδευτει με τα κατω θα εμφανιζε ερορ
        if y==int(hmerominies[i][0]) and m==int(hmerominies[i][1]):#αν ετος ιδιο με το ετος καποιας ημερομηνιες το ιδιο και για το μηνα αυτο σημαινει οτι υπαρχει γεγονος σε αυτο το μηνα
            print(str(k)+'. ['+events[i][3]+'] -> Date:'+events[i][0]+', Time:'+events[i][1]+', Duration:'+events[i][2])
            k+=1
            gegonota_mina.append(events[i])#φτιαχνω λιστα με γεγονοτα μηνα
    return gegonota_mina


def sin(year,month):

    '''''
    Η συνάρτηση sin υλοποιεί την διαχείρηση των γεγονότων του ημερολογίου. Ο χρήστης επιλέγει ενέργεια (1,2,3,0).
        Αν η επιλογή είναι 1, το πρόγραμμα ζητάει από τον χρήστη έτος,μήνα,μερα που θα διεξαχθεί το γεγονός,ωρα,διάρκεια και τίτλο του γεγονότος,
    κάνει τους κατάλληλους ελέγχους εγκυρότητας και καλεί την συνάρτηση pros8eto_event και προσθέτει το γεγονός στο αρχείο events.csv .
        Αν η επιλογή είναι 2,το πρόγραμμα φτιάχνει μια λίστα με όλα τα γεγονότα, καλώντας την συνάρτηση events_ola(),μια λίστα με τα γεγονότα του μήνα
    που επιλέγει ο χρήστης, καλώντας την συνάρτηση anazitisi() η οποία εμφανίζει παράλληλα μια λίστα με τα γεγονότα του μήνα και ο χρηστης επιλέγει ποιό από
    τα γεγονότα της λίστας θέλει να διαγράψει. Η επιλογή του αποτυπώνεται στην μεταβλητή c και ύστερα καλείται η συνάρτηση διαγραφή, η οποία διαγράφει το γεγονός
    από το αρχείο events.csv .
        Αν η επιλογή είναι 3, πάλι το πρόγραμμα  φτιάχνει λίστα με ολα τα γεγονότα, τα γεγονότα του μήνα, αποθηκεύει την επιλογή του χρήστη σχετικά με το γογονός
    που θέλει να επεξεργαστεί ,διαγρλαφει αυτό το γεγονός και δημιουργεί καινούριο με τα νέα στοιχεία που θα δώσει ο χρήστης. Τέλος, το νέο γεγονός το προσθέτει στο αρχειο events.csv .
        Αν η επιλογή είναι 0, εμφανίζεται το ημερολόγιο του μήνα που εμφανιζόταν πριν την επιλογή +

    '''

    print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
    print('     1 Καταγραφή νέου γεγονότος')
    print('     2 Διαγραφή γεγονότος')
    print('     3 Ενημέρωση γεγονότος')
    print('     0 Επιστροφή στο κυρίως μενού')
    ep=int(input('       ->'))
    while ep!=1 and ep!=2 and ep!=3 and ep!=0:
        print('Λαθος επιλογή')
        ep=int(input('       ->'))
    if ep==1:
        y=int(input('Έτος γεγονότος: '))    
        while y<=2022:
            y=int(input('Έτος γεγονότος: '))
        m=int(input('Μήνας γεγονότος(σε μορφη ΜΜ πχ 01 για Ιανουάριο): '))
        while m<1 or m>12:
            m=int(input('Μήνας γεγονότος(σε μορφη ΜΜ πχ 01 για Ιανουάριο): '))
        event_month=calendar.monthrange(y,m)    
        d=int(input('Ημέρα γεγονότος(σε μορφη DD πχ 08 για 8 του μηνός): '))
        while d<1 or d>event_month[1]:
            d=int(input('Ημέρα γεγονότος(σε μορφη DD πχ 08 για 8 του μηνός): '))
        date=datetime.date(y,m,d)   
        h=int(input('Ώρα γεγονότος (σε ψηφιακή μορφή): '))
        while h<0 or h>23:
            h=int(input('Ώρα γεγονότος (σε ψηφιακή μορφή): '))
        min=int(input('Λεπτά: '))
        while min<0 or min>59:
            min=int(input('Λεπτά: '))
        oraArxis=datetime.time(h,min)
        dur=int(input('Διάρκεια (σε λεπτά): '))
        while dur<=0 or dur!=int(dur):
            dur=int(input('Διάρκεια (σε λεπτά): '))
        title=input('Τίτλος γεγονότος: ')
        komma=',' in title
        while komma==True:
            title=input('Τίτλος γεγονότος: ')
            komma=',' in title        
        pros8eto_event(date,oraArxis,dur,title)
    elif ep==2:
        gegonota_ola2=events_Ola()
        gegonota_mina2= anazitisi()
        if gegonota_mina2 != []:
                c= int(input('Επιλέξτε γεγονός προς διαγραφή: '))
                while c not in range(len(gegonota_mina2)):
                    c= int(input('Επιλέξτε γεγονός προς διαγραφή: '))
                diagrafi(gegonota_ola2,gegonota_mina2,c)
        else:
            print('Δεν υπάρχουν γεγονότα σε αυτό το μήνα')
    elif ep==3:
        gegonota_ola3=events_Ola()
        gegonota_mina3 = anazitisi()
        if gegonota_mina3 != []:
            c = int(input('Επιλέξτε γεγονός προς ενημέρωση: '))
            while c not in range(len(gegonota_mina3)):
                c = int(input('Επιλέξτε γεγονός προς ενημέρωση: '))  
            nea_hmerominia = input('Ημερομηνία γεγονότος ('+gegonota_mina3[c][0]+'): ')
            if nea_hmerominia=='':
                nea_hmerominia=gegonota_mina3[c][0]
            else:
                hmerominia=nea_hmerominia.split('-')
                tm=calendar.monthrange(int(hmerominia[0]),int(hmerominia[1]))
                while int(hmerominia[0])<=2022 or (int(hmerominia[1])<1 or int(hmerominia[1])>12) or (int(hmerominia[2])<1 or int(hmerominia[2])>tm[1]):
                    nea_hmerominia = input('Ημερομηνία γεγονότος ('+gegonota_mina3[c][0]+'): ')
                    hmerominia=nea_hmerominia.split('-')
                    tm=calendar.monthrange(int(hmerominia[0]),int(hmerominia[1]))
            nea_ora = input('Ώρα γεγονότος ('+gegonota_mina3[c][1]+'): ')
            if nea_ora=='':
                nea_ora=gegonota_mina3[c][1]
            else:
                ora=nea_ora.split(':')
                while (int(ora[0])<0 or int(ora[0])>23) or (int(ora[1])<0 or int(ora[1])>59):
                    nea_ora = input('Ώρα γεγονότος ('+gegonota_mina3[c][1]+'): ')
                    ora=nea_ora.split(':')
            nea_dur=input('Διάρκεια γεγονότος ('+gegonota_mina3[c][2]+'): ')
            if nea_dur=='':
                nea_dur=gegonota_mina3[c][2]
            else:
                while int(nea_dur)<=0 or int(nea_dur)!=int(nea_dur):
                    nea_dur=input('Διάρκεια γεγονότος ('+gegonota_mina3[c][2]+'): ')
            neo_title= input('Τίτλος γεγονότος ('+gegonota_mina3[c][3]+'): ')
            if neo_title=='':
                neo_title=gegonota_mina3[c][3]
            else:
                komma= ',' in neo_title
                while komma==True:
                    neo_title= input('Τίτλος γεγονότος ('+gegonota_mina3[c][3]+'): ')
                    komma= ',' in neo_title
            diagrafi(gegonota_ola3,gegonota_mina3,c)
            pros8eto_event(nea_hmerominia,nea_ora,nea_dur,neo_title)



#ΟΙ ΑΚΟΛΟΥΘΕΣ ΣΥΝΑΡΤΗΣΕΙΣ ΕΝΕΡΓΟΠΟΙΟΥΝΤΑΙ ΣΤΗΝ ΠΕΡΙΠΤΩΣΗ ΠΟΥ ΔΕΝ ΥΠΑΡΧΕΙ ΤΟ ΑΡΧΕΙΟ events.csv

#Στην περίπτωση που δεν υπάρχει το αρχείο, έχω ένα dictionary και διαχειρίζομαι με όνομα events, το οποίο σαν keys έχει τις 
#ημερομηνίες των γεγονότων και σαν values την ώρα,την διάρκεια και τον τίτλο του γεγονότος.

def asteraki2(y,m,d):

    '''''
    Η συνάρτηση asteraki2 χρησιμοποιείται για να εμφανιστεί το αστεράκι στο ημερολόγιο. Για το σκοπό αυτό, αρχικοποιούμε μια μεταβλητή x=False. 
    Ανοίγουμε μια for η οποία τρέχει τους δείκτες του dict, το i δηλαδή αναπαριστά την ημερομηνία ενός γεγονότος. Την ημερομηνία αυτή την κάνουμε 
    split,δημιουργόντας έτσι μια λίστα με όνομα hmerominia η οποία περιέχει τα στοιχεία της ημερομηνίας και είναι της μορφής ['YYY','MM','DD']
    Αν υπάρχει κάποιο event καταγεγραμμένο την συγκεκριμένη ημερομηνία τότε η συνάρτηση επιστρέφει True. Αυτό το καταλαβαίνουμε συγκρίνοντας
    το έτος ,το μήνα και τη μέρα κάθε καταγεγραμμένης ημερομηνίας στο dict με το έτος,το μήνα και την μέρα πού έχουν δωθεί σαν παράμετροι
    '''

    x=False
    for i in events:
        if i=='Date':
            continue
        hmerominia = str(i).split('-')
        if hmerominia[0] == str(y) and hmerominia[1] == m and hmerominia[2] == d:
            x= True
    return x

def pros8eto_event2(date,oraArxis,dur,title):

    #Η συνάρτηση pros8eto_event2 δέχεται σαν παραμέτρους την ημερομηνία,την ώρα,την διάρκεια και τον τίτλο του 
    #γεγονότος και τα προσθέτει στο dict και στο αρχείο.

    events[str(date)] = [str(oraArxis),str(dur),str(title)]
    with open("events.csv","a") as file:
        file.write(str(date)+','+str(oraArxis)+','+str(dur)+','+str(title)+'\n')


def grafo_dict():

    #Η συνάρτηση grafo_dict() ανοίγει το αρχείο events.csv με w και περνάει όλο το dict στο αρχείο events.csv

    with open('events.csv','w') as file:
        for i in events:
            file.write(str(i)+','+str(events[i][0])+','+str(events[i][1])+','+str(events[i][2])+'\n')


def anazitisi2():

    '''''
    Η συνάρτηση anazitisi2() ψάχνει τα γεγονότα ενός μήνα και τα εμφανίζει στη μορφή που ζητάει η άσκηση. Για το σκοπό αυτό, ανοίγει μια for η οποία περνάει 
    απ'όλες τις ημερομηνίες του dictionary ,κανει split καθε ημερομηνία και συγκρίνει το έτος και το μήνα με το αντίστοιχο έτος και μήνα που έχει δώσει
    ο χρήστης. Αν το έτος και ο μήνας κάποιας ημερομηνίας απο το dict είναι ίδιος με το έτος και το μήνα που έδωσε ο χρήστης τότε εμφανίζει τα στοιχεία του
    γεγονότος σε μορφή λίστας. Άκομη, στην αρχή αρχικοποιεί μια λίστα με όνομα hmerominies με κενό, η οποία θα περιέχει τις ημερομηνίες των γεγονότων εκείνου του μήνα που έχει επιλέξει ο χρήστης και έχει τη μορφή ['YYY-MM-DD','YYY-MM-DD',....] όπου κάθε string είναι μια ημερομηνία του γεγονότος του εκείνου μήνα. Έτσι κάθε φορά που ισχυεί η συνθήκη προσθέτει την ημερομηνία στη λίστα. Τέλος, επιστρέφει τη λίστα hmeromhnies
    '''
    hmerominies=[]
    k=0
    print('===Aναζήτηση Γεγονότων===\n')
    year=int(input('Εισάγετε έτος:'))
    while year<=2022:
        year=int(input('Εισάγετε έτος:'))
    month=int(input('Εισάγετε μήνα:'))
    while month<1 or month>12:
        month=int(input('Εισάγετε μήνα:'))
    print('\n')
    for i in events:
        if i == 'Date':
            continue
        hmerominia= i.split('-')
        if hmerominia[0] == str(year) and hmerominia[1] == '0'+str(month) if month<10 else str(month):
            hmerominies.append(i)
            print(str(k)+'. ['+str(events[i][2])+'] -> Date: '+str(i)+', Time: '+str(events[i][0])+', Duration: '+str(events[i][1]))
            k+=1
    if hmerominies==[]:
        print('Δεν υπάρχουν γεγονότα σε αυτό το μήνα')
    return hmerominies



def sin2(year,month):

    '''''
    Η συνάρτηση sin2 υλοποιεί την διαχείρηση των γεγονότων του ημερολογίου. Ο χρήστης επιλέγει ενέργεια (1,2,3,0).
        Αν η επιλογή είναι 1, το πρόγραμμα ζητάει από τον χρήστη έτος,μήνα,μερα που θα διεξαχθεί το γεγονός,ωρα,διάρκεια και τίτλο του γεγονότος,
    κάνει τους κατάλληλους ελέγχους εγκυρότητας και καλεί την συνάρτηση pros8eto_event2 και προσθέτει το γεγονός στο αρχείο events.csv και στο dict.
        Αν η επιλογή είναι 2, το πρόγραμμα καλεί την συνάρτηση anzitisi2() η οποια εμφανίζει αριθμημένη λίστα με τα γεγονότα του μήνα και ταυτόχρονα αποθηκεύει την
    λίστα με τις ημερομηνίες των γεγονότων του μήνα στη λίστα hmerominies. Αν η λίστα hmerominies δεν είναι κενή, δηλαδή αν υπάρχουν γεγονότα σε αυτό το μήνα,τότε
    ο χρήστης επιλέγει απο την αριθμημένη λίστα γεγονότων ένα event προς διαγραφή,η επιλογή του αποθηκεύεται στην μεταβλητή c ,το event διαγράφεται απο το dict και
    καλείται η συνάρτηση grafo_dict() η οποία γραφεί το νέο πλέον dictionary στο αρχείο events.csv .
        Αν η επιλογή είναι 3, πάλι το πρόγραμμα καλεί την συνάρτηση anzitisi2() η οποια εμφανίζει αριθμημένη λίστα με τα γεγονότα του μήνα και ταυτόχρονα αποθηκεύει την
    λίστα με τις ημερομηνίες των γεγονότων του μήνα στη λίστα hmerominies, ο χρήστης επιλέγει ποιό γεγονός θέλει να επεξεργαστεί, το γεγονός αυτό διαγράφεται,
    τα νέα στοιχεία του αποθηκεύονται σαν νεο γεγεγονός,δηλαδή προστήθονται στο dict και με την συνάρτηση grafo_dict() το ανανεωμένο dict περνιέται στο αρχείο events.csv
        Αν η επιλογή είναι 0, εμφανίζεται το ημερολόγιο του μήνα που εμφανιζόταν πριν την επιλογή + 

    '''


    print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
    print('     1 Καταγραφή νέου γεγονότος')
    print('     2 Διαγραφή γεγονότος')
    print('     3 Ενημέρωση γεγονότος')
    print('     0 Επιστροφή στο κυρίως μενού')
    ep=int(input('       ->'))
    while ep!=1 and ep!=2 and ep!=3 and ep!=0:
        print('Λάθος επιλογή')
        ep=int(input('       ->'))
    if ep==1:
        y=int(input('Έτος γεγονότος: '))    
        while y<=2022:
            y=int(input('Έτος γεγονότος: '))
        m=int(input('Μήνας γεγονότος(σε μορφη ΜΜ πχ 01 για Ιανουάριο): '))
        while m<1 or m>12:
            m=int(input('Μήνας γεγονότος(σε μορφη ΜΜ πχ 01 για Ιανουάριο): '))
        event_month=calendar.monthrange(y,m)    
        d=int(input('Ημέρα γεγονότος(σε μορφη DD πχ 08 για 8 του μηνός): '))
        while d<1 or d>event_month[1]:
            d=int(input('Ημέρα γεγονότος(σε μορφη DD πχ 08 για 8 του μηνός): '))
        date=datetime.date(y,m,d) 
        h=int(input('Ώρα γεγονότος (σε ψηφιακή μορφή): '))
        while h<0 or h>23:
            h=int(input('Ώρα γεγονότος (σε ψηφιακή μορφή): '))
        min=int(input('Λεπτά: '))
        while min<0 or min>59:
            min=int(input('Λεπτά: '))
        oraArxis=datetime.time(h,min)
        dur=int(input('Διάρκεια (σε λεπτά): '))
        while dur<=0 or dur!=int(dur):
            dur=int(input('Διάρκεια (σε λεπτά): '))   
        title=input('Τίτλος γεγονότος: ')
        komma=',' in title
        while komma==True:
            title=input('Τίτλος γεγονότος: ')
            komma=',' in title        
        pros8eto_event2(date,oraArxis,dur,title)
    elif ep==2:
        hmerominies = anazitisi2()
        if hmerominies != []:
                c= int(input('Επιλέξτε γεγονός προς διαγραφή: '))
                while c not in range(len(hmerominies)):
                    c= int(input('Επιλέξτε γεγονός προς διαγραφή: '))
                del events[hmerominies[c]]
                grafo_dict()
    elif ep==3:
        hmerominies = anazitisi2()
        if hmerominies != []:
            c = int(input('Επιλέξτε γεγονός προς ενημέρωση: '))
            while c not in range(len(hmerominies)):
                c = int(input('Επιλέξτε γεγονός προς ενημέρωση: '))  
            epilegmeni_hmerominia= hmerominies[c]
            nea_hmerominia = input('Ημερομηνία γεγονότος ('+epilegmeni_hmerominia+'): ')
            if nea_hmerominia=='':
                nea_hmerominia=epilegmeni_hmerominia
            else:
                hmerominia=nea_hmerominia.split('-')
                tm=calendar.monthrange(int(hmerominia[0]),int(hmerominia[1]))
                while int(hmerominia[0])<=2022 or (int(hmerominia[1])<1 or int(hmerominia[1])>12) or (int(hmerominia[2])<1 or int(hmerominia[2])>tm[1]):
                    nea_hmerominia = input('Ημερομηνία γεγονότος ('+epilegmeni_hmerominia+'): ')
                    hmerominia=nea_hmerominia.split('-')
                    tm=calendar.monthrange(int(hmerominia[0]),int(hmerominia[1]))
            nea_ora = input('Ώρα γεγονότος ('+events[epilegmeni_hmerominia][0]+'): ')
            if nea_ora=='':
                nea_ora=events[epilegmeni_hmerominia][0]
            else:
                ora=nea_ora.split(':')
                while (int(ora[0])<0 or int(ora[0])>23) or (int(ora[1])<0 or int(ora[1])>59):
                    nea_ora = input('Ώρα γεγονότος ('+events[epilegmeni_hmerominia][0]+'): ')
                    ora=nea_ora.split(':')
            nea_dur=int(input('Διάρκεια γεγονότος ('+events[epilegmeni_hmerominia][1]+'): '))
            if nea_dur=='':
                nea_dur=events[epilegmeni_hmerominia][1]
            else:
                while nea_dur<=0 or nea_dur!=int(nea_dur):
                    nea_dur=int(input('Διάρκεια γεγονότος ('+events[epilegmeni_hmerominia][1]+'): '))
            neo_title= input('Τίτλος γεγονότος ('+events[epilegmeni_hmerominia][2]+'): ')
            if neo_title=='':
                neo_title=events[epilegmeni_hmerominia][2]
            else:
                komma= ',' in neo_title
                while komma==True:
                    neo_title= input('Τίτλος γεγονότος ('+events[epilegmeni_hmerominia][2]+'): ')
                    komma= ',' in neo_title
            del events[epilegmeni_hmerominia]
            events[nea_hmerominia] = [nea_ora,nea_dur,neo_title]
            grafo_dict()





if arxeio==False:
    # Ο κώδικας ενεργοποιείται στην περίπτωση που το αρχείο δεν υπάρχει
    onomata=['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']
    events={}
    events['Date'] = ['Time', 'Duration', 'Title']
    grafo_dict()
    td=datetime.date.today()
    ty=td.year
    tm=td.month
    minas(ty,tm)
    while True:
        ep= input('     ->')
        print(ep)
        while (ep!="" and ep!="q" and ep!="-" and ep!="+" and ep!="*"):
            print('Λαθος επιλογή')
            ep=input('      ->')
        if ep== "-":
            if tm==1:
                tm=12
                ty-=1
            else:
                tm-=1
        elif ep== "+":
            sin2(ty,tm)
        elif ep== "*":
            anazitisi2()
            c= input('Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:')
        elif ep=="":
            if tm == 12:
                tm = 1
                ty += 1
            else:
                tm += 1 
        elif ep=="q":
            quit()
        minas(ty,tm)
else:
    # Ο κώδικας ενεργοποιείται στην περίπτωση που το αρχείο υπάρχει
    onomata=['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']
    td=datetime.date.today()
    ty=td.year
    tm=td.month
    minas(ty,tm)
    while True:
        ep=str(input('     ->'))
        print(ep)
        while (ep!="" and ep!="q" and ep!="-" and ep!="+" and ep!="*"):
            print('Λαθος επιλογή')
            ep=str(input('      ->'))
        if ep== "-":
            if tm==1:
                tm=12
                ty-=1
            else:
                tm-=1
        elif ep== "+":
            sin(ty,tm)
        elif ep== "*":
            anazitisi()
            c= input('Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:')
        elif ep=="":
            if tm == 12:
                tm = 1
                ty += 1
            else:
                tm += 1 
        elif ep=="q":
            quit()
        minas(ty,tm)
    

#ΟΜΑΔΑ: ΠΡΩΙΚΑΚΗΣ ΣΠΥΡΟΣ           AM:3220167
#       ΚΟΣΜΙΔΗ ΕΛΛΗ               ΑΜ:3220086
#       ΠΑΠΑΝΔΡΕΟΠΟΥΛΟΥ ΚΑΛΛΙΟΠΗ   ΑΜ:3220154
   

