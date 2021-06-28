
import os
from py4web import action, request, abort, redirect, URL, Field, HTTP
from yatl.helpers import A, I
from py4web.utils.form import Form, FormStyleDefault
from py4web.utils.factories import ActionFactory, Inject
from py4web.utils.grid import Grid, GridClassStyle, Column
from py4web.utils.param import Param
from py4web.utils.publisher import Publisher, ALLOW_ALL_POLICY
from pydal.validators import IS_NOT_EMPTY, IS_INT_IN_RANGE, IS_IN_SET, IS_IN_DB
from yatl.helpers import INPUT, H1, HTML, BODY, A, DIV
from py4web.utils.param import Param
from .settings import SESSION_SECRET_KEY

from .common import db, session, T, flash, cache, authenticated, unauthenticated, auth

@action('ctrl_act0')
def ctrl_nm0():
    return 'ret0' 

@action('ctrl_act1')
def ctrl_nm1():
    return 'ret1' 

@action('ctrl_act2')
def ctrl_nm2():
    return 'ret2' 

@action('ctrl_act3')
def ctrl_nm3():
    return 'ret3' 

@action('ctrl_act4')
def ctrl_nm4():
    return 'ret4' 

@action('ctrl_act5')
def ctrl_nm5():
    return 'ret5' 

@action('ctrl_act6')
def ctrl_nm6():
    return 'ret6' 

@action('ctrl_act7')
def ctrl_nm7():
    return 'ret7' 

@action('ctrl_act8')
def ctrl_nm8():
    return 'ret8' 

@action('ctrl_act9')
def ctrl_nm9():
    return 'ret9' 

@action('ctrl_act10')
def ctrl_nm10():
    return 'ret10' 

@action('ctrl_act11')
def ctrl_nm11():
    return 'ret11' 

@action('ctrl_act12')
def ctrl_nm12():
    return 'ret12' 

@action('ctrl_act13')
def ctrl_nm13():
    return 'ret13' 

@action('ctrl_act14')
def ctrl_nm14():
    return 'ret14' 

@action('ctrl_act15')
def ctrl_nm15():
    return 'ret15' 

@action('ctrl_act16')
def ctrl_nm16():
    return 'ret16' 

@action('ctrl_act17')
def ctrl_nm17():
    return 'ret17' 

@action('ctrl_act18')
def ctrl_nm18():
    return 'ret18' 

@action('ctrl_act19')
def ctrl_nm19():
    return 'ret19' 

@action('ctrl_act20')
def ctrl_nm20():
    return 'ret20' 

@action('ctrl_act21')
def ctrl_nm21():
    return 'ret21' 

@action('ctrl_act22')
def ctrl_nm22():
    return 'ret22' 

@action('ctrl_act23')
def ctrl_nm23():
    return 'ret23' 

@action('ctrl_act24')
def ctrl_nm24():
    return 'ret24' 

@action('ctrl_act25')
def ctrl_nm25():
    return 'ret25' 

@action('ctrl_act26')
def ctrl_nm26():
    return 'ret26' 

@action('ctrl_act27')
def ctrl_nm27():
    return 'ret27' 

@action('ctrl_act28')
def ctrl_nm28():
    return 'ret28' 

@action('ctrl_act29')
def ctrl_nm29():
    return 'ret29' 

@action('ctrl_act30')
def ctrl_nm30():
    return 'ret30' 

@action('ctrl_act31')
def ctrl_nm31():
    return 'ret31' 

@action('ctrl_act32')
def ctrl_nm32():
    return 'ret32' 

@action('ctrl_act33')
def ctrl_nm33():
    return 'ret33' 

@action('ctrl_act34')
def ctrl_nm34():
    return 'ret34' 

@action('ctrl_act35')
def ctrl_nm35():
    return 'ret35' 

@action('ctrl_act36')
def ctrl_nm36():
    return 'ret36' 

@action('ctrl_act37')
def ctrl_nm37():
    return 'ret37' 

@action('ctrl_act38')
def ctrl_nm38():
    return 'ret38' 

@action('ctrl_act39')
def ctrl_nm39():
    return 'ret39' 

@action('ctrl_act40')
def ctrl_nm40():
    return 'ret40' 

@action('ctrl_act41')
def ctrl_nm41():
    return 'ret41' 

@action('ctrl_act42')
def ctrl_nm42():
    return 'ret42' 

@action('ctrl_act43')
def ctrl_nm43():
    return 'ret43' 

@action('ctrl_act44')
def ctrl_nm44():
    return 'ret44' 

@action('ctrl_act45')
def ctrl_nm45():
    return 'ret45' 

@action('ctrl_act46')
def ctrl_nm46():
    return 'ret46' 

@action('ctrl_act47')
def ctrl_nm47():
    return 'ret47' 

@action('ctrl_act48')
def ctrl_nm48():
    return 'ret48' 

@action('ctrl_act49')
def ctrl_nm49():
    return 'ret49' 

@action('ctrl_act50')
def ctrl_nm50():
    return 'ret50' 

@action('ctrl_act51')
def ctrl_nm51():
    return 'ret51' 

@action('ctrl_act52')
def ctrl_nm52():
    return 'ret52' 

@action('ctrl_act53')
def ctrl_nm53():
    return 'ret53' 

@action('ctrl_act54')
def ctrl_nm54():
    return 'ret54' 

@action('ctrl_act55')
def ctrl_nm55():
    return 'ret55' 

@action('ctrl_act56')
def ctrl_nm56():
    return 'ret56' 

@action('ctrl_act57')
def ctrl_nm57():
    return 'ret57' 

@action('ctrl_act58')
def ctrl_nm58():
    return 'ret58' 

@action('ctrl_act59')
def ctrl_nm59():
    return 'ret59' 

@action('ctrl_act60')
def ctrl_nm60():
    return 'ret60' 

@action('ctrl_act61')
def ctrl_nm61():
    return 'ret61' 

@action('ctrl_act62')
def ctrl_nm62():
    return 'ret62' 

@action('ctrl_act63')
def ctrl_nm63():
    return 'ret63' 

@action('ctrl_act64')
def ctrl_nm64():
    return 'ret64' 

@action('ctrl_act65')
def ctrl_nm65():
    return 'ret65' 

@action('ctrl_act66')
def ctrl_nm66():
    return 'ret66' 

@action('ctrl_act67')
def ctrl_nm67():
    return 'ret67' 

@action('ctrl_act68')
def ctrl_nm68():
    return 'ret68' 

@action('ctrl_act69')
def ctrl_nm69():
    return 'ret69' 

@action('ctrl_act70')
def ctrl_nm70():
    return 'ret70' 

@action('ctrl_act71')
def ctrl_nm71():
    return 'ret71' 

@action('ctrl_act72')
def ctrl_nm72():
    return 'ret72' 

@action('ctrl_act73')
def ctrl_nm73():
    return 'ret73' 

@action('ctrl_act74')
def ctrl_nm74():
    return 'ret74' 

@action('ctrl_act75')
def ctrl_nm75():
    return 'ret75' 

@action('ctrl_act76')
def ctrl_nm76():
    return 'ret76' 

@action('ctrl_act77')
def ctrl_nm77():
    return 'ret77' 

@action('ctrl_act78')
def ctrl_nm78():
    return 'ret78' 

@action('ctrl_act79')
def ctrl_nm79():
    return 'ret79' 

@action('ctrl_act80')
def ctrl_nm80():
    return 'ret80' 

@action('ctrl_act81')
def ctrl_nm81():
    return 'ret81' 

@action('ctrl_act82')
def ctrl_nm82():
    return 'ret82' 

@action('ctrl_act83')
def ctrl_nm83():
    return 'ret83' 

@action('ctrl_act84')
def ctrl_nm84():
    return 'ret84' 

@action('ctrl_act85')
def ctrl_nm85():
    return 'ret85' 

@action('ctrl_act86')
def ctrl_nm86():
    return 'ret86' 

@action('ctrl_act87')
def ctrl_nm87():
    return 'ret87' 

@action('ctrl_act88')
def ctrl_nm88():
    return 'ret88' 

@action('ctrl_act89')
def ctrl_nm89():
    return 'ret89' 

@action('ctrl_act90')
def ctrl_nm90():
    return 'ret90' 

@action('ctrl_act91')
def ctrl_nm91():
    return 'ret91' 

@action('ctrl_act92')
def ctrl_nm92():
    return 'ret92' 

@action('ctrl_act93')
def ctrl_nm93():
    return 'ret93' 

@action('ctrl_act94')
def ctrl_nm94():
    return 'ret94' 

@action('ctrl_act95')
def ctrl_nm95():
    return 'ret95' 

@action('ctrl_act96')
def ctrl_nm96():
    return 'ret96' 

@action('ctrl_act97')
def ctrl_nm97():
    return 'ret97' 

@action('ctrl_act98')
def ctrl_nm98():
    return 'ret98' 

@action('ctrl_act99')
def ctrl_nm99():
    return 'ret99' 

@action('ctrl_act100')
def ctrl_nm100():
    return 'ret100' 

@action('ctrl_act101')
def ctrl_nm101():
    return 'ret101' 

@action('ctrl_act102')
def ctrl_nm102():
    return 'ret102' 

@action('ctrl_act103')
def ctrl_nm103():
    return 'ret103' 

@action('ctrl_act104')
def ctrl_nm104():
    return 'ret104' 

@action('ctrl_act105')
def ctrl_nm105():
    return 'ret105' 

@action('ctrl_act106')
def ctrl_nm106():
    return 'ret106' 

@action('ctrl_act107')
def ctrl_nm107():
    return 'ret107' 

@action('ctrl_act108')
def ctrl_nm108():
    return 'ret108' 

@action('ctrl_act109')
def ctrl_nm109():
    return 'ret109' 

@action('ctrl_act110')
def ctrl_nm110():
    return 'ret110' 

@action('ctrl_act111')
def ctrl_nm111():
    return 'ret111' 

@action('ctrl_act112')
def ctrl_nm112():
    return 'ret112' 

@action('ctrl_act113')
def ctrl_nm113():
    return 'ret113' 

@action('ctrl_act114')
def ctrl_nm114():
    return 'ret114' 

@action('ctrl_act115')
def ctrl_nm115():
    return 'ret115' 

@action('ctrl_act116')
def ctrl_nm116():
    return 'ret116' 

@action('ctrl_act117')
def ctrl_nm117():
    return 'ret117' 

@action('ctrl_act118')
def ctrl_nm118():
    return 'ret118' 

@action('ctrl_act119')
def ctrl_nm119():
    return 'ret119' 

@action('ctrl_act120')
def ctrl_nm120():
    return 'ret120' 

@action('ctrl_act121')
def ctrl_nm121():
    return 'ret121' 

@action('ctrl_act122')
def ctrl_nm122():
    return 'ret122' 

@action('ctrl_act123')
def ctrl_nm123():
    return 'ret123' 

@action('ctrl_act124')
def ctrl_nm124():
    return 'ret124' 

@action('ctrl_act125')
def ctrl_nm125():
    return 'ret125' 

@action('ctrl_act126')
def ctrl_nm126():
    return 'ret126' 

@action('ctrl_act127')
def ctrl_nm127():
    return 'ret127' 

@action('ctrl_act128')
def ctrl_nm128():
    return 'ret128' 

@action('ctrl_act129')
def ctrl_nm129():
    return 'ret129' 

@action('ctrl_act130')
def ctrl_nm130():
    return 'ret130' 

@action('ctrl_act131')
def ctrl_nm131():
    return 'ret131' 

@action('ctrl_act132')
def ctrl_nm132():
    return 'ret132' 

@action('ctrl_act133')
def ctrl_nm133():
    return 'ret133' 

@action('ctrl_act134')
def ctrl_nm134():
    return 'ret134' 

@action('ctrl_act135')
def ctrl_nm135():
    return 'ret135' 

@action('ctrl_act136')
def ctrl_nm136():
    return 'ret136' 

@action('ctrl_act137')
def ctrl_nm137():
    return 'ret137' 

@action('ctrl_act138')
def ctrl_nm138():
    return 'ret138' 

@action('ctrl_act139')
def ctrl_nm139():
    return 'ret139' 

@action('ctrl_act140')
def ctrl_nm140():
    return 'ret140' 

@action('ctrl_act141')
def ctrl_nm141():
    return 'ret141' 

@action('ctrl_act142')
def ctrl_nm142():
    return 'ret142' 

@action('ctrl_act143')
def ctrl_nm143():
    return 'ret143' 

@action('ctrl_act144')
def ctrl_nm144():
    return 'ret144' 

@action('ctrl_act145')
def ctrl_nm145():
    return 'ret145' 

@action('ctrl_act146')
def ctrl_nm146():
    return 'ret146' 

@action('ctrl_act147')
def ctrl_nm147():
    return 'ret147' 

@action('ctrl_act148')
def ctrl_nm148():
    return 'ret148' 

@action('ctrl_act149')
def ctrl_nm149():
    return 'ret149' 

@action('ctrl_act150')
def ctrl_nm150():
    return 'ret150' 

@action('ctrl_act151')
def ctrl_nm151():
    return 'ret151' 

@action('ctrl_act152')
def ctrl_nm152():
    return 'ret152' 

@action('ctrl_act153')
def ctrl_nm153():
    return 'ret153' 

@action('ctrl_act154')
def ctrl_nm154():
    return 'ret154' 

@action('ctrl_act155')
def ctrl_nm155():
    return 'ret155' 

@action('ctrl_act156')
def ctrl_nm156():
    return 'ret156' 

@action('ctrl_act157')
def ctrl_nm157():
    return 'ret157' 

@action('ctrl_act158')
def ctrl_nm158():
    return 'ret158' 

@action('ctrl_act159')
def ctrl_nm159():
    return 'ret159' 

@action('ctrl_act160')
def ctrl_nm160():
    return 'ret160' 

@action('ctrl_act161')
def ctrl_nm161():
    return 'ret161' 

@action('ctrl_act162')
def ctrl_nm162():
    return 'ret162' 

@action('ctrl_act163')
def ctrl_nm163():
    return 'ret163' 

@action('ctrl_act164')
def ctrl_nm164():
    return 'ret164' 

@action('ctrl_act165')
def ctrl_nm165():
    return 'ret165' 

@action('ctrl_act166')
def ctrl_nm166():
    return 'ret166' 

@action('ctrl_act167')
def ctrl_nm167():
    return 'ret167' 

@action('ctrl_act168')
def ctrl_nm168():
    return 'ret168' 

@action('ctrl_act169')
def ctrl_nm169():
    return 'ret169' 

@action('ctrl_act170')
def ctrl_nm170():
    return 'ret170' 

@action('ctrl_act171')
def ctrl_nm171():
    return 'ret171' 

@action('ctrl_act172')
def ctrl_nm172():
    return 'ret172' 

@action('ctrl_act173')
def ctrl_nm173():
    return 'ret173' 

@action('ctrl_act174')
def ctrl_nm174():
    return 'ret174' 

@action('ctrl_act175')
def ctrl_nm175():
    return 'ret175' 

@action('ctrl_act176')
def ctrl_nm176():
    return 'ret176' 

@action('ctrl_act177')
def ctrl_nm177():
    return 'ret177' 

@action('ctrl_act178')
def ctrl_nm178():
    return 'ret178' 

@action('ctrl_act179')
def ctrl_nm179():
    return 'ret179' 

@action('ctrl_act180')
def ctrl_nm180():
    return 'ret180' 

@action('ctrl_act181')
def ctrl_nm181():
    return 'ret181' 

@action('ctrl_act182')
def ctrl_nm182():
    return 'ret182' 

@action('ctrl_act183')
def ctrl_nm183():
    return 'ret183' 

@action('ctrl_act184')
def ctrl_nm184():
    return 'ret184' 

@action('ctrl_act185')
def ctrl_nm185():
    return 'ret185' 

@action('ctrl_act186')
def ctrl_nm186():
    return 'ret186' 

@action('ctrl_act187')
def ctrl_nm187():
    return 'ret187' 

@action('ctrl_act188')
def ctrl_nm188():
    return 'ret188' 

@action('ctrl_act189')
def ctrl_nm189():
    return 'ret189' 

@action('ctrl_act190')
def ctrl_nm190():
    return 'ret190' 

@action('ctrl_act191')
def ctrl_nm191():
    return 'ret191' 

@action('ctrl_act192')
def ctrl_nm192():
    return 'ret192' 

@action('ctrl_act193')
def ctrl_nm193():
    return 'ret193' 

@action('ctrl_act194')
def ctrl_nm194():
    return 'ret194' 

@action('ctrl_act195')
def ctrl_nm195():
    return 'ret195' 

@action('ctrl_act196')
def ctrl_nm196():
    return 'ret196' 

@action('ctrl_act197')
def ctrl_nm197():
    return 'ret197' 

@action('ctrl_act198')
def ctrl_nm198():
    return 'ret198' 

@action('ctrl_act199')
def ctrl_nm199():
    return 'ret199' 

@action('ctrl_act200')
def ctrl_nm200():
    return 'ret200' 

@action('ctrl_act201')
def ctrl_nm201():
    return 'ret201' 

@action('ctrl_act202')
def ctrl_nm202():
    return 'ret202' 

@action('ctrl_act203')
def ctrl_nm203():
    return 'ret203' 

@action('ctrl_act204')
def ctrl_nm204():
    return 'ret204' 

@action('ctrl_act205')
def ctrl_nm205():
    return 'ret205' 

@action('ctrl_act206')
def ctrl_nm206():
    return 'ret206' 

@action('ctrl_act207')
def ctrl_nm207():
    return 'ret207' 

@action('ctrl_act208')
def ctrl_nm208():
    return 'ret208' 

@action('ctrl_act209')
def ctrl_nm209():
    return 'ret209' 

@action('ctrl_act210')
def ctrl_nm210():
    return 'ret210' 

@action('ctrl_act211')
def ctrl_nm211():
    return 'ret211' 

@action('ctrl_act212')
def ctrl_nm212():
    return 'ret212' 

@action('ctrl_act213')
def ctrl_nm213():
    return 'ret213' 

@action('ctrl_act214')
def ctrl_nm214():
    return 'ret214' 

@action('ctrl_act215')
def ctrl_nm215():
    return 'ret215' 

@action('ctrl_act216')
def ctrl_nm216():
    return 'ret216' 

@action('ctrl_act217')
def ctrl_nm217():
    return 'ret217' 

@action('ctrl_act218')
def ctrl_nm218():
    return 'ret218' 

@action('ctrl_act219')
def ctrl_nm219():
    return 'ret219' 

@action('ctrl_act220')
def ctrl_nm220():
    return 'ret220' 

@action('ctrl_act221')
def ctrl_nm221():
    return 'ret221' 

@action('ctrl_act222')
def ctrl_nm222():
    return 'ret222' 

@action('ctrl_act223')
def ctrl_nm223():
    return 'ret223' 

@action('ctrl_act224')
def ctrl_nm224():
    return 'ret224' 

@action('ctrl_act225')
def ctrl_nm225():
    return 'ret225' 

@action('ctrl_act226')
def ctrl_nm226():
    return 'ret226' 

@action('ctrl_act227')
def ctrl_nm227():
    return 'ret227' 

@action('ctrl_act228')
def ctrl_nm228():
    return 'ret228' 

@action('ctrl_act229')
def ctrl_nm229():
    return 'ret229' 

@action('ctrl_act230')
def ctrl_nm230():
    return 'ret230' 

@action('ctrl_act231')
def ctrl_nm231():
    return 'ret231' 

@action('ctrl_act232')
def ctrl_nm232():
    return 'ret232' 

@action('ctrl_act233')
def ctrl_nm233():
    return 'ret233' 

@action('ctrl_act234')
def ctrl_nm234():
    return 'ret234' 

@action('ctrl_act235')
def ctrl_nm235():
    return 'ret235' 

@action('ctrl_act236')
def ctrl_nm236():
    return 'ret236' 

@action('ctrl_act237')
def ctrl_nm237():
    return 'ret237' 

@action('ctrl_act238')
def ctrl_nm238():
    return 'ret238' 

@action('ctrl_act239')
def ctrl_nm239():
    return 'ret239' 

@action('ctrl_act240')
def ctrl_nm240():
    return 'ret240' 

@action('ctrl_act241')
def ctrl_nm241():
    return 'ret241' 

@action('ctrl_act242')
def ctrl_nm242():
    return 'ret242' 

@action('ctrl_act243')
def ctrl_nm243():
    return 'ret243' 

@action('ctrl_act244')
def ctrl_nm244():
    return 'ret244' 

@action('ctrl_act245')
def ctrl_nm245():
    return 'ret245' 

@action('ctrl_act246')
def ctrl_nm246():
    return 'ret246' 

@action('ctrl_act247')
def ctrl_nm247():
    return 'ret247' 

@action('ctrl_act248')
def ctrl_nm248():
    return 'ret248' 

@action('ctrl_act249')
def ctrl_nm249():
    return 'ret249' 

@action('ctrl_act250')
def ctrl_nm250():
    return 'ret250' 

@action('ctrl_act251')
def ctrl_nm251():
    return 'ret251' 

@action('ctrl_act252')
def ctrl_nm252():
    return 'ret252' 

@action('ctrl_act253')
def ctrl_nm253():
    return 'ret253' 

@action('ctrl_act254')
def ctrl_nm254():
    return 'ret254' 

@action('ctrl_act255')
def ctrl_nm255():
    return 'ret255' 

@action('ctrl_act256')
def ctrl_nm256():
    return 'ret256' 

@action('ctrl_act257')
def ctrl_nm257():
    return 'ret257' 

@action('ctrl_act258')
def ctrl_nm258():
    return 'ret258' 

@action('ctrl_act259')
def ctrl_nm259():
    return 'ret259' 

@action('ctrl_act260')
def ctrl_nm260():
    return 'ret260' 

@action('ctrl_act261')
def ctrl_nm261():
    return 'ret261' 

@action('ctrl_act262')
def ctrl_nm262():
    return 'ret262' 

@action('ctrl_act263')
def ctrl_nm263():
    return 'ret263' 

@action('ctrl_act264')
def ctrl_nm264():
    return 'ret264' 

@action('ctrl_act265')
def ctrl_nm265():
    return 'ret265' 

@action('ctrl_act266')
def ctrl_nm266():
    return 'ret266' 

@action('ctrl_act267')
def ctrl_nm267():
    return 'ret267' 

@action('ctrl_act268')
def ctrl_nm268():
    return 'ret268' 

@action('ctrl_act269')
def ctrl_nm269():
    return 'ret269' 

@action('ctrl_act270')
def ctrl_nm270():
    return 'ret270' 

@action('ctrl_act271')
def ctrl_nm271():
    return 'ret271' 

@action('ctrl_act272')
def ctrl_nm272():
    return 'ret272' 

@action('ctrl_act273')
def ctrl_nm273():
    return 'ret273' 

@action('ctrl_act274')
def ctrl_nm274():
    return 'ret274' 

@action('ctrl_act275')
def ctrl_nm275():
    return 'ret275' 

@action('ctrl_act276')
def ctrl_nm276():
    return 'ret276' 

@action('ctrl_act277')
def ctrl_nm277():
    return 'ret277' 

@action('ctrl_act278')
def ctrl_nm278():
    return 'ret278' 

@action('ctrl_act279')
def ctrl_nm279():
    return 'ret279' 

@action('ctrl_act280')
def ctrl_nm280():
    return 'ret280' 

@action('ctrl_act281')
def ctrl_nm281():
    return 'ret281' 

@action('ctrl_act282')
def ctrl_nm282():
    return 'ret282' 

@action('ctrl_act283')
def ctrl_nm283():
    return 'ret283' 

@action('ctrl_act284')
def ctrl_nm284():
    return 'ret284' 

@action('ctrl_act285')
def ctrl_nm285():
    return 'ret285' 

@action('ctrl_act286')
def ctrl_nm286():
    return 'ret286' 

@action('ctrl_act287')
def ctrl_nm287():
    return 'ret287' 

@action('ctrl_act288')
def ctrl_nm288():
    return 'ret288' 

@action('ctrl_act289')
def ctrl_nm289():
    return 'ret289' 

@action('ctrl_act290')
def ctrl_nm290():
    return 'ret290' 

@action('ctrl_act291')
def ctrl_nm291():
    return 'ret291' 

@action('ctrl_act292')
def ctrl_nm292():
    return 'ret292' 

@action('ctrl_act293')
def ctrl_nm293():
    return 'ret293' 

@action('ctrl_act294')
def ctrl_nm294():
    return 'ret294' 

@action('ctrl_act295')
def ctrl_nm295():
    return 'ret295' 

@action('ctrl_act296')
def ctrl_nm296():
    return 'ret296' 

@action('ctrl_act297')
def ctrl_nm297():
    return 'ret297' 

@action('ctrl_act298')
def ctrl_nm298():
    return 'ret298' 

@action('ctrl_act299')
def ctrl_nm299():
    return 'ret299' 

@action('ctrl_act300')
def ctrl_nm300():
    return 'ret300' 

@action('ctrl_act301')
def ctrl_nm301():
    return 'ret301' 

@action('ctrl_act302')
def ctrl_nm302():
    return 'ret302' 

@action('ctrl_act303')
def ctrl_nm303():
    return 'ret303' 

@action('ctrl_act304')
def ctrl_nm304():
    return 'ret304' 

@action('ctrl_act305')
def ctrl_nm305():
    return 'ret305' 

@action('ctrl_act306')
def ctrl_nm306():
    return 'ret306' 

@action('ctrl_act307')
def ctrl_nm307():
    return 'ret307' 

@action('ctrl_act308')
def ctrl_nm308():
    return 'ret308' 

@action('ctrl_act309')
def ctrl_nm309():
    return 'ret309' 

@action('ctrl_act310')
def ctrl_nm310():
    return 'ret310' 

@action('ctrl_act311')
def ctrl_nm311():
    return 'ret311' 

@action('ctrl_act312')
def ctrl_nm312():
    return 'ret312' 

@action('ctrl_act313')
def ctrl_nm313():
    return 'ret313' 

@action('ctrl_act314')
def ctrl_nm314():
    return 'ret314' 

@action('ctrl_act315')
def ctrl_nm315():
    return 'ret315' 

@action('ctrl_act316')
def ctrl_nm316():
    return 'ret316' 

@action('ctrl_act317')
def ctrl_nm317():
    return 'ret317' 

@action('ctrl_act318')
def ctrl_nm318():
    return 'ret318' 

@action('ctrl_act319')
def ctrl_nm319():
    return 'ret319' 

@action('ctrl_act320')
def ctrl_nm320():
    return 'ret320' 

@action('ctrl_act321')
def ctrl_nm321():
    return 'ret321' 

@action('ctrl_act322')
def ctrl_nm322():
    return 'ret322' 

@action('ctrl_act323')
def ctrl_nm323():
    return 'ret323' 

@action('ctrl_act324')
def ctrl_nm324():
    return 'ret324' 

@action('ctrl_act325')
def ctrl_nm325():
    return 'ret325' 

@action('ctrl_act326')
def ctrl_nm326():
    return 'ret326' 

@action('ctrl_act327')
def ctrl_nm327():
    return 'ret327' 

@action('ctrl_act328')
def ctrl_nm328():
    return 'ret328' 

@action('ctrl_act329')
def ctrl_nm329():
    return 'ret329' 

@action('ctrl_act330')
def ctrl_nm330():
    return 'ret330' 

@action('ctrl_act331')
def ctrl_nm331():
    return 'ret331' 

@action('ctrl_act332')
def ctrl_nm332():
    return 'ret332' 

@action('ctrl_act333')
def ctrl_nm333():
    return 'ret333' 

@action('ctrl_act334')
def ctrl_nm334():
    return 'ret334' 

@action('ctrl_act335')
def ctrl_nm335():
    return 'ret335' 

@action('ctrl_act336')
def ctrl_nm336():
    return 'ret336' 

@action('ctrl_act337')
def ctrl_nm337():
    return 'ret337' 

@action('ctrl_act338')
def ctrl_nm338():
    return 'ret338' 

@action('ctrl_act339')
def ctrl_nm339():
    return 'ret339' 

@action('ctrl_act340')
def ctrl_nm340():
    return 'ret340' 

@action('ctrl_act341')
def ctrl_nm341():
    return 'ret341' 

@action('ctrl_act342')
def ctrl_nm342():
    return 'ret342' 

@action('ctrl_act343')
def ctrl_nm343():
    return 'ret343' 

@action('ctrl_act344')
def ctrl_nm344():
    return 'ret344' 

@action('ctrl_act345')
def ctrl_nm345():
    return 'ret345' 

@action('ctrl_act346')
def ctrl_nm346():
    return 'ret346' 

@action('ctrl_act347')
def ctrl_nm347():
    return 'ret347' 

@action('ctrl_act348')
def ctrl_nm348():
    return 'ret348' 

@action('ctrl_act349')
def ctrl_nm349():
    return 'ret349' 

@action('ctrl_act350')
def ctrl_nm350():
    return 'ret350' 

@action('ctrl_act351')
def ctrl_nm351():
    return 'ret351' 

@action('ctrl_act352')
def ctrl_nm352():
    return 'ret352' 

@action('ctrl_act353')
def ctrl_nm353():
    return 'ret353' 

@action('ctrl_act354')
def ctrl_nm354():
    return 'ret354' 

@action('ctrl_act355')
def ctrl_nm355():
    return 'ret355' 

@action('ctrl_act356')
def ctrl_nm356():
    return 'ret356' 

@action('ctrl_act357')
def ctrl_nm357():
    return 'ret357' 

@action('ctrl_act358')
def ctrl_nm358():
    return 'ret358' 

@action('ctrl_act359')
def ctrl_nm359():
    return 'ret359' 

@action('ctrl_act360')
def ctrl_nm360():
    return 'ret360' 

@action('ctrl_act361')
def ctrl_nm361():
    return 'ret361' 

@action('ctrl_act362')
def ctrl_nm362():
    return 'ret362' 

@action('ctrl_act363')
def ctrl_nm363():
    return 'ret363' 

@action('ctrl_act364')
def ctrl_nm364():
    return 'ret364' 

@action('ctrl_act365')
def ctrl_nm365():
    return 'ret365' 

@action('ctrl_act366')
def ctrl_nm366():
    return 'ret366' 

@action('ctrl_act367')
def ctrl_nm367():
    return 'ret367' 

@action('ctrl_act368')
def ctrl_nm368():
    return 'ret368' 

@action('ctrl_act369')
def ctrl_nm369():
    return 'ret369' 

@action('ctrl_act370')
def ctrl_nm370():
    return 'ret370' 

@action('ctrl_act371')
def ctrl_nm371():
    return 'ret371' 

@action('ctrl_act372')
def ctrl_nm372():
    return 'ret372' 

@action('ctrl_act373')
def ctrl_nm373():
    return 'ret373' 

@action('ctrl_act374')
def ctrl_nm374():
    return 'ret374' 

@action('ctrl_act375')
def ctrl_nm375():
    return 'ret375' 

@action('ctrl_act376')
def ctrl_nm376():
    return 'ret376' 

@action('ctrl_act377')
def ctrl_nm377():
    return 'ret377' 

@action('ctrl_act378')
def ctrl_nm378():
    return 'ret378' 

@action('ctrl_act379')
def ctrl_nm379():
    return 'ret379' 

@action('ctrl_act380')
def ctrl_nm380():
    return 'ret380' 

@action('ctrl_act381')
def ctrl_nm381():
    return 'ret381' 

@action('ctrl_act382')
def ctrl_nm382():
    return 'ret382' 

@action('ctrl_act383')
def ctrl_nm383():
    return 'ret383' 

@action('ctrl_act384')
def ctrl_nm384():
    return 'ret384' 

@action('ctrl_act385')
def ctrl_nm385():
    return 'ret385' 

@action('ctrl_act386')
def ctrl_nm386():
    return 'ret386' 

@action('ctrl_act387')
def ctrl_nm387():
    return 'ret387' 

@action('ctrl_act388')
def ctrl_nm388():
    return 'ret388' 

@action('ctrl_act389')
def ctrl_nm389():
    return 'ret389' 

@action('ctrl_act390')
def ctrl_nm390():
    return 'ret390' 

@action('ctrl_act391')
def ctrl_nm391():
    return 'ret391' 

@action('ctrl_act392')
def ctrl_nm392():
    return 'ret392' 

@action('ctrl_act393')
def ctrl_nm393():
    return 'ret393' 

@action('ctrl_act394')
def ctrl_nm394():
    return 'ret394' 

@action('ctrl_act395')
def ctrl_nm395():
    return 'ret395' 

@action('ctrl_act396')
def ctrl_nm396():
    return 'ret396' 

@action('ctrl_act397')
def ctrl_nm397():
    return 'ret397' 

@action('ctrl_act398')
def ctrl_nm398():
    return 'ret398' 

@action('ctrl_act399')
def ctrl_nm399():
    return 'ret399' 

@action('ctrl_act400')
def ctrl_nm400():
    return 'ret400' 

@action('ctrl_act401')
def ctrl_nm401():
    return 'ret401' 

@action('ctrl_act402')
def ctrl_nm402():
    return 'ret402' 

@action('ctrl_act403')
def ctrl_nm403():
    return 'ret403' 

@action('ctrl_act404')
def ctrl_nm404():
    return 'ret404' 

@action('ctrl_act405')
def ctrl_nm405():
    return 'ret405' 

@action('ctrl_act406')
def ctrl_nm406():
    return 'ret406' 

@action('ctrl_act407')
def ctrl_nm407():
    return 'ret407' 

@action('ctrl_act408')
def ctrl_nm408():
    return 'ret408' 

@action('ctrl_act409')
def ctrl_nm409():
    return 'ret409' 

@action('ctrl_act410')
def ctrl_nm410():
    return 'ret410' 

@action('ctrl_act411')
def ctrl_nm411():
    return 'ret411' 

@action('ctrl_act412')
def ctrl_nm412():
    return 'ret412' 

@action('ctrl_act413')
def ctrl_nm413():
    return 'ret413' 

@action('ctrl_act414')
def ctrl_nm414():
    return 'ret414' 

@action('ctrl_act415')
def ctrl_nm415():
    return 'ret415' 

@action('ctrl_act416')
def ctrl_nm416():
    return 'ret416' 

@action('ctrl_act417')
def ctrl_nm417():
    return 'ret417' 

@action('ctrl_act418')
def ctrl_nm418():
    return 'ret418' 

@action('ctrl_act419')
def ctrl_nm419():
    return 'ret419' 

@action('ctrl_act420')
def ctrl_nm420():
    return 'ret420' 

@action('ctrl_act421')
def ctrl_nm421():
    return 'ret421' 

@action('ctrl_act422')
def ctrl_nm422():
    return 'ret422' 

@action('ctrl_act423')
def ctrl_nm423():
    return 'ret423' 

@action('ctrl_act424')
def ctrl_nm424():
    return 'ret424' 

@action('ctrl_act425')
def ctrl_nm425():
    return 'ret425' 

@action('ctrl_act426')
def ctrl_nm426():
    return 'ret426' 

@action('ctrl_act427')
def ctrl_nm427():
    return 'ret427' 

@action('ctrl_act428')
def ctrl_nm428():
    return 'ret428' 

@action('ctrl_act429')
def ctrl_nm429():
    return 'ret429' 

@action('ctrl_act430')
def ctrl_nm430():
    return 'ret430' 

@action('ctrl_act431')
def ctrl_nm431():
    return 'ret431' 

@action('ctrl_act432')
def ctrl_nm432():
    return 'ret432' 

@action('ctrl_act433')
def ctrl_nm433():
    return 'ret433' 

@action('ctrl_act434')
def ctrl_nm434():
    return 'ret434' 

@action('ctrl_act435')
def ctrl_nm435():
    return 'ret435' 

@action('ctrl_act436')
def ctrl_nm436():
    return 'ret436' 

@action('ctrl_act437')
def ctrl_nm437():
    return 'ret437' 

@action('ctrl_act438')
def ctrl_nm438():
    return 'ret438' 

@action('ctrl_act439')
def ctrl_nm439():
    return 'ret439' 

@action('ctrl_act440')
def ctrl_nm440():
    return 'ret440' 

@action('ctrl_act441')
def ctrl_nm441():
    return 'ret441' 

@action('ctrl_act442')
def ctrl_nm442():
    return 'ret442' 

@action('ctrl_act443')
def ctrl_nm443():
    return 'ret443' 

@action('ctrl_act444')
def ctrl_nm444():
    return 'ret444' 

@action('ctrl_act445')
def ctrl_nm445():
    return 'ret445' 

@action('ctrl_act446')
def ctrl_nm446():
    return 'ret446' 

@action('ctrl_act447')
def ctrl_nm447():
    return 'ret447' 

@action('ctrl_act448')
def ctrl_nm448():
    return 'ret448' 

@action('ctrl_act449')
def ctrl_nm449():
    return 'ret449' 

@action('ctrl_act450')
def ctrl_nm450():
    return 'ret450' 

@action('ctrl_act451')
def ctrl_nm451():
    return 'ret451' 

@action('ctrl_act452')
def ctrl_nm452():
    return 'ret452' 

@action('ctrl_act453')
def ctrl_nm453():
    return 'ret453' 

@action('ctrl_act454')
def ctrl_nm454():
    return 'ret454' 

@action('ctrl_act455')
def ctrl_nm455():
    return 'ret455' 

@action('ctrl_act456')
def ctrl_nm456():
    return 'ret456' 

@action('ctrl_act457')
def ctrl_nm457():
    return 'ret457' 

@action('ctrl_act458')
def ctrl_nm458():
    return 'ret458' 

@action('ctrl_act459')
def ctrl_nm459():
    return 'ret459' 

@action('ctrl_act460')
def ctrl_nm460():
    return 'ret460' 

@action('ctrl_act461')
def ctrl_nm461():
    return 'ret461' 

@action('ctrl_act462')
def ctrl_nm462():
    return 'ret462' 

@action('ctrl_act463')
def ctrl_nm463():
    return 'ret463' 

@action('ctrl_act464')
def ctrl_nm464():
    return 'ret464' 

@action('ctrl_act465')
def ctrl_nm465():
    return 'ret465' 

@action('ctrl_act466')
def ctrl_nm466():
    return 'ret466' 

@action('ctrl_act467')
def ctrl_nm467():
    return 'ret467' 

@action('ctrl_act468')
def ctrl_nm468():
    return 'ret468' 

@action('ctrl_act469')
def ctrl_nm469():
    return 'ret469' 

@action('ctrl_act470')
def ctrl_nm470():
    return 'ret470' 

@action('ctrl_act471')
def ctrl_nm471():
    return 'ret471' 

@action('ctrl_act472')
def ctrl_nm472():
    return 'ret472' 

@action('ctrl_act473')
def ctrl_nm473():
    return 'ret473' 

@action('ctrl_act474')
def ctrl_nm474():
    return 'ret474' 

@action('ctrl_act475')
def ctrl_nm475():
    return 'ret475' 

@action('ctrl_act476')
def ctrl_nm476():
    return 'ret476' 

@action('ctrl_act477')
def ctrl_nm477():
    return 'ret477' 

@action('ctrl_act478')
def ctrl_nm478():
    return 'ret478' 

@action('ctrl_act479')
def ctrl_nm479():
    return 'ret479' 

@action('ctrl_act480')
def ctrl_nm480():
    return 'ret480' 

@action('ctrl_act481')
def ctrl_nm481():
    return 'ret481' 

@action('ctrl_act482')
def ctrl_nm482():
    return 'ret482' 

@action('ctrl_act483')
def ctrl_nm483():
    return 'ret483' 

@action('ctrl_act484')
def ctrl_nm484():
    return 'ret484' 

@action('ctrl_act485')
def ctrl_nm485():
    return 'ret485' 

@action('ctrl_act486')
def ctrl_nm486():
    return 'ret486' 

@action('ctrl_act487')
def ctrl_nm487():
    return 'ret487' 

@action('ctrl_act488')
def ctrl_nm488():
    return 'ret488' 

@action('ctrl_act489')
def ctrl_nm489():
    return 'ret489' 

@action('ctrl_act490')
def ctrl_nm490():
    return 'ret490' 

@action('ctrl_act491')
def ctrl_nm491():
    return 'ret491' 

@action('ctrl_act492')
def ctrl_nm492():
    return 'ret492' 

@action('ctrl_act493')
def ctrl_nm493():
    return 'ret493' 

@action('ctrl_act494')
def ctrl_nm494():
    return 'ret494' 

@action('ctrl_act495')
def ctrl_nm495():
    return 'ret495' 

@action('ctrl_act496')
def ctrl_nm496():
    return 'ret496' 

@action('ctrl_act497')
def ctrl_nm497():
    return 'ret497' 

@action('ctrl_act498')
def ctrl_nm498():
    return 'ret498' 

@action('ctrl_act499')
def ctrl_nm499():
    return 'ret499' 

@action('ctrl_act500')
def ctrl_nm500():
    return 'ret500' 

@action('ctrl_act501')
def ctrl_nm501():
    return 'ret501' 

@action('ctrl_act502')
def ctrl_nm502():
    return 'ret502' 

@action('ctrl_act503')
def ctrl_nm503():
    return 'ret503' 

@action('ctrl_act504')
def ctrl_nm504():
    return 'ret504' 

@action('ctrl_act505')
def ctrl_nm505():
    return 'ret505' 

@action('ctrl_act506')
def ctrl_nm506():
    return 'ret506' 

@action('ctrl_act507')
def ctrl_nm507():
    return 'ret507' 

@action('ctrl_act508')
def ctrl_nm508():
    return 'ret508' 

@action('ctrl_act509')
def ctrl_nm509():
    return 'ret509' 

@action('ctrl_act510')
def ctrl_nm510():
    return 'ret510' 

@action('ctrl_act511')
def ctrl_nm511():
    return 'ret511' 

@action('ctrl_act512')
def ctrl_nm512():
    return 'ret512' 

@action('ctrl_act513')
def ctrl_nm513():
    return 'ret513' 

@action('ctrl_act514')
def ctrl_nm514():
    return 'ret514' 

@action('ctrl_act515')
def ctrl_nm515():
    return 'ret515' 

@action('ctrl_act516')
def ctrl_nm516():
    return 'ret516' 

@action('ctrl_act517')
def ctrl_nm517():
    return 'ret517' 

@action('ctrl_act518')
def ctrl_nm518():
    return 'ret518' 

@action('ctrl_act519')
def ctrl_nm519():
    return 'ret519' 

@action('ctrl_act520')
def ctrl_nm520():
    return 'ret520' 

@action('ctrl_act521')
def ctrl_nm521():
    return 'ret521' 

@action('ctrl_act522')
def ctrl_nm522():
    return 'ret522' 

@action('ctrl_act523')
def ctrl_nm523():
    return 'ret523' 

@action('ctrl_act524')
def ctrl_nm524():
    return 'ret524' 

@action('ctrl_act525')
def ctrl_nm525():
    return 'ret525' 

@action('ctrl_act526')
def ctrl_nm526():
    return 'ret526' 

@action('ctrl_act527')
def ctrl_nm527():
    return 'ret527' 

@action('ctrl_act528')
def ctrl_nm528():
    return 'ret528' 

@action('ctrl_act529')
def ctrl_nm529():
    return 'ret529' 

@action('ctrl_act530')
def ctrl_nm530():
    return 'ret530' 

@action('ctrl_act531')
def ctrl_nm531():
    return 'ret531' 

@action('ctrl_act532')
def ctrl_nm532():
    return 'ret532' 

@action('ctrl_act533')
def ctrl_nm533():
    return 'ret533' 

@action('ctrl_act534')
def ctrl_nm534():
    return 'ret534' 

@action('ctrl_act535')
def ctrl_nm535():
    return 'ret535' 

@action('ctrl_act536')
def ctrl_nm536():
    return 'ret536' 

@action('ctrl_act537')
def ctrl_nm537():
    return 'ret537' 

@action('ctrl_act538')
def ctrl_nm538():
    return 'ret538' 

@action('ctrl_act539')
def ctrl_nm539():
    return 'ret539' 

@action('ctrl_act540')
def ctrl_nm540():
    return 'ret540' 

@action('ctrl_act541')
def ctrl_nm541():
    return 'ret541' 

@action('ctrl_act542')
def ctrl_nm542():
    return 'ret542' 

@action('ctrl_act543')
def ctrl_nm543():
    return 'ret543' 

@action('ctrl_act544')
def ctrl_nm544():
    return 'ret544' 

@action('ctrl_act545')
def ctrl_nm545():
    return 'ret545' 

@action('ctrl_act546')
def ctrl_nm546():
    return 'ret546' 

@action('ctrl_act547')
def ctrl_nm547():
    return 'ret547' 

@action('ctrl_act548')
def ctrl_nm548():
    return 'ret548' 

@action('ctrl_act549')
def ctrl_nm549():
    return 'ret549' 

@action('ctrl_act550')
def ctrl_nm550():
    return 'ret550' 

@action('ctrl_act551')
def ctrl_nm551():
    return 'ret551' 

@action('ctrl_act552')
def ctrl_nm552():
    return 'ret552' 

@action('ctrl_act553')
def ctrl_nm553():
    return 'ret553' 

@action('ctrl_act554')
def ctrl_nm554():
    return 'ret554' 

@action('ctrl_act555')
def ctrl_nm555():
    return 'ret555' 

@action('ctrl_act556')
def ctrl_nm556():
    return 'ret556' 

@action('ctrl_act557')
def ctrl_nm557():
    return 'ret557' 

@action('ctrl_act558')
def ctrl_nm558():
    return 'ret558' 

@action('ctrl_act559')
def ctrl_nm559():
    return 'ret559' 

@action('ctrl_act560')
def ctrl_nm560():
    return 'ret560' 

@action('ctrl_act561')
def ctrl_nm561():
    return 'ret561' 

@action('ctrl_act562')
def ctrl_nm562():
    return 'ret562' 

@action('ctrl_act563')
def ctrl_nm563():
    return 'ret563' 

@action('ctrl_act564')
def ctrl_nm564():
    return 'ret564' 

@action('ctrl_act565')
def ctrl_nm565():
    return 'ret565' 

@action('ctrl_act566')
def ctrl_nm566():
    return 'ret566' 

@action('ctrl_act567')
def ctrl_nm567():
    return 'ret567' 

@action('ctrl_act568')
def ctrl_nm568():
    return 'ret568' 

@action('ctrl_act569')
def ctrl_nm569():
    return 'ret569' 

@action('ctrl_act570')
def ctrl_nm570():
    return 'ret570' 

@action('ctrl_act571')
def ctrl_nm571():
    return 'ret571' 

@action('ctrl_act572')
def ctrl_nm572():
    return 'ret572' 

@action('ctrl_act573')
def ctrl_nm573():
    return 'ret573' 

@action('ctrl_act574')
def ctrl_nm574():
    return 'ret574' 

@action('ctrl_act575')
def ctrl_nm575():
    return 'ret575' 

@action('ctrl_act576')
def ctrl_nm576():
    return 'ret576' 

@action('ctrl_act577')
def ctrl_nm577():
    return 'ret577' 

@action('ctrl_act578')
def ctrl_nm578():
    return 'ret578' 

@action('ctrl_act579')
def ctrl_nm579():
    return 'ret579' 

@action('ctrl_act580')
def ctrl_nm580():
    return 'ret580' 

@action('ctrl_act581')
def ctrl_nm581():
    return 'ret581' 

@action('ctrl_act582')
def ctrl_nm582():
    return 'ret582' 

@action('ctrl_act583')
def ctrl_nm583():
    return 'ret583' 

@action('ctrl_act584')
def ctrl_nm584():
    return 'ret584' 

@action('ctrl_act585')
def ctrl_nm585():
    return 'ret585' 

@action('ctrl_act586')
def ctrl_nm586():
    return 'ret586' 

@action('ctrl_act587')
def ctrl_nm587():
    return 'ret587' 

@action('ctrl_act588')
def ctrl_nm588():
    return 'ret588' 

@action('ctrl_act589')
def ctrl_nm589():
    return 'ret589' 

@action('ctrl_act590')
def ctrl_nm590():
    return 'ret590' 

@action('ctrl_act591')
def ctrl_nm591():
    return 'ret591' 

@action('ctrl_act592')
def ctrl_nm592():
    return 'ret592' 

@action('ctrl_act593')
def ctrl_nm593():
    return 'ret593' 

@action('ctrl_act594')
def ctrl_nm594():
    return 'ret594' 

@action('ctrl_act595')
def ctrl_nm595():
    return 'ret595' 

@action('ctrl_act596')
def ctrl_nm596():
    return 'ret596' 

@action('ctrl_act597')
def ctrl_nm597():
    return 'ret597' 

@action('ctrl_act598')
def ctrl_nm598():
    return 'ret598' 

@action('ctrl_act599')
def ctrl_nm599():
    return 'ret599' 

@action('ctrl_act600')
def ctrl_nm600():
    return 'ret600' 

@action('ctrl_act601')
def ctrl_nm601():
    return 'ret601' 

@action('ctrl_act602')
def ctrl_nm602():
    return 'ret602' 

@action('ctrl_act603')
def ctrl_nm603():
    return 'ret603' 

@action('ctrl_act604')
def ctrl_nm604():
    return 'ret604' 

@action('ctrl_act605')
def ctrl_nm605():
    return 'ret605' 

@action('ctrl_act606')
def ctrl_nm606():
    return 'ret606' 

@action('ctrl_act607')
def ctrl_nm607():
    return 'ret607' 

@action('ctrl_act608')
def ctrl_nm608():
    return 'ret608' 

@action('ctrl_act609')
def ctrl_nm609():
    return 'ret609' 

@action('ctrl_act610')
def ctrl_nm610():
    return 'ret610' 

@action('ctrl_act611')
def ctrl_nm611():
    return 'ret611' 

@action('ctrl_act612')
def ctrl_nm612():
    return 'ret612' 

@action('ctrl_act613')
def ctrl_nm613():
    return 'ret613' 

@action('ctrl_act614')
def ctrl_nm614():
    return 'ret614' 

@action('ctrl_act615')
def ctrl_nm615():
    return 'ret615' 

@action('ctrl_act616')
def ctrl_nm616():
    return 'ret616' 

@action('ctrl_act617')
def ctrl_nm617():
    return 'ret617' 

@action('ctrl_act618')
def ctrl_nm618():
    return 'ret618' 

@action('ctrl_act619')
def ctrl_nm619():
    return 'ret619' 

@action('ctrl_act620')
def ctrl_nm620():
    return 'ret620' 

@action('ctrl_act621')
def ctrl_nm621():
    return 'ret621' 

@action('ctrl_act622')
def ctrl_nm622():
    return 'ret622' 

@action('ctrl_act623')
def ctrl_nm623():
    return 'ret623' 

@action('ctrl_act624')
def ctrl_nm624():
    return 'ret624' 

@action('ctrl_act625')
def ctrl_nm625():
    return 'ret625' 

@action('ctrl_act626')
def ctrl_nm626():
    return 'ret626' 

@action('ctrl_act627')
def ctrl_nm627():
    return 'ret627' 

@action('ctrl_act628')
def ctrl_nm628():
    return 'ret628' 

@action('ctrl_act629')
def ctrl_nm629():
    return 'ret629' 

@action('ctrl_act630')
def ctrl_nm630():
    return 'ret630' 

@action('ctrl_act631')
def ctrl_nm631():
    return 'ret631' 

@action('ctrl_act632')
def ctrl_nm632():
    return 'ret632' 

@action('ctrl_act633')
def ctrl_nm633():
    return 'ret633' 

@action('ctrl_act634')
def ctrl_nm634():
    return 'ret634' 

@action('ctrl_act635')
def ctrl_nm635():
    return 'ret635' 

@action('ctrl_act636')
def ctrl_nm636():
    return 'ret636' 

@action('ctrl_act637')
def ctrl_nm637():
    return 'ret637' 

@action('ctrl_act638')
def ctrl_nm638():
    return 'ret638' 

@action('ctrl_act639')
def ctrl_nm639():
    return 'ret639' 

@action('ctrl_act640')
def ctrl_nm640():
    return 'ret640' 

@action('ctrl_act641')
def ctrl_nm641():
    return 'ret641' 

@action('ctrl_act642')
def ctrl_nm642():
    return 'ret642' 

@action('ctrl_act643')
def ctrl_nm643():
    return 'ret643' 

@action('ctrl_act644')
def ctrl_nm644():
    return 'ret644' 

@action('ctrl_act645')
def ctrl_nm645():
    return 'ret645' 

@action('ctrl_act646')
def ctrl_nm646():
    return 'ret646' 

@action('ctrl_act647')
def ctrl_nm647():
    return 'ret647' 

@action('ctrl_act648')
def ctrl_nm648():
    return 'ret648' 

@action('ctrl_act649')
def ctrl_nm649():
    return 'ret649' 

@action('ctrl_act650')
def ctrl_nm650():
    return 'ret650' 

@action('ctrl_act651')
def ctrl_nm651():
    return 'ret651' 

@action('ctrl_act652')
def ctrl_nm652():
    return 'ret652' 

@action('ctrl_act653')
def ctrl_nm653():
    return 'ret653' 

@action('ctrl_act654')
def ctrl_nm654():
    return 'ret654' 

@action('ctrl_act655')
def ctrl_nm655():
    return 'ret655' 

@action('ctrl_act656')
def ctrl_nm656():
    return 'ret656' 

@action('ctrl_act657')
def ctrl_nm657():
    return 'ret657' 

@action('ctrl_act658')
def ctrl_nm658():
    return 'ret658' 

@action('ctrl_act659')
def ctrl_nm659():
    return 'ret659' 

@action('ctrl_act660')
def ctrl_nm660():
    return 'ret660' 

@action('ctrl_act661')
def ctrl_nm661():
    return 'ret661' 

@action('ctrl_act662')
def ctrl_nm662():
    return 'ret662' 

@action('ctrl_act663')
def ctrl_nm663():
    return 'ret663' 

@action('ctrl_act664')
def ctrl_nm664():
    return 'ret664' 

@action('ctrl_act665')
def ctrl_nm665():
    return 'ret665' 

@action('ctrl_act666')
def ctrl_nm666():
    return 'ret666' 

@action('ctrl_act667')
def ctrl_nm667():
    return 'ret667' 

@action('ctrl_act668')
def ctrl_nm668():
    return 'ret668' 

@action('ctrl_act669')
def ctrl_nm669():
    return 'ret669' 

@action('ctrl_act670')
def ctrl_nm670():
    return 'ret670' 

@action('ctrl_act671')
def ctrl_nm671():
    return 'ret671' 

@action('ctrl_act672')
def ctrl_nm672():
    return 'ret672' 

@action('ctrl_act673')
def ctrl_nm673():
    return 'ret673' 

@action('ctrl_act674')
def ctrl_nm674():
    return 'ret674' 

@action('ctrl_act675')
def ctrl_nm675():
    return 'ret675' 

@action('ctrl_act676')
def ctrl_nm676():
    return 'ret676' 

@action('ctrl_act677')
def ctrl_nm677():
    return 'ret677' 

@action('ctrl_act678')
def ctrl_nm678():
    return 'ret678' 

@action('ctrl_act679')
def ctrl_nm679():
    return 'ret679' 

@action('ctrl_act680')
def ctrl_nm680():
    return 'ret680' 

@action('ctrl_act681')
def ctrl_nm681():
    return 'ret681' 

@action('ctrl_act682')
def ctrl_nm682():
    return 'ret682' 

@action('ctrl_act683')
def ctrl_nm683():
    return 'ret683' 

@action('ctrl_act684')
def ctrl_nm684():
    return 'ret684' 

@action('ctrl_act685')
def ctrl_nm685():
    return 'ret685' 

@action('ctrl_act686')
def ctrl_nm686():
    return 'ret686' 

@action('ctrl_act687')
def ctrl_nm687():
    return 'ret687' 

@action('ctrl_act688')
def ctrl_nm688():
    return 'ret688' 

@action('ctrl_act689')
def ctrl_nm689():
    return 'ret689' 

@action('ctrl_act690')
def ctrl_nm690():
    return 'ret690' 

@action('ctrl_act691')
def ctrl_nm691():
    return 'ret691' 

@action('ctrl_act692')
def ctrl_nm692():
    return 'ret692' 

@action('ctrl_act693')
def ctrl_nm693():
    return 'ret693' 

@action('ctrl_act694')
def ctrl_nm694():
    return 'ret694' 

@action('ctrl_act695')
def ctrl_nm695():
    return 'ret695' 

@action('ctrl_act696')
def ctrl_nm696():
    return 'ret696' 

@action('ctrl_act697')
def ctrl_nm697():
    return 'ret697' 

@action('ctrl_act698')
def ctrl_nm698():
    return 'ret698' 

@action('ctrl_act699')
def ctrl_nm699():
    return 'ret699' 

@action('ctrl_act700')
def ctrl_nm700():
    return 'ret700' 

@action('ctrl_act701')
def ctrl_nm701():
    return 'ret701' 

@action('ctrl_act702')
def ctrl_nm702():
    return 'ret702' 

@action('ctrl_act703')
def ctrl_nm703():
    return 'ret703' 

@action('ctrl_act704')
def ctrl_nm704():
    return 'ret704' 

@action('ctrl_act705')
def ctrl_nm705():
    return 'ret705' 

@action('ctrl_act706')
def ctrl_nm706():
    return 'ret706' 

@action('ctrl_act707')
def ctrl_nm707():
    return 'ret707' 

@action('ctrl_act708')
def ctrl_nm708():
    return 'ret708' 

@action('ctrl_act709')
def ctrl_nm709():
    return 'ret709' 

@action('ctrl_act710')
def ctrl_nm710():
    return 'ret710' 

@action('ctrl_act711')
def ctrl_nm711():
    return 'ret711' 

@action('ctrl_act712')
def ctrl_nm712():
    return 'ret712' 

@action('ctrl_act713')
def ctrl_nm713():
    return 'ret713' 

@action('ctrl_act714')
def ctrl_nm714():
    return 'ret714' 

@action('ctrl_act715')
def ctrl_nm715():
    return 'ret715' 

@action('ctrl_act716')
def ctrl_nm716():
    return 'ret716' 

@action('ctrl_act717')
def ctrl_nm717():
    return 'ret717' 

@action('ctrl_act718')
def ctrl_nm718():
    return 'ret718' 

@action('ctrl_act719')
def ctrl_nm719():
    return 'ret719' 

@action('ctrl_act720')
def ctrl_nm720():
    return 'ret720' 

@action('ctrl_act721')
def ctrl_nm721():
    return 'ret721' 

@action('ctrl_act722')
def ctrl_nm722():
    return 'ret722' 

@action('ctrl_act723')
def ctrl_nm723():
    return 'ret723' 

@action('ctrl_act724')
def ctrl_nm724():
    return 'ret724' 

@action('ctrl_act725')
def ctrl_nm725():
    return 'ret725' 

@action('ctrl_act726')
def ctrl_nm726():
    return 'ret726' 

@action('ctrl_act727')
def ctrl_nm727():
    return 'ret727' 

@action('ctrl_act728')
def ctrl_nm728():
    return 'ret728' 

@action('ctrl_act729')
def ctrl_nm729():
    return 'ret729' 

@action('ctrl_act730')
def ctrl_nm730():
    return 'ret730' 

@action('ctrl_act731')
def ctrl_nm731():
    return 'ret731' 

@action('ctrl_act732')
def ctrl_nm732():
    return 'ret732' 

@action('ctrl_act733')
def ctrl_nm733():
    return 'ret733' 

@action('ctrl_act734')
def ctrl_nm734():
    return 'ret734' 

@action('ctrl_act735')
def ctrl_nm735():
    return 'ret735' 

@action('ctrl_act736')
def ctrl_nm736():
    return 'ret736' 

@action('ctrl_act737')
def ctrl_nm737():
    return 'ret737' 

@action('ctrl_act738')
def ctrl_nm738():
    return 'ret738' 

@action('ctrl_act739')
def ctrl_nm739():
    return 'ret739' 

@action('ctrl_act740')
def ctrl_nm740():
    return 'ret740' 

@action('ctrl_act741')
def ctrl_nm741():
    return 'ret741' 

@action('ctrl_act742')
def ctrl_nm742():
    return 'ret742' 

@action('ctrl_act743')
def ctrl_nm743():
    return 'ret743' 

@action('ctrl_act744')
def ctrl_nm744():
    return 'ret744' 

@action('ctrl_act745')
def ctrl_nm745():
    return 'ret745' 

@action('ctrl_act746')
def ctrl_nm746():
    return 'ret746' 

@action('ctrl_act747')
def ctrl_nm747():
    return 'ret747' 

@action('ctrl_act748')
def ctrl_nm748():
    return 'ret748' 

@action('ctrl_act749')
def ctrl_nm749():
    return 'ret749' 

@action('ctrl_act750')
def ctrl_nm750():
    return 'ret750' 

@action('ctrl_act751')
def ctrl_nm751():
    return 'ret751' 

@action('ctrl_act752')
def ctrl_nm752():
    return 'ret752' 

@action('ctrl_act753')
def ctrl_nm753():
    return 'ret753' 

@action('ctrl_act754')
def ctrl_nm754():
    return 'ret754' 

@action('ctrl_act755')
def ctrl_nm755():
    return 'ret755' 

@action('ctrl_act756')
def ctrl_nm756():
    return 'ret756' 

@action('ctrl_act757')
def ctrl_nm757():
    return 'ret757' 

@action('ctrl_act758')
def ctrl_nm758():
    return 'ret758' 

@action('ctrl_act759')
def ctrl_nm759():
    return 'ret759' 

@action('ctrl_act760')
def ctrl_nm760():
    return 'ret760' 

@action('ctrl_act761')
def ctrl_nm761():
    return 'ret761' 

@action('ctrl_act762')
def ctrl_nm762():
    return 'ret762' 

@action('ctrl_act763')
def ctrl_nm763():
    return 'ret763' 

@action('ctrl_act764')
def ctrl_nm764():
    return 'ret764' 

@action('ctrl_act765')
def ctrl_nm765():
    return 'ret765' 

@action('ctrl_act766')
def ctrl_nm766():
    return 'ret766' 

@action('ctrl_act767')
def ctrl_nm767():
    return 'ret767' 

@action('ctrl_act768')
def ctrl_nm768():
    return 'ret768' 

@action('ctrl_act769')
def ctrl_nm769():
    return 'ret769' 

@action('ctrl_act770')
def ctrl_nm770():
    return 'ret770' 

@action('ctrl_act771')
def ctrl_nm771():
    return 'ret771' 

@action('ctrl_act772')
def ctrl_nm772():
    return 'ret772' 

@action('ctrl_act773')
def ctrl_nm773():
    return 'ret773' 

@action('ctrl_act774')
def ctrl_nm774():
    return 'ret774' 

@action('ctrl_act775')
def ctrl_nm775():
    return 'ret775' 

@action('ctrl_act776')
def ctrl_nm776():
    return 'ret776' 

@action('ctrl_act777')
def ctrl_nm777():
    return 'ret777' 

@action('ctrl_act778')
def ctrl_nm778():
    return 'ret778' 

@action('ctrl_act779')
def ctrl_nm779():
    return 'ret779' 

@action('ctrl_act780')
def ctrl_nm780():
    return 'ret780' 

@action('ctrl_act781')
def ctrl_nm781():
    return 'ret781' 

@action('ctrl_act782')
def ctrl_nm782():
    return 'ret782' 

@action('ctrl_act783')
def ctrl_nm783():
    return 'ret783' 

@action('ctrl_act784')
def ctrl_nm784():
    return 'ret784' 

@action('ctrl_act785')
def ctrl_nm785():
    return 'ret785' 

@action('ctrl_act786')
def ctrl_nm786():
    return 'ret786' 

@action('ctrl_act787')
def ctrl_nm787():
    return 'ret787' 

@action('ctrl_act788')
def ctrl_nm788():
    return 'ret788' 

@action('ctrl_act789')
def ctrl_nm789():
    return 'ret789' 

@action('ctrl_act790')
def ctrl_nm790():
    return 'ret790' 

@action('ctrl_act791')
def ctrl_nm791():
    return 'ret791' 

@action('ctrl_act792')
def ctrl_nm792():
    return 'ret792' 

@action('ctrl_act793')
def ctrl_nm793():
    return 'ret793' 

@action('ctrl_act794')
def ctrl_nm794():
    return 'ret794' 

@action('ctrl_act795')
def ctrl_nm795():
    return 'ret795' 

@action('ctrl_act796')
def ctrl_nm796():
    return 'ret796' 

@action('ctrl_act797')
def ctrl_nm797():
    return 'ret797' 

@action('ctrl_act798')
def ctrl_nm798():
    return 'ret798' 

@action('ctrl_act799')
def ctrl_nm799():
    return 'ret799' 

@action('ctrl_act800')
def ctrl_nm800():
    return 'ret800' 

@action('ctrl_act801')
def ctrl_nm801():
    return 'ret801' 

@action('ctrl_act802')
def ctrl_nm802():
    return 'ret802' 

@action('ctrl_act803')
def ctrl_nm803():
    return 'ret803' 

@action('ctrl_act804')
def ctrl_nm804():
    return 'ret804' 

@action('ctrl_act805')
def ctrl_nm805():
    return 'ret805' 

@action('ctrl_act806')
def ctrl_nm806():
    return 'ret806' 

@action('ctrl_act807')
def ctrl_nm807():
    return 'ret807' 

@action('ctrl_act808')
def ctrl_nm808():
    return 'ret808' 

@action('ctrl_act809')
def ctrl_nm809():
    return 'ret809' 

@action('ctrl_act810')
def ctrl_nm810():
    return 'ret810' 

@action('ctrl_act811')
def ctrl_nm811():
    return 'ret811' 

@action('ctrl_act812')
def ctrl_nm812():
    return 'ret812' 

@action('ctrl_act813')
def ctrl_nm813():
    return 'ret813' 

@action('ctrl_act814')
def ctrl_nm814():
    return 'ret814' 

@action('ctrl_act815')
def ctrl_nm815():
    return 'ret815' 

@action('ctrl_act816')
def ctrl_nm816():
    return 'ret816' 

@action('ctrl_act817')
def ctrl_nm817():
    return 'ret817' 

@action('ctrl_act818')
def ctrl_nm818():
    return 'ret818' 

@action('ctrl_act819')
def ctrl_nm819():
    return 'ret819' 

@action('ctrl_act820')
def ctrl_nm820():
    return 'ret820' 

@action('ctrl_act821')
def ctrl_nm821():
    return 'ret821' 

@action('ctrl_act822')
def ctrl_nm822():
    return 'ret822' 

@action('ctrl_act823')
def ctrl_nm823():
    return 'ret823' 

@action('ctrl_act824')
def ctrl_nm824():
    return 'ret824' 

@action('ctrl_act825')
def ctrl_nm825():
    return 'ret825' 

@action('ctrl_act826')
def ctrl_nm826():
    return 'ret826' 

@action('ctrl_act827')
def ctrl_nm827():
    return 'ret827' 

@action('ctrl_act828')
def ctrl_nm828():
    return 'ret828' 

@action('ctrl_act829')
def ctrl_nm829():
    return 'ret829' 

@action('ctrl_act830')
def ctrl_nm830():
    return 'ret830' 

@action('ctrl_act831')
def ctrl_nm831():
    return 'ret831' 

@action('ctrl_act832')
def ctrl_nm832():
    return 'ret832' 

@action('ctrl_act833')
def ctrl_nm833():
    return 'ret833' 

@action('ctrl_act834')
def ctrl_nm834():
    return 'ret834' 

@action('ctrl_act835')
def ctrl_nm835():
    return 'ret835' 

@action('ctrl_act836')
def ctrl_nm836():
    return 'ret836' 

@action('ctrl_act837')
def ctrl_nm837():
    return 'ret837' 

@action('ctrl_act838')
def ctrl_nm838():
    return 'ret838' 

@action('ctrl_act839')
def ctrl_nm839():
    return 'ret839' 

@action('ctrl_act840')
def ctrl_nm840():
    return 'ret840' 

@action('ctrl_act841')
def ctrl_nm841():
    return 'ret841' 

@action('ctrl_act842')
def ctrl_nm842():
    return 'ret842' 

@action('ctrl_act843')
def ctrl_nm843():
    return 'ret843' 

@action('ctrl_act844')
def ctrl_nm844():
    return 'ret844' 

@action('ctrl_act845')
def ctrl_nm845():
    return 'ret845' 

@action('ctrl_act846')
def ctrl_nm846():
    return 'ret846' 

@action('ctrl_act847')
def ctrl_nm847():
    return 'ret847' 

@action('ctrl_act848')
def ctrl_nm848():
    return 'ret848' 

@action('ctrl_act849')
def ctrl_nm849():
    return 'ret849' 

@action('ctrl_act850')
def ctrl_nm850():
    return 'ret850' 

@action('ctrl_act851')
def ctrl_nm851():
    return 'ret851' 

@action('ctrl_act852')
def ctrl_nm852():
    return 'ret852' 

@action('ctrl_act853')
def ctrl_nm853():
    return 'ret853' 

@action('ctrl_act854')
def ctrl_nm854():
    return 'ret854' 

@action('ctrl_act855')
def ctrl_nm855():
    return 'ret855' 

@action('ctrl_act856')
def ctrl_nm856():
    return 'ret856' 

@action('ctrl_act857')
def ctrl_nm857():
    return 'ret857' 

@action('ctrl_act858')
def ctrl_nm858():
    return 'ret858' 

@action('ctrl_act859')
def ctrl_nm859():
    return 'ret859' 

@action('ctrl_act860')
def ctrl_nm860():
    return 'ret860' 

@action('ctrl_act861')
def ctrl_nm861():
    return 'ret861' 

@action('ctrl_act862')
def ctrl_nm862():
    return 'ret862' 

@action('ctrl_act863')
def ctrl_nm863():
    return 'ret863' 

@action('ctrl_act864')
def ctrl_nm864():
    return 'ret864' 

@action('ctrl_act865')
def ctrl_nm865():
    return 'ret865' 

@action('ctrl_act866')
def ctrl_nm866():
    return 'ret866' 

@action('ctrl_act867')
def ctrl_nm867():
    return 'ret867' 

@action('ctrl_act868')
def ctrl_nm868():
    return 'ret868' 

@action('ctrl_act869')
def ctrl_nm869():
    return 'ret869' 

@action('ctrl_act870')
def ctrl_nm870():
    return 'ret870' 

@action('ctrl_act871')
def ctrl_nm871():
    return 'ret871' 

@action('ctrl_act872')
def ctrl_nm872():
    return 'ret872' 

@action('ctrl_act873')
def ctrl_nm873():
    return 'ret873' 

@action('ctrl_act874')
def ctrl_nm874():
    return 'ret874' 

@action('ctrl_act875')
def ctrl_nm875():
    return 'ret875' 

@action('ctrl_act876')
def ctrl_nm876():
    return 'ret876' 

@action('ctrl_act877')
def ctrl_nm877():
    return 'ret877' 

@action('ctrl_act878')
def ctrl_nm878():
    return 'ret878' 

@action('ctrl_act879')
def ctrl_nm879():
    return 'ret879' 

@action('ctrl_act880')
def ctrl_nm880():
    return 'ret880' 

@action('ctrl_act881')
def ctrl_nm881():
    return 'ret881' 

@action('ctrl_act882')
def ctrl_nm882():
    return 'ret882' 

@action('ctrl_act883')
def ctrl_nm883():
    return 'ret883' 

@action('ctrl_act884')
def ctrl_nm884():
    return 'ret884' 

@action('ctrl_act885')
def ctrl_nm885():
    return 'ret885' 

@action('ctrl_act886')
def ctrl_nm886():
    return 'ret886' 

@action('ctrl_act887')
def ctrl_nm887():
    return 'ret887' 

@action('ctrl_act888')
def ctrl_nm888():
    return 'ret888' 

@action('ctrl_act889')
def ctrl_nm889():
    return 'ret889' 

@action('ctrl_act890')
def ctrl_nm890():
    return 'ret890' 

@action('ctrl_act891')
def ctrl_nm891():
    return 'ret891' 

@action('ctrl_act892')
def ctrl_nm892():
    return 'ret892' 

@action('ctrl_act893')
def ctrl_nm893():
    return 'ret893' 

@action('ctrl_act894')
def ctrl_nm894():
    return 'ret894' 

@action('ctrl_act895')
def ctrl_nm895():
    return 'ret895' 

@action('ctrl_act896')
def ctrl_nm896():
    return 'ret896' 

@action('ctrl_act897')
def ctrl_nm897():
    return 'ret897' 

@action('ctrl_act898')
def ctrl_nm898():
    return 'ret898' 

@action('ctrl_act899')
def ctrl_nm899():
    return 'ret899' 

@action('ctrl_act900')
def ctrl_nm900():
    return 'ret900' 

@action('ctrl_act901')
def ctrl_nm901():
    return 'ret901' 

@action('ctrl_act902')
def ctrl_nm902():
    return 'ret902' 

@action('ctrl_act903')
def ctrl_nm903():
    return 'ret903' 

@action('ctrl_act904')
def ctrl_nm904():
    return 'ret904' 

@action('ctrl_act905')
def ctrl_nm905():
    return 'ret905' 

@action('ctrl_act906')
def ctrl_nm906():
    return 'ret906' 

@action('ctrl_act907')
def ctrl_nm907():
    return 'ret907' 

@action('ctrl_act908')
def ctrl_nm908():
    return 'ret908' 

@action('ctrl_act909')
def ctrl_nm909():
    return 'ret909' 

@action('ctrl_act910')
def ctrl_nm910():
    return 'ret910' 

@action('ctrl_act911')
def ctrl_nm911():
    return 'ret911' 

@action('ctrl_act912')
def ctrl_nm912():
    return 'ret912' 

@action('ctrl_act913')
def ctrl_nm913():
    return 'ret913' 

@action('ctrl_act914')
def ctrl_nm914():
    return 'ret914' 

@action('ctrl_act915')
def ctrl_nm915():
    return 'ret915' 

@action('ctrl_act916')
def ctrl_nm916():
    return 'ret916' 

@action('ctrl_act917')
def ctrl_nm917():
    return 'ret917' 

@action('ctrl_act918')
def ctrl_nm918():
    return 'ret918' 

@action('ctrl_act919')
def ctrl_nm919():
    return 'ret919' 

@action('ctrl_act920')
def ctrl_nm920():
    return 'ret920' 

@action('ctrl_act921')
def ctrl_nm921():
    return 'ret921' 

@action('ctrl_act922')
def ctrl_nm922():
    return 'ret922' 

@action('ctrl_act923')
def ctrl_nm923():
    return 'ret923' 

@action('ctrl_act924')
def ctrl_nm924():
    return 'ret924' 

@action('ctrl_act925')
def ctrl_nm925():
    return 'ret925' 

@action('ctrl_act926')
def ctrl_nm926():
    return 'ret926' 

@action('ctrl_act927')
def ctrl_nm927():
    return 'ret927' 

@action('ctrl_act928')
def ctrl_nm928():
    return 'ret928' 

@action('ctrl_act929')
def ctrl_nm929():
    return 'ret929' 

@action('ctrl_act930')
def ctrl_nm930():
    return 'ret930' 

@action('ctrl_act931')
def ctrl_nm931():
    return 'ret931' 

@action('ctrl_act932')
def ctrl_nm932():
    return 'ret932' 

@action('ctrl_act933')
def ctrl_nm933():
    return 'ret933' 

@action('ctrl_act934')
def ctrl_nm934():
    return 'ret934' 

@action('ctrl_act935')
def ctrl_nm935():
    return 'ret935' 

@action('ctrl_act936')
def ctrl_nm936():
    return 'ret936' 

@action('ctrl_act937')
def ctrl_nm937():
    return 'ret937' 

@action('ctrl_act938')
def ctrl_nm938():
    return 'ret938' 

@action('ctrl_act939')
def ctrl_nm939():
    return 'ret939' 

@action('ctrl_act940')
def ctrl_nm940():
    return 'ret940' 

@action('ctrl_act941')
def ctrl_nm941():
    return 'ret941' 

@action('ctrl_act942')
def ctrl_nm942():
    return 'ret942' 

@action('ctrl_act943')
def ctrl_nm943():
    return 'ret943' 

@action('ctrl_act944')
def ctrl_nm944():
    return 'ret944' 

@action('ctrl_act945')
def ctrl_nm945():
    return 'ret945' 

@action('ctrl_act946')
def ctrl_nm946():
    return 'ret946' 

@action('ctrl_act947')
def ctrl_nm947():
    return 'ret947' 

@action('ctrl_act948')
def ctrl_nm948():
    return 'ret948' 

@action('ctrl_act949')
def ctrl_nm949():
    return 'ret949' 

@action('ctrl_act950')
def ctrl_nm950():
    return 'ret950' 

@action('ctrl_act951')
def ctrl_nm951():
    return 'ret951' 

@action('ctrl_act952')
def ctrl_nm952():
    return 'ret952' 

@action('ctrl_act953')
def ctrl_nm953():
    return 'ret953' 

@action('ctrl_act954')
def ctrl_nm954():
    return 'ret954' 

@action('ctrl_act955')
def ctrl_nm955():
    return 'ret955' 

@action('ctrl_act956')
def ctrl_nm956():
    return 'ret956' 

@action('ctrl_act957')
def ctrl_nm957():
    return 'ret957' 

@action('ctrl_act958')
def ctrl_nm958():
    return 'ret958' 

@action('ctrl_act959')
def ctrl_nm959():
    return 'ret959' 

@action('ctrl_act960')
def ctrl_nm960():
    return 'ret960' 

@action('ctrl_act961')
def ctrl_nm961():
    return 'ret961' 

@action('ctrl_act962')
def ctrl_nm962():
    return 'ret962' 

@action('ctrl_act963')
def ctrl_nm963():
    return 'ret963' 

@action('ctrl_act964')
def ctrl_nm964():
    return 'ret964' 

@action('ctrl_act965')
def ctrl_nm965():
    return 'ret965' 

@action('ctrl_act966')
def ctrl_nm966():
    return 'ret966' 

@action('ctrl_act967')
def ctrl_nm967():
    return 'ret967' 

@action('ctrl_act968')
def ctrl_nm968():
    return 'ret968' 

@action('ctrl_act969')
def ctrl_nm969():
    return 'ret969' 

@action('ctrl_act970')
def ctrl_nm970():
    return 'ret970' 

@action('ctrl_act971')
def ctrl_nm971():
    return 'ret971' 

@action('ctrl_act972')
def ctrl_nm972():
    return 'ret972' 

@action('ctrl_act973')
def ctrl_nm973():
    return 'ret973' 

@action('ctrl_act974')
def ctrl_nm974():
    return 'ret974' 

@action('ctrl_act975')
def ctrl_nm975():
    return 'ret975' 

@action('ctrl_act976')
def ctrl_nm976():
    return 'ret976' 

@action('ctrl_act977')
def ctrl_nm977():
    return 'ret977' 

@action('ctrl_act978')
def ctrl_nm978():
    return 'ret978' 

@action('ctrl_act979')
def ctrl_nm979():
    return 'ret979' 

@action('ctrl_act980')
def ctrl_nm980():
    return 'ret980' 

@action('ctrl_act981')
def ctrl_nm981():
    return 'ret981' 

@action('ctrl_act982')
def ctrl_nm982():
    return 'ret982' 

@action('ctrl_act983')
def ctrl_nm983():
    return 'ret983' 

@action('ctrl_act984')
def ctrl_nm984():
    return 'ret984' 

@action('ctrl_act985')
def ctrl_nm985():
    return 'ret985' 

@action('ctrl_act986')
def ctrl_nm986():
    return 'ret986' 

@action('ctrl_act987')
def ctrl_nm987():
    return 'ret987' 

@action('ctrl_act988')
def ctrl_nm988():
    return 'ret988' 

@action('ctrl_act989')
def ctrl_nm989():
    return 'ret989' 

@action('ctrl_act990')
def ctrl_nm990():
    return 'ret990' 

@action('ctrl_act991')
def ctrl_nm991():
    return 'ret991' 

@action('ctrl_act992')
def ctrl_nm992():
    return 'ret992' 

@action('ctrl_act993')
def ctrl_nm993():
    return 'ret993' 

@action('ctrl_act994')
def ctrl_nm994():
    return 'ret994' 

@action('ctrl_act995')
def ctrl_nm995():
    return 'ret995' 

@action('ctrl_act996')
def ctrl_nm996():
    return 'ret996' 

@action('ctrl_act997')
def ctrl_nm997():
    return 'ret997' 

@action('ctrl_act998')
def ctrl_nm998():
    return 'ret998' 

@action('ctrl_act999')
def ctrl_nm999():
    return 'ret999' 

@action('ctrl_act1000')
def ctrl_nm1000():
    return 'ret1000' 

@action('ctrl_act1001')
def ctrl_nm1001():
    return 'ret1001' 

@action('ctrl_act1002')
def ctrl_nm1002():
    return 'ret1002' 

@action('ctrl_act1003')
def ctrl_nm1003():
    return 'ret1003' 

@action('ctrl_act1004')
def ctrl_nm1004():
    return 'ret1004' 

@action('ctrl_act1005')
def ctrl_nm1005():
    return 'ret1005' 

@action('ctrl_act1006')
def ctrl_nm1006():
    return 'ret1006' 

@action('ctrl_act1007')
def ctrl_nm1007():
    return 'ret1007' 

@action('ctrl_act1008')
def ctrl_nm1008():
    return 'ret1008' 

@action('ctrl_act1009')
def ctrl_nm1009():
    return 'ret1009' 

@action('ctrl_act1010')
def ctrl_nm1010():
    return 'ret1010' 

@action('ctrl_act1011')
def ctrl_nm1011():
    return 'ret1011' 

@action('ctrl_act1012')
def ctrl_nm1012():
    return 'ret1012' 

@action('ctrl_act1013')
def ctrl_nm1013():
    return 'ret1013' 

@action('ctrl_act1014')
def ctrl_nm1014():
    return 'ret1014' 

@action('ctrl_act1015')
def ctrl_nm1015():
    return 'ret1015' 

@action('ctrl_act1016')
def ctrl_nm1016():
    return 'ret1016' 

@action('ctrl_act1017')
def ctrl_nm1017():
    return 'ret1017' 

@action('ctrl_act1018')
def ctrl_nm1018():
    return 'ret1018' 

@action('ctrl_act1019')
def ctrl_nm1019():
    return 'ret1019' 

@action('ctrl_act1020')
def ctrl_nm1020():
    return 'ret1020' 

@action('ctrl_act1021')
def ctrl_nm1021():
    return 'ret1021' 

@action('ctrl_act1022')
def ctrl_nm1022():
    return 'ret1022' 

@action('ctrl_act1023')
def ctrl_nm1023():
    return 'ret1023' 

@action('ctrl_act1024')
def ctrl_nm1024():
    return 'ret1024' 

@action('ctrl_act1025')
def ctrl_nm1025():
    return 'ret1025' 

@action('ctrl_act1026')
def ctrl_nm1026():
    return 'ret1026' 

@action('ctrl_act1027')
def ctrl_nm1027():
    return 'ret1027' 

@action('ctrl_act1028')
def ctrl_nm1028():
    return 'ret1028' 

@action('ctrl_act1029')
def ctrl_nm1029():
    return 'ret1029' 

@action('ctrl_act1030')
def ctrl_nm1030():
    return 'ret1030' 

@action('ctrl_act1031')
def ctrl_nm1031():
    return 'ret1031' 

@action('ctrl_act1032')
def ctrl_nm1032():
    return 'ret1032' 

@action('ctrl_act1033')
def ctrl_nm1033():
    return 'ret1033' 

@action('ctrl_act1034')
def ctrl_nm1034():
    return 'ret1034' 

@action('ctrl_act1035')
def ctrl_nm1035():
    return 'ret1035' 

@action('ctrl_act1036')
def ctrl_nm1036():
    return 'ret1036' 

@action('ctrl_act1037')
def ctrl_nm1037():
    return 'ret1037' 

@action('ctrl_act1038')
def ctrl_nm1038():
    return 'ret1038' 

@action('ctrl_act1039')
def ctrl_nm1039():
    return 'ret1039' 

@action('ctrl_act1040')
def ctrl_nm1040():
    return 'ret1040' 

@action('ctrl_act1041')
def ctrl_nm1041():
    return 'ret1041' 

@action('ctrl_act1042')
def ctrl_nm1042():
    return 'ret1042' 

@action('ctrl_act1043')
def ctrl_nm1043():
    return 'ret1043' 

@action('ctrl_act1044')
def ctrl_nm1044():
    return 'ret1044' 

@action('ctrl_act1045')
def ctrl_nm1045():
    return 'ret1045' 

@action('ctrl_act1046')
def ctrl_nm1046():
    return 'ret1046' 

@action('ctrl_act1047')
def ctrl_nm1047():
    return 'ret1047' 

@action('ctrl_act1048')
def ctrl_nm1048():
    return 'ret1048' 

@action('ctrl_act1049')
def ctrl_nm1049():
    return 'ret1049' 

@action('ctrl_act1050')
def ctrl_nm1050():
    return 'ret1050' 

@action('ctrl_act1051')
def ctrl_nm1051():
    return 'ret1051' 

@action('ctrl_act1052')
def ctrl_nm1052():
    return 'ret1052' 

@action('ctrl_act1053')
def ctrl_nm1053():
    return 'ret1053' 

@action('ctrl_act1054')
def ctrl_nm1054():
    return 'ret1054' 

@action('ctrl_act1055')
def ctrl_nm1055():
    return 'ret1055' 

@action('ctrl_act1056')
def ctrl_nm1056():
    return 'ret1056' 

@action('ctrl_act1057')
def ctrl_nm1057():
    return 'ret1057' 

@action('ctrl_act1058')
def ctrl_nm1058():
    return 'ret1058' 

@action('ctrl_act1059')
def ctrl_nm1059():
    return 'ret1059' 

@action('ctrl_act1060')
def ctrl_nm1060():
    return 'ret1060' 

@action('ctrl_act1061')
def ctrl_nm1061():
    return 'ret1061' 

@action('ctrl_act1062')
def ctrl_nm1062():
    return 'ret1062' 

@action('ctrl_act1063')
def ctrl_nm1063():
    return 'ret1063' 

@action('ctrl_act1064')
def ctrl_nm1064():
    return 'ret1064' 

@action('ctrl_act1065')
def ctrl_nm1065():
    return 'ret1065' 

@action('ctrl_act1066')
def ctrl_nm1066():
    return 'ret1066' 

@action('ctrl_act1067')
def ctrl_nm1067():
    return 'ret1067' 

@action('ctrl_act1068')
def ctrl_nm1068():
    return 'ret1068' 

@action('ctrl_act1069')
def ctrl_nm1069():
    return 'ret1069' 

@action('ctrl_act1070')
def ctrl_nm1070():
    return 'ret1070' 

@action('ctrl_act1071')
def ctrl_nm1071():
    return 'ret1071' 

@action('ctrl_act1072')
def ctrl_nm1072():
    return 'ret1072' 

@action('ctrl_act1073')
def ctrl_nm1073():
    return 'ret1073' 

@action('ctrl_act1074')
def ctrl_nm1074():
    return 'ret1074' 

@action('ctrl_act1075')
def ctrl_nm1075():
    return 'ret1075' 

@action('ctrl_act1076')
def ctrl_nm1076():
    return 'ret1076' 

@action('ctrl_act1077')
def ctrl_nm1077():
    return 'ret1077' 

@action('ctrl_act1078')
def ctrl_nm1078():
    return 'ret1078' 

@action('ctrl_act1079')
def ctrl_nm1079():
    return 'ret1079' 

@action('ctrl_act1080')
def ctrl_nm1080():
    return 'ret1080' 

@action('ctrl_act1081')
def ctrl_nm1081():
    return 'ret1081' 

@action('ctrl_act1082')
def ctrl_nm1082():
    return 'ret1082' 

@action('ctrl_act1083')
def ctrl_nm1083():
    return 'ret1083' 

@action('ctrl_act1084')
def ctrl_nm1084():
    return 'ret1084' 

@action('ctrl_act1085')
def ctrl_nm1085():
    return 'ret1085' 

@action('ctrl_act1086')
def ctrl_nm1086():
    return 'ret1086' 

@action('ctrl_act1087')
def ctrl_nm1087():
    return 'ret1087' 

@action('ctrl_act1088')
def ctrl_nm1088():
    return 'ret1088' 

@action('ctrl_act1089')
def ctrl_nm1089():
    return 'ret1089' 

@action('ctrl_act1090')
def ctrl_nm1090():
    return 'ret1090' 

@action('ctrl_act1091')
def ctrl_nm1091():
    return 'ret1091' 

@action('ctrl_act1092')
def ctrl_nm1092():
    return 'ret1092' 

@action('ctrl_act1093')
def ctrl_nm1093():
    return 'ret1093' 

@action('ctrl_act1094')
def ctrl_nm1094():
    return 'ret1094' 

@action('ctrl_act1095')
def ctrl_nm1095():
    return 'ret1095' 

@action('ctrl_act1096')
def ctrl_nm1096():
    return 'ret1096' 

@action('ctrl_act1097')
def ctrl_nm1097():
    return 'ret1097' 

@action('ctrl_act1098')
def ctrl_nm1098():
    return 'ret1098' 

@action('ctrl_act1099')
def ctrl_nm1099():
    return 'ret1099' 

@action('ctrl_act1100')
def ctrl_nm1100():
    return 'ret1100' 

@action('ctrl_act1101')
def ctrl_nm1101():
    return 'ret1101' 

@action('ctrl_act1102')
def ctrl_nm1102():
    return 'ret1102' 

@action('ctrl_act1103')
def ctrl_nm1103():
    return 'ret1103' 

@action('ctrl_act1104')
def ctrl_nm1104():
    return 'ret1104' 

@action('ctrl_act1105')
def ctrl_nm1105():
    return 'ret1105' 

@action('ctrl_act1106')
def ctrl_nm1106():
    return 'ret1106' 

@action('ctrl_act1107')
def ctrl_nm1107():
    return 'ret1107' 

@action('ctrl_act1108')
def ctrl_nm1108():
    return 'ret1108' 

@action('ctrl_act1109')
def ctrl_nm1109():
    return 'ret1109' 

@action('ctrl_act1110')
def ctrl_nm1110():
    return 'ret1110' 

@action('ctrl_act1111')
def ctrl_nm1111():
    return 'ret1111' 

@action('ctrl_act1112')
def ctrl_nm1112():
    return 'ret1112' 

@action('ctrl_act1113')
def ctrl_nm1113():
    return 'ret1113' 

@action('ctrl_act1114')
def ctrl_nm1114():
    return 'ret1114' 

@action('ctrl_act1115')
def ctrl_nm1115():
    return 'ret1115' 

@action('ctrl_act1116')
def ctrl_nm1116():
    return 'ret1116' 

@action('ctrl_act1117')
def ctrl_nm1117():
    return 'ret1117' 

@action('ctrl_act1118')
def ctrl_nm1118():
    return 'ret1118' 

@action('ctrl_act1119')
def ctrl_nm1119():
    return 'ret1119' 

@action('ctrl_act1120')
def ctrl_nm1120():
    return 'ret1120' 

@action('ctrl_act1121')
def ctrl_nm1121():
    return 'ret1121' 

@action('ctrl_act1122')
def ctrl_nm1122():
    return 'ret1122' 

@action('ctrl_act1123')
def ctrl_nm1123():
    return 'ret1123' 

@action('ctrl_act1124')
def ctrl_nm1124():
    return 'ret1124' 

@action('ctrl_act1125')
def ctrl_nm1125():
    return 'ret1125' 

@action('ctrl_act1126')
def ctrl_nm1126():
    return 'ret1126' 

@action('ctrl_act1127')
def ctrl_nm1127():
    return 'ret1127' 

@action('ctrl_act1128')
def ctrl_nm1128():
    return 'ret1128' 

@action('ctrl_act1129')
def ctrl_nm1129():
    return 'ret1129' 

@action('ctrl_act1130')
def ctrl_nm1130():
    return 'ret1130' 

@action('ctrl_act1131')
def ctrl_nm1131():
    return 'ret1131' 

@action('ctrl_act1132')
def ctrl_nm1132():
    return 'ret1132' 

@action('ctrl_act1133')
def ctrl_nm1133():
    return 'ret1133' 

@action('ctrl_act1134')
def ctrl_nm1134():
    return 'ret1134' 

@action('ctrl_act1135')
def ctrl_nm1135():
    return 'ret1135' 

@action('ctrl_act1136')
def ctrl_nm1136():
    return 'ret1136' 

@action('ctrl_act1137')
def ctrl_nm1137():
    return 'ret1137' 

@action('ctrl_act1138')
def ctrl_nm1138():
    return 'ret1138' 

@action('ctrl_act1139')
def ctrl_nm1139():
    return 'ret1139' 

@action('ctrl_act1140')
def ctrl_nm1140():
    return 'ret1140' 

@action('ctrl_act1141')
def ctrl_nm1141():
    return 'ret1141' 

@action('ctrl_act1142')
def ctrl_nm1142():
    return 'ret1142' 

@action('ctrl_act1143')
def ctrl_nm1143():
    return 'ret1143' 

@action('ctrl_act1144')
def ctrl_nm1144():
    return 'ret1144' 

@action('ctrl_act1145')
def ctrl_nm1145():
    return 'ret1145' 

@action('ctrl_act1146')
def ctrl_nm1146():
    return 'ret1146' 

@action('ctrl_act1147')
def ctrl_nm1147():
    return 'ret1147' 

@action('ctrl_act1148')
def ctrl_nm1148():
    return 'ret1148' 

@action('ctrl_act1149')
def ctrl_nm1149():
    return 'ret1149' 

@action('ctrl_act1150')
def ctrl_nm1150():
    return 'ret1150' 

@action('ctrl_act1151')
def ctrl_nm1151():
    return 'ret1151' 

@action('ctrl_act1152')
def ctrl_nm1152():
    return 'ret1152' 

@action('ctrl_act1153')
def ctrl_nm1153():
    return 'ret1153' 

@action('ctrl_act1154')
def ctrl_nm1154():
    return 'ret1154' 

@action('ctrl_act1155')
def ctrl_nm1155():
    return 'ret1155' 

@action('ctrl_act1156')
def ctrl_nm1156():
    return 'ret1156' 

@action('ctrl_act1157')
def ctrl_nm1157():
    return 'ret1157' 

@action('ctrl_act1158')
def ctrl_nm1158():
    return 'ret1158' 

@action('ctrl_act1159')
def ctrl_nm1159():
    return 'ret1159' 

@action('ctrl_act1160')
def ctrl_nm1160():
    return 'ret1160' 

@action('ctrl_act1161')
def ctrl_nm1161():
    return 'ret1161' 

@action('ctrl_act1162')
def ctrl_nm1162():
    return 'ret1162' 

@action('ctrl_act1163')
def ctrl_nm1163():
    return 'ret1163' 

@action('ctrl_act1164')
def ctrl_nm1164():
    return 'ret1164' 

@action('ctrl_act1165')
def ctrl_nm1165():
    return 'ret1165' 

@action('ctrl_act1166')
def ctrl_nm1166():
    return 'ret1166' 

@action('ctrl_act1167')
def ctrl_nm1167():
    return 'ret1167' 

@action('ctrl_act1168')
def ctrl_nm1168():
    return 'ret1168' 

@action('ctrl_act1169')
def ctrl_nm1169():
    return 'ret1169' 

@action('ctrl_act1170')
def ctrl_nm1170():
    return 'ret1170' 

@action('ctrl_act1171')
def ctrl_nm1171():
    return 'ret1171' 

@action('ctrl_act1172')
def ctrl_nm1172():
    return 'ret1172' 

@action('ctrl_act1173')
def ctrl_nm1173():
    return 'ret1173' 

@action('ctrl_act1174')
def ctrl_nm1174():
    return 'ret1174' 

@action('ctrl_act1175')
def ctrl_nm1175():
    return 'ret1175' 

@action('ctrl_act1176')
def ctrl_nm1176():
    return 'ret1176' 

@action('ctrl_act1177')
def ctrl_nm1177():
    return 'ret1177' 

@action('ctrl_act1178')
def ctrl_nm1178():
    return 'ret1178' 

@action('ctrl_act1179')
def ctrl_nm1179():
    return 'ret1179' 

@action('ctrl_act1180')
def ctrl_nm1180():
    return 'ret1180' 

@action('ctrl_act1181')
def ctrl_nm1181():
    return 'ret1181' 

@action('ctrl_act1182')
def ctrl_nm1182():
    return 'ret1182' 

@action('ctrl_act1183')
def ctrl_nm1183():
    return 'ret1183' 

@action('ctrl_act1184')
def ctrl_nm1184():
    return 'ret1184' 

@action('ctrl_act1185')
def ctrl_nm1185():
    return 'ret1185' 

@action('ctrl_act1186')
def ctrl_nm1186():
    return 'ret1186' 

@action('ctrl_act1187')
def ctrl_nm1187():
    return 'ret1187' 

@action('ctrl_act1188')
def ctrl_nm1188():
    return 'ret1188' 

@action('ctrl_act1189')
def ctrl_nm1189():
    return 'ret1189' 

@action('ctrl_act1190')
def ctrl_nm1190():
    return 'ret1190' 

@action('ctrl_act1191')
def ctrl_nm1191():
    return 'ret1191' 

@action('ctrl_act1192')
def ctrl_nm1192():
    return 'ret1192' 

@action('ctrl_act1193')
def ctrl_nm1193():
    return 'ret1193' 

@action('ctrl_act1194')
def ctrl_nm1194():
    return 'ret1194' 

@action('ctrl_act1195')
def ctrl_nm1195():
    return 'ret1195' 

@action('ctrl_act1196')
def ctrl_nm1196():
    return 'ret1196' 

@action('ctrl_act1197')
def ctrl_nm1197():
    return 'ret1197' 

@action('ctrl_act1198')
def ctrl_nm1198():
    return 'ret1198' 

@action('ctrl_act1199')
def ctrl_nm1199():
    return 'ret1199' 

@action('ctrl_act1200')
def ctrl_nm1200():
    return 'ret1200' 

@action('ctrl_act1201')
def ctrl_nm1201():
    return 'ret1201' 

@action('ctrl_act1202')
def ctrl_nm1202():
    return 'ret1202' 

@action('ctrl_act1203')
def ctrl_nm1203():
    return 'ret1203' 

@action('ctrl_act1204')
def ctrl_nm1204():
    return 'ret1204' 

@action('ctrl_act1205')
def ctrl_nm1205():
    return 'ret1205' 

@action('ctrl_act1206')
def ctrl_nm1206():
    return 'ret1206' 

@action('ctrl_act1207')
def ctrl_nm1207():
    return 'ret1207' 

@action('ctrl_act1208')
def ctrl_nm1208():
    return 'ret1208' 

@action('ctrl_act1209')
def ctrl_nm1209():
    return 'ret1209' 

@action('ctrl_act1210')
def ctrl_nm1210():
    return 'ret1210' 

@action('ctrl_act1211')
def ctrl_nm1211():
    return 'ret1211' 

@action('ctrl_act1212')
def ctrl_nm1212():
    return 'ret1212' 

@action('ctrl_act1213')
def ctrl_nm1213():
    return 'ret1213' 

@action('ctrl_act1214')
def ctrl_nm1214():
    return 'ret1214' 

@action('ctrl_act1215')
def ctrl_nm1215():
    return 'ret1215' 

@action('ctrl_act1216')
def ctrl_nm1216():
    return 'ret1216' 

@action('ctrl_act1217')
def ctrl_nm1217():
    return 'ret1217' 

@action('ctrl_act1218')
def ctrl_nm1218():
    return 'ret1218' 

@action('ctrl_act1219')
def ctrl_nm1219():
    return 'ret1219' 

@action('ctrl_act1220')
def ctrl_nm1220():
    return 'ret1220' 

@action('ctrl_act1221')
def ctrl_nm1221():
    return 'ret1221' 

@action('ctrl_act1222')
def ctrl_nm1222():
    return 'ret1222' 

@action('ctrl_act1223')
def ctrl_nm1223():
    return 'ret1223' 

@action('ctrl_act1224')
def ctrl_nm1224():
    return 'ret1224' 

@action('ctrl_act1225')
def ctrl_nm1225():
    return 'ret1225' 

@action('ctrl_act1226')
def ctrl_nm1226():
    return 'ret1226' 

@action('ctrl_act1227')
def ctrl_nm1227():
    return 'ret1227' 

@action('ctrl_act1228')
def ctrl_nm1228():
    return 'ret1228' 

@action('ctrl_act1229')
def ctrl_nm1229():
    return 'ret1229' 

@action('ctrl_act1230')
def ctrl_nm1230():
    return 'ret1230' 

@action('ctrl_act1231')
def ctrl_nm1231():
    return 'ret1231' 

@action('ctrl_act1232')
def ctrl_nm1232():
    return 'ret1232' 

@action('ctrl_act1233')
def ctrl_nm1233():
    return 'ret1233' 

@action('ctrl_act1234')
def ctrl_nm1234():
    return 'ret1234' 

@action('ctrl_act1235')
def ctrl_nm1235():
    return 'ret1235' 

@action('ctrl_act1236')
def ctrl_nm1236():
    return 'ret1236' 

@action('ctrl_act1237')
def ctrl_nm1237():
    return 'ret1237' 

@action('ctrl_act1238')
def ctrl_nm1238():
    return 'ret1238' 

@action('ctrl_act1239')
def ctrl_nm1239():
    return 'ret1239' 

@action('ctrl_act1240')
def ctrl_nm1240():
    return 'ret1240' 

@action('ctrl_act1241')
def ctrl_nm1241():
    return 'ret1241' 

@action('ctrl_act1242')
def ctrl_nm1242():
    return 'ret1242' 

@action('ctrl_act1243')
def ctrl_nm1243():
    return 'ret1243' 

@action('ctrl_act1244')
def ctrl_nm1244():
    return 'ret1244' 

@action('ctrl_act1245')
def ctrl_nm1245():
    return 'ret1245' 

@action('ctrl_act1246')
def ctrl_nm1246():
    return 'ret1246' 

@action('ctrl_act1247')
def ctrl_nm1247():
    return 'ret1247' 

@action('ctrl_act1248')
def ctrl_nm1248():
    return 'ret1248' 

@action('ctrl_act1249')
def ctrl_nm1249():
    return 'ret1249' 

@action('ctrl_act1250')
def ctrl_nm1250():
    return 'ret1250' 

@action('ctrl_act1251')
def ctrl_nm1251():
    return 'ret1251' 

@action('ctrl_act1252')
def ctrl_nm1252():
    return 'ret1252' 

@action('ctrl_act1253')
def ctrl_nm1253():
    return 'ret1253' 

@action('ctrl_act1254')
def ctrl_nm1254():
    return 'ret1254' 

@action('ctrl_act1255')
def ctrl_nm1255():
    return 'ret1255' 

@action('ctrl_act1256')
def ctrl_nm1256():
    return 'ret1256' 

@action('ctrl_act1257')
def ctrl_nm1257():
    return 'ret1257' 

@action('ctrl_act1258')
def ctrl_nm1258():
    return 'ret1258' 

@action('ctrl_act1259')
def ctrl_nm1259():
    return 'ret1259' 

@action('ctrl_act1260')
def ctrl_nm1260():
    return 'ret1260' 

@action('ctrl_act1261')
def ctrl_nm1261():
    return 'ret1261' 

@action('ctrl_act1262')
def ctrl_nm1262():
    return 'ret1262' 

@action('ctrl_act1263')
def ctrl_nm1263():
    return 'ret1263' 

@action('ctrl_act1264')
def ctrl_nm1264():
    return 'ret1264' 

@action('ctrl_act1265')
def ctrl_nm1265():
    return 'ret1265' 

@action('ctrl_act1266')
def ctrl_nm1266():
    return 'ret1266' 

@action('ctrl_act1267')
def ctrl_nm1267():
    return 'ret1267' 

@action('ctrl_act1268')
def ctrl_nm1268():
    return 'ret1268' 

@action('ctrl_act1269')
def ctrl_nm1269():
    return 'ret1269' 

@action('ctrl_act1270')
def ctrl_nm1270():
    return 'ret1270' 

@action('ctrl_act1271')
def ctrl_nm1271():
    return 'ret1271' 

@action('ctrl_act1272')
def ctrl_nm1272():
    return 'ret1272' 

@action('ctrl_act1273')
def ctrl_nm1273():
    return 'ret1273' 

@action('ctrl_act1274')
def ctrl_nm1274():
    return 'ret1274' 

@action('ctrl_act1275')
def ctrl_nm1275():
    return 'ret1275' 

@action('ctrl_act1276')
def ctrl_nm1276():
    return 'ret1276' 

@action('ctrl_act1277')
def ctrl_nm1277():
    return 'ret1277' 

@action('ctrl_act1278')
def ctrl_nm1278():
    return 'ret1278' 

@action('ctrl_act1279')
def ctrl_nm1279():
    return 'ret1279' 

@action('ctrl_act1280')
def ctrl_nm1280():
    return 'ret1280' 

@action('ctrl_act1281')
def ctrl_nm1281():
    return 'ret1281' 

@action('ctrl_act1282')
def ctrl_nm1282():
    return 'ret1282' 

@action('ctrl_act1283')
def ctrl_nm1283():
    return 'ret1283' 

@action('ctrl_act1284')
def ctrl_nm1284():
    return 'ret1284' 

@action('ctrl_act1285')
def ctrl_nm1285():
    return 'ret1285' 

@action('ctrl_act1286')
def ctrl_nm1286():
    return 'ret1286' 

@action('ctrl_act1287')
def ctrl_nm1287():
    return 'ret1287' 

@action('ctrl_act1288')
def ctrl_nm1288():
    return 'ret1288' 

@action('ctrl_act1289')
def ctrl_nm1289():
    return 'ret1289' 

@action('ctrl_act1290')
def ctrl_nm1290():
    return 'ret1290' 

@action('ctrl_act1291')
def ctrl_nm1291():
    return 'ret1291' 

@action('ctrl_act1292')
def ctrl_nm1292():
    return 'ret1292' 

@action('ctrl_act1293')
def ctrl_nm1293():
    return 'ret1293' 

@action('ctrl_act1294')
def ctrl_nm1294():
    return 'ret1294' 

@action('ctrl_act1295')
def ctrl_nm1295():
    return 'ret1295' 

@action('ctrl_act1296')
def ctrl_nm1296():
    return 'ret1296' 

@action('ctrl_act1297')
def ctrl_nm1297():
    return 'ret1297' 

@action('ctrl_act1298')
def ctrl_nm1298():
    return 'ret1298' 

@action('ctrl_act1299')
def ctrl_nm1299():
    return 'ret1299' 

@action('ctrl_act1300')
def ctrl_nm1300():
    return 'ret1300' 

@action('ctrl_act1301')
def ctrl_nm1301():
    return 'ret1301' 

@action('ctrl_act1302')
def ctrl_nm1302():
    return 'ret1302' 

@action('ctrl_act1303')
def ctrl_nm1303():
    return 'ret1303' 

@action('ctrl_act1304')
def ctrl_nm1304():
    return 'ret1304' 

@action('ctrl_act1305')
def ctrl_nm1305():
    return 'ret1305' 

@action('ctrl_act1306')
def ctrl_nm1306():
    return 'ret1306' 

@action('ctrl_act1307')
def ctrl_nm1307():
    return 'ret1307' 

@action('ctrl_act1308')
def ctrl_nm1308():
    return 'ret1308' 

@action('ctrl_act1309')
def ctrl_nm1309():
    return 'ret1309' 

@action('ctrl_act1310')
def ctrl_nm1310():
    return 'ret1310' 

@action('ctrl_act1311')
def ctrl_nm1311():
    return 'ret1311' 

@action('ctrl_act1312')
def ctrl_nm1312():
    return 'ret1312' 

@action('ctrl_act1313')
def ctrl_nm1313():
    return 'ret1313' 

@action('ctrl_act1314')
def ctrl_nm1314():
    return 'ret1314' 

@action('ctrl_act1315')
def ctrl_nm1315():
    return 'ret1315' 

@action('ctrl_act1316')
def ctrl_nm1316():
    return 'ret1316' 

@action('ctrl_act1317')
def ctrl_nm1317():
    return 'ret1317' 

@action('ctrl_act1318')
def ctrl_nm1318():
    return 'ret1318' 

@action('ctrl_act1319')
def ctrl_nm1319():
    return 'ret1319' 

@action('ctrl_act1320')
def ctrl_nm1320():
    return 'ret1320' 

@action('ctrl_act1321')
def ctrl_nm1321():
    return 'ret1321' 

@action('ctrl_act1322')
def ctrl_nm1322():
    return 'ret1322' 

@action('ctrl_act1323')
def ctrl_nm1323():
    return 'ret1323' 

@action('ctrl_act1324')
def ctrl_nm1324():
    return 'ret1324' 

@action('ctrl_act1325')
def ctrl_nm1325():
    return 'ret1325' 

@action('ctrl_act1326')
def ctrl_nm1326():
    return 'ret1326' 

@action('ctrl_act1327')
def ctrl_nm1327():
    return 'ret1327' 

@action('ctrl_act1328')
def ctrl_nm1328():
    return 'ret1328' 

@action('ctrl_act1329')
def ctrl_nm1329():
    return 'ret1329' 

@action('ctrl_act1330')
def ctrl_nm1330():
    return 'ret1330' 

@action('ctrl_act1331')
def ctrl_nm1331():
    return 'ret1331' 

@action('ctrl_act1332')
def ctrl_nm1332():
    return 'ret1332' 

@action('ctrl_act1333')
def ctrl_nm1333():
    return 'ret1333' 

@action('ctrl_act1334')
def ctrl_nm1334():
    return 'ret1334' 

@action('ctrl_act1335')
def ctrl_nm1335():
    return 'ret1335' 

@action('ctrl_act1336')
def ctrl_nm1336():
    return 'ret1336' 

@action('ctrl_act1337')
def ctrl_nm1337():
    return 'ret1337' 

@action('ctrl_act1338')
def ctrl_nm1338():
    return 'ret1338' 

@action('ctrl_act1339')
def ctrl_nm1339():
    return 'ret1339' 

@action('ctrl_act1340')
def ctrl_nm1340():
    return 'ret1340' 

@action('ctrl_act1341')
def ctrl_nm1341():
    return 'ret1341' 

@action('ctrl_act1342')
def ctrl_nm1342():
    return 'ret1342' 

@action('ctrl_act1343')
def ctrl_nm1343():
    return 'ret1343' 

@action('ctrl_act1344')
def ctrl_nm1344():
    return 'ret1344' 

@action('ctrl_act1345')
def ctrl_nm1345():
    return 'ret1345' 

@action('ctrl_act1346')
def ctrl_nm1346():
    return 'ret1346' 

@action('ctrl_act1347')
def ctrl_nm1347():
    return 'ret1347' 

@action('ctrl_act1348')
def ctrl_nm1348():
    return 'ret1348' 

@action('ctrl_act1349')
def ctrl_nm1349():
    return 'ret1349' 

@action('ctrl_act1350')
def ctrl_nm1350():
    return 'ret1350' 

@action('ctrl_act1351')
def ctrl_nm1351():
    return 'ret1351' 

@action('ctrl_act1352')
def ctrl_nm1352():
    return 'ret1352' 

@action('ctrl_act1353')
def ctrl_nm1353():
    return 'ret1353' 

@action('ctrl_act1354')
def ctrl_nm1354():
    return 'ret1354' 

@action('ctrl_act1355')
def ctrl_nm1355():
    return 'ret1355' 

@action('ctrl_act1356')
def ctrl_nm1356():
    return 'ret1356' 

@action('ctrl_act1357')
def ctrl_nm1357():
    return 'ret1357' 

@action('ctrl_act1358')
def ctrl_nm1358():
    return 'ret1358' 

@action('ctrl_act1359')
def ctrl_nm1359():
    return 'ret1359' 

@action('ctrl_act1360')
def ctrl_nm1360():
    return 'ret1360' 

@action('ctrl_act1361')
def ctrl_nm1361():
    return 'ret1361' 

@action('ctrl_act1362')
def ctrl_nm1362():
    return 'ret1362' 

@action('ctrl_act1363')
def ctrl_nm1363():
    return 'ret1363' 

@action('ctrl_act1364')
def ctrl_nm1364():
    return 'ret1364' 

@action('ctrl_act1365')
def ctrl_nm1365():
    return 'ret1365' 

@action('ctrl_act1366')
def ctrl_nm1366():
    return 'ret1366' 

@action('ctrl_act1367')
def ctrl_nm1367():
    return 'ret1367' 

@action('ctrl_act1368')
def ctrl_nm1368():
    return 'ret1368' 

@action('ctrl_act1369')
def ctrl_nm1369():
    return 'ret1369' 

@action('ctrl_act1370')
def ctrl_nm1370():
    return 'ret1370' 

@action('ctrl_act1371')
def ctrl_nm1371():
    return 'ret1371' 

@action('ctrl_act1372')
def ctrl_nm1372():
    return 'ret1372' 

@action('ctrl_act1373')
def ctrl_nm1373():
    return 'ret1373' 

@action('ctrl_act1374')
def ctrl_nm1374():
    return 'ret1374' 

@action('ctrl_act1375')
def ctrl_nm1375():
    return 'ret1375' 

@action('ctrl_act1376')
def ctrl_nm1376():
    return 'ret1376' 

@action('ctrl_act1377')
def ctrl_nm1377():
    return 'ret1377' 

@action('ctrl_act1378')
def ctrl_nm1378():
    return 'ret1378' 

@action('ctrl_act1379')
def ctrl_nm1379():
    return 'ret1379' 

@action('ctrl_act1380')
def ctrl_nm1380():
    return 'ret1380' 

@action('ctrl_act1381')
def ctrl_nm1381():
    return 'ret1381' 

@action('ctrl_act1382')
def ctrl_nm1382():
    return 'ret1382' 

@action('ctrl_act1383')
def ctrl_nm1383():
    return 'ret1383' 

@action('ctrl_act1384')
def ctrl_nm1384():
    return 'ret1384' 

@action('ctrl_act1385')
def ctrl_nm1385():
    return 'ret1385' 

@action('ctrl_act1386')
def ctrl_nm1386():
    return 'ret1386' 

@action('ctrl_act1387')
def ctrl_nm1387():
    return 'ret1387' 

@action('ctrl_act1388')
def ctrl_nm1388():
    return 'ret1388' 

@action('ctrl_act1389')
def ctrl_nm1389():
    return 'ret1389' 

@action('ctrl_act1390')
def ctrl_nm1390():
    return 'ret1390' 

@action('ctrl_act1391')
def ctrl_nm1391():
    return 'ret1391' 

@action('ctrl_act1392')
def ctrl_nm1392():
    return 'ret1392' 

@action('ctrl_act1393')
def ctrl_nm1393():
    return 'ret1393' 

@action('ctrl_act1394')
def ctrl_nm1394():
    return 'ret1394' 

@action('ctrl_act1395')
def ctrl_nm1395():
    return 'ret1395' 

@action('ctrl_act1396')
def ctrl_nm1396():
    return 'ret1396' 

@action('ctrl_act1397')
def ctrl_nm1397():
    return 'ret1397' 

@action('ctrl_act1398')
def ctrl_nm1398():
    return 'ret1398' 

@action('ctrl_act1399')
def ctrl_nm1399():
    return 'ret1399' 

@action('ctrl_act1400')
def ctrl_nm1400():
    return 'ret1400' 

@action('ctrl_act1401')
def ctrl_nm1401():
    return 'ret1401' 

@action('ctrl_act1402')
def ctrl_nm1402():
    return 'ret1402' 

@action('ctrl_act1403')
def ctrl_nm1403():
    return 'ret1403' 

@action('ctrl_act1404')
def ctrl_nm1404():
    return 'ret1404' 

@action('ctrl_act1405')
def ctrl_nm1405():
    return 'ret1405' 

@action('ctrl_act1406')
def ctrl_nm1406():
    return 'ret1406' 

@action('ctrl_act1407')
def ctrl_nm1407():
    return 'ret1407' 

@action('ctrl_act1408')
def ctrl_nm1408():
    return 'ret1408' 

@action('ctrl_act1409')
def ctrl_nm1409():
    return 'ret1409' 

@action('ctrl_act1410')
def ctrl_nm1410():
    return 'ret1410' 

@action('ctrl_act1411')
def ctrl_nm1411():
    return 'ret1411' 

@action('ctrl_act1412')
def ctrl_nm1412():
    return 'ret1412' 

@action('ctrl_act1413')
def ctrl_nm1413():
    return 'ret1413' 

@action('ctrl_act1414')
def ctrl_nm1414():
    return 'ret1414' 

@action('ctrl_act1415')
def ctrl_nm1415():
    return 'ret1415' 

@action('ctrl_act1416')
def ctrl_nm1416():
    return 'ret1416' 

@action('ctrl_act1417')
def ctrl_nm1417():
    return 'ret1417' 

@action('ctrl_act1418')
def ctrl_nm1418():
    return 'ret1418' 

@action('ctrl_act1419')
def ctrl_nm1419():
    return 'ret1419' 

@action('ctrl_act1420')
def ctrl_nm1420():
    return 'ret1420' 

@action('ctrl_act1421')
def ctrl_nm1421():
    return 'ret1421' 

@action('ctrl_act1422')
def ctrl_nm1422():
    return 'ret1422' 

@action('ctrl_act1423')
def ctrl_nm1423():
    return 'ret1423' 

@action('ctrl_act1424')
def ctrl_nm1424():
    return 'ret1424' 

@action('ctrl_act1425')
def ctrl_nm1425():
    return 'ret1425' 

@action('ctrl_act1426')
def ctrl_nm1426():
    return 'ret1426' 

@action('ctrl_act1427')
def ctrl_nm1427():
    return 'ret1427' 

@action('ctrl_act1428')
def ctrl_nm1428():
    return 'ret1428' 

@action('ctrl_act1429')
def ctrl_nm1429():
    return 'ret1429' 

@action('ctrl_act1430')
def ctrl_nm1430():
    return 'ret1430' 

@action('ctrl_act1431')
def ctrl_nm1431():
    return 'ret1431' 

@action('ctrl_act1432')
def ctrl_nm1432():
    return 'ret1432' 

@action('ctrl_act1433')
def ctrl_nm1433():
    return 'ret1433' 

@action('ctrl_act1434')
def ctrl_nm1434():
    return 'ret1434' 

@action('ctrl_act1435')
def ctrl_nm1435():
    return 'ret1435' 

@action('ctrl_act1436')
def ctrl_nm1436():
    return 'ret1436' 

@action('ctrl_act1437')
def ctrl_nm1437():
    return 'ret1437' 

@action('ctrl_act1438')
def ctrl_nm1438():
    return 'ret1438' 

@action('ctrl_act1439')
def ctrl_nm1439():
    return 'ret1439' 

@action('ctrl_act1440')
def ctrl_nm1440():
    return 'ret1440' 

@action('ctrl_act1441')
def ctrl_nm1441():
    return 'ret1441' 

@action('ctrl_act1442')
def ctrl_nm1442():
    return 'ret1442' 

@action('ctrl_act1443')
def ctrl_nm1443():
    return 'ret1443' 

@action('ctrl_act1444')
def ctrl_nm1444():
    return 'ret1444' 

@action('ctrl_act1445')
def ctrl_nm1445():
    return 'ret1445' 

@action('ctrl_act1446')
def ctrl_nm1446():
    return 'ret1446' 

@action('ctrl_act1447')
def ctrl_nm1447():
    return 'ret1447' 

@action('ctrl_act1448')
def ctrl_nm1448():
    return 'ret1448' 

@action('ctrl_act1449')
def ctrl_nm1449():
    return 'ret1449' 

@action('ctrl_act1450')
def ctrl_nm1450():
    return 'ret1450' 

@action('ctrl_act1451')
def ctrl_nm1451():
    return 'ret1451' 

@action('ctrl_act1452')
def ctrl_nm1452():
    return 'ret1452' 

@action('ctrl_act1453')
def ctrl_nm1453():
    return 'ret1453' 

@action('ctrl_act1454')
def ctrl_nm1454():
    return 'ret1454' 

@action('ctrl_act1455')
def ctrl_nm1455():
    return 'ret1455' 

@action('ctrl_act1456')
def ctrl_nm1456():
    return 'ret1456' 

@action('ctrl_act1457')
def ctrl_nm1457():
    return 'ret1457' 

@action('ctrl_act1458')
def ctrl_nm1458():
    return 'ret1458' 

@action('ctrl_act1459')
def ctrl_nm1459():
    return 'ret1459' 

@action('ctrl_act1460')
def ctrl_nm1460():
    return 'ret1460' 

@action('ctrl_act1461')
def ctrl_nm1461():
    return 'ret1461' 

@action('ctrl_act1462')
def ctrl_nm1462():
    return 'ret1462' 

@action('ctrl_act1463')
def ctrl_nm1463():
    return 'ret1463' 

@action('ctrl_act1464')
def ctrl_nm1464():
    return 'ret1464' 

@action('ctrl_act1465')
def ctrl_nm1465():
    return 'ret1465' 

@action('ctrl_act1466')
def ctrl_nm1466():
    return 'ret1466' 

@action('ctrl_act1467')
def ctrl_nm1467():
    return 'ret1467' 

@action('ctrl_act1468')
def ctrl_nm1468():
    return 'ret1468' 

@action('ctrl_act1469')
def ctrl_nm1469():
    return 'ret1469' 

@action('ctrl_act1470')
def ctrl_nm1470():
    return 'ret1470' 

@action('ctrl_act1471')
def ctrl_nm1471():
    return 'ret1471' 

@action('ctrl_act1472')
def ctrl_nm1472():
    return 'ret1472' 

@action('ctrl_act1473')
def ctrl_nm1473():
    return 'ret1473' 

@action('ctrl_act1474')
def ctrl_nm1474():
    return 'ret1474' 

@action('ctrl_act1475')
def ctrl_nm1475():
    return 'ret1475' 

@action('ctrl_act1476')
def ctrl_nm1476():
    return 'ret1476' 

@action('ctrl_act1477')
def ctrl_nm1477():
    return 'ret1477' 

@action('ctrl_act1478')
def ctrl_nm1478():
    return 'ret1478' 

@action('ctrl_act1479')
def ctrl_nm1479():
    return 'ret1479' 

@action('ctrl_act1480')
def ctrl_nm1480():
    return 'ret1480' 

@action('ctrl_act1481')
def ctrl_nm1481():
    return 'ret1481' 

@action('ctrl_act1482')
def ctrl_nm1482():
    return 'ret1482' 

@action('ctrl_act1483')
def ctrl_nm1483():
    return 'ret1483' 

@action('ctrl_act1484')
def ctrl_nm1484():
    return 'ret1484' 

@action('ctrl_act1485')
def ctrl_nm1485():
    return 'ret1485' 

@action('ctrl_act1486')
def ctrl_nm1486():
    return 'ret1486' 

@action('ctrl_act1487')
def ctrl_nm1487():
    return 'ret1487' 

@action('ctrl_act1488')
def ctrl_nm1488():
    return 'ret1488' 

@action('ctrl_act1489')
def ctrl_nm1489():
    return 'ret1489' 

@action('ctrl_act1490')
def ctrl_nm1490():
    return 'ret1490' 

@action('ctrl_act1491')
def ctrl_nm1491():
    return 'ret1491' 

@action('ctrl_act1492')
def ctrl_nm1492():
    return 'ret1492' 

@action('ctrl_act1493')
def ctrl_nm1493():
    return 'ret1493' 

@action('ctrl_act1494')
def ctrl_nm1494():
    return 'ret1494' 

@action('ctrl_act1495')
def ctrl_nm1495():
    return 'ret1495' 

@action('ctrl_act1496')
def ctrl_nm1496():
    return 'ret1496' 

@action('ctrl_act1497')
def ctrl_nm1497():
    return 'ret1497' 

@action('ctrl_act1498')
def ctrl_nm1498():
    return 'ret1498' 

@action('ctrl_act1499')
def ctrl_nm1499():
    return 'ret1499' 

@action('ctrl_act1500')
def ctrl_nm1500():
    return 'ret1500' 

@action('ctrl_act1501')
def ctrl_nm1501():
    return 'ret1501' 

@action('ctrl_act1502')
def ctrl_nm1502():
    return 'ret1502' 

@action('ctrl_act1503')
def ctrl_nm1503():
    return 'ret1503' 

@action('ctrl_act1504')
def ctrl_nm1504():
    return 'ret1504' 

@action('ctrl_act1505')
def ctrl_nm1505():
    return 'ret1505' 

@action('ctrl_act1506')
def ctrl_nm1506():
    return 'ret1506' 

@action('ctrl_act1507')
def ctrl_nm1507():
    return 'ret1507' 

@action('ctrl_act1508')
def ctrl_nm1508():
    return 'ret1508' 

@action('ctrl_act1509')
def ctrl_nm1509():
    return 'ret1509' 

@action('ctrl_act1510')
def ctrl_nm1510():
    return 'ret1510' 

@action('ctrl_act1511')
def ctrl_nm1511():
    return 'ret1511' 

@action('ctrl_act1512')
def ctrl_nm1512():
    return 'ret1512' 

@action('ctrl_act1513')
def ctrl_nm1513():
    return 'ret1513' 

@action('ctrl_act1514')
def ctrl_nm1514():
    return 'ret1514' 

@action('ctrl_act1515')
def ctrl_nm1515():
    return 'ret1515' 

@action('ctrl_act1516')
def ctrl_nm1516():
    return 'ret1516' 

@action('ctrl_act1517')
def ctrl_nm1517():
    return 'ret1517' 

@action('ctrl_act1518')
def ctrl_nm1518():
    return 'ret1518' 

@action('ctrl_act1519')
def ctrl_nm1519():
    return 'ret1519' 

@action('ctrl_act1520')
def ctrl_nm1520():
    return 'ret1520' 

@action('ctrl_act1521')
def ctrl_nm1521():
    return 'ret1521' 

@action('ctrl_act1522')
def ctrl_nm1522():
    return 'ret1522' 

@action('ctrl_act1523')
def ctrl_nm1523():
    return 'ret1523' 

@action('ctrl_act1524')
def ctrl_nm1524():
    return 'ret1524' 

@action('ctrl_act1525')
def ctrl_nm1525():
    return 'ret1525' 

@action('ctrl_act1526')
def ctrl_nm1526():
    return 'ret1526' 

@action('ctrl_act1527')
def ctrl_nm1527():
    return 'ret1527' 

@action('ctrl_act1528')
def ctrl_nm1528():
    return 'ret1528' 

@action('ctrl_act1529')
def ctrl_nm1529():
    return 'ret1529' 

@action('ctrl_act1530')
def ctrl_nm1530():
    return 'ret1530' 

@action('ctrl_act1531')
def ctrl_nm1531():
    return 'ret1531' 

@action('ctrl_act1532')
def ctrl_nm1532():
    return 'ret1532' 

@action('ctrl_act1533')
def ctrl_nm1533():
    return 'ret1533' 

@action('ctrl_act1534')
def ctrl_nm1534():
    return 'ret1534' 

@action('ctrl_act1535')
def ctrl_nm1535():
    return 'ret1535' 

@action('ctrl_act1536')
def ctrl_nm1536():
    return 'ret1536' 

@action('ctrl_act1537')
def ctrl_nm1537():
    return 'ret1537' 

@action('ctrl_act1538')
def ctrl_nm1538():
    return 'ret1538' 

@action('ctrl_act1539')
def ctrl_nm1539():
    return 'ret1539' 

@action('ctrl_act1540')
def ctrl_nm1540():
    return 'ret1540' 

@action('ctrl_act1541')
def ctrl_nm1541():
    return 'ret1541' 

@action('ctrl_act1542')
def ctrl_nm1542():
    return 'ret1542' 

@action('ctrl_act1543')
def ctrl_nm1543():
    return 'ret1543' 

@action('ctrl_act1544')
def ctrl_nm1544():
    return 'ret1544' 

@action('ctrl_act1545')
def ctrl_nm1545():
    return 'ret1545' 

@action('ctrl_act1546')
def ctrl_nm1546():
    return 'ret1546' 

@action('ctrl_act1547')
def ctrl_nm1547():
    return 'ret1547' 

@action('ctrl_act1548')
def ctrl_nm1548():
    return 'ret1548' 

@action('ctrl_act1549')
def ctrl_nm1549():
    return 'ret1549' 

@action('ctrl_act1550')
def ctrl_nm1550():
    return 'ret1550' 

@action('ctrl_act1551')
def ctrl_nm1551():
    return 'ret1551' 

@action('ctrl_act1552')
def ctrl_nm1552():
    return 'ret1552' 

@action('ctrl_act1553')
def ctrl_nm1553():
    return 'ret1553' 

@action('ctrl_act1554')
def ctrl_nm1554():
    return 'ret1554' 

@action('ctrl_act1555')
def ctrl_nm1555():
    return 'ret1555' 

@action('ctrl_act1556')
def ctrl_nm1556():
    return 'ret1556' 

@action('ctrl_act1557')
def ctrl_nm1557():
    return 'ret1557' 

@action('ctrl_act1558')
def ctrl_nm1558():
    return 'ret1558' 

@action('ctrl_act1559')
def ctrl_nm1559():
    return 'ret1559' 

@action('ctrl_act1560')
def ctrl_nm1560():
    return 'ret1560' 

@action('ctrl_act1561')
def ctrl_nm1561():
    return 'ret1561' 

@action('ctrl_act1562')
def ctrl_nm1562():
    return 'ret1562' 

@action('ctrl_act1563')
def ctrl_nm1563():
    return 'ret1563' 

@action('ctrl_act1564')
def ctrl_nm1564():
    return 'ret1564' 

@action('ctrl_act1565')
def ctrl_nm1565():
    return 'ret1565' 

@action('ctrl_act1566')
def ctrl_nm1566():
    return 'ret1566' 

@action('ctrl_act1567')
def ctrl_nm1567():
    return 'ret1567' 

@action('ctrl_act1568')
def ctrl_nm1568():
    return 'ret1568' 

@action('ctrl_act1569')
def ctrl_nm1569():
    return 'ret1569' 

@action('ctrl_act1570')
def ctrl_nm1570():
    return 'ret1570' 

@action('ctrl_act1571')
def ctrl_nm1571():
    return 'ret1571' 

@action('ctrl_act1572')
def ctrl_nm1572():
    return 'ret1572' 

@action('ctrl_act1573')
def ctrl_nm1573():
    return 'ret1573' 

@action('ctrl_act1574')
def ctrl_nm1574():
    return 'ret1574' 

@action('ctrl_act1575')
def ctrl_nm1575():
    return 'ret1575' 

@action('ctrl_act1576')
def ctrl_nm1576():
    return 'ret1576' 

@action('ctrl_act1577')
def ctrl_nm1577():
    return 'ret1577' 

@action('ctrl_act1578')
def ctrl_nm1578():
    return 'ret1578' 

@action('ctrl_act1579')
def ctrl_nm1579():
    return 'ret1579' 

@action('ctrl_act1580')
def ctrl_nm1580():
    return 'ret1580' 

@action('ctrl_act1581')
def ctrl_nm1581():
    return 'ret1581' 

@action('ctrl_act1582')
def ctrl_nm1582():
    return 'ret1582' 

@action('ctrl_act1583')
def ctrl_nm1583():
    return 'ret1583' 

@action('ctrl_act1584')
def ctrl_nm1584():
    return 'ret1584' 

@action('ctrl_act1585')
def ctrl_nm1585():
    return 'ret1585' 

@action('ctrl_act1586')
def ctrl_nm1586():
    return 'ret1586' 

@action('ctrl_act1587')
def ctrl_nm1587():
    return 'ret1587' 

@action('ctrl_act1588')
def ctrl_nm1588():
    return 'ret1588' 

@action('ctrl_act1589')
def ctrl_nm1589():
    return 'ret1589' 

@action('ctrl_act1590')
def ctrl_nm1590():
    return 'ret1590' 

@action('ctrl_act1591')
def ctrl_nm1591():
    return 'ret1591' 

@action('ctrl_act1592')
def ctrl_nm1592():
    return 'ret1592' 

@action('ctrl_act1593')
def ctrl_nm1593():
    return 'ret1593' 

@action('ctrl_act1594')
def ctrl_nm1594():
    return 'ret1594' 

@action('ctrl_act1595')
def ctrl_nm1595():
    return 'ret1595' 

@action('ctrl_act1596')
def ctrl_nm1596():
    return 'ret1596' 

@action('ctrl_act1597')
def ctrl_nm1597():
    return 'ret1597' 

@action('ctrl_act1598')
def ctrl_nm1598():
    return 'ret1598' 

@action('ctrl_act1599')
def ctrl_nm1599():
    return 'ret1599' 

@action('ctrl_act1600')
def ctrl_nm1600():
    return 'ret1600' 

@action('ctrl_act1601')
def ctrl_nm1601():
    return 'ret1601' 

@action('ctrl_act1602')
def ctrl_nm1602():
    return 'ret1602' 

@action('ctrl_act1603')
def ctrl_nm1603():
    return 'ret1603' 

@action('ctrl_act1604')
def ctrl_nm1604():
    return 'ret1604' 

@action('ctrl_act1605')
def ctrl_nm1605():
    return 'ret1605' 

@action('ctrl_act1606')
def ctrl_nm1606():
    return 'ret1606' 

@action('ctrl_act1607')
def ctrl_nm1607():
    return 'ret1607' 

@action('ctrl_act1608')
def ctrl_nm1608():
    return 'ret1608' 

@action('ctrl_act1609')
def ctrl_nm1609():
    return 'ret1609' 

@action('ctrl_act1610')
def ctrl_nm1610():
    return 'ret1610' 

@action('ctrl_act1611')
def ctrl_nm1611():
    return 'ret1611' 

@action('ctrl_act1612')
def ctrl_nm1612():
    return 'ret1612' 

@action('ctrl_act1613')
def ctrl_nm1613():
    return 'ret1613' 

@action('ctrl_act1614')
def ctrl_nm1614():
    return 'ret1614' 

@action('ctrl_act1615')
def ctrl_nm1615():
    return 'ret1615' 

@action('ctrl_act1616')
def ctrl_nm1616():
    return 'ret1616' 

@action('ctrl_act1617')
def ctrl_nm1617():
    return 'ret1617' 

@action('ctrl_act1618')
def ctrl_nm1618():
    return 'ret1618' 

@action('ctrl_act1619')
def ctrl_nm1619():
    return 'ret1619' 

@action('ctrl_act1620')
def ctrl_nm1620():
    return 'ret1620' 

@action('ctrl_act1621')
def ctrl_nm1621():
    return 'ret1621' 

@action('ctrl_act1622')
def ctrl_nm1622():
    return 'ret1622' 

@action('ctrl_act1623')
def ctrl_nm1623():
    return 'ret1623' 

@action('ctrl_act1624')
def ctrl_nm1624():
    return 'ret1624' 

@action('ctrl_act1625')
def ctrl_nm1625():
    return 'ret1625' 

@action('ctrl_act1626')
def ctrl_nm1626():
    return 'ret1626' 

@action('ctrl_act1627')
def ctrl_nm1627():
    return 'ret1627' 

@action('ctrl_act1628')
def ctrl_nm1628():
    return 'ret1628' 

@action('ctrl_act1629')
def ctrl_nm1629():
    return 'ret1629' 

@action('ctrl_act1630')
def ctrl_nm1630():
    return 'ret1630' 

@action('ctrl_act1631')
def ctrl_nm1631():
    return 'ret1631' 

@action('ctrl_act1632')
def ctrl_nm1632():
    return 'ret1632' 

@action('ctrl_act1633')
def ctrl_nm1633():
    return 'ret1633' 

@action('ctrl_act1634')
def ctrl_nm1634():
    return 'ret1634' 

@action('ctrl_act1635')
def ctrl_nm1635():
    return 'ret1635' 

@action('ctrl_act1636')
def ctrl_nm1636():
    return 'ret1636' 

@action('ctrl_act1637')
def ctrl_nm1637():
    return 'ret1637' 

@action('ctrl_act1638')
def ctrl_nm1638():
    return 'ret1638' 

@action('ctrl_act1639')
def ctrl_nm1639():
    return 'ret1639' 

@action('ctrl_act1640')
def ctrl_nm1640():
    return 'ret1640' 

@action('ctrl_act1641')
def ctrl_nm1641():
    return 'ret1641' 

@action('ctrl_act1642')
def ctrl_nm1642():
    return 'ret1642' 

@action('ctrl_act1643')
def ctrl_nm1643():
    return 'ret1643' 

@action('ctrl_act1644')
def ctrl_nm1644():
    return 'ret1644' 

@action('ctrl_act1645')
def ctrl_nm1645():
    return 'ret1645' 

@action('ctrl_act1646')
def ctrl_nm1646():
    return 'ret1646' 

@action('ctrl_act1647')
def ctrl_nm1647():
    return 'ret1647' 

@action('ctrl_act1648')
def ctrl_nm1648():
    return 'ret1648' 

@action('ctrl_act1649')
def ctrl_nm1649():
    return 'ret1649' 

@action('ctrl_act1650')
def ctrl_nm1650():
    return 'ret1650' 

@action('ctrl_act1651')
def ctrl_nm1651():
    return 'ret1651' 

@action('ctrl_act1652')
def ctrl_nm1652():
    return 'ret1652' 

@action('ctrl_act1653')
def ctrl_nm1653():
    return 'ret1653' 

@action('ctrl_act1654')
def ctrl_nm1654():
    return 'ret1654' 

@action('ctrl_act1655')
def ctrl_nm1655():
    return 'ret1655' 

@action('ctrl_act1656')
def ctrl_nm1656():
    return 'ret1656' 

@action('ctrl_act1657')
def ctrl_nm1657():
    return 'ret1657' 

@action('ctrl_act1658')
def ctrl_nm1658():
    return 'ret1658' 

@action('ctrl_act1659')
def ctrl_nm1659():
    return 'ret1659' 

@action('ctrl_act1660')
def ctrl_nm1660():
    return 'ret1660' 

@action('ctrl_act1661')
def ctrl_nm1661():
    return 'ret1661' 

@action('ctrl_act1662')
def ctrl_nm1662():
    return 'ret1662' 

@action('ctrl_act1663')
def ctrl_nm1663():
    return 'ret1663' 

@action('ctrl_act1664')
def ctrl_nm1664():
    return 'ret1664' 

@action('ctrl_act1665')
def ctrl_nm1665():
    return 'ret1665' 

@action('ctrl_act1666')
def ctrl_nm1666():
    return 'ret1666' 

@action('ctrl_act1667')
def ctrl_nm1667():
    return 'ret1667' 

@action('ctrl_act1668')
def ctrl_nm1668():
    return 'ret1668' 

@action('ctrl_act1669')
def ctrl_nm1669():
    return 'ret1669' 

@action('ctrl_act1670')
def ctrl_nm1670():
    return 'ret1670' 

@action('ctrl_act1671')
def ctrl_nm1671():
    return 'ret1671' 

@action('ctrl_act1672')
def ctrl_nm1672():
    return 'ret1672' 

@action('ctrl_act1673')
def ctrl_nm1673():
    return 'ret1673' 

@action('ctrl_act1674')
def ctrl_nm1674():
    return 'ret1674' 

@action('ctrl_act1675')
def ctrl_nm1675():
    return 'ret1675' 

@action('ctrl_act1676')
def ctrl_nm1676():
    return 'ret1676' 

@action('ctrl_act1677')
def ctrl_nm1677():
    return 'ret1677' 

@action('ctrl_act1678')
def ctrl_nm1678():
    return 'ret1678' 

@action('ctrl_act1679')
def ctrl_nm1679():
    return 'ret1679' 

@action('ctrl_act1680')
def ctrl_nm1680():
    return 'ret1680' 

@action('ctrl_act1681')
def ctrl_nm1681():
    return 'ret1681' 

@action('ctrl_act1682')
def ctrl_nm1682():
    return 'ret1682' 

@action('ctrl_act1683')
def ctrl_nm1683():
    return 'ret1683' 

@action('ctrl_act1684')
def ctrl_nm1684():
    return 'ret1684' 

@action('ctrl_act1685')
def ctrl_nm1685():
    return 'ret1685' 

@action('ctrl_act1686')
def ctrl_nm1686():
    return 'ret1686' 

@action('ctrl_act1687')
def ctrl_nm1687():
    return 'ret1687' 

@action('ctrl_act1688')
def ctrl_nm1688():
    return 'ret1688' 

@action('ctrl_act1689')
def ctrl_nm1689():
    return 'ret1689' 

@action('ctrl_act1690')
def ctrl_nm1690():
    return 'ret1690' 

@action('ctrl_act1691')
def ctrl_nm1691():
    return 'ret1691' 

@action('ctrl_act1692')
def ctrl_nm1692():
    return 'ret1692' 

@action('ctrl_act1693')
def ctrl_nm1693():
    return 'ret1693' 

@action('ctrl_act1694')
def ctrl_nm1694():
    return 'ret1694' 

@action('ctrl_act1695')
def ctrl_nm1695():
    return 'ret1695' 

@action('ctrl_act1696')
def ctrl_nm1696():
    return 'ret1696' 

@action('ctrl_act1697')
def ctrl_nm1697():
    return 'ret1697' 

@action('ctrl_act1698')
def ctrl_nm1698():
    return 'ret1698' 

@action('ctrl_act1699')
def ctrl_nm1699():
    return 'ret1699' 

@action('ctrl_act1700')
def ctrl_nm1700():
    return 'ret1700' 

@action('ctrl_act1701')
def ctrl_nm1701():
    return 'ret1701' 

@action('ctrl_act1702')
def ctrl_nm1702():
    return 'ret1702' 

@action('ctrl_act1703')
def ctrl_nm1703():
    return 'ret1703' 

@action('ctrl_act1704')
def ctrl_nm1704():
    return 'ret1704' 

@action('ctrl_act1705')
def ctrl_nm1705():
    return 'ret1705' 

@action('ctrl_act1706')
def ctrl_nm1706():
    return 'ret1706' 

@action('ctrl_act1707')
def ctrl_nm1707():
    return 'ret1707' 

@action('ctrl_act1708')
def ctrl_nm1708():
    return 'ret1708' 

@action('ctrl_act1709')
def ctrl_nm1709():
    return 'ret1709' 

@action('ctrl_act1710')
def ctrl_nm1710():
    return 'ret1710' 

@action('ctrl_act1711')
def ctrl_nm1711():
    return 'ret1711' 

@action('ctrl_act1712')
def ctrl_nm1712():
    return 'ret1712' 

@action('ctrl_act1713')
def ctrl_nm1713():
    return 'ret1713' 

@action('ctrl_act1714')
def ctrl_nm1714():
    return 'ret1714' 

@action('ctrl_act1715')
def ctrl_nm1715():
    return 'ret1715' 

@action('ctrl_act1716')
def ctrl_nm1716():
    return 'ret1716' 

@action('ctrl_act1717')
def ctrl_nm1717():
    return 'ret1717' 

@action('ctrl_act1718')
def ctrl_nm1718():
    return 'ret1718' 

@action('ctrl_act1719')
def ctrl_nm1719():
    return 'ret1719' 

@action('ctrl_act1720')
def ctrl_nm1720():
    return 'ret1720' 

@action('ctrl_act1721')
def ctrl_nm1721():
    return 'ret1721' 

@action('ctrl_act1722')
def ctrl_nm1722():
    return 'ret1722' 

@action('ctrl_act1723')
def ctrl_nm1723():
    return 'ret1723' 

@action('ctrl_act1724')
def ctrl_nm1724():
    return 'ret1724' 

@action('ctrl_act1725')
def ctrl_nm1725():
    return 'ret1725' 

@action('ctrl_act1726')
def ctrl_nm1726():
    return 'ret1726' 

@action('ctrl_act1727')
def ctrl_nm1727():
    return 'ret1727' 

@action('ctrl_act1728')
def ctrl_nm1728():
    return 'ret1728' 

@action('ctrl_act1729')
def ctrl_nm1729():
    return 'ret1729' 

@action('ctrl_act1730')
def ctrl_nm1730():
    return 'ret1730' 

@action('ctrl_act1731')
def ctrl_nm1731():
    return 'ret1731' 

@action('ctrl_act1732')
def ctrl_nm1732():
    return 'ret1732' 

@action('ctrl_act1733')
def ctrl_nm1733():
    return 'ret1733' 

@action('ctrl_act1734')
def ctrl_nm1734():
    return 'ret1734' 

@action('ctrl_act1735')
def ctrl_nm1735():
    return 'ret1735' 

@action('ctrl_act1736')
def ctrl_nm1736():
    return 'ret1736' 

@action('ctrl_act1737')
def ctrl_nm1737():
    return 'ret1737' 

@action('ctrl_act1738')
def ctrl_nm1738():
    return 'ret1738' 

@action('ctrl_act1739')
def ctrl_nm1739():
    return 'ret1739' 

@action('ctrl_act1740')
def ctrl_nm1740():
    return 'ret1740' 

@action('ctrl_act1741')
def ctrl_nm1741():
    return 'ret1741' 

@action('ctrl_act1742')
def ctrl_nm1742():
    return 'ret1742' 

@action('ctrl_act1743')
def ctrl_nm1743():
    return 'ret1743' 

@action('ctrl_act1744')
def ctrl_nm1744():
    return 'ret1744' 

@action('ctrl_act1745')
def ctrl_nm1745():
    return 'ret1745' 

@action('ctrl_act1746')
def ctrl_nm1746():
    return 'ret1746' 

@action('ctrl_act1747')
def ctrl_nm1747():
    return 'ret1747' 

@action('ctrl_act1748')
def ctrl_nm1748():
    return 'ret1748' 

@action('ctrl_act1749')
def ctrl_nm1749():
    return 'ret1749' 

@action('ctrl_act1750')
def ctrl_nm1750():
    return 'ret1750' 

@action('ctrl_act1751')
def ctrl_nm1751():
    return 'ret1751' 

@action('ctrl_act1752')
def ctrl_nm1752():
    return 'ret1752' 

@action('ctrl_act1753')
def ctrl_nm1753():
    return 'ret1753' 

@action('ctrl_act1754')
def ctrl_nm1754():
    return 'ret1754' 

@action('ctrl_act1755')
def ctrl_nm1755():
    return 'ret1755' 

@action('ctrl_act1756')
def ctrl_nm1756():
    return 'ret1756' 

@action('ctrl_act1757')
def ctrl_nm1757():
    return 'ret1757' 

@action('ctrl_act1758')
def ctrl_nm1758():
    return 'ret1758' 

@action('ctrl_act1759')
def ctrl_nm1759():
    return 'ret1759' 

@action('ctrl_act1760')
def ctrl_nm1760():
    return 'ret1760' 

@action('ctrl_act1761')
def ctrl_nm1761():
    return 'ret1761' 

@action('ctrl_act1762')
def ctrl_nm1762():
    return 'ret1762' 

@action('ctrl_act1763')
def ctrl_nm1763():
    return 'ret1763' 

@action('ctrl_act1764')
def ctrl_nm1764():
    return 'ret1764' 

@action('ctrl_act1765')
def ctrl_nm1765():
    return 'ret1765' 

@action('ctrl_act1766')
def ctrl_nm1766():
    return 'ret1766' 

@action('ctrl_act1767')
def ctrl_nm1767():
    return 'ret1767' 

@action('ctrl_act1768')
def ctrl_nm1768():
    return 'ret1768' 

@action('ctrl_act1769')
def ctrl_nm1769():
    return 'ret1769' 

@action('ctrl_act1770')
def ctrl_nm1770():
    return 'ret1770' 

@action('ctrl_act1771')
def ctrl_nm1771():
    return 'ret1771' 

@action('ctrl_act1772')
def ctrl_nm1772():
    return 'ret1772' 

@action('ctrl_act1773')
def ctrl_nm1773():
    return 'ret1773' 

@action('ctrl_act1774')
def ctrl_nm1774():
    return 'ret1774' 

@action('ctrl_act1775')
def ctrl_nm1775():
    return 'ret1775' 

@action('ctrl_act1776')
def ctrl_nm1776():
    return 'ret1776' 

@action('ctrl_act1777')
def ctrl_nm1777():
    return 'ret1777' 

@action('ctrl_act1778')
def ctrl_nm1778():
    return 'ret1778' 

@action('ctrl_act1779')
def ctrl_nm1779():
    return 'ret1779' 

@action('ctrl_act1780')
def ctrl_nm1780():
    return 'ret1780' 

@action('ctrl_act1781')
def ctrl_nm1781():
    return 'ret1781' 

@action('ctrl_act1782')
def ctrl_nm1782():
    return 'ret1782' 

@action('ctrl_act1783')
def ctrl_nm1783():
    return 'ret1783' 

@action('ctrl_act1784')
def ctrl_nm1784():
    return 'ret1784' 

@action('ctrl_act1785')
def ctrl_nm1785():
    return 'ret1785' 

@action('ctrl_act1786')
def ctrl_nm1786():
    return 'ret1786' 

@action('ctrl_act1787')
def ctrl_nm1787():
    return 'ret1787' 

@action('ctrl_act1788')
def ctrl_nm1788():
    return 'ret1788' 

@action('ctrl_act1789')
def ctrl_nm1789():
    return 'ret1789' 

@action('ctrl_act1790')
def ctrl_nm1790():
    return 'ret1790' 

@action('ctrl_act1791')
def ctrl_nm1791():
    return 'ret1791' 

@action('ctrl_act1792')
def ctrl_nm1792():
    return 'ret1792' 

@action('ctrl_act1793')
def ctrl_nm1793():
    return 'ret1793' 

@action('ctrl_act1794')
def ctrl_nm1794():
    return 'ret1794' 

@action('ctrl_act1795')
def ctrl_nm1795():
    return 'ret1795' 

@action('ctrl_act1796')
def ctrl_nm1796():
    return 'ret1796' 

@action('ctrl_act1797')
def ctrl_nm1797():
    return 'ret1797' 

@action('ctrl_act1798')
def ctrl_nm1798():
    return 'ret1798' 

@action('ctrl_act1799')
def ctrl_nm1799():
    return 'ret1799' 

@action('ctrl_act1800')
def ctrl_nm1800():
    return 'ret1800' 

@action('ctrl_act1801')
def ctrl_nm1801():
    return 'ret1801' 

@action('ctrl_act1802')
def ctrl_nm1802():
    return 'ret1802' 

@action('ctrl_act1803')
def ctrl_nm1803():
    return 'ret1803' 

@action('ctrl_act1804')
def ctrl_nm1804():
    return 'ret1804' 

@action('ctrl_act1805')
def ctrl_nm1805():
    return 'ret1805' 

@action('ctrl_act1806')
def ctrl_nm1806():
    return 'ret1806' 

@action('ctrl_act1807')
def ctrl_nm1807():
    return 'ret1807' 

@action('ctrl_act1808')
def ctrl_nm1808():
    return 'ret1808' 

@action('ctrl_act1809')
def ctrl_nm1809():
    return 'ret1809' 

@action('ctrl_act1810')
def ctrl_nm1810():
    return 'ret1810' 

@action('ctrl_act1811')
def ctrl_nm1811():
    return 'ret1811' 

@action('ctrl_act1812')
def ctrl_nm1812():
    return 'ret1812' 

@action('ctrl_act1813')
def ctrl_nm1813():
    return 'ret1813' 

@action('ctrl_act1814')
def ctrl_nm1814():
    return 'ret1814' 

@action('ctrl_act1815')
def ctrl_nm1815():
    return 'ret1815' 

@action('ctrl_act1816')
def ctrl_nm1816():
    return 'ret1816' 

@action('ctrl_act1817')
def ctrl_nm1817():
    return 'ret1817' 

@action('ctrl_act1818')
def ctrl_nm1818():
    return 'ret1818' 

@action('ctrl_act1819')
def ctrl_nm1819():
    return 'ret1819' 

@action('ctrl_act1820')
def ctrl_nm1820():
    return 'ret1820' 

@action('ctrl_act1821')
def ctrl_nm1821():
    return 'ret1821' 

@action('ctrl_act1822')
def ctrl_nm1822():
    return 'ret1822' 

@action('ctrl_act1823')
def ctrl_nm1823():
    return 'ret1823' 

@action('ctrl_act1824')
def ctrl_nm1824():
    return 'ret1824' 

@action('ctrl_act1825')
def ctrl_nm1825():
    return 'ret1825' 

@action('ctrl_act1826')
def ctrl_nm1826():
    return 'ret1826' 

@action('ctrl_act1827')
def ctrl_nm1827():
    return 'ret1827' 

@action('ctrl_act1828')
def ctrl_nm1828():
    return 'ret1828' 

@action('ctrl_act1829')
def ctrl_nm1829():
    return 'ret1829' 

@action('ctrl_act1830')
def ctrl_nm1830():
    return 'ret1830' 

@action('ctrl_act1831')
def ctrl_nm1831():
    return 'ret1831' 

@action('ctrl_act1832')
def ctrl_nm1832():
    return 'ret1832' 

@action('ctrl_act1833')
def ctrl_nm1833():
    return 'ret1833' 

@action('ctrl_act1834')
def ctrl_nm1834():
    return 'ret1834' 

@action('ctrl_act1835')
def ctrl_nm1835():
    return 'ret1835' 

@action('ctrl_act1836')
def ctrl_nm1836():
    return 'ret1836' 

@action('ctrl_act1837')
def ctrl_nm1837():
    return 'ret1837' 

@action('ctrl_act1838')
def ctrl_nm1838():
    return 'ret1838' 

@action('ctrl_act1839')
def ctrl_nm1839():
    return 'ret1839' 

@action('ctrl_act1840')
def ctrl_nm1840():
    return 'ret1840' 

@action('ctrl_act1841')
def ctrl_nm1841():
    return 'ret1841' 

@action('ctrl_act1842')
def ctrl_nm1842():
    return 'ret1842' 

@action('ctrl_act1843')
def ctrl_nm1843():
    return 'ret1843' 

@action('ctrl_act1844')
def ctrl_nm1844():
    return 'ret1844' 

@action('ctrl_act1845')
def ctrl_nm1845():
    return 'ret1845' 

@action('ctrl_act1846')
def ctrl_nm1846():
    return 'ret1846' 

@action('ctrl_act1847')
def ctrl_nm1847():
    return 'ret1847' 

@action('ctrl_act1848')
def ctrl_nm1848():
    return 'ret1848' 

@action('ctrl_act1849')
def ctrl_nm1849():
    return 'ret1849' 

@action('ctrl_act1850')
def ctrl_nm1850():
    return 'ret1850' 

@action('ctrl_act1851')
def ctrl_nm1851():
    return 'ret1851' 

@action('ctrl_act1852')
def ctrl_nm1852():
    return 'ret1852' 

@action('ctrl_act1853')
def ctrl_nm1853():
    return 'ret1853' 

@action('ctrl_act1854')
def ctrl_nm1854():
    return 'ret1854' 

@action('ctrl_act1855')
def ctrl_nm1855():
    return 'ret1855' 

@action('ctrl_act1856')
def ctrl_nm1856():
    return 'ret1856' 

@action('ctrl_act1857')
def ctrl_nm1857():
    return 'ret1857' 

@action('ctrl_act1858')
def ctrl_nm1858():
    return 'ret1858' 

@action('ctrl_act1859')
def ctrl_nm1859():
    return 'ret1859' 

@action('ctrl_act1860')
def ctrl_nm1860():
    return 'ret1860' 

@action('ctrl_act1861')
def ctrl_nm1861():
    return 'ret1861' 

@action('ctrl_act1862')
def ctrl_nm1862():
    return 'ret1862' 

@action('ctrl_act1863')
def ctrl_nm1863():
    return 'ret1863' 

@action('ctrl_act1864')
def ctrl_nm1864():
    return 'ret1864' 

@action('ctrl_act1865')
def ctrl_nm1865():
    return 'ret1865' 

@action('ctrl_act1866')
def ctrl_nm1866():
    return 'ret1866' 

@action('ctrl_act1867')
def ctrl_nm1867():
    return 'ret1867' 

@action('ctrl_act1868')
def ctrl_nm1868():
    return 'ret1868' 

@action('ctrl_act1869')
def ctrl_nm1869():
    return 'ret1869' 

@action('ctrl_act1870')
def ctrl_nm1870():
    return 'ret1870' 

@action('ctrl_act1871')
def ctrl_nm1871():
    return 'ret1871' 

@action('ctrl_act1872')
def ctrl_nm1872():
    return 'ret1872' 

@action('ctrl_act1873')
def ctrl_nm1873():
    return 'ret1873' 

@action('ctrl_act1874')
def ctrl_nm1874():
    return 'ret1874' 

@action('ctrl_act1875')
def ctrl_nm1875():
    return 'ret1875' 

@action('ctrl_act1876')
def ctrl_nm1876():
    return 'ret1876' 

@action('ctrl_act1877')
def ctrl_nm1877():
    return 'ret1877' 

@action('ctrl_act1878')
def ctrl_nm1878():
    return 'ret1878' 

@action('ctrl_act1879')
def ctrl_nm1879():
    return 'ret1879' 

@action('ctrl_act1880')
def ctrl_nm1880():
    return 'ret1880' 

@action('ctrl_act1881')
def ctrl_nm1881():
    return 'ret1881' 

@action('ctrl_act1882')
def ctrl_nm1882():
    return 'ret1882' 

@action('ctrl_act1883')
def ctrl_nm1883():
    return 'ret1883' 

@action('ctrl_act1884')
def ctrl_nm1884():
    return 'ret1884' 

@action('ctrl_act1885')
def ctrl_nm1885():
    return 'ret1885' 

@action('ctrl_act1886')
def ctrl_nm1886():
    return 'ret1886' 

@action('ctrl_act1887')
def ctrl_nm1887():
    return 'ret1887' 

@action('ctrl_act1888')
def ctrl_nm1888():
    return 'ret1888' 

@action('ctrl_act1889')
def ctrl_nm1889():
    return 'ret1889' 

@action('ctrl_act1890')
def ctrl_nm1890():
    return 'ret1890' 

@action('ctrl_act1891')
def ctrl_nm1891():
    return 'ret1891' 

@action('ctrl_act1892')
def ctrl_nm1892():
    return 'ret1892' 

@action('ctrl_act1893')
def ctrl_nm1893():
    return 'ret1893' 

@action('ctrl_act1894')
def ctrl_nm1894():
    return 'ret1894' 

@action('ctrl_act1895')
def ctrl_nm1895():
    return 'ret1895' 

@action('ctrl_act1896')
def ctrl_nm1896():
    return 'ret1896' 

@action('ctrl_act1897')
def ctrl_nm1897():
    return 'ret1897' 

@action('ctrl_act1898')
def ctrl_nm1898():
    return 'ret1898' 

@action('ctrl_act1899')
def ctrl_nm1899():
    return 'ret1899' 

@action('ctrl_act1900')
def ctrl_nm1900():
    return 'ret1900' 

@action('ctrl_act1901')
def ctrl_nm1901():
    return 'ret1901' 

@action('ctrl_act1902')
def ctrl_nm1902():
    return 'ret1902' 

@action('ctrl_act1903')
def ctrl_nm1903():
    return 'ret1903' 

@action('ctrl_act1904')
def ctrl_nm1904():
    return 'ret1904' 

@action('ctrl_act1905')
def ctrl_nm1905():
    return 'ret1905' 

@action('ctrl_act1906')
def ctrl_nm1906():
    return 'ret1906' 

@action('ctrl_act1907')
def ctrl_nm1907():
    return 'ret1907' 

@action('ctrl_act1908')
def ctrl_nm1908():
    return 'ret1908' 

@action('ctrl_act1909')
def ctrl_nm1909():
    return 'ret1909' 

@action('ctrl_act1910')
def ctrl_nm1910():
    return 'ret1910' 

@action('ctrl_act1911')
def ctrl_nm1911():
    return 'ret1911' 

@action('ctrl_act1912')
def ctrl_nm1912():
    return 'ret1912' 

@action('ctrl_act1913')
def ctrl_nm1913():
    return 'ret1913' 

@action('ctrl_act1914')
def ctrl_nm1914():
    return 'ret1914' 

@action('ctrl_act1915')
def ctrl_nm1915():
    return 'ret1915' 

@action('ctrl_act1916')
def ctrl_nm1916():
    return 'ret1916' 

@action('ctrl_act1917')
def ctrl_nm1917():
    return 'ret1917' 

@action('ctrl_act1918')
def ctrl_nm1918():
    return 'ret1918' 

@action('ctrl_act1919')
def ctrl_nm1919():
    return 'ret1919' 

@action('ctrl_act1920')
def ctrl_nm1920():
    return 'ret1920' 

@action('ctrl_act1921')
def ctrl_nm1921():
    return 'ret1921' 

@action('ctrl_act1922')
def ctrl_nm1922():
    return 'ret1922' 

@action('ctrl_act1923')
def ctrl_nm1923():
    return 'ret1923' 

@action('ctrl_act1924')
def ctrl_nm1924():
    return 'ret1924' 

@action('ctrl_act1925')
def ctrl_nm1925():
    return 'ret1925' 

@action('ctrl_act1926')
def ctrl_nm1926():
    return 'ret1926' 

@action('ctrl_act1927')
def ctrl_nm1927():
    return 'ret1927' 

@action('ctrl_act1928')
def ctrl_nm1928():
    return 'ret1928' 

@action('ctrl_act1929')
def ctrl_nm1929():
    return 'ret1929' 

@action('ctrl_act1930')
def ctrl_nm1930():
    return 'ret1930' 

@action('ctrl_act1931')
def ctrl_nm1931():
    return 'ret1931' 

@action('ctrl_act1932')
def ctrl_nm1932():
    return 'ret1932' 

@action('ctrl_act1933')
def ctrl_nm1933():
    return 'ret1933' 

@action('ctrl_act1934')
def ctrl_nm1934():
    return 'ret1934' 

@action('ctrl_act1935')
def ctrl_nm1935():
    return 'ret1935' 

@action('ctrl_act1936')
def ctrl_nm1936():
    return 'ret1936' 

@action('ctrl_act1937')
def ctrl_nm1937():
    return 'ret1937' 

@action('ctrl_act1938')
def ctrl_nm1938():
    return 'ret1938' 

@action('ctrl_act1939')
def ctrl_nm1939():
    return 'ret1939' 

@action('ctrl_act1940')
def ctrl_nm1940():
    return 'ret1940' 

@action('ctrl_act1941')
def ctrl_nm1941():
    return 'ret1941' 

@action('ctrl_act1942')
def ctrl_nm1942():
    return 'ret1942' 

@action('ctrl_act1943')
def ctrl_nm1943():
    return 'ret1943' 

@action('ctrl_act1944')
def ctrl_nm1944():
    return 'ret1944' 

@action('ctrl_act1945')
def ctrl_nm1945():
    return 'ret1945' 

@action('ctrl_act1946')
def ctrl_nm1946():
    return 'ret1946' 

@action('ctrl_act1947')
def ctrl_nm1947():
    return 'ret1947' 

@action('ctrl_act1948')
def ctrl_nm1948():
    return 'ret1948' 

@action('ctrl_act1949')
def ctrl_nm1949():
    return 'ret1949' 

@action('ctrl_act1950')
def ctrl_nm1950():
    return 'ret1950' 

@action('ctrl_act1951')
def ctrl_nm1951():
    return 'ret1951' 

@action('ctrl_act1952')
def ctrl_nm1952():
    return 'ret1952' 

@action('ctrl_act1953')
def ctrl_nm1953():
    return 'ret1953' 

@action('ctrl_act1954')
def ctrl_nm1954():
    return 'ret1954' 

@action('ctrl_act1955')
def ctrl_nm1955():
    return 'ret1955' 

@action('ctrl_act1956')
def ctrl_nm1956():
    return 'ret1956' 

@action('ctrl_act1957')
def ctrl_nm1957():
    return 'ret1957' 

@action('ctrl_act1958')
def ctrl_nm1958():
    return 'ret1958' 

@action('ctrl_act1959')
def ctrl_nm1959():
    return 'ret1959' 

@action('ctrl_act1960')
def ctrl_nm1960():
    return 'ret1960' 

@action('ctrl_act1961')
def ctrl_nm1961():
    return 'ret1961' 

@action('ctrl_act1962')
def ctrl_nm1962():
    return 'ret1962' 

@action('ctrl_act1963')
def ctrl_nm1963():
    return 'ret1963' 

@action('ctrl_act1964')
def ctrl_nm1964():
    return 'ret1964' 

@action('ctrl_act1965')
def ctrl_nm1965():
    return 'ret1965' 

@action('ctrl_act1966')
def ctrl_nm1966():
    return 'ret1966' 

@action('ctrl_act1967')
def ctrl_nm1967():
    return 'ret1967' 

@action('ctrl_act1968')
def ctrl_nm1968():
    return 'ret1968' 

@action('ctrl_act1969')
def ctrl_nm1969():
    return 'ret1969' 

@action('ctrl_act1970')
def ctrl_nm1970():
    return 'ret1970' 

@action('ctrl_act1971')
def ctrl_nm1971():
    return 'ret1971' 

@action('ctrl_act1972')
def ctrl_nm1972():
    return 'ret1972' 

@action('ctrl_act1973')
def ctrl_nm1973():
    return 'ret1973' 

@action('ctrl_act1974')
def ctrl_nm1974():
    return 'ret1974' 

@action('ctrl_act1975')
def ctrl_nm1975():
    return 'ret1975' 

@action('ctrl_act1976')
def ctrl_nm1976():
    return 'ret1976' 

@action('ctrl_act1977')
def ctrl_nm1977():
    return 'ret1977' 

@action('ctrl_act1978')
def ctrl_nm1978():
    return 'ret1978' 

@action('ctrl_act1979')
def ctrl_nm1979():
    return 'ret1979' 

@action('ctrl_act1980')
def ctrl_nm1980():
    return 'ret1980' 

@action('ctrl_act1981')
def ctrl_nm1981():
    return 'ret1981' 

@action('ctrl_act1982')
def ctrl_nm1982():
    return 'ret1982' 

@action('ctrl_act1983')
def ctrl_nm1983():
    return 'ret1983' 

@action('ctrl_act1984')
def ctrl_nm1984():
    return 'ret1984' 

@action('ctrl_act1985')
def ctrl_nm1985():
    return 'ret1985' 

@action('ctrl_act1986')
def ctrl_nm1986():
    return 'ret1986' 

@action('ctrl_act1987')
def ctrl_nm1987():
    return 'ret1987' 

@action('ctrl_act1988')
def ctrl_nm1988():
    return 'ret1988' 

@action('ctrl_act1989')
def ctrl_nm1989():
    return 'ret1989' 

@action('ctrl_act1990')
def ctrl_nm1990():
    return 'ret1990' 

@action('ctrl_act1991')
def ctrl_nm1991():
    return 'ret1991' 

@action('ctrl_act1992')
def ctrl_nm1992():
    return 'ret1992' 

@action('ctrl_act1993')
def ctrl_nm1993():
    return 'ret1993' 

@action('ctrl_act1994')
def ctrl_nm1994():
    return 'ret1994' 

@action('ctrl_act1995')
def ctrl_nm1995():
    return 'ret1995' 

@action('ctrl_act1996')
def ctrl_nm1996():
    return 'ret1996' 

@action('ctrl_act1997')
def ctrl_nm1997():
    return 'ret1997' 

@action('ctrl_act1998')
def ctrl_nm1998():
    return 'ret1998' 

@action('ctrl_act1999')
def ctrl_nm1999():
    return 'ret1999' 

@action('ctrl_act2000')
def ctrl_nm2000():
    return 'ret2000' 

@action('ctrl_act2001')
def ctrl_nm2001():
    return 'ret2001' 

@action('ctrl_act2002')
def ctrl_nm2002():
    return 'ret2002' 

@action('ctrl_act2003')
def ctrl_nm2003():
    return 'ret2003' 

@action('ctrl_act2004')
def ctrl_nm2004():
    return 'ret2004' 

@action('ctrl_act2005')
def ctrl_nm2005():
    return 'ret2005' 

@action('ctrl_act2006')
def ctrl_nm2006():
    return 'ret2006' 

@action('ctrl_act2007')
def ctrl_nm2007():
    return 'ret2007' 

@action('ctrl_act2008')
def ctrl_nm2008():
    return 'ret2008' 

@action('ctrl_act2009')
def ctrl_nm2009():
    return 'ret2009' 

@action('ctrl_act2010')
def ctrl_nm2010():
    return 'ret2010' 

@action('ctrl_act2011')
def ctrl_nm2011():
    return 'ret2011' 

@action('ctrl_act2012')
def ctrl_nm2012():
    return 'ret2012' 

@action('ctrl_act2013')
def ctrl_nm2013():
    return 'ret2013' 

@action('ctrl_act2014')
def ctrl_nm2014():
    return 'ret2014' 

@action('ctrl_act2015')
def ctrl_nm2015():
    return 'ret2015' 

@action('ctrl_act2016')
def ctrl_nm2016():
    return 'ret2016' 

@action('ctrl_act2017')
def ctrl_nm2017():
    return 'ret2017' 

@action('ctrl_act2018')
def ctrl_nm2018():
    return 'ret2018' 

@action('ctrl_act2019')
def ctrl_nm2019():
    return 'ret2019' 

@action('ctrl_act2020')
def ctrl_nm2020():
    return 'ret2020' 

@action('ctrl_act2021')
def ctrl_nm2021():
    return 'ret2021' 

@action('ctrl_act2022')
def ctrl_nm2022():
    return 'ret2022' 

@action('ctrl_act2023')
def ctrl_nm2023():
    return 'ret2023' 

@action('ctrl_act2024')
def ctrl_nm2024():
    return 'ret2024' 

@action('ctrl_act2025')
def ctrl_nm2025():
    return 'ret2025' 

@action('ctrl_act2026')
def ctrl_nm2026():
    return 'ret2026' 

@action('ctrl_act2027')
def ctrl_nm2027():
    return 'ret2027' 

@action('ctrl_act2028')
def ctrl_nm2028():
    return 'ret2028' 

@action('ctrl_act2029')
def ctrl_nm2029():
    return 'ret2029' 

@action('ctrl_act2030')
def ctrl_nm2030():
    return 'ret2030' 

@action('ctrl_act2031')
def ctrl_nm2031():
    return 'ret2031' 

@action('ctrl_act2032')
def ctrl_nm2032():
    return 'ret2032' 

@action('ctrl_act2033')
def ctrl_nm2033():
    return 'ret2033' 

@action('ctrl_act2034')
def ctrl_nm2034():
    return 'ret2034' 

@action('ctrl_act2035')
def ctrl_nm2035():
    return 'ret2035' 

@action('ctrl_act2036')
def ctrl_nm2036():
    return 'ret2036' 

@action('ctrl_act2037')
def ctrl_nm2037():
    return 'ret2037' 

@action('ctrl_act2038')
def ctrl_nm2038():
    return 'ret2038' 

@action('ctrl_act2039')
def ctrl_nm2039():
    return 'ret2039' 

@action('ctrl_act2040')
def ctrl_nm2040():
    return 'ret2040' 

@action('ctrl_act2041')
def ctrl_nm2041():
    return 'ret2041' 

@action('ctrl_act2042')
def ctrl_nm2042():
    return 'ret2042' 

@action('ctrl_act2043')
def ctrl_nm2043():
    return 'ret2043' 

@action('ctrl_act2044')
def ctrl_nm2044():
    return 'ret2044' 

@action('ctrl_act2045')
def ctrl_nm2045():
    return 'ret2045' 

@action('ctrl_act2046')
def ctrl_nm2046():
    return 'ret2046' 

@action('ctrl_act2047')
def ctrl_nm2047():
    return 'ret2047' 

@action('ctrl_act2048')
def ctrl_nm2048():
    return 'ret2048' 

@action('ctrl_act2049')
def ctrl_nm2049():
    return 'ret2049' 

@action('ctrl_act2050')
def ctrl_nm2050():
    return 'ret2050' 

@action('ctrl_act2051')
def ctrl_nm2051():
    return 'ret2051' 

@action('ctrl_act2052')
def ctrl_nm2052():
    return 'ret2052' 

@action('ctrl_act2053')
def ctrl_nm2053():
    return 'ret2053' 

@action('ctrl_act2054')
def ctrl_nm2054():
    return 'ret2054' 

@action('ctrl_act2055')
def ctrl_nm2055():
    return 'ret2055' 

@action('ctrl_act2056')
def ctrl_nm2056():
    return 'ret2056' 

@action('ctrl_act2057')
def ctrl_nm2057():
    return 'ret2057' 

@action('ctrl_act2058')
def ctrl_nm2058():
    return 'ret2058' 

@action('ctrl_act2059')
def ctrl_nm2059():
    return 'ret2059' 

@action('ctrl_act2060')
def ctrl_nm2060():
    return 'ret2060' 

@action('ctrl_act2061')
def ctrl_nm2061():
    return 'ret2061' 

@action('ctrl_act2062')
def ctrl_nm2062():
    return 'ret2062' 

@action('ctrl_act2063')
def ctrl_nm2063():
    return 'ret2063' 

@action('ctrl_act2064')
def ctrl_nm2064():
    return 'ret2064' 

@action('ctrl_act2065')
def ctrl_nm2065():
    return 'ret2065' 

@action('ctrl_act2066')
def ctrl_nm2066():
    return 'ret2066' 

@action('ctrl_act2067')
def ctrl_nm2067():
    return 'ret2067' 

@action('ctrl_act2068')
def ctrl_nm2068():
    return 'ret2068' 

@action('ctrl_act2069')
def ctrl_nm2069():
    return 'ret2069' 

@action('ctrl_act2070')
def ctrl_nm2070():
    return 'ret2070' 

@action('ctrl_act2071')
def ctrl_nm2071():
    return 'ret2071' 

@action('ctrl_act2072')
def ctrl_nm2072():
    return 'ret2072' 

@action('ctrl_act2073')
def ctrl_nm2073():
    return 'ret2073' 

@action('ctrl_act2074')
def ctrl_nm2074():
    return 'ret2074' 

@action('ctrl_act2075')
def ctrl_nm2075():
    return 'ret2075' 

@action('ctrl_act2076')
def ctrl_nm2076():
    return 'ret2076' 

@action('ctrl_act2077')
def ctrl_nm2077():
    return 'ret2077' 

@action('ctrl_act2078')
def ctrl_nm2078():
    return 'ret2078' 

@action('ctrl_act2079')
def ctrl_nm2079():
    return 'ret2079' 

@action('ctrl_act2080')
def ctrl_nm2080():
    return 'ret2080' 

@action('ctrl_act2081')
def ctrl_nm2081():
    return 'ret2081' 

@action('ctrl_act2082')
def ctrl_nm2082():
    return 'ret2082' 

@action('ctrl_act2083')
def ctrl_nm2083():
    return 'ret2083' 

@action('ctrl_act2084')
def ctrl_nm2084():
    return 'ret2084' 

@action('ctrl_act2085')
def ctrl_nm2085():
    return 'ret2085' 

@action('ctrl_act2086')
def ctrl_nm2086():
    return 'ret2086' 

@action('ctrl_act2087')
def ctrl_nm2087():
    return 'ret2087' 

@action('ctrl_act2088')
def ctrl_nm2088():
    return 'ret2088' 

@action('ctrl_act2089')
def ctrl_nm2089():
    return 'ret2089' 

@action('ctrl_act2090')
def ctrl_nm2090():
    return 'ret2090' 

@action('ctrl_act2091')
def ctrl_nm2091():
    return 'ret2091' 

@action('ctrl_act2092')
def ctrl_nm2092():
    return 'ret2092' 

@action('ctrl_act2093')
def ctrl_nm2093():
    return 'ret2093' 

@action('ctrl_act2094')
def ctrl_nm2094():
    return 'ret2094' 

@action('ctrl_act2095')
def ctrl_nm2095():
    return 'ret2095' 

@action('ctrl_act2096')
def ctrl_nm2096():
    return 'ret2096' 

@action('ctrl_act2097')
def ctrl_nm2097():
    return 'ret2097' 

@action('ctrl_act2098')
def ctrl_nm2098():
    return 'ret2098' 

@action('ctrl_act2099')
def ctrl_nm2099():
    return 'ret2099' 

@action('ctrl_act2100')
def ctrl_nm2100():
    return 'ret2100' 

@action('ctrl_act2101')
def ctrl_nm2101():
    return 'ret2101' 

@action('ctrl_act2102')
def ctrl_nm2102():
    return 'ret2102' 

@action('ctrl_act2103')
def ctrl_nm2103():
    return 'ret2103' 

@action('ctrl_act2104')
def ctrl_nm2104():
    return 'ret2104' 

@action('ctrl_act2105')
def ctrl_nm2105():
    return 'ret2105' 

@action('ctrl_act2106')
def ctrl_nm2106():
    return 'ret2106' 

@action('ctrl_act2107')
def ctrl_nm2107():
    return 'ret2107' 

@action('ctrl_act2108')
def ctrl_nm2108():
    return 'ret2108' 

@action('ctrl_act2109')
def ctrl_nm2109():
    return 'ret2109' 

@action('ctrl_act2110')
def ctrl_nm2110():
    return 'ret2110' 

@action('ctrl_act2111')
def ctrl_nm2111():
    return 'ret2111' 

@action('ctrl_act2112')
def ctrl_nm2112():
    return 'ret2112' 

@action('ctrl_act2113')
def ctrl_nm2113():
    return 'ret2113' 

@action('ctrl_act2114')
def ctrl_nm2114():
    return 'ret2114' 

@action('ctrl_act2115')
def ctrl_nm2115():
    return 'ret2115' 

@action('ctrl_act2116')
def ctrl_nm2116():
    return 'ret2116' 

@action('ctrl_act2117')
def ctrl_nm2117():
    return 'ret2117' 

@action('ctrl_act2118')
def ctrl_nm2118():
    return 'ret2118' 

@action('ctrl_act2119')
def ctrl_nm2119():
    return 'ret2119' 

@action('ctrl_act2120')
def ctrl_nm2120():
    return 'ret2120' 

@action('ctrl_act2121')
def ctrl_nm2121():
    return 'ret2121' 

@action('ctrl_act2122')
def ctrl_nm2122():
    return 'ret2122' 

@action('ctrl_act2123')
def ctrl_nm2123():
    return 'ret2123' 

@action('ctrl_act2124')
def ctrl_nm2124():
    return 'ret2124' 

@action('ctrl_act2125')
def ctrl_nm2125():
    return 'ret2125' 

@action('ctrl_act2126')
def ctrl_nm2126():
    return 'ret2126' 

@action('ctrl_act2127')
def ctrl_nm2127():
    return 'ret2127' 

@action('ctrl_act2128')
def ctrl_nm2128():
    return 'ret2128' 

@action('ctrl_act2129')
def ctrl_nm2129():
    return 'ret2129' 

@action('ctrl_act2130')
def ctrl_nm2130():
    return 'ret2130' 

@action('ctrl_act2131')
def ctrl_nm2131():
    return 'ret2131' 

@action('ctrl_act2132')
def ctrl_nm2132():
    return 'ret2132' 

@action('ctrl_act2133')
def ctrl_nm2133():
    return 'ret2133' 

@action('ctrl_act2134')
def ctrl_nm2134():
    return 'ret2134' 

@action('ctrl_act2135')
def ctrl_nm2135():
    return 'ret2135' 

@action('ctrl_act2136')
def ctrl_nm2136():
    return 'ret2136' 

@action('ctrl_act2137')
def ctrl_nm2137():
    return 'ret2137' 

@action('ctrl_act2138')
def ctrl_nm2138():
    return 'ret2138' 

@action('ctrl_act2139')
def ctrl_nm2139():
    return 'ret2139' 

@action('ctrl_act2140')
def ctrl_nm2140():
    return 'ret2140' 

@action('ctrl_act2141')
def ctrl_nm2141():
    return 'ret2141' 

@action('ctrl_act2142')
def ctrl_nm2142():
    return 'ret2142' 

@action('ctrl_act2143')
def ctrl_nm2143():
    return 'ret2143' 

@action('ctrl_act2144')
def ctrl_nm2144():
    return 'ret2144' 

@action('ctrl_act2145')
def ctrl_nm2145():
    return 'ret2145' 

@action('ctrl_act2146')
def ctrl_nm2146():
    return 'ret2146' 

@action('ctrl_act2147')
def ctrl_nm2147():
    return 'ret2147' 

@action('ctrl_act2148')
def ctrl_nm2148():
    return 'ret2148' 

@action('ctrl_act2149')
def ctrl_nm2149():
    return 'ret2149' 

@action('ctrl_act2150')
def ctrl_nm2150():
    return 'ret2150' 

@action('ctrl_act2151')
def ctrl_nm2151():
    return 'ret2151' 

@action('ctrl_act2152')
def ctrl_nm2152():
    return 'ret2152' 

@action('ctrl_act2153')
def ctrl_nm2153():
    return 'ret2153' 

@action('ctrl_act2154')
def ctrl_nm2154():
    return 'ret2154' 

@action('ctrl_act2155')
def ctrl_nm2155():
    return 'ret2155' 

@action('ctrl_act2156')
def ctrl_nm2156():
    return 'ret2156' 

@action('ctrl_act2157')
def ctrl_nm2157():
    return 'ret2157' 

@action('ctrl_act2158')
def ctrl_nm2158():
    return 'ret2158' 

@action('ctrl_act2159')
def ctrl_nm2159():
    return 'ret2159' 

@action('ctrl_act2160')
def ctrl_nm2160():
    return 'ret2160' 

@action('ctrl_act2161')
def ctrl_nm2161():
    return 'ret2161' 

@action('ctrl_act2162')
def ctrl_nm2162():
    return 'ret2162' 

@action('ctrl_act2163')
def ctrl_nm2163():
    return 'ret2163' 

@action('ctrl_act2164')
def ctrl_nm2164():
    return 'ret2164' 

@action('ctrl_act2165')
def ctrl_nm2165():
    return 'ret2165' 

@action('ctrl_act2166')
def ctrl_nm2166():
    return 'ret2166' 

@action('ctrl_act2167')
def ctrl_nm2167():
    return 'ret2167' 

@action('ctrl_act2168')
def ctrl_nm2168():
    return 'ret2168' 

@action('ctrl_act2169')
def ctrl_nm2169():
    return 'ret2169' 

@action('ctrl_act2170')
def ctrl_nm2170():
    return 'ret2170' 

@action('ctrl_act2171')
def ctrl_nm2171():
    return 'ret2171' 

@action('ctrl_act2172')
def ctrl_nm2172():
    return 'ret2172' 

@action('ctrl_act2173')
def ctrl_nm2173():
    return 'ret2173' 

@action('ctrl_act2174')
def ctrl_nm2174():
    return 'ret2174' 

@action('ctrl_act2175')
def ctrl_nm2175():
    return 'ret2175' 

@action('ctrl_act2176')
def ctrl_nm2176():
    return 'ret2176' 

@action('ctrl_act2177')
def ctrl_nm2177():
    return 'ret2177' 

@action('ctrl_act2178')
def ctrl_nm2178():
    return 'ret2178' 

@action('ctrl_act2179')
def ctrl_nm2179():
    return 'ret2179' 

@action('ctrl_act2180')
def ctrl_nm2180():
    return 'ret2180' 

@action('ctrl_act2181')
def ctrl_nm2181():
    return 'ret2181' 

@action('ctrl_act2182')
def ctrl_nm2182():
    return 'ret2182' 

@action('ctrl_act2183')
def ctrl_nm2183():
    return 'ret2183' 

@action('ctrl_act2184')
def ctrl_nm2184():
    return 'ret2184' 

@action('ctrl_act2185')
def ctrl_nm2185():
    return 'ret2185' 

@action('ctrl_act2186')
def ctrl_nm2186():
    return 'ret2186' 

@action('ctrl_act2187')
def ctrl_nm2187():
    return 'ret2187' 

@action('ctrl_act2188')
def ctrl_nm2188():
    return 'ret2188' 

@action('ctrl_act2189')
def ctrl_nm2189():
    return 'ret2189' 

@action('ctrl_act2190')
def ctrl_nm2190():
    return 'ret2190' 

@action('ctrl_act2191')
def ctrl_nm2191():
    return 'ret2191' 

@action('ctrl_act2192')
def ctrl_nm2192():
    return 'ret2192' 

@action('ctrl_act2193')
def ctrl_nm2193():
    return 'ret2193' 

@action('ctrl_act2194')
def ctrl_nm2194():
    return 'ret2194' 

@action('ctrl_act2195')
def ctrl_nm2195():
    return 'ret2195' 

@action('ctrl_act2196')
def ctrl_nm2196():
    return 'ret2196' 

@action('ctrl_act2197')
def ctrl_nm2197():
    return 'ret2197' 

@action('ctrl_act2198')
def ctrl_nm2198():
    return 'ret2198' 

@action('ctrl_act2199')
def ctrl_nm2199():
    return 'ret2199' 

@action('ctrl_act2200')
def ctrl_nm2200():
    return 'ret2200' 

@action('ctrl_act2201')
def ctrl_nm2201():
    return 'ret2201' 

@action('ctrl_act2202')
def ctrl_nm2202():
    return 'ret2202' 

@action('ctrl_act2203')
def ctrl_nm2203():
    return 'ret2203' 

@action('ctrl_act2204')
def ctrl_nm2204():
    return 'ret2204' 

@action('ctrl_act2205')
def ctrl_nm2205():
    return 'ret2205' 

@action('ctrl_act2206')
def ctrl_nm2206():
    return 'ret2206' 

@action('ctrl_act2207')
def ctrl_nm2207():
    return 'ret2207' 

@action('ctrl_act2208')
def ctrl_nm2208():
    return 'ret2208' 

@action('ctrl_act2209')
def ctrl_nm2209():
    return 'ret2209' 

@action('ctrl_act2210')
def ctrl_nm2210():
    return 'ret2210' 

@action('ctrl_act2211')
def ctrl_nm2211():
    return 'ret2211' 

@action('ctrl_act2212')
def ctrl_nm2212():
    return 'ret2212' 

@action('ctrl_act2213')
def ctrl_nm2213():
    return 'ret2213' 

@action('ctrl_act2214')
def ctrl_nm2214():
    return 'ret2214' 

@action('ctrl_act2215')
def ctrl_nm2215():
    return 'ret2215' 

@action('ctrl_act2216')
def ctrl_nm2216():
    return 'ret2216' 

@action('ctrl_act2217')
def ctrl_nm2217():
    return 'ret2217' 

@action('ctrl_act2218')
def ctrl_nm2218():
    return 'ret2218' 

@action('ctrl_act2219')
def ctrl_nm2219():
    return 'ret2219' 

@action('ctrl_act2220')
def ctrl_nm2220():
    return 'ret2220' 

@action('ctrl_act2221')
def ctrl_nm2221():
    return 'ret2221' 

@action('ctrl_act2222')
def ctrl_nm2222():
    return 'ret2222' 

@action('ctrl_act2223')
def ctrl_nm2223():
    return 'ret2223' 

@action('ctrl_act2224')
def ctrl_nm2224():
    return 'ret2224' 

@action('ctrl_act2225')
def ctrl_nm2225():
    return 'ret2225' 

@action('ctrl_act2226')
def ctrl_nm2226():
    return 'ret2226' 

@action('ctrl_act2227')
def ctrl_nm2227():
    return 'ret2227' 

@action('ctrl_act2228')
def ctrl_nm2228():
    return 'ret2228' 

@action('ctrl_act2229')
def ctrl_nm2229():
    return 'ret2229' 

@action('ctrl_act2230')
def ctrl_nm2230():
    return 'ret2230' 

@action('ctrl_act2231')
def ctrl_nm2231():
    return 'ret2231' 

@action('ctrl_act2232')
def ctrl_nm2232():
    return 'ret2232' 

@action('ctrl_act2233')
def ctrl_nm2233():
    return 'ret2233' 

@action('ctrl_act2234')
def ctrl_nm2234():
    return 'ret2234' 

@action('ctrl_act2235')
def ctrl_nm2235():
    return 'ret2235' 

@action('ctrl_act2236')
def ctrl_nm2236():
    return 'ret2236' 

@action('ctrl_act2237')
def ctrl_nm2237():
    return 'ret2237' 

@action('ctrl_act2238')
def ctrl_nm2238():
    return 'ret2238' 

@action('ctrl_act2239')
def ctrl_nm2239():
    return 'ret2239' 

@action('ctrl_act2240')
def ctrl_nm2240():
    return 'ret2240' 

@action('ctrl_act2241')
def ctrl_nm2241():
    return 'ret2241' 

@action('ctrl_act2242')
def ctrl_nm2242():
    return 'ret2242' 

@action('ctrl_act2243')
def ctrl_nm2243():
    return 'ret2243' 

@action('ctrl_act2244')
def ctrl_nm2244():
    return 'ret2244' 

@action('ctrl_act2245')
def ctrl_nm2245():
    return 'ret2245' 

@action('ctrl_act2246')
def ctrl_nm2246():
    return 'ret2246' 

@action('ctrl_act2247')
def ctrl_nm2247():
    return 'ret2247' 

@action('ctrl_act2248')
def ctrl_nm2248():
    return 'ret2248' 

@action('ctrl_act2249')
def ctrl_nm2249():
    return 'ret2249' 

@action('ctrl_act2250')
def ctrl_nm2250():
    return 'ret2250' 

@action('ctrl_act2251')
def ctrl_nm2251():
    return 'ret2251' 

@action('ctrl_act2252')
def ctrl_nm2252():
    return 'ret2252' 

@action('ctrl_act2253')
def ctrl_nm2253():
    return 'ret2253' 

@action('ctrl_act2254')
def ctrl_nm2254():
    return 'ret2254' 

@action('ctrl_act2255')
def ctrl_nm2255():
    return 'ret2255' 

@action('ctrl_act2256')
def ctrl_nm2256():
    return 'ret2256' 

@action('ctrl_act2257')
def ctrl_nm2257():
    return 'ret2257' 

@action('ctrl_act2258')
def ctrl_nm2258():
    return 'ret2258' 

@action('ctrl_act2259')
def ctrl_nm2259():
    return 'ret2259' 

@action('ctrl_act2260')
def ctrl_nm2260():
    return 'ret2260' 

@action('ctrl_act2261')
def ctrl_nm2261():
    return 'ret2261' 

@action('ctrl_act2262')
def ctrl_nm2262():
    return 'ret2262' 

@action('ctrl_act2263')
def ctrl_nm2263():
    return 'ret2263' 

@action('ctrl_act2264')
def ctrl_nm2264():
    return 'ret2264' 

@action('ctrl_act2265')
def ctrl_nm2265():
    return 'ret2265' 

@action('ctrl_act2266')
def ctrl_nm2266():
    return 'ret2266' 

@action('ctrl_act2267')
def ctrl_nm2267():
    return 'ret2267' 

@action('ctrl_act2268')
def ctrl_nm2268():
    return 'ret2268' 

@action('ctrl_act2269')
def ctrl_nm2269():
    return 'ret2269' 

@action('ctrl_act2270')
def ctrl_nm2270():
    return 'ret2270' 

@action('ctrl_act2271')
def ctrl_nm2271():
    return 'ret2271' 

@action('ctrl_act2272')
def ctrl_nm2272():
    return 'ret2272' 

@action('ctrl_act2273')
def ctrl_nm2273():
    return 'ret2273' 

@action('ctrl_act2274')
def ctrl_nm2274():
    return 'ret2274' 

@action('ctrl_act2275')
def ctrl_nm2275():
    return 'ret2275' 

@action('ctrl_act2276')
def ctrl_nm2276():
    return 'ret2276' 

@action('ctrl_act2277')
def ctrl_nm2277():
    return 'ret2277' 

@action('ctrl_act2278')
def ctrl_nm2278():
    return 'ret2278' 

@action('ctrl_act2279')
def ctrl_nm2279():
    return 'ret2279' 

@action('ctrl_act2280')
def ctrl_nm2280():
    return 'ret2280' 

@action('ctrl_act2281')
def ctrl_nm2281():
    return 'ret2281' 

@action('ctrl_act2282')
def ctrl_nm2282():
    return 'ret2282' 

@action('ctrl_act2283')
def ctrl_nm2283():
    return 'ret2283' 

@action('ctrl_act2284')
def ctrl_nm2284():
    return 'ret2284' 

@action('ctrl_act2285')
def ctrl_nm2285():
    return 'ret2285' 

@action('ctrl_act2286')
def ctrl_nm2286():
    return 'ret2286' 

@action('ctrl_act2287')
def ctrl_nm2287():
    return 'ret2287' 

@action('ctrl_act2288')
def ctrl_nm2288():
    return 'ret2288' 

@action('ctrl_act2289')
def ctrl_nm2289():
    return 'ret2289' 

@action('ctrl_act2290')
def ctrl_nm2290():
    return 'ret2290' 

@action('ctrl_act2291')
def ctrl_nm2291():
    return 'ret2291' 

@action('ctrl_act2292')
def ctrl_nm2292():
    return 'ret2292' 

@action('ctrl_act2293')
def ctrl_nm2293():
    return 'ret2293' 

@action('ctrl_act2294')
def ctrl_nm2294():
    return 'ret2294' 

@action('ctrl_act2295')
def ctrl_nm2295():
    return 'ret2295' 

@action('ctrl_act2296')
def ctrl_nm2296():
    return 'ret2296' 

@action('ctrl_act2297')
def ctrl_nm2297():
    return 'ret2297' 

@action('ctrl_act2298')
def ctrl_nm2298():
    return 'ret2298' 

@action('ctrl_act2299')
def ctrl_nm2299():
    return 'ret2299' 

@action('ctrl_act2300')
def ctrl_nm2300():
    return 'ret2300' 

@action('ctrl_act2301')
def ctrl_nm2301():
    return 'ret2301' 

@action('ctrl_act2302')
def ctrl_nm2302():
    return 'ret2302' 

@action('ctrl_act2303')
def ctrl_nm2303():
    return 'ret2303' 

@action('ctrl_act2304')
def ctrl_nm2304():
    return 'ret2304' 

@action('ctrl_act2305')
def ctrl_nm2305():
    return 'ret2305' 

@action('ctrl_act2306')
def ctrl_nm2306():
    return 'ret2306' 

@action('ctrl_act2307')
def ctrl_nm2307():
    return 'ret2307' 

@action('ctrl_act2308')
def ctrl_nm2308():
    return 'ret2308' 

@action('ctrl_act2309')
def ctrl_nm2309():
    return 'ret2309' 

@action('ctrl_act2310')
def ctrl_nm2310():
    return 'ret2310' 

@action('ctrl_act2311')
def ctrl_nm2311():
    return 'ret2311' 

@action('ctrl_act2312')
def ctrl_nm2312():
    return 'ret2312' 

@action('ctrl_act2313')
def ctrl_nm2313():
    return 'ret2313' 

@action('ctrl_act2314')
def ctrl_nm2314():
    return 'ret2314' 

@action('ctrl_act2315')
def ctrl_nm2315():
    return 'ret2315' 

@action('ctrl_act2316')
def ctrl_nm2316():
    return 'ret2316' 

@action('ctrl_act2317')
def ctrl_nm2317():
    return 'ret2317' 

@action('ctrl_act2318')
def ctrl_nm2318():
    return 'ret2318' 

@action('ctrl_act2319')
def ctrl_nm2319():
    return 'ret2319' 

@action('ctrl_act2320')
def ctrl_nm2320():
    return 'ret2320' 

@action('ctrl_act2321')
def ctrl_nm2321():
    return 'ret2321' 

@action('ctrl_act2322')
def ctrl_nm2322():
    return 'ret2322' 

@action('ctrl_act2323')
def ctrl_nm2323():
    return 'ret2323' 

@action('ctrl_act2324')
def ctrl_nm2324():
    return 'ret2324' 

@action('ctrl_act2325')
def ctrl_nm2325():
    return 'ret2325' 

@action('ctrl_act2326')
def ctrl_nm2326():
    return 'ret2326' 

@action('ctrl_act2327')
def ctrl_nm2327():
    return 'ret2327' 

@action('ctrl_act2328')
def ctrl_nm2328():
    return 'ret2328' 

@action('ctrl_act2329')
def ctrl_nm2329():
    return 'ret2329' 

@action('ctrl_act2330')
def ctrl_nm2330():
    return 'ret2330' 

@action('ctrl_act2331')
def ctrl_nm2331():
    return 'ret2331' 

@action('ctrl_act2332')
def ctrl_nm2332():
    return 'ret2332' 

@action('ctrl_act2333')
def ctrl_nm2333():
    return 'ret2333' 

@action('ctrl_act2334')
def ctrl_nm2334():
    return 'ret2334' 

@action('ctrl_act2335')
def ctrl_nm2335():
    return 'ret2335' 

@action('ctrl_act2336')
def ctrl_nm2336():
    return 'ret2336' 

@action('ctrl_act2337')
def ctrl_nm2337():
    return 'ret2337' 

@action('ctrl_act2338')
def ctrl_nm2338():
    return 'ret2338' 

@action('ctrl_act2339')
def ctrl_nm2339():
    return 'ret2339' 

@action('ctrl_act2340')
def ctrl_nm2340():
    return 'ret2340' 

@action('ctrl_act2341')
def ctrl_nm2341():
    return 'ret2341' 

@action('ctrl_act2342')
def ctrl_nm2342():
    return 'ret2342' 

@action('ctrl_act2343')
def ctrl_nm2343():
    return 'ret2343' 

@action('ctrl_act2344')
def ctrl_nm2344():
    return 'ret2344' 

@action('ctrl_act2345')
def ctrl_nm2345():
    return 'ret2345' 

@action('ctrl_act2346')
def ctrl_nm2346():
    return 'ret2346' 

@action('ctrl_act2347')
def ctrl_nm2347():
    return 'ret2347' 

@action('ctrl_act2348')
def ctrl_nm2348():
    return 'ret2348' 

@action('ctrl_act2349')
def ctrl_nm2349():
    return 'ret2349' 

@action('ctrl_act2350')
def ctrl_nm2350():
    return 'ret2350' 

@action('ctrl_act2351')
def ctrl_nm2351():
    return 'ret2351' 

@action('ctrl_act2352')
def ctrl_nm2352():
    return 'ret2352' 

@action('ctrl_act2353')
def ctrl_nm2353():
    return 'ret2353' 

@action('ctrl_act2354')
def ctrl_nm2354():
    return 'ret2354' 

@action('ctrl_act2355')
def ctrl_nm2355():
    return 'ret2355' 

@action('ctrl_act2356')
def ctrl_nm2356():
    return 'ret2356' 

@action('ctrl_act2357')
def ctrl_nm2357():
    return 'ret2357' 

@action('ctrl_act2358')
def ctrl_nm2358():
    return 'ret2358' 

@action('ctrl_act2359')
def ctrl_nm2359():
    return 'ret2359' 

@action('ctrl_act2360')
def ctrl_nm2360():
    return 'ret2360' 

@action('ctrl_act2361')
def ctrl_nm2361():
    return 'ret2361' 

@action('ctrl_act2362')
def ctrl_nm2362():
    return 'ret2362' 

@action('ctrl_act2363')
def ctrl_nm2363():
    return 'ret2363' 

@action('ctrl_act2364')
def ctrl_nm2364():
    return 'ret2364' 

@action('ctrl_act2365')
def ctrl_nm2365():
    return 'ret2365' 

@action('ctrl_act2366')
def ctrl_nm2366():
    return 'ret2366' 

@action('ctrl_act2367')
def ctrl_nm2367():
    return 'ret2367' 

@action('ctrl_act2368')
def ctrl_nm2368():
    return 'ret2368' 

@action('ctrl_act2369')
def ctrl_nm2369():
    return 'ret2369' 

@action('ctrl_act2370')
def ctrl_nm2370():
    return 'ret2370' 

@action('ctrl_act2371')
def ctrl_nm2371():
    return 'ret2371' 

@action('ctrl_act2372')
def ctrl_nm2372():
    return 'ret2372' 

@action('ctrl_act2373')
def ctrl_nm2373():
    return 'ret2373' 

@action('ctrl_act2374')
def ctrl_nm2374():
    return 'ret2374' 

@action('ctrl_act2375')
def ctrl_nm2375():
    return 'ret2375' 

@action('ctrl_act2376')
def ctrl_nm2376():
    return 'ret2376' 

@action('ctrl_act2377')
def ctrl_nm2377():
    return 'ret2377' 

@action('ctrl_act2378')
def ctrl_nm2378():
    return 'ret2378' 

@action('ctrl_act2379')
def ctrl_nm2379():
    return 'ret2379' 

@action('ctrl_act2380')
def ctrl_nm2380():
    return 'ret2380' 

@action('ctrl_act2381')
def ctrl_nm2381():
    return 'ret2381' 

@action('ctrl_act2382')
def ctrl_nm2382():
    return 'ret2382' 

@action('ctrl_act2383')
def ctrl_nm2383():
    return 'ret2383' 

@action('ctrl_act2384')
def ctrl_nm2384():
    return 'ret2384' 

@action('ctrl_act2385')
def ctrl_nm2385():
    return 'ret2385' 

@action('ctrl_act2386')
def ctrl_nm2386():
    return 'ret2386' 

@action('ctrl_act2387')
def ctrl_nm2387():
    return 'ret2387' 

@action('ctrl_act2388')
def ctrl_nm2388():
    return 'ret2388' 

@action('ctrl_act2389')
def ctrl_nm2389():
    return 'ret2389' 

@action('ctrl_act2390')
def ctrl_nm2390():
    return 'ret2390' 

@action('ctrl_act2391')
def ctrl_nm2391():
    return 'ret2391' 

@action('ctrl_act2392')
def ctrl_nm2392():
    return 'ret2392' 

@action('ctrl_act2393')
def ctrl_nm2393():
    return 'ret2393' 

@action('ctrl_act2394')
def ctrl_nm2394():
    return 'ret2394' 

@action('ctrl_act2395')
def ctrl_nm2395():
    return 'ret2395' 

@action('ctrl_act2396')
def ctrl_nm2396():
    return 'ret2396' 

@action('ctrl_act2397')
def ctrl_nm2397():
    return 'ret2397' 

@action('ctrl_act2398')
def ctrl_nm2398():
    return 'ret2398' 

@action('ctrl_act2399')
def ctrl_nm2399():
    return 'ret2399' 

@action('ctrl_act2400')
def ctrl_nm2400():
    return 'ret2400' 

@action('ctrl_act2401')
def ctrl_nm2401():
    return 'ret2401' 

@action('ctrl_act2402')
def ctrl_nm2402():
    return 'ret2402' 

@action('ctrl_act2403')
def ctrl_nm2403():
    return 'ret2403' 

@action('ctrl_act2404')
def ctrl_nm2404():
    return 'ret2404' 

@action('ctrl_act2405')
def ctrl_nm2405():
    return 'ret2405' 

@action('ctrl_act2406')
def ctrl_nm2406():
    return 'ret2406' 

@action('ctrl_act2407')
def ctrl_nm2407():
    return 'ret2407' 

@action('ctrl_act2408')
def ctrl_nm2408():
    return 'ret2408' 

@action('ctrl_act2409')
def ctrl_nm2409():
    return 'ret2409' 

@action('ctrl_act2410')
def ctrl_nm2410():
    return 'ret2410' 

@action('ctrl_act2411')
def ctrl_nm2411():
    return 'ret2411' 

@action('ctrl_act2412')
def ctrl_nm2412():
    return 'ret2412' 

@action('ctrl_act2413')
def ctrl_nm2413():
    return 'ret2413' 

@action('ctrl_act2414')
def ctrl_nm2414():
    return 'ret2414' 

@action('ctrl_act2415')
def ctrl_nm2415():
    return 'ret2415' 

@action('ctrl_act2416')
def ctrl_nm2416():
    return 'ret2416' 

@action('ctrl_act2417')
def ctrl_nm2417():
    return 'ret2417' 

@action('ctrl_act2418')
def ctrl_nm2418():
    return 'ret2418' 

@action('ctrl_act2419')
def ctrl_nm2419():
    return 'ret2419' 

@action('ctrl_act2420')
def ctrl_nm2420():
    return 'ret2420' 

@action('ctrl_act2421')
def ctrl_nm2421():
    return 'ret2421' 

@action('ctrl_act2422')
def ctrl_nm2422():
    return 'ret2422' 

@action('ctrl_act2423')
def ctrl_nm2423():
    return 'ret2423' 

@action('ctrl_act2424')
def ctrl_nm2424():
    return 'ret2424' 

@action('ctrl_act2425')
def ctrl_nm2425():
    return 'ret2425' 

@action('ctrl_act2426')
def ctrl_nm2426():
    return 'ret2426' 

@action('ctrl_act2427')
def ctrl_nm2427():
    return 'ret2427' 

@action('ctrl_act2428')
def ctrl_nm2428():
    return 'ret2428' 

@action('ctrl_act2429')
def ctrl_nm2429():
    return 'ret2429' 

@action('ctrl_act2430')
def ctrl_nm2430():
    return 'ret2430' 

@action('ctrl_act2431')
def ctrl_nm2431():
    return 'ret2431' 

@action('ctrl_act2432')
def ctrl_nm2432():
    return 'ret2432' 

@action('ctrl_act2433')
def ctrl_nm2433():
    return 'ret2433' 

@action('ctrl_act2434')
def ctrl_nm2434():
    return 'ret2434' 

@action('ctrl_act2435')
def ctrl_nm2435():
    return 'ret2435' 

@action('ctrl_act2436')
def ctrl_nm2436():
    return 'ret2436' 

@action('ctrl_act2437')
def ctrl_nm2437():
    return 'ret2437' 

@action('ctrl_act2438')
def ctrl_nm2438():
    return 'ret2438' 

@action('ctrl_act2439')
def ctrl_nm2439():
    return 'ret2439' 

@action('ctrl_act2440')
def ctrl_nm2440():
    return 'ret2440' 

@action('ctrl_act2441')
def ctrl_nm2441():
    return 'ret2441' 

@action('ctrl_act2442')
def ctrl_nm2442():
    return 'ret2442' 

@action('ctrl_act2443')
def ctrl_nm2443():
    return 'ret2443' 

@action('ctrl_act2444')
def ctrl_nm2444():
    return 'ret2444' 

@action('ctrl_act2445')
def ctrl_nm2445():
    return 'ret2445' 

@action('ctrl_act2446')
def ctrl_nm2446():
    return 'ret2446' 

@action('ctrl_act2447')
def ctrl_nm2447():
    return 'ret2447' 

@action('ctrl_act2448')
def ctrl_nm2448():
    return 'ret2448' 

@action('ctrl_act2449')
def ctrl_nm2449():
    return 'ret2449' 

@action('ctrl_act2450')
def ctrl_nm2450():
    return 'ret2450' 

@action('ctrl_act2451')
def ctrl_nm2451():
    return 'ret2451' 

@action('ctrl_act2452')
def ctrl_nm2452():
    return 'ret2452' 

@action('ctrl_act2453')
def ctrl_nm2453():
    return 'ret2453' 

@action('ctrl_act2454')
def ctrl_nm2454():
    return 'ret2454' 

@action('ctrl_act2455')
def ctrl_nm2455():
    return 'ret2455' 

@action('ctrl_act2456')
def ctrl_nm2456():
    return 'ret2456' 

@action('ctrl_act2457')
def ctrl_nm2457():
    return 'ret2457' 

@action('ctrl_act2458')
def ctrl_nm2458():
    return 'ret2458' 

@action('ctrl_act2459')
def ctrl_nm2459():
    return 'ret2459' 

@action('ctrl_act2460')
def ctrl_nm2460():
    return 'ret2460' 

@action('ctrl_act2461')
def ctrl_nm2461():
    return 'ret2461' 

@action('ctrl_act2462')
def ctrl_nm2462():
    return 'ret2462' 

@action('ctrl_act2463')
def ctrl_nm2463():
    return 'ret2463' 

@action('ctrl_act2464')
def ctrl_nm2464():
    return 'ret2464' 

@action('ctrl_act2465')
def ctrl_nm2465():
    return 'ret2465' 

@action('ctrl_act2466')
def ctrl_nm2466():
    return 'ret2466' 

@action('ctrl_act2467')
def ctrl_nm2467():
    return 'ret2467' 

@action('ctrl_act2468')
def ctrl_nm2468():
    return 'ret2468' 

@action('ctrl_act2469')
def ctrl_nm2469():
    return 'ret2469' 

@action('ctrl_act2470')
def ctrl_nm2470():
    return 'ret2470' 

@action('ctrl_act2471')
def ctrl_nm2471():
    return 'ret2471' 

@action('ctrl_act2472')
def ctrl_nm2472():
    return 'ret2472' 

@action('ctrl_act2473')
def ctrl_nm2473():
    return 'ret2473' 

@action('ctrl_act2474')
def ctrl_nm2474():
    return 'ret2474' 

@action('ctrl_act2475')
def ctrl_nm2475():
    return 'ret2475' 

@action('ctrl_act2476')
def ctrl_nm2476():
    return 'ret2476' 

@action('ctrl_act2477')
def ctrl_nm2477():
    return 'ret2477' 

@action('ctrl_act2478')
def ctrl_nm2478():
    return 'ret2478' 

@action('ctrl_act2479')
def ctrl_nm2479():
    return 'ret2479' 

@action('ctrl_act2480')
def ctrl_nm2480():
    return 'ret2480' 

@action('ctrl_act2481')
def ctrl_nm2481():
    return 'ret2481' 

@action('ctrl_act2482')
def ctrl_nm2482():
    return 'ret2482' 

@action('ctrl_act2483')
def ctrl_nm2483():
    return 'ret2483' 

@action('ctrl_act2484')
def ctrl_nm2484():
    return 'ret2484' 

@action('ctrl_act2485')
def ctrl_nm2485():
    return 'ret2485' 

@action('ctrl_act2486')
def ctrl_nm2486():
    return 'ret2486' 

@action('ctrl_act2487')
def ctrl_nm2487():
    return 'ret2487' 

@action('ctrl_act2488')
def ctrl_nm2488():
    return 'ret2488' 

@action('ctrl_act2489')
def ctrl_nm2489():
    return 'ret2489' 

@action('ctrl_act2490')
def ctrl_nm2490():
    return 'ret2490' 

@action('ctrl_act2491')
def ctrl_nm2491():
    return 'ret2491' 

@action('ctrl_act2492')
def ctrl_nm2492():
    return 'ret2492' 

@action('ctrl_act2493')
def ctrl_nm2493():
    return 'ret2493' 

@action('ctrl_act2494')
def ctrl_nm2494():
    return 'ret2494' 

@action('ctrl_act2495')
def ctrl_nm2495():
    return 'ret2495' 

@action('ctrl_act2496')
def ctrl_nm2496():
    return 'ret2496' 

@action('ctrl_act2497')
def ctrl_nm2497():
    return 'ret2497' 

@action('ctrl_act2498')
def ctrl_nm2498():
    return 'ret2498' 

@action('ctrl_act2499')
def ctrl_nm2499():
    return 'ret2499' 

@action('ctrl_act2500')
def ctrl_nm2500():
    return 'ret2500' 

@action('ctrl_act2501')
def ctrl_nm2501():
    return 'ret2501' 

@action('ctrl_act2502')
def ctrl_nm2502():
    return 'ret2502' 

@action('ctrl_act2503')
def ctrl_nm2503():
    return 'ret2503' 

@action('ctrl_act2504')
def ctrl_nm2504():
    return 'ret2504' 

@action('ctrl_act2505')
def ctrl_nm2505():
    return 'ret2505' 

@action('ctrl_act2506')
def ctrl_nm2506():
    return 'ret2506' 

@action('ctrl_act2507')
def ctrl_nm2507():
    return 'ret2507' 

@action('ctrl_act2508')
def ctrl_nm2508():
    return 'ret2508' 

@action('ctrl_act2509')
def ctrl_nm2509():
    return 'ret2509' 

@action('ctrl_act2510')
def ctrl_nm2510():
    return 'ret2510' 

@action('ctrl_act2511')
def ctrl_nm2511():
    return 'ret2511' 

@action('ctrl_act2512')
def ctrl_nm2512():
    return 'ret2512' 

@action('ctrl_act2513')
def ctrl_nm2513():
    return 'ret2513' 

@action('ctrl_act2514')
def ctrl_nm2514():
    return 'ret2514' 

@action('ctrl_act2515')
def ctrl_nm2515():
    return 'ret2515' 

@action('ctrl_act2516')
def ctrl_nm2516():
    return 'ret2516' 

@action('ctrl_act2517')
def ctrl_nm2517():
    return 'ret2517' 

@action('ctrl_act2518')
def ctrl_nm2518():
    return 'ret2518' 

@action('ctrl_act2519')
def ctrl_nm2519():
    return 'ret2519' 

@action('ctrl_act2520')
def ctrl_nm2520():
    return 'ret2520' 

@action('ctrl_act2521')
def ctrl_nm2521():
    return 'ret2521' 

@action('ctrl_act2522')
def ctrl_nm2522():
    return 'ret2522' 

@action('ctrl_act2523')
def ctrl_nm2523():
    return 'ret2523' 

@action('ctrl_act2524')
def ctrl_nm2524():
    return 'ret2524' 

@action('ctrl_act2525')
def ctrl_nm2525():
    return 'ret2525' 

@action('ctrl_act2526')
def ctrl_nm2526():
    return 'ret2526' 

@action('ctrl_act2527')
def ctrl_nm2527():
    return 'ret2527' 

@action('ctrl_act2528')
def ctrl_nm2528():
    return 'ret2528' 

@action('ctrl_act2529')
def ctrl_nm2529():
    return 'ret2529' 

@action('ctrl_act2530')
def ctrl_nm2530():
    return 'ret2530' 

@action('ctrl_act2531')
def ctrl_nm2531():
    return 'ret2531' 

@action('ctrl_act2532')
def ctrl_nm2532():
    return 'ret2532' 

@action('ctrl_act2533')
def ctrl_nm2533():
    return 'ret2533' 

@action('ctrl_act2534')
def ctrl_nm2534():
    return 'ret2534' 

@action('ctrl_act2535')
def ctrl_nm2535():
    return 'ret2535' 

@action('ctrl_act2536')
def ctrl_nm2536():
    return 'ret2536' 

@action('ctrl_act2537')
def ctrl_nm2537():
    return 'ret2537' 

@action('ctrl_act2538')
def ctrl_nm2538():
    return 'ret2538' 

@action('ctrl_act2539')
def ctrl_nm2539():
    return 'ret2539' 

@action('ctrl_act2540')
def ctrl_nm2540():
    return 'ret2540' 

@action('ctrl_act2541')
def ctrl_nm2541():
    return 'ret2541' 

@action('ctrl_act2542')
def ctrl_nm2542():
    return 'ret2542' 

@action('ctrl_act2543')
def ctrl_nm2543():
    return 'ret2543' 

@action('ctrl_act2544')
def ctrl_nm2544():
    return 'ret2544' 

@action('ctrl_act2545')
def ctrl_nm2545():
    return 'ret2545' 

@action('ctrl_act2546')
def ctrl_nm2546():
    return 'ret2546' 

@action('ctrl_act2547')
def ctrl_nm2547():
    return 'ret2547' 

@action('ctrl_act2548')
def ctrl_nm2548():
    return 'ret2548' 

@action('ctrl_act2549')
def ctrl_nm2549():
    return 'ret2549' 

@action('ctrl_act2550')
def ctrl_nm2550():
    return 'ret2550' 

@action('ctrl_act2551')
def ctrl_nm2551():
    return 'ret2551' 

@action('ctrl_act2552')
def ctrl_nm2552():
    return 'ret2552' 

@action('ctrl_act2553')
def ctrl_nm2553():
    return 'ret2553' 

@action('ctrl_act2554')
def ctrl_nm2554():
    return 'ret2554' 

@action('ctrl_act2555')
def ctrl_nm2555():
    return 'ret2555' 

@action('ctrl_act2556')
def ctrl_nm2556():
    return 'ret2556' 

@action('ctrl_act2557')
def ctrl_nm2557():
    return 'ret2557' 

@action('ctrl_act2558')
def ctrl_nm2558():
    return 'ret2558' 

@action('ctrl_act2559')
def ctrl_nm2559():
    return 'ret2559' 

@action('ctrl_act2560')
def ctrl_nm2560():
    return 'ret2560' 

@action('ctrl_act2561')
def ctrl_nm2561():
    return 'ret2561' 

@action('ctrl_act2562')
def ctrl_nm2562():
    return 'ret2562' 

@action('ctrl_act2563')
def ctrl_nm2563():
    return 'ret2563' 

@action('ctrl_act2564')
def ctrl_nm2564():
    return 'ret2564' 

@action('ctrl_act2565')
def ctrl_nm2565():
    return 'ret2565' 

@action('ctrl_act2566')
def ctrl_nm2566():
    return 'ret2566' 

@action('ctrl_act2567')
def ctrl_nm2567():
    return 'ret2567' 

@action('ctrl_act2568')
def ctrl_nm2568():
    return 'ret2568' 

@action('ctrl_act2569')
def ctrl_nm2569():
    return 'ret2569' 

@action('ctrl_act2570')
def ctrl_nm2570():
    return 'ret2570' 

@action('ctrl_act2571')
def ctrl_nm2571():
    return 'ret2571' 

@action('ctrl_act2572')
def ctrl_nm2572():
    return 'ret2572' 

@action('ctrl_act2573')
def ctrl_nm2573():
    return 'ret2573' 

@action('ctrl_act2574')
def ctrl_nm2574():
    return 'ret2574' 

@action('ctrl_act2575')
def ctrl_nm2575():
    return 'ret2575' 

@action('ctrl_act2576')
def ctrl_nm2576():
    return 'ret2576' 

@action('ctrl_act2577')
def ctrl_nm2577():
    return 'ret2577' 

@action('ctrl_act2578')
def ctrl_nm2578():
    return 'ret2578' 

@action('ctrl_act2579')
def ctrl_nm2579():
    return 'ret2579' 

@action('ctrl_act2580')
def ctrl_nm2580():
    return 'ret2580' 

@action('ctrl_act2581')
def ctrl_nm2581():
    return 'ret2581' 

@action('ctrl_act2582')
def ctrl_nm2582():
    return 'ret2582' 

@action('ctrl_act2583')
def ctrl_nm2583():
    return 'ret2583' 

@action('ctrl_act2584')
def ctrl_nm2584():
    return 'ret2584' 

@action('ctrl_act2585')
def ctrl_nm2585():
    return 'ret2585' 

@action('ctrl_act2586')
def ctrl_nm2586():
    return 'ret2586' 

@action('ctrl_act2587')
def ctrl_nm2587():
    return 'ret2587' 

@action('ctrl_act2588')
def ctrl_nm2588():
    return 'ret2588' 

@action('ctrl_act2589')
def ctrl_nm2589():
    return 'ret2589' 

@action('ctrl_act2590')
def ctrl_nm2590():
    return 'ret2590' 

@action('ctrl_act2591')
def ctrl_nm2591():
    return 'ret2591' 

@action('ctrl_act2592')
def ctrl_nm2592():
    return 'ret2592' 

@action('ctrl_act2593')
def ctrl_nm2593():
    return 'ret2593' 

@action('ctrl_act2594')
def ctrl_nm2594():
    return 'ret2594' 

@action('ctrl_act2595')
def ctrl_nm2595():
    return 'ret2595' 

@action('ctrl_act2596')
def ctrl_nm2596():
    return 'ret2596' 

@action('ctrl_act2597')
def ctrl_nm2597():
    return 'ret2597' 

@action('ctrl_act2598')
def ctrl_nm2598():
    return 'ret2598' 

@action('ctrl_act2599')
def ctrl_nm2599():
    return 'ret2599' 

@action('ctrl_act2600')
def ctrl_nm2600():
    return 'ret2600' 

@action('ctrl_act2601')
def ctrl_nm2601():
    return 'ret2601' 

@action('ctrl_act2602')
def ctrl_nm2602():
    return 'ret2602' 

@action('ctrl_act2603')
def ctrl_nm2603():
    return 'ret2603' 

@action('ctrl_act2604')
def ctrl_nm2604():
    return 'ret2604' 

@action('ctrl_act2605')
def ctrl_nm2605():
    return 'ret2605' 

@action('ctrl_act2606')
def ctrl_nm2606():
    return 'ret2606' 

@action('ctrl_act2607')
def ctrl_nm2607():
    return 'ret2607' 

@action('ctrl_act2608')
def ctrl_nm2608():
    return 'ret2608' 

@action('ctrl_act2609')
def ctrl_nm2609():
    return 'ret2609' 

@action('ctrl_act2610')
def ctrl_nm2610():
    return 'ret2610' 

@action('ctrl_act2611')
def ctrl_nm2611():
    return 'ret2611' 

@action('ctrl_act2612')
def ctrl_nm2612():
    return 'ret2612' 

@action('ctrl_act2613')
def ctrl_nm2613():
    return 'ret2613' 

@action('ctrl_act2614')
def ctrl_nm2614():
    return 'ret2614' 

@action('ctrl_act2615')
def ctrl_nm2615():
    return 'ret2615' 

@action('ctrl_act2616')
def ctrl_nm2616():
    return 'ret2616' 

@action('ctrl_act2617')
def ctrl_nm2617():
    return 'ret2617' 

@action('ctrl_act2618')
def ctrl_nm2618():
    return 'ret2618' 

@action('ctrl_act2619')
def ctrl_nm2619():
    return 'ret2619' 

@action('ctrl_act2620')
def ctrl_nm2620():
    return 'ret2620' 

@action('ctrl_act2621')
def ctrl_nm2621():
    return 'ret2621' 

@action('ctrl_act2622')
def ctrl_nm2622():
    return 'ret2622' 

@action('ctrl_act2623')
def ctrl_nm2623():
    return 'ret2623' 

@action('ctrl_act2624')
def ctrl_nm2624():
    return 'ret2624' 

@action('ctrl_act2625')
def ctrl_nm2625():
    return 'ret2625' 

@action('ctrl_act2626')
def ctrl_nm2626():
    return 'ret2626' 

@action('ctrl_act2627')
def ctrl_nm2627():
    return 'ret2627' 

@action('ctrl_act2628')
def ctrl_nm2628():
    return 'ret2628' 

@action('ctrl_act2629')
def ctrl_nm2629():
    return 'ret2629' 

@action('ctrl_act2630')
def ctrl_nm2630():
    return 'ret2630' 

@action('ctrl_act2631')
def ctrl_nm2631():
    return 'ret2631' 

@action('ctrl_act2632')
def ctrl_nm2632():
    return 'ret2632' 

@action('ctrl_act2633')
def ctrl_nm2633():
    return 'ret2633' 

@action('ctrl_act2634')
def ctrl_nm2634():
    return 'ret2634' 

@action('ctrl_act2635')
def ctrl_nm2635():
    return 'ret2635' 

@action('ctrl_act2636')
def ctrl_nm2636():
    return 'ret2636' 

@action('ctrl_act2637')
def ctrl_nm2637():
    return 'ret2637' 

@action('ctrl_act2638')
def ctrl_nm2638():
    return 'ret2638' 

@action('ctrl_act2639')
def ctrl_nm2639():
    return 'ret2639' 

@action('ctrl_act2640')
def ctrl_nm2640():
    return 'ret2640' 

@action('ctrl_act2641')
def ctrl_nm2641():
    return 'ret2641' 

@action('ctrl_act2642')
def ctrl_nm2642():
    return 'ret2642' 

@action('ctrl_act2643')
def ctrl_nm2643():
    return 'ret2643' 

@action('ctrl_act2644')
def ctrl_nm2644():
    return 'ret2644' 

@action('ctrl_act2645')
def ctrl_nm2645():
    return 'ret2645' 

@action('ctrl_act2646')
def ctrl_nm2646():
    return 'ret2646' 

@action('ctrl_act2647')
def ctrl_nm2647():
    return 'ret2647' 

@action('ctrl_act2648')
def ctrl_nm2648():
    return 'ret2648' 

@action('ctrl_act2649')
def ctrl_nm2649():
    return 'ret2649' 

@action('ctrl_act2650')
def ctrl_nm2650():
    return 'ret2650' 

@action('ctrl_act2651')
def ctrl_nm2651():
    return 'ret2651' 

@action('ctrl_act2652')
def ctrl_nm2652():
    return 'ret2652' 

@action('ctrl_act2653')
def ctrl_nm2653():
    return 'ret2653' 

@action('ctrl_act2654')
def ctrl_nm2654():
    return 'ret2654' 

@action('ctrl_act2655')
def ctrl_nm2655():
    return 'ret2655' 

@action('ctrl_act2656')
def ctrl_nm2656():
    return 'ret2656' 

@action('ctrl_act2657')
def ctrl_nm2657():
    return 'ret2657' 

@action('ctrl_act2658')
def ctrl_nm2658():
    return 'ret2658' 

@action('ctrl_act2659')
def ctrl_nm2659():
    return 'ret2659' 

@action('ctrl_act2660')
def ctrl_nm2660():
    return 'ret2660' 

@action('ctrl_act2661')
def ctrl_nm2661():
    return 'ret2661' 

@action('ctrl_act2662')
def ctrl_nm2662():
    return 'ret2662' 

@action('ctrl_act2663')
def ctrl_nm2663():
    return 'ret2663' 

@action('ctrl_act2664')
def ctrl_nm2664():
    return 'ret2664' 

@action('ctrl_act2665')
def ctrl_nm2665():
    return 'ret2665' 

@action('ctrl_act2666')
def ctrl_nm2666():
    return 'ret2666' 

@action('ctrl_act2667')
def ctrl_nm2667():
    return 'ret2667' 

@action('ctrl_act2668')
def ctrl_nm2668():
    return 'ret2668' 

@action('ctrl_act2669')
def ctrl_nm2669():
    return 'ret2669' 

@action('ctrl_act2670')
def ctrl_nm2670():
    return 'ret2670' 

@action('ctrl_act2671')
def ctrl_nm2671():
    return 'ret2671' 

@action('ctrl_act2672')
def ctrl_nm2672():
    return 'ret2672' 

@action('ctrl_act2673')
def ctrl_nm2673():
    return 'ret2673' 

@action('ctrl_act2674')
def ctrl_nm2674():
    return 'ret2674' 

@action('ctrl_act2675')
def ctrl_nm2675():
    return 'ret2675' 

@action('ctrl_act2676')
def ctrl_nm2676():
    return 'ret2676' 

@action('ctrl_act2677')
def ctrl_nm2677():
    return 'ret2677' 

@action('ctrl_act2678')
def ctrl_nm2678():
    return 'ret2678' 

@action('ctrl_act2679')
def ctrl_nm2679():
    return 'ret2679' 

@action('ctrl_act2680')
def ctrl_nm2680():
    return 'ret2680' 

@action('ctrl_act2681')
def ctrl_nm2681():
    return 'ret2681' 

@action('ctrl_act2682')
def ctrl_nm2682():
    return 'ret2682' 

@action('ctrl_act2683')
def ctrl_nm2683():
    return 'ret2683' 

@action('ctrl_act2684')
def ctrl_nm2684():
    return 'ret2684' 

@action('ctrl_act2685')
def ctrl_nm2685():
    return 'ret2685' 

@action('ctrl_act2686')
def ctrl_nm2686():
    return 'ret2686' 

@action('ctrl_act2687')
def ctrl_nm2687():
    return 'ret2687' 

@action('ctrl_act2688')
def ctrl_nm2688():
    return 'ret2688' 

@action('ctrl_act2689')
def ctrl_nm2689():
    return 'ret2689' 

@action('ctrl_act2690')
def ctrl_nm2690():
    return 'ret2690' 

@action('ctrl_act2691')
def ctrl_nm2691():
    return 'ret2691' 

@action('ctrl_act2692')
def ctrl_nm2692():
    return 'ret2692' 

@action('ctrl_act2693')
def ctrl_nm2693():
    return 'ret2693' 

@action('ctrl_act2694')
def ctrl_nm2694():
    return 'ret2694' 

@action('ctrl_act2695')
def ctrl_nm2695():
    return 'ret2695' 

@action('ctrl_act2696')
def ctrl_nm2696():
    return 'ret2696' 

@action('ctrl_act2697')
def ctrl_nm2697():
    return 'ret2697' 

@action('ctrl_act2698')
def ctrl_nm2698():
    return 'ret2698' 

@action('ctrl_act2699')
def ctrl_nm2699():
    return 'ret2699' 

@action('ctrl_act2700')
def ctrl_nm2700():
    return 'ret2700' 

@action('ctrl_act2701')
def ctrl_nm2701():
    return 'ret2701' 

@action('ctrl_act2702')
def ctrl_nm2702():
    return 'ret2702' 

@action('ctrl_act2703')
def ctrl_nm2703():
    return 'ret2703' 

@action('ctrl_act2704')
def ctrl_nm2704():
    return 'ret2704' 

@action('ctrl_act2705')
def ctrl_nm2705():
    return 'ret2705' 

@action('ctrl_act2706')
def ctrl_nm2706():
    return 'ret2706' 

@action('ctrl_act2707')
def ctrl_nm2707():
    return 'ret2707' 

@action('ctrl_act2708')
def ctrl_nm2708():
    return 'ret2708' 

@action('ctrl_act2709')
def ctrl_nm2709():
    return 'ret2709' 

@action('ctrl_act2710')
def ctrl_nm2710():
    return 'ret2710' 

@action('ctrl_act2711')
def ctrl_nm2711():
    return 'ret2711' 

@action('ctrl_act2712')
def ctrl_nm2712():
    return 'ret2712' 

@action('ctrl_act2713')
def ctrl_nm2713():
    return 'ret2713' 

@action('ctrl_act2714')
def ctrl_nm2714():
    return 'ret2714' 

@action('ctrl_act2715')
def ctrl_nm2715():
    return 'ret2715' 

@action('ctrl_act2716')
def ctrl_nm2716():
    return 'ret2716' 

@action('ctrl_act2717')
def ctrl_nm2717():
    return 'ret2717' 

@action('ctrl_act2718')
def ctrl_nm2718():
    return 'ret2718' 

@action('ctrl_act2719')
def ctrl_nm2719():
    return 'ret2719' 

@action('ctrl_act2720')
def ctrl_nm2720():
    return 'ret2720' 

@action('ctrl_act2721')
def ctrl_nm2721():
    return 'ret2721' 

@action('ctrl_act2722')
def ctrl_nm2722():
    return 'ret2722' 

@action('ctrl_act2723')
def ctrl_nm2723():
    return 'ret2723' 

@action('ctrl_act2724')
def ctrl_nm2724():
    return 'ret2724' 

@action('ctrl_act2725')
def ctrl_nm2725():
    return 'ret2725' 

@action('ctrl_act2726')
def ctrl_nm2726():
    return 'ret2726' 

@action('ctrl_act2727')
def ctrl_nm2727():
    return 'ret2727' 

@action('ctrl_act2728')
def ctrl_nm2728():
    return 'ret2728' 

@action('ctrl_act2729')
def ctrl_nm2729():
    return 'ret2729' 

@action('ctrl_act2730')
def ctrl_nm2730():
    return 'ret2730' 

@action('ctrl_act2731')
def ctrl_nm2731():
    return 'ret2731' 

@action('ctrl_act2732')
def ctrl_nm2732():
    return 'ret2732' 

@action('ctrl_act2733')
def ctrl_nm2733():
    return 'ret2733' 

@action('ctrl_act2734')
def ctrl_nm2734():
    return 'ret2734' 

@action('ctrl_act2735')
def ctrl_nm2735():
    return 'ret2735' 

@action('ctrl_act2736')
def ctrl_nm2736():
    return 'ret2736' 

@action('ctrl_act2737')
def ctrl_nm2737():
    return 'ret2737' 

@action('ctrl_act2738')
def ctrl_nm2738():
    return 'ret2738' 

@action('ctrl_act2739')
def ctrl_nm2739():
    return 'ret2739' 

@action('ctrl_act2740')
def ctrl_nm2740():
    return 'ret2740' 

@action('ctrl_act2741')
def ctrl_nm2741():
    return 'ret2741' 

@action('ctrl_act2742')
def ctrl_nm2742():
    return 'ret2742' 

@action('ctrl_act2743')
def ctrl_nm2743():
    return 'ret2743' 

@action('ctrl_act2744')
def ctrl_nm2744():
    return 'ret2744' 

@action('ctrl_act2745')
def ctrl_nm2745():
    return 'ret2745' 

@action('ctrl_act2746')
def ctrl_nm2746():
    return 'ret2746' 

@action('ctrl_act2747')
def ctrl_nm2747():
    return 'ret2747' 

@action('ctrl_act2748')
def ctrl_nm2748():
    return 'ret2748' 

@action('ctrl_act2749')
def ctrl_nm2749():
    return 'ret2749' 

@action('ctrl_act2750')
def ctrl_nm2750():
    return 'ret2750' 

@action('ctrl_act2751')
def ctrl_nm2751():
    return 'ret2751' 

@action('ctrl_act2752')
def ctrl_nm2752():
    return 'ret2752' 

@action('ctrl_act2753')
def ctrl_nm2753():
    return 'ret2753' 

@action('ctrl_act2754')
def ctrl_nm2754():
    return 'ret2754' 

@action('ctrl_act2755')
def ctrl_nm2755():
    return 'ret2755' 

@action('ctrl_act2756')
def ctrl_nm2756():
    return 'ret2756' 

@action('ctrl_act2757')
def ctrl_nm2757():
    return 'ret2757' 

@action('ctrl_act2758')
def ctrl_nm2758():
    return 'ret2758' 

@action('ctrl_act2759')
def ctrl_nm2759():
    return 'ret2759' 

@action('ctrl_act2760')
def ctrl_nm2760():
    return 'ret2760' 

@action('ctrl_act2761')
def ctrl_nm2761():
    return 'ret2761' 

@action('ctrl_act2762')
def ctrl_nm2762():
    return 'ret2762' 

@action('ctrl_act2763')
def ctrl_nm2763():
    return 'ret2763' 

@action('ctrl_act2764')
def ctrl_nm2764():
    return 'ret2764' 

@action('ctrl_act2765')
def ctrl_nm2765():
    return 'ret2765' 

@action('ctrl_act2766')
def ctrl_nm2766():
    return 'ret2766' 

@action('ctrl_act2767')
def ctrl_nm2767():
    return 'ret2767' 

@action('ctrl_act2768')
def ctrl_nm2768():
    return 'ret2768' 

@action('ctrl_act2769')
def ctrl_nm2769():
    return 'ret2769' 

@action('ctrl_act2770')
def ctrl_nm2770():
    return 'ret2770' 

@action('ctrl_act2771')
def ctrl_nm2771():
    return 'ret2771' 

@action('ctrl_act2772')
def ctrl_nm2772():
    return 'ret2772' 

@action('ctrl_act2773')
def ctrl_nm2773():
    return 'ret2773' 

@action('ctrl_act2774')
def ctrl_nm2774():
    return 'ret2774' 

@action('ctrl_act2775')
def ctrl_nm2775():
    return 'ret2775' 

@action('ctrl_act2776')
def ctrl_nm2776():
    return 'ret2776' 

@action('ctrl_act2777')
def ctrl_nm2777():
    return 'ret2777' 

@action('ctrl_act2778')
def ctrl_nm2778():
    return 'ret2778' 

@action('ctrl_act2779')
def ctrl_nm2779():
    return 'ret2779' 

@action('ctrl_act2780')
def ctrl_nm2780():
    return 'ret2780' 

@action('ctrl_act2781')
def ctrl_nm2781():
    return 'ret2781' 

@action('ctrl_act2782')
def ctrl_nm2782():
    return 'ret2782' 

@action('ctrl_act2783')
def ctrl_nm2783():
    return 'ret2783' 

@action('ctrl_act2784')
def ctrl_nm2784():
    return 'ret2784' 

@action('ctrl_act2785')
def ctrl_nm2785():
    return 'ret2785' 

@action('ctrl_act2786')
def ctrl_nm2786():
    return 'ret2786' 

@action('ctrl_act2787')
def ctrl_nm2787():
    return 'ret2787' 

@action('ctrl_act2788')
def ctrl_nm2788():
    return 'ret2788' 

@action('ctrl_act2789')
def ctrl_nm2789():
    return 'ret2789' 

@action('ctrl_act2790')
def ctrl_nm2790():
    return 'ret2790' 

@action('ctrl_act2791')
def ctrl_nm2791():
    return 'ret2791' 

@action('ctrl_act2792')
def ctrl_nm2792():
    return 'ret2792' 

@action('ctrl_act2793')
def ctrl_nm2793():
    return 'ret2793' 

@action('ctrl_act2794')
def ctrl_nm2794():
    return 'ret2794' 

@action('ctrl_act2795')
def ctrl_nm2795():
    return 'ret2795' 

@action('ctrl_act2796')
def ctrl_nm2796():
    return 'ret2796' 

@action('ctrl_act2797')
def ctrl_nm2797():
    return 'ret2797' 

@action('ctrl_act2798')
def ctrl_nm2798():
    return 'ret2798' 

@action('ctrl_act2799')
def ctrl_nm2799():
    return 'ret2799' 

@action('ctrl_act2800')
def ctrl_nm2800():
    return 'ret2800' 

@action('ctrl_act2801')
def ctrl_nm2801():
    return 'ret2801' 

@action('ctrl_act2802')
def ctrl_nm2802():
    return 'ret2802' 

@action('ctrl_act2803')
def ctrl_nm2803():
    return 'ret2803' 

@action('ctrl_act2804')
def ctrl_nm2804():
    return 'ret2804' 

@action('ctrl_act2805')
def ctrl_nm2805():
    return 'ret2805' 

@action('ctrl_act2806')
def ctrl_nm2806():
    return 'ret2806' 

@action('ctrl_act2807')
def ctrl_nm2807():
    return 'ret2807' 

@action('ctrl_act2808')
def ctrl_nm2808():
    return 'ret2808' 

@action('ctrl_act2809')
def ctrl_nm2809():
    return 'ret2809' 

@action('ctrl_act2810')
def ctrl_nm2810():
    return 'ret2810' 

@action('ctrl_act2811')
def ctrl_nm2811():
    return 'ret2811' 

@action('ctrl_act2812')
def ctrl_nm2812():
    return 'ret2812' 

@action('ctrl_act2813')
def ctrl_nm2813():
    return 'ret2813' 

@action('ctrl_act2814')
def ctrl_nm2814():
    return 'ret2814' 

@action('ctrl_act2815')
def ctrl_nm2815():
    return 'ret2815' 

@action('ctrl_act2816')
def ctrl_nm2816():
    return 'ret2816' 

@action('ctrl_act2817')
def ctrl_nm2817():
    return 'ret2817' 

@action('ctrl_act2818')
def ctrl_nm2818():
    return 'ret2818' 

@action('ctrl_act2819')
def ctrl_nm2819():
    return 'ret2819' 

@action('ctrl_act2820')
def ctrl_nm2820():
    return 'ret2820' 

@action('ctrl_act2821')
def ctrl_nm2821():
    return 'ret2821' 

@action('ctrl_act2822')
def ctrl_nm2822():
    return 'ret2822' 

@action('ctrl_act2823')
def ctrl_nm2823():
    return 'ret2823' 

@action('ctrl_act2824')
def ctrl_nm2824():
    return 'ret2824' 

@action('ctrl_act2825')
def ctrl_nm2825():
    return 'ret2825' 

@action('ctrl_act2826')
def ctrl_nm2826():
    return 'ret2826' 

@action('ctrl_act2827')
def ctrl_nm2827():
    return 'ret2827' 

@action('ctrl_act2828')
def ctrl_nm2828():
    return 'ret2828' 

@action('ctrl_act2829')
def ctrl_nm2829():
    return 'ret2829' 

@action('ctrl_act2830')
def ctrl_nm2830():
    return 'ret2830' 

@action('ctrl_act2831')
def ctrl_nm2831():
    return 'ret2831' 

@action('ctrl_act2832')
def ctrl_nm2832():
    return 'ret2832' 

@action('ctrl_act2833')
def ctrl_nm2833():
    return 'ret2833' 

@action('ctrl_act2834')
def ctrl_nm2834():
    return 'ret2834' 

@action('ctrl_act2835')
def ctrl_nm2835():
    return 'ret2835' 

@action('ctrl_act2836')
def ctrl_nm2836():
    return 'ret2836' 

@action('ctrl_act2837')
def ctrl_nm2837():
    return 'ret2837' 

@action('ctrl_act2838')
def ctrl_nm2838():
    return 'ret2838' 

@action('ctrl_act2839')
def ctrl_nm2839():
    return 'ret2839' 

@action('ctrl_act2840')
def ctrl_nm2840():
    return 'ret2840' 

@action('ctrl_act2841')
def ctrl_nm2841():
    return 'ret2841' 

@action('ctrl_act2842')
def ctrl_nm2842():
    return 'ret2842' 

@action('ctrl_act2843')
def ctrl_nm2843():
    return 'ret2843' 

@action('ctrl_act2844')
def ctrl_nm2844():
    return 'ret2844' 

@action('ctrl_act2845')
def ctrl_nm2845():
    return 'ret2845' 

@action('ctrl_act2846')
def ctrl_nm2846():
    return 'ret2846' 

@action('ctrl_act2847')
def ctrl_nm2847():
    return 'ret2847' 

@action('ctrl_act2848')
def ctrl_nm2848():
    return 'ret2848' 

@action('ctrl_act2849')
def ctrl_nm2849():
    return 'ret2849' 

@action('ctrl_act2850')
def ctrl_nm2850():
    return 'ret2850' 

@action('ctrl_act2851')
def ctrl_nm2851():
    return 'ret2851' 

@action('ctrl_act2852')
def ctrl_nm2852():
    return 'ret2852' 

@action('ctrl_act2853')
def ctrl_nm2853():
    return 'ret2853' 

@action('ctrl_act2854')
def ctrl_nm2854():
    return 'ret2854' 

@action('ctrl_act2855')
def ctrl_nm2855():
    return 'ret2855' 

@action('ctrl_act2856')
def ctrl_nm2856():
    return 'ret2856' 

@action('ctrl_act2857')
def ctrl_nm2857():
    return 'ret2857' 

@action('ctrl_act2858')
def ctrl_nm2858():
    return 'ret2858' 

@action('ctrl_act2859')
def ctrl_nm2859():
    return 'ret2859' 

@action('ctrl_act2860')
def ctrl_nm2860():
    return 'ret2860' 

@action('ctrl_act2861')
def ctrl_nm2861():
    return 'ret2861' 

@action('ctrl_act2862')
def ctrl_nm2862():
    return 'ret2862' 

@action('ctrl_act2863')
def ctrl_nm2863():
    return 'ret2863' 

@action('ctrl_act2864')
def ctrl_nm2864():
    return 'ret2864' 

@action('ctrl_act2865')
def ctrl_nm2865():
    return 'ret2865' 

@action('ctrl_act2866')
def ctrl_nm2866():
    return 'ret2866' 

@action('ctrl_act2867')
def ctrl_nm2867():
    return 'ret2867' 

@action('ctrl_act2868')
def ctrl_nm2868():
    return 'ret2868' 

@action('ctrl_act2869')
def ctrl_nm2869():
    return 'ret2869' 

@action('ctrl_act2870')
def ctrl_nm2870():
    return 'ret2870' 

@action('ctrl_act2871')
def ctrl_nm2871():
    return 'ret2871' 

@action('ctrl_act2872')
def ctrl_nm2872():
    return 'ret2872' 

@action('ctrl_act2873')
def ctrl_nm2873():
    return 'ret2873' 

@action('ctrl_act2874')
def ctrl_nm2874():
    return 'ret2874' 

@action('ctrl_act2875')
def ctrl_nm2875():
    return 'ret2875' 

@action('ctrl_act2876')
def ctrl_nm2876():
    return 'ret2876' 

@action('ctrl_act2877')
def ctrl_nm2877():
    return 'ret2877' 

@action('ctrl_act2878')
def ctrl_nm2878():
    return 'ret2878' 

@action('ctrl_act2879')
def ctrl_nm2879():
    return 'ret2879' 

@action('ctrl_act2880')
def ctrl_nm2880():
    return 'ret2880' 

@action('ctrl_act2881')
def ctrl_nm2881():
    return 'ret2881' 

@action('ctrl_act2882')
def ctrl_nm2882():
    return 'ret2882' 

@action('ctrl_act2883')
def ctrl_nm2883():
    return 'ret2883' 

@action('ctrl_act2884')
def ctrl_nm2884():
    return 'ret2884' 

@action('ctrl_act2885')
def ctrl_nm2885():
    return 'ret2885' 

@action('ctrl_act2886')
def ctrl_nm2886():
    return 'ret2886' 

@action('ctrl_act2887')
def ctrl_nm2887():
    return 'ret2887' 

@action('ctrl_act2888')
def ctrl_nm2888():
    return 'ret2888' 

@action('ctrl_act2889')
def ctrl_nm2889():
    return 'ret2889' 

@action('ctrl_act2890')
def ctrl_nm2890():
    return 'ret2890' 

@action('ctrl_act2891')
def ctrl_nm2891():
    return 'ret2891' 

@action('ctrl_act2892')
def ctrl_nm2892():
    return 'ret2892' 

@action('ctrl_act2893')
def ctrl_nm2893():
    return 'ret2893' 

@action('ctrl_act2894')
def ctrl_nm2894():
    return 'ret2894' 

@action('ctrl_act2895')
def ctrl_nm2895():
    return 'ret2895' 

@action('ctrl_act2896')
def ctrl_nm2896():
    return 'ret2896' 

@action('ctrl_act2897')
def ctrl_nm2897():
    return 'ret2897' 

@action('ctrl_act2898')
def ctrl_nm2898():
    return 'ret2898' 

@action('ctrl_act2899')
def ctrl_nm2899():
    return 'ret2899' 

@action('ctrl_act2900')
def ctrl_nm2900():
    return 'ret2900' 

@action('ctrl_act2901')
def ctrl_nm2901():
    return 'ret2901' 

@action('ctrl_act2902')
def ctrl_nm2902():
    return 'ret2902' 

@action('ctrl_act2903')
def ctrl_nm2903():
    return 'ret2903' 

@action('ctrl_act2904')
def ctrl_nm2904():
    return 'ret2904' 

@action('ctrl_act2905')
def ctrl_nm2905():
    return 'ret2905' 

@action('ctrl_act2906')
def ctrl_nm2906():
    return 'ret2906' 

@action('ctrl_act2907')
def ctrl_nm2907():
    return 'ret2907' 

@action('ctrl_act2908')
def ctrl_nm2908():
    return 'ret2908' 

@action('ctrl_act2909')
def ctrl_nm2909():
    return 'ret2909' 

@action('ctrl_act2910')
def ctrl_nm2910():
    return 'ret2910' 

@action('ctrl_act2911')
def ctrl_nm2911():
    return 'ret2911' 

@action('ctrl_act2912')
def ctrl_nm2912():
    return 'ret2912' 

@action('ctrl_act2913')
def ctrl_nm2913():
    return 'ret2913' 

@action('ctrl_act2914')
def ctrl_nm2914():
    return 'ret2914' 

@action('ctrl_act2915')
def ctrl_nm2915():
    return 'ret2915' 

@action('ctrl_act2916')
def ctrl_nm2916():
    return 'ret2916' 

@action('ctrl_act2917')
def ctrl_nm2917():
    return 'ret2917' 

@action('ctrl_act2918')
def ctrl_nm2918():
    return 'ret2918' 

@action('ctrl_act2919')
def ctrl_nm2919():
    return 'ret2919' 

@action('ctrl_act2920')
def ctrl_nm2920():
    return 'ret2920' 

@action('ctrl_act2921')
def ctrl_nm2921():
    return 'ret2921' 

@action('ctrl_act2922')
def ctrl_nm2922():
    return 'ret2922' 

@action('ctrl_act2923')
def ctrl_nm2923():
    return 'ret2923' 

@action('ctrl_act2924')
def ctrl_nm2924():
    return 'ret2924' 

@action('ctrl_act2925')
def ctrl_nm2925():
    return 'ret2925' 

@action('ctrl_act2926')
def ctrl_nm2926():
    return 'ret2926' 

@action('ctrl_act2927')
def ctrl_nm2927():
    return 'ret2927' 

@action('ctrl_act2928')
def ctrl_nm2928():
    return 'ret2928' 

@action('ctrl_act2929')
def ctrl_nm2929():
    return 'ret2929' 

@action('ctrl_act2930')
def ctrl_nm2930():
    return 'ret2930' 

@action('ctrl_act2931')
def ctrl_nm2931():
    return 'ret2931' 

@action('ctrl_act2932')
def ctrl_nm2932():
    return 'ret2932' 

@action('ctrl_act2933')
def ctrl_nm2933():
    return 'ret2933' 

@action('ctrl_act2934')
def ctrl_nm2934():
    return 'ret2934' 

@action('ctrl_act2935')
def ctrl_nm2935():
    return 'ret2935' 

@action('ctrl_act2936')
def ctrl_nm2936():
    return 'ret2936' 

@action('ctrl_act2937')
def ctrl_nm2937():
    return 'ret2937' 

@action('ctrl_act2938')
def ctrl_nm2938():
    return 'ret2938' 

@action('ctrl_act2939')
def ctrl_nm2939():
    return 'ret2939' 

@action('ctrl_act2940')
def ctrl_nm2940():
    return 'ret2940' 

@action('ctrl_act2941')
def ctrl_nm2941():
    return 'ret2941' 

@action('ctrl_act2942')
def ctrl_nm2942():
    return 'ret2942' 

@action('ctrl_act2943')
def ctrl_nm2943():
    return 'ret2943' 

@action('ctrl_act2944')
def ctrl_nm2944():
    return 'ret2944' 

@action('ctrl_act2945')
def ctrl_nm2945():
    return 'ret2945' 

@action('ctrl_act2946')
def ctrl_nm2946():
    return 'ret2946' 

@action('ctrl_act2947')
def ctrl_nm2947():
    return 'ret2947' 

@action('ctrl_act2948')
def ctrl_nm2948():
    return 'ret2948' 

@action('ctrl_act2949')
def ctrl_nm2949():
    return 'ret2949' 

@action('ctrl_act2950')
def ctrl_nm2950():
    return 'ret2950' 

@action('ctrl_act2951')
def ctrl_nm2951():
    return 'ret2951' 

@action('ctrl_act2952')
def ctrl_nm2952():
    return 'ret2952' 

@action('ctrl_act2953')
def ctrl_nm2953():
    return 'ret2953' 

@action('ctrl_act2954')
def ctrl_nm2954():
    return 'ret2954' 

@action('ctrl_act2955')
def ctrl_nm2955():
    return 'ret2955' 

@action('ctrl_act2956')
def ctrl_nm2956():
    return 'ret2956' 

@action('ctrl_act2957')
def ctrl_nm2957():
    return 'ret2957' 

@action('ctrl_act2958')
def ctrl_nm2958():
    return 'ret2958' 

@action('ctrl_act2959')
def ctrl_nm2959():
    return 'ret2959' 

@action('ctrl_act2960')
def ctrl_nm2960():
    return 'ret2960' 

@action('ctrl_act2961')
def ctrl_nm2961():
    return 'ret2961' 

@action('ctrl_act2962')
def ctrl_nm2962():
    return 'ret2962' 

@action('ctrl_act2963')
def ctrl_nm2963():
    return 'ret2963' 

@action('ctrl_act2964')
def ctrl_nm2964():
    return 'ret2964' 

@action('ctrl_act2965')
def ctrl_nm2965():
    return 'ret2965' 

@action('ctrl_act2966')
def ctrl_nm2966():
    return 'ret2966' 

@action('ctrl_act2967')
def ctrl_nm2967():
    return 'ret2967' 

@action('ctrl_act2968')
def ctrl_nm2968():
    return 'ret2968' 

@action('ctrl_act2969')
def ctrl_nm2969():
    return 'ret2969' 

@action('ctrl_act2970')
def ctrl_nm2970():
    return 'ret2970' 

@action('ctrl_act2971')
def ctrl_nm2971():
    return 'ret2971' 

@action('ctrl_act2972')
def ctrl_nm2972():
    return 'ret2972' 

@action('ctrl_act2973')
def ctrl_nm2973():
    return 'ret2973' 

@action('ctrl_act2974')
def ctrl_nm2974():
    return 'ret2974' 

@action('ctrl_act2975')
def ctrl_nm2975():
    return 'ret2975' 

@action('ctrl_act2976')
def ctrl_nm2976():
    return 'ret2976' 

@action('ctrl_act2977')
def ctrl_nm2977():
    return 'ret2977' 

@action('ctrl_act2978')
def ctrl_nm2978():
    return 'ret2978' 

@action('ctrl_act2979')
def ctrl_nm2979():
    return 'ret2979' 

@action('ctrl_act2980')
def ctrl_nm2980():
    return 'ret2980' 

@action('ctrl_act2981')
def ctrl_nm2981():
    return 'ret2981' 

@action('ctrl_act2982')
def ctrl_nm2982():
    return 'ret2982' 

@action('ctrl_act2983')
def ctrl_nm2983():
    return 'ret2983' 

@action('ctrl_act2984')
def ctrl_nm2984():
    return 'ret2984' 

@action('ctrl_act2985')
def ctrl_nm2985():
    return 'ret2985' 

@action('ctrl_act2986')
def ctrl_nm2986():
    return 'ret2986' 

@action('ctrl_act2987')
def ctrl_nm2987():
    return 'ret2987' 

@action('ctrl_act2988')
def ctrl_nm2988():
    return 'ret2988' 

@action('ctrl_act2989')
def ctrl_nm2989():
    return 'ret2989' 

@action('ctrl_act2990')
def ctrl_nm2990():
    return 'ret2990' 

@action('ctrl_act2991')
def ctrl_nm2991():
    return 'ret2991' 

@action('ctrl_act2992')
def ctrl_nm2992():
    return 'ret2992' 

@action('ctrl_act2993')
def ctrl_nm2993():
    return 'ret2993' 

@action('ctrl_act2994')
def ctrl_nm2994():
    return 'ret2994' 

@action('ctrl_act2995')
def ctrl_nm2995():
    return 'ret2995' 

@action('ctrl_act2996')
def ctrl_nm2996():
    return 'ret2996' 

@action('ctrl_act2997')
def ctrl_nm2997():
    return 'ret2997' 

@action('ctrl_act2998')
def ctrl_nm2998():
    return 'ret2998' 

@action('ctrl_act2999')
def ctrl_nm2999():
    return 'ret2999' 

@action('ctrl_act3000')
def ctrl_nm3000():
    return 'ret3000' 

@action('ctrl_act3001')
def ctrl_nm3001():
    return 'ret3001' 

@action('ctrl_act3002')
def ctrl_nm3002():
    return 'ret3002' 

@action('ctrl_act3003')
def ctrl_nm3003():
    return 'ret3003' 

@action('ctrl_act3004')
def ctrl_nm3004():
    return 'ret3004' 

@action('ctrl_act3005')
def ctrl_nm3005():
    return 'ret3005' 

@action('ctrl_act3006')
def ctrl_nm3006():
    return 'ret3006' 

@action('ctrl_act3007')
def ctrl_nm3007():
    return 'ret3007' 

@action('ctrl_act3008')
def ctrl_nm3008():
    return 'ret3008' 

@action('ctrl_act3009')
def ctrl_nm3009():
    return 'ret3009' 

@action('ctrl_act3010')
def ctrl_nm3010():
    return 'ret3010' 

@action('ctrl_act3011')
def ctrl_nm3011():
    return 'ret3011' 

@action('ctrl_act3012')
def ctrl_nm3012():
    return 'ret3012' 

@action('ctrl_act3013')
def ctrl_nm3013():
    return 'ret3013' 

@action('ctrl_act3014')
def ctrl_nm3014():
    return 'ret3014' 

@action('ctrl_act3015')
def ctrl_nm3015():
    return 'ret3015' 

@action('ctrl_act3016')
def ctrl_nm3016():
    return 'ret3016' 

@action('ctrl_act3017')
def ctrl_nm3017():
    return 'ret3017' 

@action('ctrl_act3018')
def ctrl_nm3018():
    return 'ret3018' 

@action('ctrl_act3019')
def ctrl_nm3019():
    return 'ret3019' 

@action('ctrl_act3020')
def ctrl_nm3020():
    return 'ret3020' 

@action('ctrl_act3021')
def ctrl_nm3021():
    return 'ret3021' 

@action('ctrl_act3022')
def ctrl_nm3022():
    return 'ret3022' 

@action('ctrl_act3023')
def ctrl_nm3023():
    return 'ret3023' 

@action('ctrl_act3024')
def ctrl_nm3024():
    return 'ret3024' 

@action('ctrl_act3025')
def ctrl_nm3025():
    return 'ret3025' 

@action('ctrl_act3026')
def ctrl_nm3026():
    return 'ret3026' 

@action('ctrl_act3027')
def ctrl_nm3027():
    return 'ret3027' 

@action('ctrl_act3028')
def ctrl_nm3028():
    return 'ret3028' 

@action('ctrl_act3029')
def ctrl_nm3029():
    return 'ret3029' 

@action('ctrl_act3030')
def ctrl_nm3030():
    return 'ret3030' 

@action('ctrl_act3031')
def ctrl_nm3031():
    return 'ret3031' 

@action('ctrl_act3032')
def ctrl_nm3032():
    return 'ret3032' 

@action('ctrl_act3033')
def ctrl_nm3033():
    return 'ret3033' 

@action('ctrl_act3034')
def ctrl_nm3034():
    return 'ret3034' 

@action('ctrl_act3035')
def ctrl_nm3035():
    return 'ret3035' 

@action('ctrl_act3036')
def ctrl_nm3036():
    return 'ret3036' 

@action('ctrl_act3037')
def ctrl_nm3037():
    return 'ret3037' 

@action('ctrl_act3038')
def ctrl_nm3038():
    return 'ret3038' 

@action('ctrl_act3039')
def ctrl_nm3039():
    return 'ret3039' 

@action('ctrl_act3040')
def ctrl_nm3040():
    return 'ret3040' 

@action('ctrl_act3041')
def ctrl_nm3041():
    return 'ret3041' 

@action('ctrl_act3042')
def ctrl_nm3042():
    return 'ret3042' 

@action('ctrl_act3043')
def ctrl_nm3043():
    return 'ret3043' 

@action('ctrl_act3044')
def ctrl_nm3044():
    return 'ret3044' 

@action('ctrl_act3045')
def ctrl_nm3045():
    return 'ret3045' 

@action('ctrl_act3046')
def ctrl_nm3046():
    return 'ret3046' 

@action('ctrl_act3047')
def ctrl_nm3047():
    return 'ret3047' 

@action('ctrl_act3048')
def ctrl_nm3048():
    return 'ret3048' 

@action('ctrl_act3049')
def ctrl_nm3049():
    return 'ret3049' 

@action('ctrl_act3050')
def ctrl_nm3050():
    return 'ret3050' 

@action('ctrl_act3051')
def ctrl_nm3051():
    return 'ret3051' 

@action('ctrl_act3052')
def ctrl_nm3052():
    return 'ret3052' 

@action('ctrl_act3053')
def ctrl_nm3053():
    return 'ret3053' 

@action('ctrl_act3054')
def ctrl_nm3054():
    return 'ret3054' 

@action('ctrl_act3055')
def ctrl_nm3055():
    return 'ret3055' 

@action('ctrl_act3056')
def ctrl_nm3056():
    return 'ret3056' 

@action('ctrl_act3057')
def ctrl_nm3057():
    return 'ret3057' 

@action('ctrl_act3058')
def ctrl_nm3058():
    return 'ret3058' 

@action('ctrl_act3059')
def ctrl_nm3059():
    return 'ret3059' 

@action('ctrl_act3060')
def ctrl_nm3060():
    return 'ret3060' 

@action('ctrl_act3061')
def ctrl_nm3061():
    return 'ret3061' 

@action('ctrl_act3062')
def ctrl_nm3062():
    return 'ret3062' 

@action('ctrl_act3063')
def ctrl_nm3063():
    return 'ret3063' 

@action('ctrl_act3064')
def ctrl_nm3064():
    return 'ret3064' 

@action('ctrl_act3065')
def ctrl_nm3065():
    return 'ret3065' 

@action('ctrl_act3066')
def ctrl_nm3066():
    return 'ret3066' 

@action('ctrl_act3067')
def ctrl_nm3067():
    return 'ret3067' 

@action('ctrl_act3068')
def ctrl_nm3068():
    return 'ret3068' 

@action('ctrl_act3069')
def ctrl_nm3069():
    return 'ret3069' 

@action('ctrl_act3070')
def ctrl_nm3070():
    return 'ret3070' 

@action('ctrl_act3071')
def ctrl_nm3071():
    return 'ret3071' 

@action('ctrl_act3072')
def ctrl_nm3072():
    return 'ret3072' 

@action('ctrl_act3073')
def ctrl_nm3073():
    return 'ret3073' 

@action('ctrl_act3074')
def ctrl_nm3074():
    return 'ret3074' 

@action('ctrl_act3075')
def ctrl_nm3075():
    return 'ret3075' 

@action('ctrl_act3076')
def ctrl_nm3076():
    return 'ret3076' 

@action('ctrl_act3077')
def ctrl_nm3077():
    return 'ret3077' 

@action('ctrl_act3078')
def ctrl_nm3078():
    return 'ret3078' 

@action('ctrl_act3079')
def ctrl_nm3079():
    return 'ret3079' 

@action('ctrl_act3080')
def ctrl_nm3080():
    return 'ret3080' 

@action('ctrl_act3081')
def ctrl_nm3081():
    return 'ret3081' 

@action('ctrl_act3082')
def ctrl_nm3082():
    return 'ret3082' 

@action('ctrl_act3083')
def ctrl_nm3083():
    return 'ret3083' 

@action('ctrl_act3084')
def ctrl_nm3084():
    return 'ret3084' 

@action('ctrl_act3085')
def ctrl_nm3085():
    return 'ret3085' 

@action('ctrl_act3086')
def ctrl_nm3086():
    return 'ret3086' 

@action('ctrl_act3087')
def ctrl_nm3087():
    return 'ret3087' 

@action('ctrl_act3088')
def ctrl_nm3088():
    return 'ret3088' 

@action('ctrl_act3089')
def ctrl_nm3089():
    return 'ret3089' 

@action('ctrl_act3090')
def ctrl_nm3090():
    return 'ret3090' 

@action('ctrl_act3091')
def ctrl_nm3091():
    return 'ret3091' 

@action('ctrl_act3092')
def ctrl_nm3092():
    return 'ret3092' 

@action('ctrl_act3093')
def ctrl_nm3093():
    return 'ret3093' 

@action('ctrl_act3094')
def ctrl_nm3094():
    return 'ret3094' 

@action('ctrl_act3095')
def ctrl_nm3095():
    return 'ret3095' 

@action('ctrl_act3096')
def ctrl_nm3096():
    return 'ret3096' 

@action('ctrl_act3097')
def ctrl_nm3097():
    return 'ret3097' 

@action('ctrl_act3098')
def ctrl_nm3098():
    return 'ret3098' 

@action('ctrl_act3099')
def ctrl_nm3099():
    return 'ret3099' 

@action('ctrl_act3100')
def ctrl_nm3100():
    return 'ret3100' 

@action('ctrl_act3101')
def ctrl_nm3101():
    return 'ret3101' 

@action('ctrl_act3102')
def ctrl_nm3102():
    return 'ret3102' 

@action('ctrl_act3103')
def ctrl_nm3103():
    return 'ret3103' 

@action('ctrl_act3104')
def ctrl_nm3104():
    return 'ret3104' 

@action('ctrl_act3105')
def ctrl_nm3105():
    return 'ret3105' 

@action('ctrl_act3106')
def ctrl_nm3106():
    return 'ret3106' 

@action('ctrl_act3107')
def ctrl_nm3107():
    return 'ret3107' 

@action('ctrl_act3108')
def ctrl_nm3108():
    return 'ret3108' 

@action('ctrl_act3109')
def ctrl_nm3109():
    return 'ret3109' 

@action('ctrl_act3110')
def ctrl_nm3110():
    return 'ret3110' 

@action('ctrl_act3111')
def ctrl_nm3111():
    return 'ret3111' 

@action('ctrl_act3112')
def ctrl_nm3112():
    return 'ret3112' 

@action('ctrl_act3113')
def ctrl_nm3113():
    return 'ret3113' 

@action('ctrl_act3114')
def ctrl_nm3114():
    return 'ret3114' 

@action('ctrl_act3115')
def ctrl_nm3115():
    return 'ret3115' 

@action('ctrl_act3116')
def ctrl_nm3116():
    return 'ret3116' 

@action('ctrl_act3117')
def ctrl_nm3117():
    return 'ret3117' 

@action('ctrl_act3118')
def ctrl_nm3118():
    return 'ret3118' 

@action('ctrl_act3119')
def ctrl_nm3119():
    return 'ret3119' 

@action('ctrl_act3120')
def ctrl_nm3120():
    return 'ret3120' 

@action('ctrl_act3121')
def ctrl_nm3121():
    return 'ret3121' 

@action('ctrl_act3122')
def ctrl_nm3122():
    return 'ret3122' 

@action('ctrl_act3123')
def ctrl_nm3123():
    return 'ret3123' 

@action('ctrl_act3124')
def ctrl_nm3124():
    return 'ret3124' 

@action('ctrl_act3125')
def ctrl_nm3125():
    return 'ret3125' 

@action('ctrl_act3126')
def ctrl_nm3126():
    return 'ret3126' 

@action('ctrl_act3127')
def ctrl_nm3127():
    return 'ret3127' 

@action('ctrl_act3128')
def ctrl_nm3128():
    return 'ret3128' 

@action('ctrl_act3129')
def ctrl_nm3129():
    return 'ret3129' 

@action('ctrl_act3130')
def ctrl_nm3130():
    return 'ret3130' 

@action('ctrl_act3131')
def ctrl_nm3131():
    return 'ret3131' 

@action('ctrl_act3132')
def ctrl_nm3132():
    return 'ret3132' 

@action('ctrl_act3133')
def ctrl_nm3133():
    return 'ret3133' 

@action('ctrl_act3134')
def ctrl_nm3134():
    return 'ret3134' 

@action('ctrl_act3135')
def ctrl_nm3135():
    return 'ret3135' 

@action('ctrl_act3136')
def ctrl_nm3136():
    return 'ret3136' 

@action('ctrl_act3137')
def ctrl_nm3137():
    return 'ret3137' 

@action('ctrl_act3138')
def ctrl_nm3138():
    return 'ret3138' 

@action('ctrl_act3139')
def ctrl_nm3139():
    return 'ret3139' 

@action('ctrl_act3140')
def ctrl_nm3140():
    return 'ret3140' 

@action('ctrl_act3141')
def ctrl_nm3141():
    return 'ret3141' 

@action('ctrl_act3142')
def ctrl_nm3142():
    return 'ret3142' 

@action('ctrl_act3143')
def ctrl_nm3143():
    return 'ret3143' 

@action('ctrl_act3144')
def ctrl_nm3144():
    return 'ret3144' 

@action('ctrl_act3145')
def ctrl_nm3145():
    return 'ret3145' 

@action('ctrl_act3146')
def ctrl_nm3146():
    return 'ret3146' 

@action('ctrl_act3147')
def ctrl_nm3147():
    return 'ret3147' 

@action('ctrl_act3148')
def ctrl_nm3148():
    return 'ret3148' 

@action('ctrl_act3149')
def ctrl_nm3149():
    return 'ret3149' 

@action('ctrl_act3150')
def ctrl_nm3150():
    return 'ret3150' 

@action('ctrl_act3151')
def ctrl_nm3151():
    return 'ret3151' 

@action('ctrl_act3152')
def ctrl_nm3152():
    return 'ret3152' 

@action('ctrl_act3153')
def ctrl_nm3153():
    return 'ret3153' 

@action('ctrl_act3154')
def ctrl_nm3154():
    return 'ret3154' 

@action('ctrl_act3155')
def ctrl_nm3155():
    return 'ret3155' 

@action('ctrl_act3156')
def ctrl_nm3156():
    return 'ret3156' 

@action('ctrl_act3157')
def ctrl_nm3157():
    return 'ret3157' 

@action('ctrl_act3158')
def ctrl_nm3158():
    return 'ret3158' 

@action('ctrl_act3159')
def ctrl_nm3159():
    return 'ret3159' 

@action('ctrl_act3160')
def ctrl_nm3160():
    return 'ret3160' 

@action('ctrl_act3161')
def ctrl_nm3161():
    return 'ret3161' 

@action('ctrl_act3162')
def ctrl_nm3162():
    return 'ret3162' 

@action('ctrl_act3163')
def ctrl_nm3163():
    return 'ret3163' 

@action('ctrl_act3164')
def ctrl_nm3164():
    return 'ret3164' 

@action('ctrl_act3165')
def ctrl_nm3165():
    return 'ret3165' 

@action('ctrl_act3166')
def ctrl_nm3166():
    return 'ret3166' 

@action('ctrl_act3167')
def ctrl_nm3167():
    return 'ret3167' 

@action('ctrl_act3168')
def ctrl_nm3168():
    return 'ret3168' 

@action('ctrl_act3169')
def ctrl_nm3169():
    return 'ret3169' 

@action('ctrl_act3170')
def ctrl_nm3170():
    return 'ret3170' 

@action('ctrl_act3171')
def ctrl_nm3171():
    return 'ret3171' 

@action('ctrl_act3172')
def ctrl_nm3172():
    return 'ret3172' 

@action('ctrl_act3173')
def ctrl_nm3173():
    return 'ret3173' 

@action('ctrl_act3174')
def ctrl_nm3174():
    return 'ret3174' 

@action('ctrl_act3175')
def ctrl_nm3175():
    return 'ret3175' 

@action('ctrl_act3176')
def ctrl_nm3176():
    return 'ret3176' 

@action('ctrl_act3177')
def ctrl_nm3177():
    return 'ret3177' 

@action('ctrl_act3178')
def ctrl_nm3178():
    return 'ret3178' 

@action('ctrl_act3179')
def ctrl_nm3179():
    return 'ret3179' 

@action('ctrl_act3180')
def ctrl_nm3180():
    return 'ret3180' 

@action('ctrl_act3181')
def ctrl_nm3181():
    return 'ret3181' 

@action('ctrl_act3182')
def ctrl_nm3182():
    return 'ret3182' 

@action('ctrl_act3183')
def ctrl_nm3183():
    return 'ret3183' 

@action('ctrl_act3184')
def ctrl_nm3184():
    return 'ret3184' 

@action('ctrl_act3185')
def ctrl_nm3185():
    return 'ret3185' 

@action('ctrl_act3186')
def ctrl_nm3186():
    return 'ret3186' 

@action('ctrl_act3187')
def ctrl_nm3187():
    return 'ret3187' 

@action('ctrl_act3188')
def ctrl_nm3188():
    return 'ret3188' 

@action('ctrl_act3189')
def ctrl_nm3189():
    return 'ret3189' 

@action('ctrl_act3190')
def ctrl_nm3190():
    return 'ret3190' 

@action('ctrl_act3191')
def ctrl_nm3191():
    return 'ret3191' 

@action('ctrl_act3192')
def ctrl_nm3192():
    return 'ret3192' 

@action('ctrl_act3193')
def ctrl_nm3193():
    return 'ret3193' 

@action('ctrl_act3194')
def ctrl_nm3194():
    return 'ret3194' 

@action('ctrl_act3195')
def ctrl_nm3195():
    return 'ret3195' 

@action('ctrl_act3196')
def ctrl_nm3196():
    return 'ret3196' 

@action('ctrl_act3197')
def ctrl_nm3197():
    return 'ret3197' 

@action('ctrl_act3198')
def ctrl_nm3198():
    return 'ret3198' 

@action('ctrl_act3199')
def ctrl_nm3199():
    return 'ret3199' 

@action('ctrl_act3200')
def ctrl_nm3200():
    return 'ret3200' 

@action('ctrl_act3201')
def ctrl_nm3201():
    return 'ret3201' 

@action('ctrl_act3202')
def ctrl_nm3202():
    return 'ret3202' 

@action('ctrl_act3203')
def ctrl_nm3203():
    return 'ret3203' 

@action('ctrl_act3204')
def ctrl_nm3204():
    return 'ret3204' 

@action('ctrl_act3205')
def ctrl_nm3205():
    return 'ret3205' 

@action('ctrl_act3206')
def ctrl_nm3206():
    return 'ret3206' 

@action('ctrl_act3207')
def ctrl_nm3207():
    return 'ret3207' 

@action('ctrl_act3208')
def ctrl_nm3208():
    return 'ret3208' 

@action('ctrl_act3209')
def ctrl_nm3209():
    return 'ret3209' 

@action('ctrl_act3210')
def ctrl_nm3210():
    return 'ret3210' 

@action('ctrl_act3211')
def ctrl_nm3211():
    return 'ret3211' 

@action('ctrl_act3212')
def ctrl_nm3212():
    return 'ret3212' 

@action('ctrl_act3213')
def ctrl_nm3213():
    return 'ret3213' 

@action('ctrl_act3214')
def ctrl_nm3214():
    return 'ret3214' 

@action('ctrl_act3215')
def ctrl_nm3215():
    return 'ret3215' 

@action('ctrl_act3216')
def ctrl_nm3216():
    return 'ret3216' 

@action('ctrl_act3217')
def ctrl_nm3217():
    return 'ret3217' 

@action('ctrl_act3218')
def ctrl_nm3218():
    return 'ret3218' 

@action('ctrl_act3219')
def ctrl_nm3219():
    return 'ret3219' 

@action('ctrl_act3220')
def ctrl_nm3220():
    return 'ret3220' 

@action('ctrl_act3221')
def ctrl_nm3221():
    return 'ret3221' 

@action('ctrl_act3222')
def ctrl_nm3222():
    return 'ret3222' 

@action('ctrl_act3223')
def ctrl_nm3223():
    return 'ret3223' 

@action('ctrl_act3224')
def ctrl_nm3224():
    return 'ret3224' 

@action('ctrl_act3225')
def ctrl_nm3225():
    return 'ret3225' 

@action('ctrl_act3226')
def ctrl_nm3226():
    return 'ret3226' 

@action('ctrl_act3227')
def ctrl_nm3227():
    return 'ret3227' 

@action('ctrl_act3228')
def ctrl_nm3228():
    return 'ret3228' 

@action('ctrl_act3229')
def ctrl_nm3229():
    return 'ret3229' 

@action('ctrl_act3230')
def ctrl_nm3230():
    return 'ret3230' 

@action('ctrl_act3231')
def ctrl_nm3231():
    return 'ret3231' 

@action('ctrl_act3232')
def ctrl_nm3232():
    return 'ret3232' 

@action('ctrl_act3233')
def ctrl_nm3233():
    return 'ret3233' 

@action('ctrl_act3234')
def ctrl_nm3234():
    return 'ret3234' 

@action('ctrl_act3235')
def ctrl_nm3235():
    return 'ret3235' 

@action('ctrl_act3236')
def ctrl_nm3236():
    return 'ret3236' 

@action('ctrl_act3237')
def ctrl_nm3237():
    return 'ret3237' 

@action('ctrl_act3238')
def ctrl_nm3238():
    return 'ret3238' 

@action('ctrl_act3239')
def ctrl_nm3239():
    return 'ret3239' 

@action('ctrl_act3240')
def ctrl_nm3240():
    return 'ret3240' 

@action('ctrl_act3241')
def ctrl_nm3241():
    return 'ret3241' 

@action('ctrl_act3242')
def ctrl_nm3242():
    return 'ret3242' 

@action('ctrl_act3243')
def ctrl_nm3243():
    return 'ret3243' 

@action('ctrl_act3244')
def ctrl_nm3244():
    return 'ret3244' 

@action('ctrl_act3245')
def ctrl_nm3245():
    return 'ret3245' 

@action('ctrl_act3246')
def ctrl_nm3246():
    return 'ret3246' 

@action('ctrl_act3247')
def ctrl_nm3247():
    return 'ret3247' 

@action('ctrl_act3248')
def ctrl_nm3248():
    return 'ret3248' 

@action('ctrl_act3249')
def ctrl_nm3249():
    return 'ret3249' 

@action('ctrl_act3250')
def ctrl_nm3250():
    return 'ret3250' 

@action('ctrl_act3251')
def ctrl_nm3251():
    return 'ret3251' 

@action('ctrl_act3252')
def ctrl_nm3252():
    return 'ret3252' 

@action('ctrl_act3253')
def ctrl_nm3253():
    return 'ret3253' 

@action('ctrl_act3254')
def ctrl_nm3254():
    return 'ret3254' 

@action('ctrl_act3255')
def ctrl_nm3255():
    return 'ret3255' 

@action('ctrl_act3256')
def ctrl_nm3256():
    return 'ret3256' 

@action('ctrl_act3257')
def ctrl_nm3257():
    return 'ret3257' 

@action('ctrl_act3258')
def ctrl_nm3258():
    return 'ret3258' 

@action('ctrl_act3259')
def ctrl_nm3259():
    return 'ret3259' 

@action('ctrl_act3260')
def ctrl_nm3260():
    return 'ret3260' 

@action('ctrl_act3261')
def ctrl_nm3261():
    return 'ret3261' 

@action('ctrl_act3262')
def ctrl_nm3262():
    return 'ret3262' 

@action('ctrl_act3263')
def ctrl_nm3263():
    return 'ret3263' 

@action('ctrl_act3264')
def ctrl_nm3264():
    return 'ret3264' 

@action('ctrl_act3265')
def ctrl_nm3265():
    return 'ret3265' 

@action('ctrl_act3266')
def ctrl_nm3266():
    return 'ret3266' 

@action('ctrl_act3267')
def ctrl_nm3267():
    return 'ret3267' 

@action('ctrl_act3268')
def ctrl_nm3268():
    return 'ret3268' 

@action('ctrl_act3269')
def ctrl_nm3269():
    return 'ret3269' 

@action('ctrl_act3270')
def ctrl_nm3270():
    return 'ret3270' 

@action('ctrl_act3271')
def ctrl_nm3271():
    return 'ret3271' 

@action('ctrl_act3272')
def ctrl_nm3272():
    return 'ret3272' 

@action('ctrl_act3273')
def ctrl_nm3273():
    return 'ret3273' 

@action('ctrl_act3274')
def ctrl_nm3274():
    return 'ret3274' 

@action('ctrl_act3275')
def ctrl_nm3275():
    return 'ret3275' 

@action('ctrl_act3276')
def ctrl_nm3276():
    return 'ret3276' 

@action('ctrl_act3277')
def ctrl_nm3277():
    return 'ret3277' 

@action('ctrl_act3278')
def ctrl_nm3278():
    return 'ret3278' 

@action('ctrl_act3279')
def ctrl_nm3279():
    return 'ret3279' 

@action('ctrl_act3280')
def ctrl_nm3280():
    return 'ret3280' 

@action('ctrl_act3281')
def ctrl_nm3281():
    return 'ret3281' 

@action('ctrl_act3282')
def ctrl_nm3282():
    return 'ret3282' 

@action('ctrl_act3283')
def ctrl_nm3283():
    return 'ret3283' 

@action('ctrl_act3284')
def ctrl_nm3284():
    return 'ret3284' 

@action('ctrl_act3285')
def ctrl_nm3285():
    return 'ret3285' 

@action('ctrl_act3286')
def ctrl_nm3286():
    return 'ret3286' 

@action('ctrl_act3287')
def ctrl_nm3287():
    return 'ret3287' 

@action('ctrl_act3288')
def ctrl_nm3288():
    return 'ret3288' 

@action('ctrl_act3289')
def ctrl_nm3289():
    return 'ret3289' 

@action('ctrl_act3290')
def ctrl_nm3290():
    return 'ret3290' 

@action('ctrl_act3291')
def ctrl_nm3291():
    return 'ret3291' 

@action('ctrl_act3292')
def ctrl_nm3292():
    return 'ret3292' 

@action('ctrl_act3293')
def ctrl_nm3293():
    return 'ret3293' 

@action('ctrl_act3294')
def ctrl_nm3294():
    return 'ret3294' 

@action('ctrl_act3295')
def ctrl_nm3295():
    return 'ret3295' 

@action('ctrl_act3296')
def ctrl_nm3296():
    return 'ret3296' 

@action('ctrl_act3297')
def ctrl_nm3297():
    return 'ret3297' 

@action('ctrl_act3298')
def ctrl_nm3298():
    return 'ret3298' 

@action('ctrl_act3299')
def ctrl_nm3299():
    return 'ret3299' 

@action('ctrl_act3300')
def ctrl_nm3300():
    return 'ret3300' 

@action('ctrl_act3301')
def ctrl_nm3301():
    return 'ret3301' 

@action('ctrl_act3302')
def ctrl_nm3302():
    return 'ret3302' 

@action('ctrl_act3303')
def ctrl_nm3303():
    return 'ret3303' 

@action('ctrl_act3304')
def ctrl_nm3304():
    return 'ret3304' 

@action('ctrl_act3305')
def ctrl_nm3305():
    return 'ret3305' 

@action('ctrl_act3306')
def ctrl_nm3306():
    return 'ret3306' 

@action('ctrl_act3307')
def ctrl_nm3307():
    return 'ret3307' 

@action('ctrl_act3308')
def ctrl_nm3308():
    return 'ret3308' 

@action('ctrl_act3309')
def ctrl_nm3309():
    return 'ret3309' 

@action('ctrl_act3310')
def ctrl_nm3310():
    return 'ret3310' 

@action('ctrl_act3311')
def ctrl_nm3311():
    return 'ret3311' 

@action('ctrl_act3312')
def ctrl_nm3312():
    return 'ret3312' 

@action('ctrl_act3313')
def ctrl_nm3313():
    return 'ret3313' 

@action('ctrl_act3314')
def ctrl_nm3314():
    return 'ret3314' 

@action('ctrl_act3315')
def ctrl_nm3315():
    return 'ret3315' 

@action('ctrl_act3316')
def ctrl_nm3316():
    return 'ret3316' 

@action('ctrl_act3317')
def ctrl_nm3317():
    return 'ret3317' 

@action('ctrl_act3318')
def ctrl_nm3318():
    return 'ret3318' 

@action('ctrl_act3319')
def ctrl_nm3319():
    return 'ret3319' 

@action('ctrl_act3320')
def ctrl_nm3320():
    return 'ret3320' 

@action('ctrl_act3321')
def ctrl_nm3321():
    return 'ret3321' 

@action('ctrl_act3322')
def ctrl_nm3322():
    return 'ret3322' 

@action('ctrl_act3323')
def ctrl_nm3323():
    return 'ret3323' 

@action('ctrl_act3324')
def ctrl_nm3324():
    return 'ret3324' 

@action('ctrl_act3325')
def ctrl_nm3325():
    return 'ret3325' 

@action('ctrl_act3326')
def ctrl_nm3326():
    return 'ret3326' 

@action('ctrl_act3327')
def ctrl_nm3327():
    return 'ret3327' 

@action('ctrl_act3328')
def ctrl_nm3328():
    return 'ret3328' 

@action('ctrl_act3329')
def ctrl_nm3329():
    return 'ret3329' 

@action('ctrl_act3330')
def ctrl_nm3330():
    return 'ret3330' 

@action('ctrl_act3331')
def ctrl_nm3331():
    return 'ret3331' 

@action('ctrl_act3332')
def ctrl_nm3332():
    return 'ret3332' 

@action('ctrl_act3333')
def ctrl_nm3333():
    return 'ret3333' 

@action('ctrl_act3334')
def ctrl_nm3334():
    return 'ret3334' 

@action('ctrl_act3335')
def ctrl_nm3335():
    return 'ret3335' 

@action('ctrl_act3336')
def ctrl_nm3336():
    return 'ret3336' 

@action('ctrl_act3337')
def ctrl_nm3337():
    return 'ret3337' 

@action('ctrl_act3338')
def ctrl_nm3338():
    return 'ret3338' 

@action('ctrl_act3339')
def ctrl_nm3339():
    return 'ret3339' 

@action('ctrl_act3340')
def ctrl_nm3340():
    return 'ret3340' 

@action('ctrl_act3341')
def ctrl_nm3341():
    return 'ret3341' 

@action('ctrl_act3342')
def ctrl_nm3342():
    return 'ret3342' 

@action('ctrl_act3343')
def ctrl_nm3343():
    return 'ret3343' 

@action('ctrl_act3344')
def ctrl_nm3344():
    return 'ret3344' 

@action('ctrl_act3345')
def ctrl_nm3345():
    return 'ret3345' 

@action('ctrl_act3346')
def ctrl_nm3346():
    return 'ret3346' 

@action('ctrl_act3347')
def ctrl_nm3347():
    return 'ret3347' 

@action('ctrl_act3348')
def ctrl_nm3348():
    return 'ret3348' 

@action('ctrl_act3349')
def ctrl_nm3349():
    return 'ret3349' 

@action('ctrl_act3350')
def ctrl_nm3350():
    return 'ret3350' 

@action('ctrl_act3351')
def ctrl_nm3351():
    return 'ret3351' 

@action('ctrl_act3352')
def ctrl_nm3352():
    return 'ret3352' 

@action('ctrl_act3353')
def ctrl_nm3353():
    return 'ret3353' 

@action('ctrl_act3354')
def ctrl_nm3354():
    return 'ret3354' 

@action('ctrl_act3355')
def ctrl_nm3355():
    return 'ret3355' 

@action('ctrl_act3356')
def ctrl_nm3356():
    return 'ret3356' 

@action('ctrl_act3357')
def ctrl_nm3357():
    return 'ret3357' 

@action('ctrl_act3358')
def ctrl_nm3358():
    return 'ret3358' 

@action('ctrl_act3359')
def ctrl_nm3359():
    return 'ret3359' 

@action('ctrl_act3360')
def ctrl_nm3360():
    return 'ret3360' 

@action('ctrl_act3361')
def ctrl_nm3361():
    return 'ret3361' 

@action('ctrl_act3362')
def ctrl_nm3362():
    return 'ret3362' 

@action('ctrl_act3363')
def ctrl_nm3363():
    return 'ret3363' 

@action('ctrl_act3364')
def ctrl_nm3364():
    return 'ret3364' 

@action('ctrl_act3365')
def ctrl_nm3365():
    return 'ret3365' 

@action('ctrl_act3366')
def ctrl_nm3366():
    return 'ret3366' 

@action('ctrl_act3367')
def ctrl_nm3367():
    return 'ret3367' 

@action('ctrl_act3368')
def ctrl_nm3368():
    return 'ret3368' 

@action('ctrl_act3369')
def ctrl_nm3369():
    return 'ret3369' 

@action('ctrl_act3370')
def ctrl_nm3370():
    return 'ret3370' 

@action('ctrl_act3371')
def ctrl_nm3371():
    return 'ret3371' 

@action('ctrl_act3372')
def ctrl_nm3372():
    return 'ret3372' 

@action('ctrl_act3373')
def ctrl_nm3373():
    return 'ret3373' 

@action('ctrl_act3374')
def ctrl_nm3374():
    return 'ret3374' 

@action('ctrl_act3375')
def ctrl_nm3375():
    return 'ret3375' 

@action('ctrl_act3376')
def ctrl_nm3376():
    return 'ret3376' 

@action('ctrl_act3377')
def ctrl_nm3377():
    return 'ret3377' 

@action('ctrl_act3378')
def ctrl_nm3378():
    return 'ret3378' 

@action('ctrl_act3379')
def ctrl_nm3379():
    return 'ret3379' 

@action('ctrl_act3380')
def ctrl_nm3380():
    return 'ret3380' 

@action('ctrl_act3381')
def ctrl_nm3381():
    return 'ret3381' 

@action('ctrl_act3382')
def ctrl_nm3382():
    return 'ret3382' 

@action('ctrl_act3383')
def ctrl_nm3383():
    return 'ret3383' 

@action('ctrl_act3384')
def ctrl_nm3384():
    return 'ret3384' 

@action('ctrl_act3385')
def ctrl_nm3385():
    return 'ret3385' 

@action('ctrl_act3386')
def ctrl_nm3386():
    return 'ret3386' 

@action('ctrl_act3387')
def ctrl_nm3387():
    return 'ret3387' 

@action('ctrl_act3388')
def ctrl_nm3388():
    return 'ret3388' 

@action('ctrl_act3389')
def ctrl_nm3389():
    return 'ret3389' 

@action('ctrl_act3390')
def ctrl_nm3390():
    return 'ret3390' 

@action('ctrl_act3391')
def ctrl_nm3391():
    return 'ret3391' 

@action('ctrl_act3392')
def ctrl_nm3392():
    return 'ret3392' 

@action('ctrl_act3393')
def ctrl_nm3393():
    return 'ret3393' 

@action('ctrl_act3394')
def ctrl_nm3394():
    return 'ret3394' 

@action('ctrl_act3395')
def ctrl_nm3395():
    return 'ret3395' 

@action('ctrl_act3396')
def ctrl_nm3396():
    return 'ret3396' 

@action('ctrl_act3397')
def ctrl_nm3397():
    return 'ret3397' 

@action('ctrl_act3398')
def ctrl_nm3398():
    return 'ret3398' 

@action('ctrl_act3399')
def ctrl_nm3399():
    return 'ret3399' 

@action('ctrl_act3400')
def ctrl_nm3400():
    return 'ret3400' 

@action('ctrl_act3401')
def ctrl_nm3401():
    return 'ret3401' 

@action('ctrl_act3402')
def ctrl_nm3402():
    return 'ret3402' 

@action('ctrl_act3403')
def ctrl_nm3403():
    return 'ret3403' 

@action('ctrl_act3404')
def ctrl_nm3404():
    return 'ret3404' 

@action('ctrl_act3405')
def ctrl_nm3405():
    return 'ret3405' 

@action('ctrl_act3406')
def ctrl_nm3406():
    return 'ret3406' 

@action('ctrl_act3407')
def ctrl_nm3407():
    return 'ret3407' 

@action('ctrl_act3408')
def ctrl_nm3408():
    return 'ret3408' 

@action('ctrl_act3409')
def ctrl_nm3409():
    return 'ret3409' 

@action('ctrl_act3410')
def ctrl_nm3410():
    return 'ret3410' 

@action('ctrl_act3411')
def ctrl_nm3411():
    return 'ret3411' 

@action('ctrl_act3412')
def ctrl_nm3412():
    return 'ret3412' 

@action('ctrl_act3413')
def ctrl_nm3413():
    return 'ret3413' 

@action('ctrl_act3414')
def ctrl_nm3414():
    return 'ret3414' 

@action('ctrl_act3415')
def ctrl_nm3415():
    return 'ret3415' 

@action('ctrl_act3416')
def ctrl_nm3416():
    return 'ret3416' 

@action('ctrl_act3417')
def ctrl_nm3417():
    return 'ret3417' 

@action('ctrl_act3418')
def ctrl_nm3418():
    return 'ret3418' 

@action('ctrl_act3419')
def ctrl_nm3419():
    return 'ret3419' 

@action('ctrl_act3420')
def ctrl_nm3420():
    return 'ret3420' 

@action('ctrl_act3421')
def ctrl_nm3421():
    return 'ret3421' 

@action('ctrl_act3422')
def ctrl_nm3422():
    return 'ret3422' 

@action('ctrl_act3423')
def ctrl_nm3423():
    return 'ret3423' 

@action('ctrl_act3424')
def ctrl_nm3424():
    return 'ret3424' 

@action('ctrl_act3425')
def ctrl_nm3425():
    return 'ret3425' 

@action('ctrl_act3426')
def ctrl_nm3426():
    return 'ret3426' 

@action('ctrl_act3427')
def ctrl_nm3427():
    return 'ret3427' 

@action('ctrl_act3428')
def ctrl_nm3428():
    return 'ret3428' 

@action('ctrl_act3429')
def ctrl_nm3429():
    return 'ret3429' 

@action('ctrl_act3430')
def ctrl_nm3430():
    return 'ret3430' 

@action('ctrl_act3431')
def ctrl_nm3431():
    return 'ret3431' 

@action('ctrl_act3432')
def ctrl_nm3432():
    return 'ret3432' 

@action('ctrl_act3433')
def ctrl_nm3433():
    return 'ret3433' 

@action('ctrl_act3434')
def ctrl_nm3434():
    return 'ret3434' 

@action('ctrl_act3435')
def ctrl_nm3435():
    return 'ret3435' 

@action('ctrl_act3436')
def ctrl_nm3436():
    return 'ret3436' 

@action('ctrl_act3437')
def ctrl_nm3437():
    return 'ret3437' 

@action('ctrl_act3438')
def ctrl_nm3438():
    return 'ret3438' 

@action('ctrl_act3439')
def ctrl_nm3439():
    return 'ret3439' 

@action('ctrl_act3440')
def ctrl_nm3440():
    return 'ret3440' 

@action('ctrl_act3441')
def ctrl_nm3441():
    return 'ret3441' 

@action('ctrl_act3442')
def ctrl_nm3442():
    return 'ret3442' 

@action('ctrl_act3443')
def ctrl_nm3443():
    return 'ret3443' 

@action('ctrl_act3444')
def ctrl_nm3444():
    return 'ret3444' 

@action('ctrl_act3445')
def ctrl_nm3445():
    return 'ret3445' 

@action('ctrl_act3446')
def ctrl_nm3446():
    return 'ret3446' 

@action('ctrl_act3447')
def ctrl_nm3447():
    return 'ret3447' 

@action('ctrl_act3448')
def ctrl_nm3448():
    return 'ret3448' 

@action('ctrl_act3449')
def ctrl_nm3449():
    return 'ret3449' 

@action('ctrl_act3450')
def ctrl_nm3450():
    return 'ret3450' 

@action('ctrl_act3451')
def ctrl_nm3451():
    return 'ret3451' 

@action('ctrl_act3452')
def ctrl_nm3452():
    return 'ret3452' 

@action('ctrl_act3453')
def ctrl_nm3453():
    return 'ret3453' 

@action('ctrl_act3454')
def ctrl_nm3454():
    return 'ret3454' 

@action('ctrl_act3455')
def ctrl_nm3455():
    return 'ret3455' 

@action('ctrl_act3456')
def ctrl_nm3456():
    return 'ret3456' 

@action('ctrl_act3457')
def ctrl_nm3457():
    return 'ret3457' 

@action('ctrl_act3458')
def ctrl_nm3458():
    return 'ret3458' 

@action('ctrl_act3459')
def ctrl_nm3459():
    return 'ret3459' 

@action('ctrl_act3460')
def ctrl_nm3460():
    return 'ret3460' 

@action('ctrl_act3461')
def ctrl_nm3461():
    return 'ret3461' 

@action('ctrl_act3462')
def ctrl_nm3462():
    return 'ret3462' 

@action('ctrl_act3463')
def ctrl_nm3463():
    return 'ret3463' 

@action('ctrl_act3464')
def ctrl_nm3464():
    return 'ret3464' 

@action('ctrl_act3465')
def ctrl_nm3465():
    return 'ret3465' 

@action('ctrl_act3466')
def ctrl_nm3466():
    return 'ret3466' 

@action('ctrl_act3467')
def ctrl_nm3467():
    return 'ret3467' 

@action('ctrl_act3468')
def ctrl_nm3468():
    return 'ret3468' 

@action('ctrl_act3469')
def ctrl_nm3469():
    return 'ret3469' 

@action('ctrl_act3470')
def ctrl_nm3470():
    return 'ret3470' 

@action('ctrl_act3471')
def ctrl_nm3471():
    return 'ret3471' 

@action('ctrl_act3472')
def ctrl_nm3472():
    return 'ret3472' 

@action('ctrl_act3473')
def ctrl_nm3473():
    return 'ret3473' 

@action('ctrl_act3474')
def ctrl_nm3474():
    return 'ret3474' 

@action('ctrl_act3475')
def ctrl_nm3475():
    return 'ret3475' 

@action('ctrl_act3476')
def ctrl_nm3476():
    return 'ret3476' 

@action('ctrl_act3477')
def ctrl_nm3477():
    return 'ret3477' 

@action('ctrl_act3478')
def ctrl_nm3478():
    return 'ret3478' 

@action('ctrl_act3479')
def ctrl_nm3479():
    return 'ret3479' 

@action('ctrl_act3480')
def ctrl_nm3480():
    return 'ret3480' 

@action('ctrl_act3481')
def ctrl_nm3481():
    return 'ret3481' 

@action('ctrl_act3482')
def ctrl_nm3482():
    return 'ret3482' 

@action('ctrl_act3483')
def ctrl_nm3483():
    return 'ret3483' 

@action('ctrl_act3484')
def ctrl_nm3484():
    return 'ret3484' 

@action('ctrl_act3485')
def ctrl_nm3485():
    return 'ret3485' 

@action('ctrl_act3486')
def ctrl_nm3486():
    return 'ret3486' 

@action('ctrl_act3487')
def ctrl_nm3487():
    return 'ret3487' 

@action('ctrl_act3488')
def ctrl_nm3488():
    return 'ret3488' 

@action('ctrl_act3489')
def ctrl_nm3489():
    return 'ret3489' 

@action('ctrl_act3490')
def ctrl_nm3490():
    return 'ret3490' 

@action('ctrl_act3491')
def ctrl_nm3491():
    return 'ret3491' 

@action('ctrl_act3492')
def ctrl_nm3492():
    return 'ret3492' 

@action('ctrl_act3493')
def ctrl_nm3493():
    return 'ret3493' 

@action('ctrl_act3494')
def ctrl_nm3494():
    return 'ret3494' 

@action('ctrl_act3495')
def ctrl_nm3495():
    return 'ret3495' 

@action('ctrl_act3496')
def ctrl_nm3496():
    return 'ret3496' 

@action('ctrl_act3497')
def ctrl_nm3497():
    return 'ret3497' 

@action('ctrl_act3498')
def ctrl_nm3498():
    return 'ret3498' 

@action('ctrl_act3499')
def ctrl_nm3499():
    return 'ret3499' 

@action('ctrl_act3500')
def ctrl_nm3500():
    return 'ret3500' 

@action('ctrl_act3501')
def ctrl_nm3501():
    return 'ret3501' 

@action('ctrl_act3502')
def ctrl_nm3502():
    return 'ret3502' 

@action('ctrl_act3503')
def ctrl_nm3503():
    return 'ret3503' 

@action('ctrl_act3504')
def ctrl_nm3504():
    return 'ret3504' 

@action('ctrl_act3505')
def ctrl_nm3505():
    return 'ret3505' 

@action('ctrl_act3506')
def ctrl_nm3506():
    return 'ret3506' 

@action('ctrl_act3507')
def ctrl_nm3507():
    return 'ret3507' 

@action('ctrl_act3508')
def ctrl_nm3508():
    return 'ret3508' 

@action('ctrl_act3509')
def ctrl_nm3509():
    return 'ret3509' 

@action('ctrl_act3510')
def ctrl_nm3510():
    return 'ret3510' 

@action('ctrl_act3511')
def ctrl_nm3511():
    return 'ret3511' 

@action('ctrl_act3512')
def ctrl_nm3512():
    return 'ret3512' 

@action('ctrl_act3513')
def ctrl_nm3513():
    return 'ret3513' 

@action('ctrl_act3514')
def ctrl_nm3514():
    return 'ret3514' 

@action('ctrl_act3515')
def ctrl_nm3515():
    return 'ret3515' 

@action('ctrl_act3516')
def ctrl_nm3516():
    return 'ret3516' 

@action('ctrl_act3517')
def ctrl_nm3517():
    return 'ret3517' 

@action('ctrl_act3518')
def ctrl_nm3518():
    return 'ret3518' 

@action('ctrl_act3519')
def ctrl_nm3519():
    return 'ret3519' 

@action('ctrl_act3520')
def ctrl_nm3520():
    return 'ret3520' 

@action('ctrl_act3521')
def ctrl_nm3521():
    return 'ret3521' 

@action('ctrl_act3522')
def ctrl_nm3522():
    return 'ret3522' 

@action('ctrl_act3523')
def ctrl_nm3523():
    return 'ret3523' 

@action('ctrl_act3524')
def ctrl_nm3524():
    return 'ret3524' 

@action('ctrl_act3525')
def ctrl_nm3525():
    return 'ret3525' 

@action('ctrl_act3526')
def ctrl_nm3526():
    return 'ret3526' 

@action('ctrl_act3527')
def ctrl_nm3527():
    return 'ret3527' 

@action('ctrl_act3528')
def ctrl_nm3528():
    return 'ret3528' 

@action('ctrl_act3529')
def ctrl_nm3529():
    return 'ret3529' 

@action('ctrl_act3530')
def ctrl_nm3530():
    return 'ret3530' 

@action('ctrl_act3531')
def ctrl_nm3531():
    return 'ret3531' 

@action('ctrl_act3532')
def ctrl_nm3532():
    return 'ret3532' 

@action('ctrl_act3533')
def ctrl_nm3533():
    return 'ret3533' 

@action('ctrl_act3534')
def ctrl_nm3534():
    return 'ret3534' 

@action('ctrl_act3535')
def ctrl_nm3535():
    return 'ret3535' 

@action('ctrl_act3536')
def ctrl_nm3536():
    return 'ret3536' 

@action('ctrl_act3537')
def ctrl_nm3537():
    return 'ret3537' 

@action('ctrl_act3538')
def ctrl_nm3538():
    return 'ret3538' 

@action('ctrl_act3539')
def ctrl_nm3539():
    return 'ret3539' 

@action('ctrl_act3540')
def ctrl_nm3540():
    return 'ret3540' 

@action('ctrl_act3541')
def ctrl_nm3541():
    return 'ret3541' 

@action('ctrl_act3542')
def ctrl_nm3542():
    return 'ret3542' 

@action('ctrl_act3543')
def ctrl_nm3543():
    return 'ret3543' 

@action('ctrl_act3544')
def ctrl_nm3544():
    return 'ret3544' 

@action('ctrl_act3545')
def ctrl_nm3545():
    return 'ret3545' 

@action('ctrl_act3546')
def ctrl_nm3546():
    return 'ret3546' 

@action('ctrl_act3547')
def ctrl_nm3547():
    return 'ret3547' 

@action('ctrl_act3548')
def ctrl_nm3548():
    return 'ret3548' 

@action('ctrl_act3549')
def ctrl_nm3549():
    return 'ret3549' 

@action('ctrl_act3550')
def ctrl_nm3550():
    return 'ret3550' 

@action('ctrl_act3551')
def ctrl_nm3551():
    return 'ret3551' 

@action('ctrl_act3552')
def ctrl_nm3552():
    return 'ret3552' 

@action('ctrl_act3553')
def ctrl_nm3553():
    return 'ret3553' 

@action('ctrl_act3554')
def ctrl_nm3554():
    return 'ret3554' 

@action('ctrl_act3555')
def ctrl_nm3555():
    return 'ret3555' 

@action('ctrl_act3556')
def ctrl_nm3556():
    return 'ret3556' 

@action('ctrl_act3557')
def ctrl_nm3557():
    return 'ret3557' 

@action('ctrl_act3558')
def ctrl_nm3558():
    return 'ret3558' 

@action('ctrl_act3559')
def ctrl_nm3559():
    return 'ret3559' 

@action('ctrl_act3560')
def ctrl_nm3560():
    return 'ret3560' 

@action('ctrl_act3561')
def ctrl_nm3561():
    return 'ret3561' 

@action('ctrl_act3562')
def ctrl_nm3562():
    return 'ret3562' 

@action('ctrl_act3563')
def ctrl_nm3563():
    return 'ret3563' 

@action('ctrl_act3564')
def ctrl_nm3564():
    return 'ret3564' 

@action('ctrl_act3565')
def ctrl_nm3565():
    return 'ret3565' 

@action('ctrl_act3566')
def ctrl_nm3566():
    return 'ret3566' 

@action('ctrl_act3567')
def ctrl_nm3567():
    return 'ret3567' 

@action('ctrl_act3568')
def ctrl_nm3568():
    return 'ret3568' 

@action('ctrl_act3569')
def ctrl_nm3569():
    return 'ret3569' 

@action('ctrl_act3570')
def ctrl_nm3570():
    return 'ret3570' 

@action('ctrl_act3571')
def ctrl_nm3571():
    return 'ret3571' 

@action('ctrl_act3572')
def ctrl_nm3572():
    return 'ret3572' 

@action('ctrl_act3573')
def ctrl_nm3573():
    return 'ret3573' 

@action('ctrl_act3574')
def ctrl_nm3574():
    return 'ret3574' 

@action('ctrl_act3575')
def ctrl_nm3575():
    return 'ret3575' 

@action('ctrl_act3576')
def ctrl_nm3576():
    return 'ret3576' 

@action('ctrl_act3577')
def ctrl_nm3577():
    return 'ret3577' 

@action('ctrl_act3578')
def ctrl_nm3578():
    return 'ret3578' 

@action('ctrl_act3579')
def ctrl_nm3579():
    return 'ret3579' 

@action('ctrl_act3580')
def ctrl_nm3580():
    return 'ret3580' 

@action('ctrl_act3581')
def ctrl_nm3581():
    return 'ret3581' 

@action('ctrl_act3582')
def ctrl_nm3582():
    return 'ret3582' 

@action('ctrl_act3583')
def ctrl_nm3583():
    return 'ret3583' 

@action('ctrl_act3584')
def ctrl_nm3584():
    return 'ret3584' 

@action('ctrl_act3585')
def ctrl_nm3585():
    return 'ret3585' 

@action('ctrl_act3586')
def ctrl_nm3586():
    return 'ret3586' 

@action('ctrl_act3587')
def ctrl_nm3587():
    return 'ret3587' 

@action('ctrl_act3588')
def ctrl_nm3588():
    return 'ret3588' 

@action('ctrl_act3589')
def ctrl_nm3589():
    return 'ret3589' 

@action('ctrl_act3590')
def ctrl_nm3590():
    return 'ret3590' 

@action('ctrl_act3591')
def ctrl_nm3591():
    return 'ret3591' 

@action('ctrl_act3592')
def ctrl_nm3592():
    return 'ret3592' 

@action('ctrl_act3593')
def ctrl_nm3593():
    return 'ret3593' 

@action('ctrl_act3594')
def ctrl_nm3594():
    return 'ret3594' 

@action('ctrl_act3595')
def ctrl_nm3595():
    return 'ret3595' 

@action('ctrl_act3596')
def ctrl_nm3596():
    return 'ret3596' 

@action('ctrl_act3597')
def ctrl_nm3597():
    return 'ret3597' 

@action('ctrl_act3598')
def ctrl_nm3598():
    return 'ret3598' 

@action('ctrl_act3599')
def ctrl_nm3599():
    return 'ret3599' 

@action('ctrl_act3600')
def ctrl_nm3600():
    return 'ret3600' 

@action('ctrl_act3601')
def ctrl_nm3601():
    return 'ret3601' 

@action('ctrl_act3602')
def ctrl_nm3602():
    return 'ret3602' 

@action('ctrl_act3603')
def ctrl_nm3603():
    return 'ret3603' 

@action('ctrl_act3604')
def ctrl_nm3604():
    return 'ret3604' 

@action('ctrl_act3605')
def ctrl_nm3605():
    return 'ret3605' 

@action('ctrl_act3606')
def ctrl_nm3606():
    return 'ret3606' 

@action('ctrl_act3607')
def ctrl_nm3607():
    return 'ret3607' 

@action('ctrl_act3608')
def ctrl_nm3608():
    return 'ret3608' 

@action('ctrl_act3609')
def ctrl_nm3609():
    return 'ret3609' 

@action('ctrl_act3610')
def ctrl_nm3610():
    return 'ret3610' 

@action('ctrl_act3611')
def ctrl_nm3611():
    return 'ret3611' 

@action('ctrl_act3612')
def ctrl_nm3612():
    return 'ret3612' 

@action('ctrl_act3613')
def ctrl_nm3613():
    return 'ret3613' 

@action('ctrl_act3614')
def ctrl_nm3614():
    return 'ret3614' 

@action('ctrl_act3615')
def ctrl_nm3615():
    return 'ret3615' 

@action('ctrl_act3616')
def ctrl_nm3616():
    return 'ret3616' 

@action('ctrl_act3617')
def ctrl_nm3617():
    return 'ret3617' 

@action('ctrl_act3618')
def ctrl_nm3618():
    return 'ret3618' 

@action('ctrl_act3619')
def ctrl_nm3619():
    return 'ret3619' 

@action('ctrl_act3620')
def ctrl_nm3620():
    return 'ret3620' 

@action('ctrl_act3621')
def ctrl_nm3621():
    return 'ret3621' 

@action('ctrl_act3622')
def ctrl_nm3622():
    return 'ret3622' 

@action('ctrl_act3623')
def ctrl_nm3623():
    return 'ret3623' 

@action('ctrl_act3624')
def ctrl_nm3624():
    return 'ret3624' 

@action('ctrl_act3625')
def ctrl_nm3625():
    return 'ret3625' 

@action('ctrl_act3626')
def ctrl_nm3626():
    return 'ret3626' 

@action('ctrl_act3627')
def ctrl_nm3627():
    return 'ret3627' 

@action('ctrl_act3628')
def ctrl_nm3628():
    return 'ret3628' 

@action('ctrl_act3629')
def ctrl_nm3629():
    return 'ret3629' 

@action('ctrl_act3630')
def ctrl_nm3630():
    return 'ret3630' 

@action('ctrl_act3631')
def ctrl_nm3631():
    return 'ret3631' 

@action('ctrl_act3632')
def ctrl_nm3632():
    return 'ret3632' 

@action('ctrl_act3633')
def ctrl_nm3633():
    return 'ret3633' 

@action('ctrl_act3634')
def ctrl_nm3634():
    return 'ret3634' 

@action('ctrl_act3635')
def ctrl_nm3635():
    return 'ret3635' 

@action('ctrl_act3636')
def ctrl_nm3636():
    return 'ret3636' 

@action('ctrl_act3637')
def ctrl_nm3637():
    return 'ret3637' 

@action('ctrl_act3638')
def ctrl_nm3638():
    return 'ret3638' 

@action('ctrl_act3639')
def ctrl_nm3639():
    return 'ret3639' 

@action('ctrl_act3640')
def ctrl_nm3640():
    return 'ret3640' 

@action('ctrl_act3641')
def ctrl_nm3641():
    return 'ret3641' 

@action('ctrl_act3642')
def ctrl_nm3642():
    return 'ret3642' 

@action('ctrl_act3643')
def ctrl_nm3643():
    return 'ret3643' 

@action('ctrl_act3644')
def ctrl_nm3644():
    return 'ret3644' 

@action('ctrl_act3645')
def ctrl_nm3645():
    return 'ret3645' 

@action('ctrl_act3646')
def ctrl_nm3646():
    return 'ret3646' 

@action('ctrl_act3647')
def ctrl_nm3647():
    return 'ret3647' 

@action('ctrl_act3648')
def ctrl_nm3648():
    return 'ret3648' 

@action('ctrl_act3649')
def ctrl_nm3649():
    return 'ret3649' 

@action('ctrl_act3650')
def ctrl_nm3650():
    return 'ret3650' 

@action('ctrl_act3651')
def ctrl_nm3651():
    return 'ret3651' 

@action('ctrl_act3652')
def ctrl_nm3652():
    return 'ret3652' 

@action('ctrl_act3653')
def ctrl_nm3653():
    return 'ret3653' 

@action('ctrl_act3654')
def ctrl_nm3654():
    return 'ret3654' 

@action('ctrl_act3655')
def ctrl_nm3655():
    return 'ret3655' 

@action('ctrl_act3656')
def ctrl_nm3656():
    return 'ret3656' 

@action('ctrl_act3657')
def ctrl_nm3657():
    return 'ret3657' 

@action('ctrl_act3658')
def ctrl_nm3658():
    return 'ret3658' 

@action('ctrl_act3659')
def ctrl_nm3659():
    return 'ret3659' 

@action('ctrl_act3660')
def ctrl_nm3660():
    return 'ret3660' 

@action('ctrl_act3661')
def ctrl_nm3661():
    return 'ret3661' 

@action('ctrl_act3662')
def ctrl_nm3662():
    return 'ret3662' 

@action('ctrl_act3663')
def ctrl_nm3663():
    return 'ret3663' 

@action('ctrl_act3664')
def ctrl_nm3664():
    return 'ret3664' 

@action('ctrl_act3665')
def ctrl_nm3665():
    return 'ret3665' 

@action('ctrl_act3666')
def ctrl_nm3666():
    return 'ret3666' 

@action('ctrl_act3667')
def ctrl_nm3667():
    return 'ret3667' 

@action('ctrl_act3668')
def ctrl_nm3668():
    return 'ret3668' 

@action('ctrl_act3669')
def ctrl_nm3669():
    return 'ret3669' 

@action('ctrl_act3670')
def ctrl_nm3670():
    return 'ret3670' 

@action('ctrl_act3671')
def ctrl_nm3671():
    return 'ret3671' 

@action('ctrl_act3672')
def ctrl_nm3672():
    return 'ret3672' 

@action('ctrl_act3673')
def ctrl_nm3673():
    return 'ret3673' 

@action('ctrl_act3674')
def ctrl_nm3674():
    return 'ret3674' 

@action('ctrl_act3675')
def ctrl_nm3675():
    return 'ret3675' 

@action('ctrl_act3676')
def ctrl_nm3676():
    return 'ret3676' 

@action('ctrl_act3677')
def ctrl_nm3677():
    return 'ret3677' 

@action('ctrl_act3678')
def ctrl_nm3678():
    return 'ret3678' 

@action('ctrl_act3679')
def ctrl_nm3679():
    return 'ret3679' 

@action('ctrl_act3680')
def ctrl_nm3680():
    return 'ret3680' 

@action('ctrl_act3681')
def ctrl_nm3681():
    return 'ret3681' 

@action('ctrl_act3682')
def ctrl_nm3682():
    return 'ret3682' 

@action('ctrl_act3683')
def ctrl_nm3683():
    return 'ret3683' 

@action('ctrl_act3684')
def ctrl_nm3684():
    return 'ret3684' 

@action('ctrl_act3685')
def ctrl_nm3685():
    return 'ret3685' 

@action('ctrl_act3686')
def ctrl_nm3686():
    return 'ret3686' 

@action('ctrl_act3687')
def ctrl_nm3687():
    return 'ret3687' 

@action('ctrl_act3688')
def ctrl_nm3688():
    return 'ret3688' 

@action('ctrl_act3689')
def ctrl_nm3689():
    return 'ret3689' 

@action('ctrl_act3690')
def ctrl_nm3690():
    return 'ret3690' 

@action('ctrl_act3691')
def ctrl_nm3691():
    return 'ret3691' 

@action('ctrl_act3692')
def ctrl_nm3692():
    return 'ret3692' 

@action('ctrl_act3693')
def ctrl_nm3693():
    return 'ret3693' 

@action('ctrl_act3694')
def ctrl_nm3694():
    return 'ret3694' 

@action('ctrl_act3695')
def ctrl_nm3695():
    return 'ret3695' 

@action('ctrl_act3696')
def ctrl_nm3696():
    return 'ret3696' 

@action('ctrl_act3697')
def ctrl_nm3697():
    return 'ret3697' 

@action('ctrl_act3698')
def ctrl_nm3698():
    return 'ret3698' 

@action('ctrl_act3699')
def ctrl_nm3699():
    return 'ret3699' 

@action('ctrl_act3700')
def ctrl_nm3700():
    return 'ret3700' 

@action('ctrl_act3701')
def ctrl_nm3701():
    return 'ret3701' 

@action('ctrl_act3702')
def ctrl_nm3702():
    return 'ret3702' 

@action('ctrl_act3703')
def ctrl_nm3703():
    return 'ret3703' 

@action('ctrl_act3704')
def ctrl_nm3704():
    return 'ret3704' 

@action('ctrl_act3705')
def ctrl_nm3705():
    return 'ret3705' 

@action('ctrl_act3706')
def ctrl_nm3706():
    return 'ret3706' 

@action('ctrl_act3707')
def ctrl_nm3707():
    return 'ret3707' 

@action('ctrl_act3708')
def ctrl_nm3708():
    return 'ret3708' 

@action('ctrl_act3709')
def ctrl_nm3709():
    return 'ret3709' 

@action('ctrl_act3710')
def ctrl_nm3710():
    return 'ret3710' 

@action('ctrl_act3711')
def ctrl_nm3711():
    return 'ret3711' 

@action('ctrl_act3712')
def ctrl_nm3712():
    return 'ret3712' 

@action('ctrl_act3713')
def ctrl_nm3713():
    return 'ret3713' 

@action('ctrl_act3714')
def ctrl_nm3714():
    return 'ret3714' 

@action('ctrl_act3715')
def ctrl_nm3715():
    return 'ret3715' 

@action('ctrl_act3716')
def ctrl_nm3716():
    return 'ret3716' 

@action('ctrl_act3717')
def ctrl_nm3717():
    return 'ret3717' 

@action('ctrl_act3718')
def ctrl_nm3718():
    return 'ret3718' 

@action('ctrl_act3719')
def ctrl_nm3719():
    return 'ret3719' 

@action('ctrl_act3720')
def ctrl_nm3720():
    return 'ret3720' 

@action('ctrl_act3721')
def ctrl_nm3721():
    return 'ret3721' 

@action('ctrl_act3722')
def ctrl_nm3722():
    return 'ret3722' 

@action('ctrl_act3723')
def ctrl_nm3723():
    return 'ret3723' 

@action('ctrl_act3724')
def ctrl_nm3724():
    return 'ret3724' 

@action('ctrl_act3725')
def ctrl_nm3725():
    return 'ret3725' 

@action('ctrl_act3726')
def ctrl_nm3726():
    return 'ret3726' 

@action('ctrl_act3727')
def ctrl_nm3727():
    return 'ret3727' 

@action('ctrl_act3728')
def ctrl_nm3728():
    return 'ret3728' 

@action('ctrl_act3729')
def ctrl_nm3729():
    return 'ret3729' 

@action('ctrl_act3730')
def ctrl_nm3730():
    return 'ret3730' 

@action('ctrl_act3731')
def ctrl_nm3731():
    return 'ret3731' 

@action('ctrl_act3732')
def ctrl_nm3732():
    return 'ret3732' 

@action('ctrl_act3733')
def ctrl_nm3733():
    return 'ret3733' 

@action('ctrl_act3734')
def ctrl_nm3734():
    return 'ret3734' 

@action('ctrl_act3735')
def ctrl_nm3735():
    return 'ret3735' 

@action('ctrl_act3736')
def ctrl_nm3736():
    return 'ret3736' 

@action('ctrl_act3737')
def ctrl_nm3737():
    return 'ret3737' 

@action('ctrl_act3738')
def ctrl_nm3738():
    return 'ret3738' 

@action('ctrl_act3739')
def ctrl_nm3739():
    return 'ret3739' 

@action('ctrl_act3740')
def ctrl_nm3740():
    return 'ret3740' 

@action('ctrl_act3741')
def ctrl_nm3741():
    return 'ret3741' 

@action('ctrl_act3742')
def ctrl_nm3742():
    return 'ret3742' 

@action('ctrl_act3743')
def ctrl_nm3743():
    return 'ret3743' 

@action('ctrl_act3744')
def ctrl_nm3744():
    return 'ret3744' 

@action('ctrl_act3745')
def ctrl_nm3745():
    return 'ret3745' 

@action('ctrl_act3746')
def ctrl_nm3746():
    return 'ret3746' 

@action('ctrl_act3747')
def ctrl_nm3747():
    return 'ret3747' 

@action('ctrl_act3748')
def ctrl_nm3748():
    return 'ret3748' 

@action('ctrl_act3749')
def ctrl_nm3749():
    return 'ret3749' 

@action('ctrl_act3750')
def ctrl_nm3750():
    return 'ret3750' 

@action('ctrl_act3751')
def ctrl_nm3751():
    return 'ret3751' 

@action('ctrl_act3752')
def ctrl_nm3752():
    return 'ret3752' 

@action('ctrl_act3753')
def ctrl_nm3753():
    return 'ret3753' 

@action('ctrl_act3754')
def ctrl_nm3754():
    return 'ret3754' 

@action('ctrl_act3755')
def ctrl_nm3755():
    return 'ret3755' 

@action('ctrl_act3756')
def ctrl_nm3756():
    return 'ret3756' 

@action('ctrl_act3757')
def ctrl_nm3757():
    return 'ret3757' 

@action('ctrl_act3758')
def ctrl_nm3758():
    return 'ret3758' 

@action('ctrl_act3759')
def ctrl_nm3759():
    return 'ret3759' 

@action('ctrl_act3760')
def ctrl_nm3760():
    return 'ret3760' 

@action('ctrl_act3761')
def ctrl_nm3761():
    return 'ret3761' 

@action('ctrl_act3762')
def ctrl_nm3762():
    return 'ret3762' 

@action('ctrl_act3763')
def ctrl_nm3763():
    return 'ret3763' 

@action('ctrl_act3764')
def ctrl_nm3764():
    return 'ret3764' 

@action('ctrl_act3765')
def ctrl_nm3765():
    return 'ret3765' 

@action('ctrl_act3766')
def ctrl_nm3766():
    return 'ret3766' 

@action('ctrl_act3767')
def ctrl_nm3767():
    return 'ret3767' 

@action('ctrl_act3768')
def ctrl_nm3768():
    return 'ret3768' 

@action('ctrl_act3769')
def ctrl_nm3769():
    return 'ret3769' 

@action('ctrl_act3770')
def ctrl_nm3770():
    return 'ret3770' 

@action('ctrl_act3771')
def ctrl_nm3771():
    return 'ret3771' 

@action('ctrl_act3772')
def ctrl_nm3772():
    return 'ret3772' 

@action('ctrl_act3773')
def ctrl_nm3773():
    return 'ret3773' 

@action('ctrl_act3774')
def ctrl_nm3774():
    return 'ret3774' 

@action('ctrl_act3775')
def ctrl_nm3775():
    return 'ret3775' 

@action('ctrl_act3776')
def ctrl_nm3776():
    return 'ret3776' 

@action('ctrl_act3777')
def ctrl_nm3777():
    return 'ret3777' 

@action('ctrl_act3778')
def ctrl_nm3778():
    return 'ret3778' 

@action('ctrl_act3779')
def ctrl_nm3779():
    return 'ret3779' 

@action('ctrl_act3780')
def ctrl_nm3780():
    return 'ret3780' 

@action('ctrl_act3781')
def ctrl_nm3781():
    return 'ret3781' 

@action('ctrl_act3782')
def ctrl_nm3782():
    return 'ret3782' 

@action('ctrl_act3783')
def ctrl_nm3783():
    return 'ret3783' 

@action('ctrl_act3784')
def ctrl_nm3784():
    return 'ret3784' 

@action('ctrl_act3785')
def ctrl_nm3785():
    return 'ret3785' 

@action('ctrl_act3786')
def ctrl_nm3786():
    return 'ret3786' 

@action('ctrl_act3787')
def ctrl_nm3787():
    return 'ret3787' 

@action('ctrl_act3788')
def ctrl_nm3788():
    return 'ret3788' 

@action('ctrl_act3789')
def ctrl_nm3789():
    return 'ret3789' 

@action('ctrl_act3790')
def ctrl_nm3790():
    return 'ret3790' 

@action('ctrl_act3791')
def ctrl_nm3791():
    return 'ret3791' 

@action('ctrl_act3792')
def ctrl_nm3792():
    return 'ret3792' 

@action('ctrl_act3793')
def ctrl_nm3793():
    return 'ret3793' 

@action('ctrl_act3794')
def ctrl_nm3794():
    return 'ret3794' 

@action('ctrl_act3795')
def ctrl_nm3795():
    return 'ret3795' 

@action('ctrl_act3796')
def ctrl_nm3796():
    return 'ret3796' 

@action('ctrl_act3797')
def ctrl_nm3797():
    return 'ret3797' 

@action('ctrl_act3798')
def ctrl_nm3798():
    return 'ret3798' 

@action('ctrl_act3799')
def ctrl_nm3799():
    return 'ret3799' 

@action('ctrl_act3800')
def ctrl_nm3800():
    return 'ret3800' 

@action('ctrl_act3801')
def ctrl_nm3801():
    return 'ret3801' 

@action('ctrl_act3802')
def ctrl_nm3802():
    return 'ret3802' 

@action('ctrl_act3803')
def ctrl_nm3803():
    return 'ret3803' 

@action('ctrl_act3804')
def ctrl_nm3804():
    return 'ret3804' 

@action('ctrl_act3805')
def ctrl_nm3805():
    return 'ret3805' 

@action('ctrl_act3806')
def ctrl_nm3806():
    return 'ret3806' 

@action('ctrl_act3807')
def ctrl_nm3807():
    return 'ret3807' 

@action('ctrl_act3808')
def ctrl_nm3808():
    return 'ret3808' 

@action('ctrl_act3809')
def ctrl_nm3809():
    return 'ret3809' 

@action('ctrl_act3810')
def ctrl_nm3810():
    return 'ret3810' 

@action('ctrl_act3811')
def ctrl_nm3811():
    return 'ret3811' 

@action('ctrl_act3812')
def ctrl_nm3812():
    return 'ret3812' 

@action('ctrl_act3813')
def ctrl_nm3813():
    return 'ret3813' 

@action('ctrl_act3814')
def ctrl_nm3814():
    return 'ret3814' 

@action('ctrl_act3815')
def ctrl_nm3815():
    return 'ret3815' 

@action('ctrl_act3816')
def ctrl_nm3816():
    return 'ret3816' 

@action('ctrl_act3817')
def ctrl_nm3817():
    return 'ret3817' 

@action('ctrl_act3818')
def ctrl_nm3818():
    return 'ret3818' 

@action('ctrl_act3819')
def ctrl_nm3819():
    return 'ret3819' 

@action('ctrl_act3820')
def ctrl_nm3820():
    return 'ret3820' 

@action('ctrl_act3821')
def ctrl_nm3821():
    return 'ret3821' 

@action('ctrl_act3822')
def ctrl_nm3822():
    return 'ret3822' 

@action('ctrl_act3823')
def ctrl_nm3823():
    return 'ret3823' 

@action('ctrl_act3824')
def ctrl_nm3824():
    return 'ret3824' 

@action('ctrl_act3825')
def ctrl_nm3825():
    return 'ret3825' 

@action('ctrl_act3826')
def ctrl_nm3826():
    return 'ret3826' 

@action('ctrl_act3827')
def ctrl_nm3827():
    return 'ret3827' 

@action('ctrl_act3828')
def ctrl_nm3828():
    return 'ret3828' 

@action('ctrl_act3829')
def ctrl_nm3829():
    return 'ret3829' 

@action('ctrl_act3830')
def ctrl_nm3830():
    return 'ret3830' 

@action('ctrl_act3831')
def ctrl_nm3831():
    return 'ret3831' 

@action('ctrl_act3832')
def ctrl_nm3832():
    return 'ret3832' 

@action('ctrl_act3833')
def ctrl_nm3833():
    return 'ret3833' 

@action('ctrl_act3834')
def ctrl_nm3834():
    return 'ret3834' 

@action('ctrl_act3835')
def ctrl_nm3835():
    return 'ret3835' 

@action('ctrl_act3836')
def ctrl_nm3836():
    return 'ret3836' 

@action('ctrl_act3837')
def ctrl_nm3837():
    return 'ret3837' 

@action('ctrl_act3838')
def ctrl_nm3838():
    return 'ret3838' 

@action('ctrl_act3839')
def ctrl_nm3839():
    return 'ret3839' 

@action('ctrl_act3840')
def ctrl_nm3840():
    return 'ret3840' 

@action('ctrl_act3841')
def ctrl_nm3841():
    return 'ret3841' 

@action('ctrl_act3842')
def ctrl_nm3842():
    return 'ret3842' 

@action('ctrl_act3843')
def ctrl_nm3843():
    return 'ret3843' 

@action('ctrl_act3844')
def ctrl_nm3844():
    return 'ret3844' 

@action('ctrl_act3845')
def ctrl_nm3845():
    return 'ret3845' 

@action('ctrl_act3846')
def ctrl_nm3846():
    return 'ret3846' 

@action('ctrl_act3847')
def ctrl_nm3847():
    return 'ret3847' 

@action('ctrl_act3848')
def ctrl_nm3848():
    return 'ret3848' 

@action('ctrl_act3849')
def ctrl_nm3849():
    return 'ret3849' 

@action('ctrl_act3850')
def ctrl_nm3850():
    return 'ret3850' 

@action('ctrl_act3851')
def ctrl_nm3851():
    return 'ret3851' 

@action('ctrl_act3852')
def ctrl_nm3852():
    return 'ret3852' 

@action('ctrl_act3853')
def ctrl_nm3853():
    return 'ret3853' 

@action('ctrl_act3854')
def ctrl_nm3854():
    return 'ret3854' 

@action('ctrl_act3855')
def ctrl_nm3855():
    return 'ret3855' 

@action('ctrl_act3856')
def ctrl_nm3856():
    return 'ret3856' 

@action('ctrl_act3857')
def ctrl_nm3857():
    return 'ret3857' 

@action('ctrl_act3858')
def ctrl_nm3858():
    return 'ret3858' 

@action('ctrl_act3859')
def ctrl_nm3859():
    return 'ret3859' 

@action('ctrl_act3860')
def ctrl_nm3860():
    return 'ret3860' 

@action('ctrl_act3861')
def ctrl_nm3861():
    return 'ret3861' 

@action('ctrl_act3862')
def ctrl_nm3862():
    return 'ret3862' 

@action('ctrl_act3863')
def ctrl_nm3863():
    return 'ret3863' 

@action('ctrl_act3864')
def ctrl_nm3864():
    return 'ret3864' 

@action('ctrl_act3865')
def ctrl_nm3865():
    return 'ret3865' 

@action('ctrl_act3866')
def ctrl_nm3866():
    return 'ret3866' 

@action('ctrl_act3867')
def ctrl_nm3867():
    return 'ret3867' 

@action('ctrl_act3868')
def ctrl_nm3868():
    return 'ret3868' 

@action('ctrl_act3869')
def ctrl_nm3869():
    return 'ret3869' 

@action('ctrl_act3870')
def ctrl_nm3870():
    return 'ret3870' 

@action('ctrl_act3871')
def ctrl_nm3871():
    return 'ret3871' 

@action('ctrl_act3872')
def ctrl_nm3872():
    return 'ret3872' 

@action('ctrl_act3873')
def ctrl_nm3873():
    return 'ret3873' 

@action('ctrl_act3874')
def ctrl_nm3874():
    return 'ret3874' 

@action('ctrl_act3875')
def ctrl_nm3875():
    return 'ret3875' 

@action('ctrl_act3876')
def ctrl_nm3876():
    return 'ret3876' 

@action('ctrl_act3877')
def ctrl_nm3877():
    return 'ret3877' 

@action('ctrl_act3878')
def ctrl_nm3878():
    return 'ret3878' 

@action('ctrl_act3879')
def ctrl_nm3879():
    return 'ret3879' 

@action('ctrl_act3880')
def ctrl_nm3880():
    return 'ret3880' 

@action('ctrl_act3881')
def ctrl_nm3881():
    return 'ret3881' 

@action('ctrl_act3882')
def ctrl_nm3882():
    return 'ret3882' 

@action('ctrl_act3883')
def ctrl_nm3883():
    return 'ret3883' 

@action('ctrl_act3884')
def ctrl_nm3884():
    return 'ret3884' 

@action('ctrl_act3885')
def ctrl_nm3885():
    return 'ret3885' 

@action('ctrl_act3886')
def ctrl_nm3886():
    return 'ret3886' 

@action('ctrl_act3887')
def ctrl_nm3887():
    return 'ret3887' 

@action('ctrl_act3888')
def ctrl_nm3888():
    return 'ret3888' 

@action('ctrl_act3889')
def ctrl_nm3889():
    return 'ret3889' 

@action('ctrl_act3890')
def ctrl_nm3890():
    return 'ret3890' 

@action('ctrl_act3891')
def ctrl_nm3891():
    return 'ret3891' 

@action('ctrl_act3892')
def ctrl_nm3892():
    return 'ret3892' 

@action('ctrl_act3893')
def ctrl_nm3893():
    return 'ret3893' 

@action('ctrl_act3894')
def ctrl_nm3894():
    return 'ret3894' 

@action('ctrl_act3895')
def ctrl_nm3895():
    return 'ret3895' 

@action('ctrl_act3896')
def ctrl_nm3896():
    return 'ret3896' 

@action('ctrl_act3897')
def ctrl_nm3897():
    return 'ret3897' 

@action('ctrl_act3898')
def ctrl_nm3898():
    return 'ret3898' 

@action('ctrl_act3899')
def ctrl_nm3899():
    return 'ret3899' 

@action('ctrl_act3900')
def ctrl_nm3900():
    return 'ret3900' 

@action('ctrl_act3901')
def ctrl_nm3901():
    return 'ret3901' 

@action('ctrl_act3902')
def ctrl_nm3902():
    return 'ret3902' 

@action('ctrl_act3903')
def ctrl_nm3903():
    return 'ret3903' 

@action('ctrl_act3904')
def ctrl_nm3904():
    return 'ret3904' 

@action('ctrl_act3905')
def ctrl_nm3905():
    return 'ret3905' 

@action('ctrl_act3906')
def ctrl_nm3906():
    return 'ret3906' 

@action('ctrl_act3907')
def ctrl_nm3907():
    return 'ret3907' 

@action('ctrl_act3908')
def ctrl_nm3908():
    return 'ret3908' 

@action('ctrl_act3909')
def ctrl_nm3909():
    return 'ret3909' 

@action('ctrl_act3910')
def ctrl_nm3910():
    return 'ret3910' 

@action('ctrl_act3911')
def ctrl_nm3911():
    return 'ret3911' 

@action('ctrl_act3912')
def ctrl_nm3912():
    return 'ret3912' 

@action('ctrl_act3913')
def ctrl_nm3913():
    return 'ret3913' 

@action('ctrl_act3914')
def ctrl_nm3914():
    return 'ret3914' 

@action('ctrl_act3915')
def ctrl_nm3915():
    return 'ret3915' 

@action('ctrl_act3916')
def ctrl_nm3916():
    return 'ret3916' 

@action('ctrl_act3917')
def ctrl_nm3917():
    return 'ret3917' 

@action('ctrl_act3918')
def ctrl_nm3918():
    return 'ret3918' 

@action('ctrl_act3919')
def ctrl_nm3919():
    return 'ret3919' 

@action('ctrl_act3920')
def ctrl_nm3920():
    return 'ret3920' 

@action('ctrl_act3921')
def ctrl_nm3921():
    return 'ret3921' 

@action('ctrl_act3922')
def ctrl_nm3922():
    return 'ret3922' 

@action('ctrl_act3923')
def ctrl_nm3923():
    return 'ret3923' 

@action('ctrl_act3924')
def ctrl_nm3924():
    return 'ret3924' 

@action('ctrl_act3925')
def ctrl_nm3925():
    return 'ret3925' 

@action('ctrl_act3926')
def ctrl_nm3926():
    return 'ret3926' 

@action('ctrl_act3927')
def ctrl_nm3927():
    return 'ret3927' 

@action('ctrl_act3928')
def ctrl_nm3928():
    return 'ret3928' 

@action('ctrl_act3929')
def ctrl_nm3929():
    return 'ret3929' 

@action('ctrl_act3930')
def ctrl_nm3930():
    return 'ret3930' 

@action('ctrl_act3931')
def ctrl_nm3931():
    return 'ret3931' 

@action('ctrl_act3932')
def ctrl_nm3932():
    return 'ret3932' 

@action('ctrl_act3933')
def ctrl_nm3933():
    return 'ret3933' 

@action('ctrl_act3934')
def ctrl_nm3934():
    return 'ret3934' 

@action('ctrl_act3935')
def ctrl_nm3935():
    return 'ret3935' 

@action('ctrl_act3936')
def ctrl_nm3936():
    return 'ret3936' 

@action('ctrl_act3937')
def ctrl_nm3937():
    return 'ret3937' 

@action('ctrl_act3938')
def ctrl_nm3938():
    return 'ret3938' 

@action('ctrl_act3939')
def ctrl_nm3939():
    return 'ret3939' 

@action('ctrl_act3940')
def ctrl_nm3940():
    return 'ret3940' 

@action('ctrl_act3941')
def ctrl_nm3941():
    return 'ret3941' 

@action('ctrl_act3942')
def ctrl_nm3942():
    return 'ret3942' 

@action('ctrl_act3943')
def ctrl_nm3943():
    return 'ret3943' 

@action('ctrl_act3944')
def ctrl_nm3944():
    return 'ret3944' 

@action('ctrl_act3945')
def ctrl_nm3945():
    return 'ret3945' 

@action('ctrl_act3946')
def ctrl_nm3946():
    return 'ret3946' 

@action('ctrl_act3947')
def ctrl_nm3947():
    return 'ret3947' 

@action('ctrl_act3948')
def ctrl_nm3948():
    return 'ret3948' 

@action('ctrl_act3949')
def ctrl_nm3949():
    return 'ret3949' 

@action('ctrl_act3950')
def ctrl_nm3950():
    return 'ret3950' 

@action('ctrl_act3951')
def ctrl_nm3951():
    return 'ret3951' 

@action('ctrl_act3952')
def ctrl_nm3952():
    return 'ret3952' 

@action('ctrl_act3953')
def ctrl_nm3953():
    return 'ret3953' 

@action('ctrl_act3954')
def ctrl_nm3954():
    return 'ret3954' 

@action('ctrl_act3955')
def ctrl_nm3955():
    return 'ret3955' 

@action('ctrl_act3956')
def ctrl_nm3956():
    return 'ret3956' 

@action('ctrl_act3957')
def ctrl_nm3957():
    return 'ret3957' 

@action('ctrl_act3958')
def ctrl_nm3958():
    return 'ret3958' 

@action('ctrl_act3959')
def ctrl_nm3959():
    return 'ret3959' 

@action('ctrl_act3960')
def ctrl_nm3960():
    return 'ret3960' 

@action('ctrl_act3961')
def ctrl_nm3961():
    return 'ret3961' 

@action('ctrl_act3962')
def ctrl_nm3962():
    return 'ret3962' 

@action('ctrl_act3963')
def ctrl_nm3963():
    return 'ret3963' 

@action('ctrl_act3964')
def ctrl_nm3964():
    return 'ret3964' 

@action('ctrl_act3965')
def ctrl_nm3965():
    return 'ret3965' 

@action('ctrl_act3966')
def ctrl_nm3966():
    return 'ret3966' 

@action('ctrl_act3967')
def ctrl_nm3967():
    return 'ret3967' 

@action('ctrl_act3968')
def ctrl_nm3968():
    return 'ret3968' 

@action('ctrl_act3969')
def ctrl_nm3969():
    return 'ret3969' 

@action('ctrl_act3970')
def ctrl_nm3970():
    return 'ret3970' 

@action('ctrl_act3971')
def ctrl_nm3971():
    return 'ret3971' 

@action('ctrl_act3972')
def ctrl_nm3972():
    return 'ret3972' 

@action('ctrl_act3973')
def ctrl_nm3973():
    return 'ret3973' 

@action('ctrl_act3974')
def ctrl_nm3974():
    return 'ret3974' 

@action('ctrl_act3975')
def ctrl_nm3975():
    return 'ret3975' 

@action('ctrl_act3976')
def ctrl_nm3976():
    return 'ret3976' 

@action('ctrl_act3977')
def ctrl_nm3977():
    return 'ret3977' 

@action('ctrl_act3978')
def ctrl_nm3978():
    return 'ret3978' 

@action('ctrl_act3979')
def ctrl_nm3979():
    return 'ret3979' 

@action('ctrl_act3980')
def ctrl_nm3980():
    return 'ret3980' 

@action('ctrl_act3981')
def ctrl_nm3981():
    return 'ret3981' 

@action('ctrl_act3982')
def ctrl_nm3982():
    return 'ret3982' 

@action('ctrl_act3983')
def ctrl_nm3983():
    return 'ret3983' 

@action('ctrl_act3984')
def ctrl_nm3984():
    return 'ret3984' 

@action('ctrl_act3985')
def ctrl_nm3985():
    return 'ret3985' 

@action('ctrl_act3986')
def ctrl_nm3986():
    return 'ret3986' 

@action('ctrl_act3987')
def ctrl_nm3987():
    return 'ret3987' 

@action('ctrl_act3988')
def ctrl_nm3988():
    return 'ret3988' 

@action('ctrl_act3989')
def ctrl_nm3989():
    return 'ret3989' 

@action('ctrl_act3990')
def ctrl_nm3990():
    return 'ret3990' 

@action('ctrl_act3991')
def ctrl_nm3991():
    return 'ret3991' 

@action('ctrl_act3992')
def ctrl_nm3992():
    return 'ret3992' 

@action('ctrl_act3993')
def ctrl_nm3993():
    return 'ret3993' 

@action('ctrl_act3994')
def ctrl_nm3994():
    return 'ret3994' 

@action('ctrl_act3995')
def ctrl_nm3995():
    return 'ret3995' 

@action('ctrl_act3996')
def ctrl_nm3996():
    return 'ret3996' 

@action('ctrl_act3997')
def ctrl_nm3997():
    return 'ret3997' 

@action('ctrl_act3998')
def ctrl_nm3998():
    return 'ret3998' 

@action('ctrl_act3999')
def ctrl_nm3999():
    return 'ret3999' 

@action('ctrl_act4000')
def ctrl_nm4000():
    return 'ret4000' 

@action('ctrl_act4001')
def ctrl_nm4001():
    return 'ret4001' 

@action('ctrl_act4002')
def ctrl_nm4002():
    return 'ret4002' 

@action('ctrl_act4003')
def ctrl_nm4003():
    return 'ret4003' 

@action('ctrl_act4004')
def ctrl_nm4004():
    return 'ret4004' 

@action('ctrl_act4005')
def ctrl_nm4005():
    return 'ret4005' 

@action('ctrl_act4006')
def ctrl_nm4006():
    return 'ret4006' 

@action('ctrl_act4007')
def ctrl_nm4007():
    return 'ret4007' 

@action('ctrl_act4008')
def ctrl_nm4008():
    return 'ret4008' 

@action('ctrl_act4009')
def ctrl_nm4009():
    return 'ret4009' 

@action('ctrl_act4010')
def ctrl_nm4010():
    return 'ret4010' 

@action('ctrl_act4011')
def ctrl_nm4011():
    return 'ret4011' 

@action('ctrl_act4012')
def ctrl_nm4012():
    return 'ret4012' 

@action('ctrl_act4013')
def ctrl_nm4013():
    return 'ret4013' 

@action('ctrl_act4014')
def ctrl_nm4014():
    return 'ret4014' 

@action('ctrl_act4015')
def ctrl_nm4015():
    return 'ret4015' 

@action('ctrl_act4016')
def ctrl_nm4016():
    return 'ret4016' 

@action('ctrl_act4017')
def ctrl_nm4017():
    return 'ret4017' 

@action('ctrl_act4018')
def ctrl_nm4018():
    return 'ret4018' 

@action('ctrl_act4019')
def ctrl_nm4019():
    return 'ret4019' 

@action('ctrl_act4020')
def ctrl_nm4020():
    return 'ret4020' 

@action('ctrl_act4021')
def ctrl_nm4021():
    return 'ret4021' 

@action('ctrl_act4022')
def ctrl_nm4022():
    return 'ret4022' 

@action('ctrl_act4023')
def ctrl_nm4023():
    return 'ret4023' 

@action('ctrl_act4024')
def ctrl_nm4024():
    return 'ret4024' 

@action('ctrl_act4025')
def ctrl_nm4025():
    return 'ret4025' 

@action('ctrl_act4026')
def ctrl_nm4026():
    return 'ret4026' 

@action('ctrl_act4027')
def ctrl_nm4027():
    return 'ret4027' 

@action('ctrl_act4028')
def ctrl_nm4028():
    return 'ret4028' 

@action('ctrl_act4029')
def ctrl_nm4029():
    return 'ret4029' 

@action('ctrl_act4030')
def ctrl_nm4030():
    return 'ret4030' 

@action('ctrl_act4031')
def ctrl_nm4031():
    return 'ret4031' 

@action('ctrl_act4032')
def ctrl_nm4032():
    return 'ret4032' 

@action('ctrl_act4033')
def ctrl_nm4033():
    return 'ret4033' 

@action('ctrl_act4034')
def ctrl_nm4034():
    return 'ret4034' 

@action('ctrl_act4035')
def ctrl_nm4035():
    return 'ret4035' 

@action('ctrl_act4036')
def ctrl_nm4036():
    return 'ret4036' 

@action('ctrl_act4037')
def ctrl_nm4037():
    return 'ret4037' 

@action('ctrl_act4038')
def ctrl_nm4038():
    return 'ret4038' 

@action('ctrl_act4039')
def ctrl_nm4039():
    return 'ret4039' 

@action('ctrl_act4040')
def ctrl_nm4040():
    return 'ret4040' 

@action('ctrl_act4041')
def ctrl_nm4041():
    return 'ret4041' 

@action('ctrl_act4042')
def ctrl_nm4042():
    return 'ret4042' 

@action('ctrl_act4043')
def ctrl_nm4043():
    return 'ret4043' 

@action('ctrl_act4044')
def ctrl_nm4044():
    return 'ret4044' 

@action('ctrl_act4045')
def ctrl_nm4045():
    return 'ret4045' 

@action('ctrl_act4046')
def ctrl_nm4046():
    return 'ret4046' 

@action('ctrl_act4047')
def ctrl_nm4047():
    return 'ret4047' 

@action('ctrl_act4048')
def ctrl_nm4048():
    return 'ret4048' 

@action('ctrl_act4049')
def ctrl_nm4049():
    return 'ret4049' 

@action('ctrl_act4050')
def ctrl_nm4050():
    return 'ret4050' 

@action('ctrl_act4051')
def ctrl_nm4051():
    return 'ret4051' 

@action('ctrl_act4052')
def ctrl_nm4052():
    return 'ret4052' 

@action('ctrl_act4053')
def ctrl_nm4053():
    return 'ret4053' 

@action('ctrl_act4054')
def ctrl_nm4054():
    return 'ret4054' 

@action('ctrl_act4055')
def ctrl_nm4055():
    return 'ret4055' 

@action('ctrl_act4056')
def ctrl_nm4056():
    return 'ret4056' 

@action('ctrl_act4057')
def ctrl_nm4057():
    return 'ret4057' 

@action('ctrl_act4058')
def ctrl_nm4058():
    return 'ret4058' 

@action('ctrl_act4059')
def ctrl_nm4059():
    return 'ret4059' 

@action('ctrl_act4060')
def ctrl_nm4060():
    return 'ret4060' 

@action('ctrl_act4061')
def ctrl_nm4061():
    return 'ret4061' 

@action('ctrl_act4062')
def ctrl_nm4062():
    return 'ret4062' 

@action('ctrl_act4063')
def ctrl_nm4063():
    return 'ret4063' 

@action('ctrl_act4064')
def ctrl_nm4064():
    return 'ret4064' 

@action('ctrl_act4065')
def ctrl_nm4065():
    return 'ret4065' 

@action('ctrl_act4066')
def ctrl_nm4066():
    return 'ret4066' 

@action('ctrl_act4067')
def ctrl_nm4067():
    return 'ret4067' 

@action('ctrl_act4068')
def ctrl_nm4068():
    return 'ret4068' 

@action('ctrl_act4069')
def ctrl_nm4069():
    return 'ret4069' 

@action('ctrl_act4070')
def ctrl_nm4070():
    return 'ret4070' 

@action('ctrl_act4071')
def ctrl_nm4071():
    return 'ret4071' 

@action('ctrl_act4072')
def ctrl_nm4072():
    return 'ret4072' 

@action('ctrl_act4073')
def ctrl_nm4073():
    return 'ret4073' 

@action('ctrl_act4074')
def ctrl_nm4074():
    return 'ret4074' 

@action('ctrl_act4075')
def ctrl_nm4075():
    return 'ret4075' 

@action('ctrl_act4076')
def ctrl_nm4076():
    return 'ret4076' 

@action('ctrl_act4077')
def ctrl_nm4077():
    return 'ret4077' 

@action('ctrl_act4078')
def ctrl_nm4078():
    return 'ret4078' 

@action('ctrl_act4079')
def ctrl_nm4079():
    return 'ret4079' 

@action('ctrl_act4080')
def ctrl_nm4080():
    return 'ret4080' 

@action('ctrl_act4081')
def ctrl_nm4081():
    return 'ret4081' 

@action('ctrl_act4082')
def ctrl_nm4082():
    return 'ret4082' 

@action('ctrl_act4083')
def ctrl_nm4083():
    return 'ret4083' 

@action('ctrl_act4084')
def ctrl_nm4084():
    return 'ret4084' 

@action('ctrl_act4085')
def ctrl_nm4085():
    return 'ret4085' 

@action('ctrl_act4086')
def ctrl_nm4086():
    return 'ret4086' 

@action('ctrl_act4087')
def ctrl_nm4087():
    return 'ret4087' 

@action('ctrl_act4088')
def ctrl_nm4088():
    return 'ret4088' 

@action('ctrl_act4089')
def ctrl_nm4089():
    return 'ret4089' 

@action('ctrl_act4090')
def ctrl_nm4090():
    return 'ret4090' 

@action('ctrl_act4091')
def ctrl_nm4091():
    return 'ret4091' 

@action('ctrl_act4092')
def ctrl_nm4092():
    return 'ret4092' 

@action('ctrl_act4093')
def ctrl_nm4093():
    return 'ret4093' 

@action('ctrl_act4094')
def ctrl_nm4094():
    return 'ret4094' 

@action('ctrl_act4095')
def ctrl_nm4095():
    return 'ret4095' 

@action('ctrl_act4096')
def ctrl_nm4096():
    return 'ret4096' 

@action('ctrl_act4097')
def ctrl_nm4097():
    return 'ret4097' 

@action('ctrl_act4098')
def ctrl_nm4098():
    return 'ret4098' 

@action('ctrl_act4099')
def ctrl_nm4099():
    return 'ret4099' 

@action('ctrl_act4100')
def ctrl_nm4100():
    return 'ret4100' 

@action('ctrl_act4101')
def ctrl_nm4101():
    return 'ret4101' 

@action('ctrl_act4102')
def ctrl_nm4102():
    return 'ret4102' 

@action('ctrl_act4103')
def ctrl_nm4103():
    return 'ret4103' 

@action('ctrl_act4104')
def ctrl_nm4104():
    return 'ret4104' 

@action('ctrl_act4105')
def ctrl_nm4105():
    return 'ret4105' 

@action('ctrl_act4106')
def ctrl_nm4106():
    return 'ret4106' 

@action('ctrl_act4107')
def ctrl_nm4107():
    return 'ret4107' 

@action('ctrl_act4108')
def ctrl_nm4108():
    return 'ret4108' 

@action('ctrl_act4109')
def ctrl_nm4109():
    return 'ret4109' 

@action('ctrl_act4110')
def ctrl_nm4110():
    return 'ret4110' 

@action('ctrl_act4111')
def ctrl_nm4111():
    return 'ret4111' 

@action('ctrl_act4112')
def ctrl_nm4112():
    return 'ret4112' 

@action('ctrl_act4113')
def ctrl_nm4113():
    return 'ret4113' 

@action('ctrl_act4114')
def ctrl_nm4114():
    return 'ret4114' 

@action('ctrl_act4115')
def ctrl_nm4115():
    return 'ret4115' 

@action('ctrl_act4116')
def ctrl_nm4116():
    return 'ret4116' 

@action('ctrl_act4117')
def ctrl_nm4117():
    return 'ret4117' 

@action('ctrl_act4118')
def ctrl_nm4118():
    return 'ret4118' 

@action('ctrl_act4119')
def ctrl_nm4119():
    return 'ret4119' 

@action('ctrl_act4120')
def ctrl_nm4120():
    return 'ret4120' 

@action('ctrl_act4121')
def ctrl_nm4121():
    return 'ret4121' 

@action('ctrl_act4122')
def ctrl_nm4122():
    return 'ret4122' 

@action('ctrl_act4123')
def ctrl_nm4123():
    return 'ret4123' 

@action('ctrl_act4124')
def ctrl_nm4124():
    return 'ret4124' 

@action('ctrl_act4125')
def ctrl_nm4125():
    return 'ret4125' 

@action('ctrl_act4126')
def ctrl_nm4126():
    return 'ret4126' 

@action('ctrl_act4127')
def ctrl_nm4127():
    return 'ret4127' 

@action('ctrl_act4128')
def ctrl_nm4128():
    return 'ret4128' 

@action('ctrl_act4129')
def ctrl_nm4129():
    return 'ret4129' 

@action('ctrl_act4130')
def ctrl_nm4130():
    return 'ret4130' 

@action('ctrl_act4131')
def ctrl_nm4131():
    return 'ret4131' 

@action('ctrl_act4132')
def ctrl_nm4132():
    return 'ret4132' 

@action('ctrl_act4133')
def ctrl_nm4133():
    return 'ret4133' 

@action('ctrl_act4134')
def ctrl_nm4134():
    return 'ret4134' 

@action('ctrl_act4135')
def ctrl_nm4135():
    return 'ret4135' 

@action('ctrl_act4136')
def ctrl_nm4136():
    return 'ret4136' 

@action('ctrl_act4137')
def ctrl_nm4137():
    return 'ret4137' 

@action('ctrl_act4138')
def ctrl_nm4138():
    return 'ret4138' 

@action('ctrl_act4139')
def ctrl_nm4139():
    return 'ret4139' 

@action('ctrl_act4140')
def ctrl_nm4140():
    return 'ret4140' 

@action('ctrl_act4141')
def ctrl_nm4141():
    return 'ret4141' 

@action('ctrl_act4142')
def ctrl_nm4142():
    return 'ret4142' 

@action('ctrl_act4143')
def ctrl_nm4143():
    return 'ret4143' 

@action('ctrl_act4144')
def ctrl_nm4144():
    return 'ret4144' 

@action('ctrl_act4145')
def ctrl_nm4145():
    return 'ret4145' 

@action('ctrl_act4146')
def ctrl_nm4146():
    return 'ret4146' 

@action('ctrl_act4147')
def ctrl_nm4147():
    return 'ret4147' 

@action('ctrl_act4148')
def ctrl_nm4148():
    return 'ret4148' 

@action('ctrl_act4149')
def ctrl_nm4149():
    return 'ret4149' 

@action('ctrl_act4150')
def ctrl_nm4150():
    return 'ret4150' 

@action('ctrl_act4151')
def ctrl_nm4151():
    return 'ret4151' 

@action('ctrl_act4152')
def ctrl_nm4152():
    return 'ret4152' 

@action('ctrl_act4153')
def ctrl_nm4153():
    return 'ret4153' 

@action('ctrl_act4154')
def ctrl_nm4154():
    return 'ret4154' 

@action('ctrl_act4155')
def ctrl_nm4155():
    return 'ret4155' 

@action('ctrl_act4156')
def ctrl_nm4156():
    return 'ret4156' 

@action('ctrl_act4157')
def ctrl_nm4157():
    return 'ret4157' 

@action('ctrl_act4158')
def ctrl_nm4158():
    return 'ret4158' 

@action('ctrl_act4159')
def ctrl_nm4159():
    return 'ret4159' 

@action('ctrl_act4160')
def ctrl_nm4160():
    return 'ret4160' 

@action('ctrl_act4161')
def ctrl_nm4161():
    return 'ret4161' 

@action('ctrl_act4162')
def ctrl_nm4162():
    return 'ret4162' 

@action('ctrl_act4163')
def ctrl_nm4163():
    return 'ret4163' 

@action('ctrl_act4164')
def ctrl_nm4164():
    return 'ret4164' 

@action('ctrl_act4165')
def ctrl_nm4165():
    return 'ret4165' 

@action('ctrl_act4166')
def ctrl_nm4166():
    return 'ret4166' 

@action('ctrl_act4167')
def ctrl_nm4167():
    return 'ret4167' 

@action('ctrl_act4168')
def ctrl_nm4168():
    return 'ret4168' 

@action('ctrl_act4169')
def ctrl_nm4169():
    return 'ret4169' 

@action('ctrl_act4170')
def ctrl_nm4170():
    return 'ret4170' 

@action('ctrl_act4171')
def ctrl_nm4171():
    return 'ret4171' 

@action('ctrl_act4172')
def ctrl_nm4172():
    return 'ret4172' 

@action('ctrl_act4173')
def ctrl_nm4173():
    return 'ret4173' 

@action('ctrl_act4174')
def ctrl_nm4174():
    return 'ret4174' 

@action('ctrl_act4175')
def ctrl_nm4175():
    return 'ret4175' 

@action('ctrl_act4176')
def ctrl_nm4176():
    return 'ret4176' 

@action('ctrl_act4177')
def ctrl_nm4177():
    return 'ret4177' 

@action('ctrl_act4178')
def ctrl_nm4178():
    return 'ret4178' 

@action('ctrl_act4179')
def ctrl_nm4179():
    return 'ret4179' 

@action('ctrl_act4180')
def ctrl_nm4180():
    return 'ret4180' 

@action('ctrl_act4181')
def ctrl_nm4181():
    return 'ret4181' 

@action('ctrl_act4182')
def ctrl_nm4182():
    return 'ret4182' 

@action('ctrl_act4183')
def ctrl_nm4183():
    return 'ret4183' 

@action('ctrl_act4184')
def ctrl_nm4184():
    return 'ret4184' 

@action('ctrl_act4185')
def ctrl_nm4185():
    return 'ret4185' 

@action('ctrl_act4186')
def ctrl_nm4186():
    return 'ret4186' 

@action('ctrl_act4187')
def ctrl_nm4187():
    return 'ret4187' 

@action('ctrl_act4188')
def ctrl_nm4188():
    return 'ret4188' 

@action('ctrl_act4189')
def ctrl_nm4189():
    return 'ret4189' 

@action('ctrl_act4190')
def ctrl_nm4190():
    return 'ret4190' 

@action('ctrl_act4191')
def ctrl_nm4191():
    return 'ret4191' 

@action('ctrl_act4192')
def ctrl_nm4192():
    return 'ret4192' 

@action('ctrl_act4193')
def ctrl_nm4193():
    return 'ret4193' 

@action('ctrl_act4194')
def ctrl_nm4194():
    return 'ret4194' 

@action('ctrl_act4195')
def ctrl_nm4195():
    return 'ret4195' 

@action('ctrl_act4196')
def ctrl_nm4196():
    return 'ret4196' 

@action('ctrl_act4197')
def ctrl_nm4197():
    return 'ret4197' 

@action('ctrl_act4198')
def ctrl_nm4198():
    return 'ret4198' 

@action('ctrl_act4199')
def ctrl_nm4199():
    return 'ret4199' 

@action('ctrl_act4200')
def ctrl_nm4200():
    return 'ret4200' 

@action('ctrl_act4201')
def ctrl_nm4201():
    return 'ret4201' 

@action('ctrl_act4202')
def ctrl_nm4202():
    return 'ret4202' 

@action('ctrl_act4203')
def ctrl_nm4203():
    return 'ret4203' 

@action('ctrl_act4204')
def ctrl_nm4204():
    return 'ret4204' 

@action('ctrl_act4205')
def ctrl_nm4205():
    return 'ret4205' 

@action('ctrl_act4206')
def ctrl_nm4206():
    return 'ret4206' 

@action('ctrl_act4207')
def ctrl_nm4207():
    return 'ret4207' 

@action('ctrl_act4208')
def ctrl_nm4208():
    return 'ret4208' 

@action('ctrl_act4209')
def ctrl_nm4209():
    return 'ret4209' 

@action('ctrl_act4210')
def ctrl_nm4210():
    return 'ret4210' 

@action('ctrl_act4211')
def ctrl_nm4211():
    return 'ret4211' 

@action('ctrl_act4212')
def ctrl_nm4212():
    return 'ret4212' 

@action('ctrl_act4213')
def ctrl_nm4213():
    return 'ret4213' 

@action('ctrl_act4214')
def ctrl_nm4214():
    return 'ret4214' 

@action('ctrl_act4215')
def ctrl_nm4215():
    return 'ret4215' 

@action('ctrl_act4216')
def ctrl_nm4216():
    return 'ret4216' 

@action('ctrl_act4217')
def ctrl_nm4217():
    return 'ret4217' 

@action('ctrl_act4218')
def ctrl_nm4218():
    return 'ret4218' 

@action('ctrl_act4219')
def ctrl_nm4219():
    return 'ret4219' 

@action('ctrl_act4220')
def ctrl_nm4220():
    return 'ret4220' 

@action('ctrl_act4221')
def ctrl_nm4221():
    return 'ret4221' 

@action('ctrl_act4222')
def ctrl_nm4222():
    return 'ret4222' 

@action('ctrl_act4223')
def ctrl_nm4223():
    return 'ret4223' 

@action('ctrl_act4224')
def ctrl_nm4224():
    return 'ret4224' 

@action('ctrl_act4225')
def ctrl_nm4225():
    return 'ret4225' 

@action('ctrl_act4226')
def ctrl_nm4226():
    return 'ret4226' 

@action('ctrl_act4227')
def ctrl_nm4227():
    return 'ret4227' 

@action('ctrl_act4228')
def ctrl_nm4228():
    return 'ret4228' 

@action('ctrl_act4229')
def ctrl_nm4229():
    return 'ret4229' 

@action('ctrl_act4230')
def ctrl_nm4230():
    return 'ret4230' 

@action('ctrl_act4231')
def ctrl_nm4231():
    return 'ret4231' 

@action('ctrl_act4232')
def ctrl_nm4232():
    return 'ret4232' 

@action('ctrl_act4233')
def ctrl_nm4233():
    return 'ret4233' 

@action('ctrl_act4234')
def ctrl_nm4234():
    return 'ret4234' 

@action('ctrl_act4235')
def ctrl_nm4235():
    return 'ret4235' 

@action('ctrl_act4236')
def ctrl_nm4236():
    return 'ret4236' 

@action('ctrl_act4237')
def ctrl_nm4237():
    return 'ret4237' 

@action('ctrl_act4238')
def ctrl_nm4238():
    return 'ret4238' 

@action('ctrl_act4239')
def ctrl_nm4239():
    return 'ret4239' 

@action('ctrl_act4240')
def ctrl_nm4240():
    return 'ret4240' 

@action('ctrl_act4241')
def ctrl_nm4241():
    return 'ret4241' 

@action('ctrl_act4242')
def ctrl_nm4242():
    return 'ret4242' 

@action('ctrl_act4243')
def ctrl_nm4243():
    return 'ret4243' 

@action('ctrl_act4244')
def ctrl_nm4244():
    return 'ret4244' 

@action('ctrl_act4245')
def ctrl_nm4245():
    return 'ret4245' 

@action('ctrl_act4246')
def ctrl_nm4246():
    return 'ret4246' 

@action('ctrl_act4247')
def ctrl_nm4247():
    return 'ret4247' 

@action('ctrl_act4248')
def ctrl_nm4248():
    return 'ret4248' 

@action('ctrl_act4249')
def ctrl_nm4249():
    return 'ret4249' 

@action('ctrl_act4250')
def ctrl_nm4250():
    return 'ret4250' 

@action('ctrl_act4251')
def ctrl_nm4251():
    return 'ret4251' 

@action('ctrl_act4252')
def ctrl_nm4252():
    return 'ret4252' 

@action('ctrl_act4253')
def ctrl_nm4253():
    return 'ret4253' 

@action('ctrl_act4254')
def ctrl_nm4254():
    return 'ret4254' 

@action('ctrl_act4255')
def ctrl_nm4255():
    return 'ret4255' 

@action('ctrl_act4256')
def ctrl_nm4256():
    return 'ret4256' 

@action('ctrl_act4257')
def ctrl_nm4257():
    return 'ret4257' 

@action('ctrl_act4258')
def ctrl_nm4258():
    return 'ret4258' 

@action('ctrl_act4259')
def ctrl_nm4259():
    return 'ret4259' 

@action('ctrl_act4260')
def ctrl_nm4260():
    return 'ret4260' 

@action('ctrl_act4261')
def ctrl_nm4261():
    return 'ret4261' 

@action('ctrl_act4262')
def ctrl_nm4262():
    return 'ret4262' 

@action('ctrl_act4263')
def ctrl_nm4263():
    return 'ret4263' 

@action('ctrl_act4264')
def ctrl_nm4264():
    return 'ret4264' 

@action('ctrl_act4265')
def ctrl_nm4265():
    return 'ret4265' 

@action('ctrl_act4266')
def ctrl_nm4266():
    return 'ret4266' 

@action('ctrl_act4267')
def ctrl_nm4267():
    return 'ret4267' 

@action('ctrl_act4268')
def ctrl_nm4268():
    return 'ret4268' 

@action('ctrl_act4269')
def ctrl_nm4269():
    return 'ret4269' 

@action('ctrl_act4270')
def ctrl_nm4270():
    return 'ret4270' 

@action('ctrl_act4271')
def ctrl_nm4271():
    return 'ret4271' 

@action('ctrl_act4272')
def ctrl_nm4272():
    return 'ret4272' 

@action('ctrl_act4273')
def ctrl_nm4273():
    return 'ret4273' 

@action('ctrl_act4274')
def ctrl_nm4274():
    return 'ret4274' 

@action('ctrl_act4275')
def ctrl_nm4275():
    return 'ret4275' 

@action('ctrl_act4276')
def ctrl_nm4276():
    return 'ret4276' 

@action('ctrl_act4277')
def ctrl_nm4277():
    return 'ret4277' 

@action('ctrl_act4278')
def ctrl_nm4278():
    return 'ret4278' 

@action('ctrl_act4279')
def ctrl_nm4279():
    return 'ret4279' 

@action('ctrl_act4280')
def ctrl_nm4280():
    return 'ret4280' 

@action('ctrl_act4281')
def ctrl_nm4281():
    return 'ret4281' 

@action('ctrl_act4282')
def ctrl_nm4282():
    return 'ret4282' 

@action('ctrl_act4283')
def ctrl_nm4283():
    return 'ret4283' 

@action('ctrl_act4284')
def ctrl_nm4284():
    return 'ret4284' 

@action('ctrl_act4285')
def ctrl_nm4285():
    return 'ret4285' 

@action('ctrl_act4286')
def ctrl_nm4286():
    return 'ret4286' 

@action('ctrl_act4287')
def ctrl_nm4287():
    return 'ret4287' 

@action('ctrl_act4288')
def ctrl_nm4288():
    return 'ret4288' 

@action('ctrl_act4289')
def ctrl_nm4289():
    return 'ret4289' 

@action('ctrl_act4290')
def ctrl_nm4290():
    return 'ret4290' 

@action('ctrl_act4291')
def ctrl_nm4291():
    return 'ret4291' 

@action('ctrl_act4292')
def ctrl_nm4292():
    return 'ret4292' 

@action('ctrl_act4293')
def ctrl_nm4293():
    return 'ret4293' 

@action('ctrl_act4294')
def ctrl_nm4294():
    return 'ret4294' 

@action('ctrl_act4295')
def ctrl_nm4295():
    return 'ret4295' 

@action('ctrl_act4296')
def ctrl_nm4296():
    return 'ret4296' 

@action('ctrl_act4297')
def ctrl_nm4297():
    return 'ret4297' 

@action('ctrl_act4298')
def ctrl_nm4298():
    return 'ret4298' 

@action('ctrl_act4299')
def ctrl_nm4299():
    return 'ret4299' 

@action('ctrl_act4300')
def ctrl_nm4300():
    return 'ret4300' 

@action('ctrl_act4301')
def ctrl_nm4301():
    return 'ret4301' 

@action('ctrl_act4302')
def ctrl_nm4302():
    return 'ret4302' 

@action('ctrl_act4303')
def ctrl_nm4303():
    return 'ret4303' 

@action('ctrl_act4304')
def ctrl_nm4304():
    return 'ret4304' 

@action('ctrl_act4305')
def ctrl_nm4305():
    return 'ret4305' 

@action('ctrl_act4306')
def ctrl_nm4306():
    return 'ret4306' 

@action('ctrl_act4307')
def ctrl_nm4307():
    return 'ret4307' 

@action('ctrl_act4308')
def ctrl_nm4308():
    return 'ret4308' 

@action('ctrl_act4309')
def ctrl_nm4309():
    return 'ret4309' 

@action('ctrl_act4310')
def ctrl_nm4310():
    return 'ret4310' 

@action('ctrl_act4311')
def ctrl_nm4311():
    return 'ret4311' 

@action('ctrl_act4312')
def ctrl_nm4312():
    return 'ret4312' 

@action('ctrl_act4313')
def ctrl_nm4313():
    return 'ret4313' 

@action('ctrl_act4314')
def ctrl_nm4314():
    return 'ret4314' 

@action('ctrl_act4315')
def ctrl_nm4315():
    return 'ret4315' 

@action('ctrl_act4316')
def ctrl_nm4316():
    return 'ret4316' 

@action('ctrl_act4317')
def ctrl_nm4317():
    return 'ret4317' 

@action('ctrl_act4318')
def ctrl_nm4318():
    return 'ret4318' 

@action('ctrl_act4319')
def ctrl_nm4319():
    return 'ret4319' 

@action('ctrl_act4320')
def ctrl_nm4320():
    return 'ret4320' 

@action('ctrl_act4321')
def ctrl_nm4321():
    return 'ret4321' 

@action('ctrl_act4322')
def ctrl_nm4322():
    return 'ret4322' 

@action('ctrl_act4323')
def ctrl_nm4323():
    return 'ret4323' 

@action('ctrl_act4324')
def ctrl_nm4324():
    return 'ret4324' 

@action('ctrl_act4325')
def ctrl_nm4325():
    return 'ret4325' 

@action('ctrl_act4326')
def ctrl_nm4326():
    return 'ret4326' 

@action('ctrl_act4327')
def ctrl_nm4327():
    return 'ret4327' 

@action('ctrl_act4328')
def ctrl_nm4328():
    return 'ret4328' 

@action('ctrl_act4329')
def ctrl_nm4329():
    return 'ret4329' 

@action('ctrl_act4330')
def ctrl_nm4330():
    return 'ret4330' 

@action('ctrl_act4331')
def ctrl_nm4331():
    return 'ret4331' 

@action('ctrl_act4332')
def ctrl_nm4332():
    return 'ret4332' 

@action('ctrl_act4333')
def ctrl_nm4333():
    return 'ret4333' 

@action('ctrl_act4334')
def ctrl_nm4334():
    return 'ret4334' 

@action('ctrl_act4335')
def ctrl_nm4335():
    return 'ret4335' 

@action('ctrl_act4336')
def ctrl_nm4336():
    return 'ret4336' 

@action('ctrl_act4337')
def ctrl_nm4337():
    return 'ret4337' 

@action('ctrl_act4338')
def ctrl_nm4338():
    return 'ret4338' 

@action('ctrl_act4339')
def ctrl_nm4339():
    return 'ret4339' 

@action('ctrl_act4340')
def ctrl_nm4340():
    return 'ret4340' 

@action('ctrl_act4341')
def ctrl_nm4341():
    return 'ret4341' 

@action('ctrl_act4342')
def ctrl_nm4342():
    return 'ret4342' 

@action('ctrl_act4343')
def ctrl_nm4343():
    return 'ret4343' 

@action('ctrl_act4344')
def ctrl_nm4344():
    return 'ret4344' 

@action('ctrl_act4345')
def ctrl_nm4345():
    return 'ret4345' 

@action('ctrl_act4346')
def ctrl_nm4346():
    return 'ret4346' 

@action('ctrl_act4347')
def ctrl_nm4347():
    return 'ret4347' 

@action('ctrl_act4348')
def ctrl_nm4348():
    return 'ret4348' 

@action('ctrl_act4349')
def ctrl_nm4349():
    return 'ret4349' 

@action('ctrl_act4350')
def ctrl_nm4350():
    return 'ret4350' 

@action('ctrl_act4351')
def ctrl_nm4351():
    return 'ret4351' 

@action('ctrl_act4352')
def ctrl_nm4352():
    return 'ret4352' 

@action('ctrl_act4353')
def ctrl_nm4353():
    return 'ret4353' 

@action('ctrl_act4354')
def ctrl_nm4354():
    return 'ret4354' 

@action('ctrl_act4355')
def ctrl_nm4355():
    return 'ret4355' 

@action('ctrl_act4356')
def ctrl_nm4356():
    return 'ret4356' 

@action('ctrl_act4357')
def ctrl_nm4357():
    return 'ret4357' 

@action('ctrl_act4358')
def ctrl_nm4358():
    return 'ret4358' 

@action('ctrl_act4359')
def ctrl_nm4359():
    return 'ret4359' 

@action('ctrl_act4360')
def ctrl_nm4360():
    return 'ret4360' 

@action('ctrl_act4361')
def ctrl_nm4361():
    return 'ret4361' 

@action('ctrl_act4362')
def ctrl_nm4362():
    return 'ret4362' 

@action('ctrl_act4363')
def ctrl_nm4363():
    return 'ret4363' 

@action('ctrl_act4364')
def ctrl_nm4364():
    return 'ret4364' 

@action('ctrl_act4365')
def ctrl_nm4365():
    return 'ret4365' 

@action('ctrl_act4366')
def ctrl_nm4366():
    return 'ret4366' 

@action('ctrl_act4367')
def ctrl_nm4367():
    return 'ret4367' 

@action('ctrl_act4368')
def ctrl_nm4368():
    return 'ret4368' 

@action('ctrl_act4369')
def ctrl_nm4369():
    return 'ret4369' 

@action('ctrl_act4370')
def ctrl_nm4370():
    return 'ret4370' 

@action('ctrl_act4371')
def ctrl_nm4371():
    return 'ret4371' 

@action('ctrl_act4372')
def ctrl_nm4372():
    return 'ret4372' 

@action('ctrl_act4373')
def ctrl_nm4373():
    return 'ret4373' 

@action('ctrl_act4374')
def ctrl_nm4374():
    return 'ret4374' 

@action('ctrl_act4375')
def ctrl_nm4375():
    return 'ret4375' 

@action('ctrl_act4376')
def ctrl_nm4376():
    return 'ret4376' 

@action('ctrl_act4377')
def ctrl_nm4377():
    return 'ret4377' 

@action('ctrl_act4378')
def ctrl_nm4378():
    return 'ret4378' 

@action('ctrl_act4379')
def ctrl_nm4379():
    return 'ret4379' 

@action('ctrl_act4380')
def ctrl_nm4380():
    return 'ret4380' 

@action('ctrl_act4381')
def ctrl_nm4381():
    return 'ret4381' 

@action('ctrl_act4382')
def ctrl_nm4382():
    return 'ret4382' 

@action('ctrl_act4383')
def ctrl_nm4383():
    return 'ret4383' 

@action('ctrl_act4384')
def ctrl_nm4384():
    return 'ret4384' 

@action('ctrl_act4385')
def ctrl_nm4385():
    return 'ret4385' 

@action('ctrl_act4386')
def ctrl_nm4386():
    return 'ret4386' 

@action('ctrl_act4387')
def ctrl_nm4387():
    return 'ret4387' 

@action('ctrl_act4388')
def ctrl_nm4388():
    return 'ret4388' 

@action('ctrl_act4389')
def ctrl_nm4389():
    return 'ret4389' 

@action('ctrl_act4390')
def ctrl_nm4390():
    return 'ret4390' 

@action('ctrl_act4391')
def ctrl_nm4391():
    return 'ret4391' 

@action('ctrl_act4392')
def ctrl_nm4392():
    return 'ret4392' 

@action('ctrl_act4393')
def ctrl_nm4393():
    return 'ret4393' 

@action('ctrl_act4394')
def ctrl_nm4394():
    return 'ret4394' 

@action('ctrl_act4395')
def ctrl_nm4395():
    return 'ret4395' 

@action('ctrl_act4396')
def ctrl_nm4396():
    return 'ret4396' 

@action('ctrl_act4397')
def ctrl_nm4397():
    return 'ret4397' 

@action('ctrl_act4398')
def ctrl_nm4398():
    return 'ret4398' 

@action('ctrl_act4399')
def ctrl_nm4399():
    return 'ret4399' 

@action('ctrl_act4400')
def ctrl_nm4400():
    return 'ret4400' 

@action('ctrl_act4401')
def ctrl_nm4401():
    return 'ret4401' 

@action('ctrl_act4402')
def ctrl_nm4402():
    return 'ret4402' 

@action('ctrl_act4403')
def ctrl_nm4403():
    return 'ret4403' 

@action('ctrl_act4404')
def ctrl_nm4404():
    return 'ret4404' 

@action('ctrl_act4405')
def ctrl_nm4405():
    return 'ret4405' 

@action('ctrl_act4406')
def ctrl_nm4406():
    return 'ret4406' 

@action('ctrl_act4407')
def ctrl_nm4407():
    return 'ret4407' 

@action('ctrl_act4408')
def ctrl_nm4408():
    return 'ret4408' 

@action('ctrl_act4409')
def ctrl_nm4409():
    return 'ret4409' 

@action('ctrl_act4410')
def ctrl_nm4410():
    return 'ret4410' 

@action('ctrl_act4411')
def ctrl_nm4411():
    return 'ret4411' 

@action('ctrl_act4412')
def ctrl_nm4412():
    return 'ret4412' 

@action('ctrl_act4413')
def ctrl_nm4413():
    return 'ret4413' 

@action('ctrl_act4414')
def ctrl_nm4414():
    return 'ret4414' 

@action('ctrl_act4415')
def ctrl_nm4415():
    return 'ret4415' 

@action('ctrl_act4416')
def ctrl_nm4416():
    return 'ret4416' 

@action('ctrl_act4417')
def ctrl_nm4417():
    return 'ret4417' 

@action('ctrl_act4418')
def ctrl_nm4418():
    return 'ret4418' 

@action('ctrl_act4419')
def ctrl_nm4419():
    return 'ret4419' 

@action('ctrl_act4420')
def ctrl_nm4420():
    return 'ret4420' 

@action('ctrl_act4421')
def ctrl_nm4421():
    return 'ret4421' 

@action('ctrl_act4422')
def ctrl_nm4422():
    return 'ret4422' 

@action('ctrl_act4423')
def ctrl_nm4423():
    return 'ret4423' 

@action('ctrl_act4424')
def ctrl_nm4424():
    return 'ret4424' 

@action('ctrl_act4425')
def ctrl_nm4425():
    return 'ret4425' 

@action('ctrl_act4426')
def ctrl_nm4426():
    return 'ret4426' 

@action('ctrl_act4427')
def ctrl_nm4427():
    return 'ret4427' 

@action('ctrl_act4428')
def ctrl_nm4428():
    return 'ret4428' 

@action('ctrl_act4429')
def ctrl_nm4429():
    return 'ret4429' 

@action('ctrl_act4430')
def ctrl_nm4430():
    return 'ret4430' 

@action('ctrl_act4431')
def ctrl_nm4431():
    return 'ret4431' 

@action('ctrl_act4432')
def ctrl_nm4432():
    return 'ret4432' 

@action('ctrl_act4433')
def ctrl_nm4433():
    return 'ret4433' 

@action('ctrl_act4434')
def ctrl_nm4434():
    return 'ret4434' 

@action('ctrl_act4435')
def ctrl_nm4435():
    return 'ret4435' 

@action('ctrl_act4436')
def ctrl_nm4436():
    return 'ret4436' 

@action('ctrl_act4437')
def ctrl_nm4437():
    return 'ret4437' 

@action('ctrl_act4438')
def ctrl_nm4438():
    return 'ret4438' 

@action('ctrl_act4439')
def ctrl_nm4439():
    return 'ret4439' 

@action('ctrl_act4440')
def ctrl_nm4440():
    return 'ret4440' 

@action('ctrl_act4441')
def ctrl_nm4441():
    return 'ret4441' 

@action('ctrl_act4442')
def ctrl_nm4442():
    return 'ret4442' 

@action('ctrl_act4443')
def ctrl_nm4443():
    return 'ret4443' 

@action('ctrl_act4444')
def ctrl_nm4444():
    return 'ret4444' 

@action('ctrl_act4445')
def ctrl_nm4445():
    return 'ret4445' 

@action('ctrl_act4446')
def ctrl_nm4446():
    return 'ret4446' 

@action('ctrl_act4447')
def ctrl_nm4447():
    return 'ret4447' 

@action('ctrl_act4448')
def ctrl_nm4448():
    return 'ret4448' 

@action('ctrl_act4449')
def ctrl_nm4449():
    return 'ret4449' 

@action('ctrl_act4450')
def ctrl_nm4450():
    return 'ret4450' 

@action('ctrl_act4451')
def ctrl_nm4451():
    return 'ret4451' 

@action('ctrl_act4452')
def ctrl_nm4452():
    return 'ret4452' 

@action('ctrl_act4453')
def ctrl_nm4453():
    return 'ret4453' 

@action('ctrl_act4454')
def ctrl_nm4454():
    return 'ret4454' 

@action('ctrl_act4455')
def ctrl_nm4455():
    return 'ret4455' 

@action('ctrl_act4456')
def ctrl_nm4456():
    return 'ret4456' 

@action('ctrl_act4457')
def ctrl_nm4457():
    return 'ret4457' 

@action('ctrl_act4458')
def ctrl_nm4458():
    return 'ret4458' 

@action('ctrl_act4459')
def ctrl_nm4459():
    return 'ret4459' 

@action('ctrl_act4460')
def ctrl_nm4460():
    return 'ret4460' 

@action('ctrl_act4461')
def ctrl_nm4461():
    return 'ret4461' 

@action('ctrl_act4462')
def ctrl_nm4462():
    return 'ret4462' 

@action('ctrl_act4463')
def ctrl_nm4463():
    return 'ret4463' 

@action('ctrl_act4464')
def ctrl_nm4464():
    return 'ret4464' 

@action('ctrl_act4465')
def ctrl_nm4465():
    return 'ret4465' 

@action('ctrl_act4466')
def ctrl_nm4466():
    return 'ret4466' 

@action('ctrl_act4467')
def ctrl_nm4467():
    return 'ret4467' 

@action('ctrl_act4468')
def ctrl_nm4468():
    return 'ret4468' 

@action('ctrl_act4469')
def ctrl_nm4469():
    return 'ret4469' 

@action('ctrl_act4470')
def ctrl_nm4470():
    return 'ret4470' 

@action('ctrl_act4471')
def ctrl_nm4471():
    return 'ret4471' 

@action('ctrl_act4472')
def ctrl_nm4472():
    return 'ret4472' 

@action('ctrl_act4473')
def ctrl_nm4473():
    return 'ret4473' 

@action('ctrl_act4474')
def ctrl_nm4474():
    return 'ret4474' 

@action('ctrl_act4475')
def ctrl_nm4475():
    return 'ret4475' 

@action('ctrl_act4476')
def ctrl_nm4476():
    return 'ret4476' 

@action('ctrl_act4477')
def ctrl_nm4477():
    return 'ret4477' 

@action('ctrl_act4478')
def ctrl_nm4478():
    return 'ret4478' 

@action('ctrl_act4479')
def ctrl_nm4479():
    return 'ret4479' 

@action('ctrl_act4480')
def ctrl_nm4480():
    return 'ret4480' 

@action('ctrl_act4481')
def ctrl_nm4481():
    return 'ret4481' 

@action('ctrl_act4482')
def ctrl_nm4482():
    return 'ret4482' 

@action('ctrl_act4483')
def ctrl_nm4483():
    return 'ret4483' 

@action('ctrl_act4484')
def ctrl_nm4484():
    return 'ret4484' 

@action('ctrl_act4485')
def ctrl_nm4485():
    return 'ret4485' 

@action('ctrl_act4486')
def ctrl_nm4486():
    return 'ret4486' 

@action('ctrl_act4487')
def ctrl_nm4487():
    return 'ret4487' 

@action('ctrl_act4488')
def ctrl_nm4488():
    return 'ret4488' 

@action('ctrl_act4489')
def ctrl_nm4489():
    return 'ret4489' 

@action('ctrl_act4490')
def ctrl_nm4490():
    return 'ret4490' 

@action('ctrl_act4491')
def ctrl_nm4491():
    return 'ret4491' 

@action('ctrl_act4492')
def ctrl_nm4492():
    return 'ret4492' 

@action('ctrl_act4493')
def ctrl_nm4493():
    return 'ret4493' 

@action('ctrl_act4494')
def ctrl_nm4494():
    return 'ret4494' 

@action('ctrl_act4495')
def ctrl_nm4495():
    return 'ret4495' 

@action('ctrl_act4496')
def ctrl_nm4496():
    return 'ret4496' 

@action('ctrl_act4497')
def ctrl_nm4497():
    return 'ret4497' 

@action('ctrl_act4498')
def ctrl_nm4498():
    return 'ret4498' 

@action('ctrl_act4499')
def ctrl_nm4499():
    return 'ret4499' 

@action('ctrl_act4500')
def ctrl_nm4500():
    return 'ret4500' 

@action('ctrl_act4501')
def ctrl_nm4501():
    return 'ret4501' 

@action('ctrl_act4502')
def ctrl_nm4502():
    return 'ret4502' 

@action('ctrl_act4503')
def ctrl_nm4503():
    return 'ret4503' 

@action('ctrl_act4504')
def ctrl_nm4504():
    return 'ret4504' 

@action('ctrl_act4505')
def ctrl_nm4505():
    return 'ret4505' 

@action('ctrl_act4506')
def ctrl_nm4506():
    return 'ret4506' 

@action('ctrl_act4507')
def ctrl_nm4507():
    return 'ret4507' 

@action('ctrl_act4508')
def ctrl_nm4508():
    return 'ret4508' 

@action('ctrl_act4509')
def ctrl_nm4509():
    return 'ret4509' 

@action('ctrl_act4510')
def ctrl_nm4510():
    return 'ret4510' 

@action('ctrl_act4511')
def ctrl_nm4511():
    return 'ret4511' 

@action('ctrl_act4512')
def ctrl_nm4512():
    return 'ret4512' 

@action('ctrl_act4513')
def ctrl_nm4513():
    return 'ret4513' 

@action('ctrl_act4514')
def ctrl_nm4514():
    return 'ret4514' 

@action('ctrl_act4515')
def ctrl_nm4515():
    return 'ret4515' 

@action('ctrl_act4516')
def ctrl_nm4516():
    return 'ret4516' 

@action('ctrl_act4517')
def ctrl_nm4517():
    return 'ret4517' 

@action('ctrl_act4518')
def ctrl_nm4518():
    return 'ret4518' 

@action('ctrl_act4519')
def ctrl_nm4519():
    return 'ret4519' 

@action('ctrl_act4520')
def ctrl_nm4520():
    return 'ret4520' 

@action('ctrl_act4521')
def ctrl_nm4521():
    return 'ret4521' 

@action('ctrl_act4522')
def ctrl_nm4522():
    return 'ret4522' 

@action('ctrl_act4523')
def ctrl_nm4523():
    return 'ret4523' 

@action('ctrl_act4524')
def ctrl_nm4524():
    return 'ret4524' 

@action('ctrl_act4525')
def ctrl_nm4525():
    return 'ret4525' 

@action('ctrl_act4526')
def ctrl_nm4526():
    return 'ret4526' 

@action('ctrl_act4527')
def ctrl_nm4527():
    return 'ret4527' 

@action('ctrl_act4528')
def ctrl_nm4528():
    return 'ret4528' 

@action('ctrl_act4529')
def ctrl_nm4529():
    return 'ret4529' 

@action('ctrl_act4530')
def ctrl_nm4530():
    return 'ret4530' 

@action('ctrl_act4531')
def ctrl_nm4531():
    return 'ret4531' 

@action('ctrl_act4532')
def ctrl_nm4532():
    return 'ret4532' 

@action('ctrl_act4533')
def ctrl_nm4533():
    return 'ret4533' 

@action('ctrl_act4534')
def ctrl_nm4534():
    return 'ret4534' 

@action('ctrl_act4535')
def ctrl_nm4535():
    return 'ret4535' 

@action('ctrl_act4536')
def ctrl_nm4536():
    return 'ret4536' 

@action('ctrl_act4537')
def ctrl_nm4537():
    return 'ret4537' 

@action('ctrl_act4538')
def ctrl_nm4538():
    return 'ret4538' 

@action('ctrl_act4539')
def ctrl_nm4539():
    return 'ret4539' 

@action('ctrl_act4540')
def ctrl_nm4540():
    return 'ret4540' 

@action('ctrl_act4541')
def ctrl_nm4541():
    return 'ret4541' 

@action('ctrl_act4542')
def ctrl_nm4542():
    return 'ret4542' 

@action('ctrl_act4543')
def ctrl_nm4543():
    return 'ret4543' 

@action('ctrl_act4544')
def ctrl_nm4544():
    return 'ret4544' 

@action('ctrl_act4545')
def ctrl_nm4545():
    return 'ret4545' 

@action('ctrl_act4546')
def ctrl_nm4546():
    return 'ret4546' 

@action('ctrl_act4547')
def ctrl_nm4547():
    return 'ret4547' 

@action('ctrl_act4548')
def ctrl_nm4548():
    return 'ret4548' 

@action('ctrl_act4549')
def ctrl_nm4549():
    return 'ret4549' 

@action('ctrl_act4550')
def ctrl_nm4550():
    return 'ret4550' 

@action('ctrl_act4551')
def ctrl_nm4551():
    return 'ret4551' 

@action('ctrl_act4552')
def ctrl_nm4552():
    return 'ret4552' 

@action('ctrl_act4553')
def ctrl_nm4553():
    return 'ret4553' 

@action('ctrl_act4554')
def ctrl_nm4554():
    return 'ret4554' 

@action('ctrl_act4555')
def ctrl_nm4555():
    return 'ret4555' 

@action('ctrl_act4556')
def ctrl_nm4556():
    return 'ret4556' 

@action('ctrl_act4557')
def ctrl_nm4557():
    return 'ret4557' 

@action('ctrl_act4558')
def ctrl_nm4558():
    return 'ret4558' 

@action('ctrl_act4559')
def ctrl_nm4559():
    return 'ret4559' 

@action('ctrl_act4560')
def ctrl_nm4560():
    return 'ret4560' 

@action('ctrl_act4561')
def ctrl_nm4561():
    return 'ret4561' 

@action('ctrl_act4562')
def ctrl_nm4562():
    return 'ret4562' 

@action('ctrl_act4563')
def ctrl_nm4563():
    return 'ret4563' 

@action('ctrl_act4564')
def ctrl_nm4564():
    return 'ret4564' 

@action('ctrl_act4565')
def ctrl_nm4565():
    return 'ret4565' 

@action('ctrl_act4566')
def ctrl_nm4566():
    return 'ret4566' 

@action('ctrl_act4567')
def ctrl_nm4567():
    return 'ret4567' 

@action('ctrl_act4568')
def ctrl_nm4568():
    return 'ret4568' 

@action('ctrl_act4569')
def ctrl_nm4569():
    return 'ret4569' 

@action('ctrl_act4570')
def ctrl_nm4570():
    return 'ret4570' 

@action('ctrl_act4571')
def ctrl_nm4571():
    return 'ret4571' 

@action('ctrl_act4572')
def ctrl_nm4572():
    return 'ret4572' 

@action('ctrl_act4573')
def ctrl_nm4573():
    return 'ret4573' 

@action('ctrl_act4574')
def ctrl_nm4574():
    return 'ret4574' 

@action('ctrl_act4575')
def ctrl_nm4575():
    return 'ret4575' 

@action('ctrl_act4576')
def ctrl_nm4576():
    return 'ret4576' 

@action('ctrl_act4577')
def ctrl_nm4577():
    return 'ret4577' 

@action('ctrl_act4578')
def ctrl_nm4578():
    return 'ret4578' 

@action('ctrl_act4579')
def ctrl_nm4579():
    return 'ret4579' 

@action('ctrl_act4580')
def ctrl_nm4580():
    return 'ret4580' 

@action('ctrl_act4581')
def ctrl_nm4581():
    return 'ret4581' 

@action('ctrl_act4582')
def ctrl_nm4582():
    return 'ret4582' 

@action('ctrl_act4583')
def ctrl_nm4583():
    return 'ret4583' 

@action('ctrl_act4584')
def ctrl_nm4584():
    return 'ret4584' 

@action('ctrl_act4585')
def ctrl_nm4585():
    return 'ret4585' 

@action('ctrl_act4586')
def ctrl_nm4586():
    return 'ret4586' 

@action('ctrl_act4587')
def ctrl_nm4587():
    return 'ret4587' 

@action('ctrl_act4588')
def ctrl_nm4588():
    return 'ret4588' 

@action('ctrl_act4589')
def ctrl_nm4589():
    return 'ret4589' 

@action('ctrl_act4590')
def ctrl_nm4590():
    return 'ret4590' 

@action('ctrl_act4591')
def ctrl_nm4591():
    return 'ret4591' 

@action('ctrl_act4592')
def ctrl_nm4592():
    return 'ret4592' 

@action('ctrl_act4593')
def ctrl_nm4593():
    return 'ret4593' 

@action('ctrl_act4594')
def ctrl_nm4594():
    return 'ret4594' 

@action('ctrl_act4595')
def ctrl_nm4595():
    return 'ret4595' 

@action('ctrl_act4596')
def ctrl_nm4596():
    return 'ret4596' 

@action('ctrl_act4597')
def ctrl_nm4597():
    return 'ret4597' 

@action('ctrl_act4598')
def ctrl_nm4598():
    return 'ret4598' 

@action('ctrl_act4599')
def ctrl_nm4599():
    return 'ret4599' 

@action('ctrl_act4600')
def ctrl_nm4600():
    return 'ret4600' 

@action('ctrl_act4601')
def ctrl_nm4601():
    return 'ret4601' 

@action('ctrl_act4602')
def ctrl_nm4602():
    return 'ret4602' 

@action('ctrl_act4603')
def ctrl_nm4603():
    return 'ret4603' 

@action('ctrl_act4604')
def ctrl_nm4604():
    return 'ret4604' 

@action('ctrl_act4605')
def ctrl_nm4605():
    return 'ret4605' 

@action('ctrl_act4606')
def ctrl_nm4606():
    return 'ret4606' 

@action('ctrl_act4607')
def ctrl_nm4607():
    return 'ret4607' 

@action('ctrl_act4608')
def ctrl_nm4608():
    return 'ret4608' 

@action('ctrl_act4609')
def ctrl_nm4609():
    return 'ret4609' 

@action('ctrl_act4610')
def ctrl_nm4610():
    return 'ret4610' 

@action('ctrl_act4611')
def ctrl_nm4611():
    return 'ret4611' 

@action('ctrl_act4612')
def ctrl_nm4612():
    return 'ret4612' 

@action('ctrl_act4613')
def ctrl_nm4613():
    return 'ret4613' 

@action('ctrl_act4614')
def ctrl_nm4614():
    return 'ret4614' 

@action('ctrl_act4615')
def ctrl_nm4615():
    return 'ret4615' 

@action('ctrl_act4616')
def ctrl_nm4616():
    return 'ret4616' 

@action('ctrl_act4617')
def ctrl_nm4617():
    return 'ret4617' 

@action('ctrl_act4618')
def ctrl_nm4618():
    return 'ret4618' 

@action('ctrl_act4619')
def ctrl_nm4619():
    return 'ret4619' 

@action('ctrl_act4620')
def ctrl_nm4620():
    return 'ret4620' 

@action('ctrl_act4621')
def ctrl_nm4621():
    return 'ret4621' 

@action('ctrl_act4622')
def ctrl_nm4622():
    return 'ret4622' 

@action('ctrl_act4623')
def ctrl_nm4623():
    return 'ret4623' 

@action('ctrl_act4624')
def ctrl_nm4624():
    return 'ret4624' 

@action('ctrl_act4625')
def ctrl_nm4625():
    return 'ret4625' 

@action('ctrl_act4626')
def ctrl_nm4626():
    return 'ret4626' 

@action('ctrl_act4627')
def ctrl_nm4627():
    return 'ret4627' 

@action('ctrl_act4628')
def ctrl_nm4628():
    return 'ret4628' 

@action('ctrl_act4629')
def ctrl_nm4629():
    return 'ret4629' 

@action('ctrl_act4630')
def ctrl_nm4630():
    return 'ret4630' 

@action('ctrl_act4631')
def ctrl_nm4631():
    return 'ret4631' 

@action('ctrl_act4632')
def ctrl_nm4632():
    return 'ret4632' 

@action('ctrl_act4633')
def ctrl_nm4633():
    return 'ret4633' 

@action('ctrl_act4634')
def ctrl_nm4634():
    return 'ret4634' 

@action('ctrl_act4635')
def ctrl_nm4635():
    return 'ret4635' 

@action('ctrl_act4636')
def ctrl_nm4636():
    return 'ret4636' 

@action('ctrl_act4637')
def ctrl_nm4637():
    return 'ret4637' 

@action('ctrl_act4638')
def ctrl_nm4638():
    return 'ret4638' 

@action('ctrl_act4639')
def ctrl_nm4639():
    return 'ret4639' 

@action('ctrl_act4640')
def ctrl_nm4640():
    return 'ret4640' 

@action('ctrl_act4641')
def ctrl_nm4641():
    return 'ret4641' 

@action('ctrl_act4642')
def ctrl_nm4642():
    return 'ret4642' 

@action('ctrl_act4643')
def ctrl_nm4643():
    return 'ret4643' 

@action('ctrl_act4644')
def ctrl_nm4644():
    return 'ret4644' 

@action('ctrl_act4645')
def ctrl_nm4645():
    return 'ret4645' 

@action('ctrl_act4646')
def ctrl_nm4646():
    return 'ret4646' 

@action('ctrl_act4647')
def ctrl_nm4647():
    return 'ret4647' 

@action('ctrl_act4648')
def ctrl_nm4648():
    return 'ret4648' 

@action('ctrl_act4649')
def ctrl_nm4649():
    return 'ret4649' 

@action('ctrl_act4650')
def ctrl_nm4650():
    return 'ret4650' 

@action('ctrl_act4651')
def ctrl_nm4651():
    return 'ret4651' 

@action('ctrl_act4652')
def ctrl_nm4652():
    return 'ret4652' 

@action('ctrl_act4653')
def ctrl_nm4653():
    return 'ret4653' 

@action('ctrl_act4654')
def ctrl_nm4654():
    return 'ret4654' 

@action('ctrl_act4655')
def ctrl_nm4655():
    return 'ret4655' 

@action('ctrl_act4656')
def ctrl_nm4656():
    return 'ret4656' 

@action('ctrl_act4657')
def ctrl_nm4657():
    return 'ret4657' 

@action('ctrl_act4658')
def ctrl_nm4658():
    return 'ret4658' 

@action('ctrl_act4659')
def ctrl_nm4659():
    return 'ret4659' 

@action('ctrl_act4660')
def ctrl_nm4660():
    return 'ret4660' 

@action('ctrl_act4661')
def ctrl_nm4661():
    return 'ret4661' 

@action('ctrl_act4662')
def ctrl_nm4662():
    return 'ret4662' 

@action('ctrl_act4663')
def ctrl_nm4663():
    return 'ret4663' 

@action('ctrl_act4664')
def ctrl_nm4664():
    return 'ret4664' 

@action('ctrl_act4665')
def ctrl_nm4665():
    return 'ret4665' 

@action('ctrl_act4666')
def ctrl_nm4666():
    return 'ret4666' 

@action('ctrl_act4667')
def ctrl_nm4667():
    return 'ret4667' 

@action('ctrl_act4668')
def ctrl_nm4668():
    return 'ret4668' 

@action('ctrl_act4669')
def ctrl_nm4669():
    return 'ret4669' 

@action('ctrl_act4670')
def ctrl_nm4670():
    return 'ret4670' 

@action('ctrl_act4671')
def ctrl_nm4671():
    return 'ret4671' 

@action('ctrl_act4672')
def ctrl_nm4672():
    return 'ret4672' 

@action('ctrl_act4673')
def ctrl_nm4673():
    return 'ret4673' 

@action('ctrl_act4674')
def ctrl_nm4674():
    return 'ret4674' 

@action('ctrl_act4675')
def ctrl_nm4675():
    return 'ret4675' 

@action('ctrl_act4676')
def ctrl_nm4676():
    return 'ret4676' 

@action('ctrl_act4677')
def ctrl_nm4677():
    return 'ret4677' 

@action('ctrl_act4678')
def ctrl_nm4678():
    return 'ret4678' 

@action('ctrl_act4679')
def ctrl_nm4679():
    return 'ret4679' 

@action('ctrl_act4680')
def ctrl_nm4680():
    return 'ret4680' 

@action('ctrl_act4681')
def ctrl_nm4681():
    return 'ret4681' 

@action('ctrl_act4682')
def ctrl_nm4682():
    return 'ret4682' 

@action('ctrl_act4683')
def ctrl_nm4683():
    return 'ret4683' 

@action('ctrl_act4684')
def ctrl_nm4684():
    return 'ret4684' 

@action('ctrl_act4685')
def ctrl_nm4685():
    return 'ret4685' 

@action('ctrl_act4686')
def ctrl_nm4686():
    return 'ret4686' 

@action('ctrl_act4687')
def ctrl_nm4687():
    return 'ret4687' 

@action('ctrl_act4688')
def ctrl_nm4688():
    return 'ret4688' 

@action('ctrl_act4689')
def ctrl_nm4689():
    return 'ret4689' 

@action('ctrl_act4690')
def ctrl_nm4690():
    return 'ret4690' 

@action('ctrl_act4691')
def ctrl_nm4691():
    return 'ret4691' 

@action('ctrl_act4692')
def ctrl_nm4692():
    return 'ret4692' 

@action('ctrl_act4693')
def ctrl_nm4693():
    return 'ret4693' 

@action('ctrl_act4694')
def ctrl_nm4694():
    return 'ret4694' 

@action('ctrl_act4695')
def ctrl_nm4695():
    return 'ret4695' 

@action('ctrl_act4696')
def ctrl_nm4696():
    return 'ret4696' 

@action('ctrl_act4697')
def ctrl_nm4697():
    return 'ret4697' 

@action('ctrl_act4698')
def ctrl_nm4698():
    return 'ret4698' 

@action('ctrl_act4699')
def ctrl_nm4699():
    return 'ret4699' 

@action('ctrl_act4700')
def ctrl_nm4700():
    return 'ret4700' 

@action('ctrl_act4701')
def ctrl_nm4701():
    return 'ret4701' 

@action('ctrl_act4702')
def ctrl_nm4702():
    return 'ret4702' 

@action('ctrl_act4703')
def ctrl_nm4703():
    return 'ret4703' 

@action('ctrl_act4704')
def ctrl_nm4704():
    return 'ret4704' 

@action('ctrl_act4705')
def ctrl_nm4705():
    return 'ret4705' 

@action('ctrl_act4706')
def ctrl_nm4706():
    return 'ret4706' 

@action('ctrl_act4707')
def ctrl_nm4707():
    return 'ret4707' 

@action('ctrl_act4708')
def ctrl_nm4708():
    return 'ret4708' 

@action('ctrl_act4709')
def ctrl_nm4709():
    return 'ret4709' 

@action('ctrl_act4710')
def ctrl_nm4710():
    return 'ret4710' 

@action('ctrl_act4711')
def ctrl_nm4711():
    return 'ret4711' 

@action('ctrl_act4712')
def ctrl_nm4712():
    return 'ret4712' 

@action('ctrl_act4713')
def ctrl_nm4713():
    return 'ret4713' 

@action('ctrl_act4714')
def ctrl_nm4714():
    return 'ret4714' 

@action('ctrl_act4715')
def ctrl_nm4715():
    return 'ret4715' 

@action('ctrl_act4716')
def ctrl_nm4716():
    return 'ret4716' 

@action('ctrl_act4717')
def ctrl_nm4717():
    return 'ret4717' 

@action('ctrl_act4718')
def ctrl_nm4718():
    return 'ret4718' 

@action('ctrl_act4719')
def ctrl_nm4719():
    return 'ret4719' 

@action('ctrl_act4720')
def ctrl_nm4720():
    return 'ret4720' 

@action('ctrl_act4721')
def ctrl_nm4721():
    return 'ret4721' 

@action('ctrl_act4722')
def ctrl_nm4722():
    return 'ret4722' 

@action('ctrl_act4723')
def ctrl_nm4723():
    return 'ret4723' 

@action('ctrl_act4724')
def ctrl_nm4724():
    return 'ret4724' 

@action('ctrl_act4725')
def ctrl_nm4725():
    return 'ret4725' 

@action('ctrl_act4726')
def ctrl_nm4726():
    return 'ret4726' 

@action('ctrl_act4727')
def ctrl_nm4727():
    return 'ret4727' 

@action('ctrl_act4728')
def ctrl_nm4728():
    return 'ret4728' 

@action('ctrl_act4729')
def ctrl_nm4729():
    return 'ret4729' 

@action('ctrl_act4730')
def ctrl_nm4730():
    return 'ret4730' 

@action('ctrl_act4731')
def ctrl_nm4731():
    return 'ret4731' 

@action('ctrl_act4732')
def ctrl_nm4732():
    return 'ret4732' 

@action('ctrl_act4733')
def ctrl_nm4733():
    return 'ret4733' 

@action('ctrl_act4734')
def ctrl_nm4734():
    return 'ret4734' 

@action('ctrl_act4735')
def ctrl_nm4735():
    return 'ret4735' 

@action('ctrl_act4736')
def ctrl_nm4736():
    return 'ret4736' 

@action('ctrl_act4737')
def ctrl_nm4737():
    return 'ret4737' 

@action('ctrl_act4738')
def ctrl_nm4738():
    return 'ret4738' 

@action('ctrl_act4739')
def ctrl_nm4739():
    return 'ret4739' 

@action('ctrl_act4740')
def ctrl_nm4740():
    return 'ret4740' 

@action('ctrl_act4741')
def ctrl_nm4741():
    return 'ret4741' 

@action('ctrl_act4742')
def ctrl_nm4742():
    return 'ret4742' 

@action('ctrl_act4743')
def ctrl_nm4743():
    return 'ret4743' 

@action('ctrl_act4744')
def ctrl_nm4744():
    return 'ret4744' 

@action('ctrl_act4745')
def ctrl_nm4745():
    return 'ret4745' 

@action('ctrl_act4746')
def ctrl_nm4746():
    return 'ret4746' 

@action('ctrl_act4747')
def ctrl_nm4747():
    return 'ret4747' 

@action('ctrl_act4748')
def ctrl_nm4748():
    return 'ret4748' 

@action('ctrl_act4749')
def ctrl_nm4749():
    return 'ret4749' 

@action('ctrl_act4750')
def ctrl_nm4750():
    return 'ret4750' 

@action('ctrl_act4751')
def ctrl_nm4751():
    return 'ret4751' 

@action('ctrl_act4752')
def ctrl_nm4752():
    return 'ret4752' 

@action('ctrl_act4753')
def ctrl_nm4753():
    return 'ret4753' 

@action('ctrl_act4754')
def ctrl_nm4754():
    return 'ret4754' 

@action('ctrl_act4755')
def ctrl_nm4755():
    return 'ret4755' 

@action('ctrl_act4756')
def ctrl_nm4756():
    return 'ret4756' 

@action('ctrl_act4757')
def ctrl_nm4757():
    return 'ret4757' 

@action('ctrl_act4758')
def ctrl_nm4758():
    return 'ret4758' 

@action('ctrl_act4759')
def ctrl_nm4759():
    return 'ret4759' 

@action('ctrl_act4760')
def ctrl_nm4760():
    return 'ret4760' 

@action('ctrl_act4761')
def ctrl_nm4761():
    return 'ret4761' 

@action('ctrl_act4762')
def ctrl_nm4762():
    return 'ret4762' 

@action('ctrl_act4763')
def ctrl_nm4763():
    return 'ret4763' 

@action('ctrl_act4764')
def ctrl_nm4764():
    return 'ret4764' 

@action('ctrl_act4765')
def ctrl_nm4765():
    return 'ret4765' 

@action('ctrl_act4766')
def ctrl_nm4766():
    return 'ret4766' 

@action('ctrl_act4767')
def ctrl_nm4767():
    return 'ret4767' 

@action('ctrl_act4768')
def ctrl_nm4768():
    return 'ret4768' 

@action('ctrl_act4769')
def ctrl_nm4769():
    return 'ret4769' 

@action('ctrl_act4770')
def ctrl_nm4770():
    return 'ret4770' 

@action('ctrl_act4771')
def ctrl_nm4771():
    return 'ret4771' 

@action('ctrl_act4772')
def ctrl_nm4772():
    return 'ret4772' 

@action('ctrl_act4773')
def ctrl_nm4773():
    return 'ret4773' 

@action('ctrl_act4774')
def ctrl_nm4774():
    return 'ret4774' 

@action('ctrl_act4775')
def ctrl_nm4775():
    return 'ret4775' 

@action('ctrl_act4776')
def ctrl_nm4776():
    return 'ret4776' 

@action('ctrl_act4777')
def ctrl_nm4777():
    return 'ret4777' 

@action('ctrl_act4778')
def ctrl_nm4778():
    return 'ret4778' 

@action('ctrl_act4779')
def ctrl_nm4779():
    return 'ret4779' 

@action('ctrl_act4780')
def ctrl_nm4780():
    return 'ret4780' 

@action('ctrl_act4781')
def ctrl_nm4781():
    return 'ret4781' 

@action('ctrl_act4782')
def ctrl_nm4782():
    return 'ret4782' 

@action('ctrl_act4783')
def ctrl_nm4783():
    return 'ret4783' 

@action('ctrl_act4784')
def ctrl_nm4784():
    return 'ret4784' 

@action('ctrl_act4785')
def ctrl_nm4785():
    return 'ret4785' 

@action('ctrl_act4786')
def ctrl_nm4786():
    return 'ret4786' 

@action('ctrl_act4787')
def ctrl_nm4787():
    return 'ret4787' 

@action('ctrl_act4788')
def ctrl_nm4788():
    return 'ret4788' 

@action('ctrl_act4789')
def ctrl_nm4789():
    return 'ret4789' 

@action('ctrl_act4790')
def ctrl_nm4790():
    return 'ret4790' 

@action('ctrl_act4791')
def ctrl_nm4791():
    return 'ret4791' 

@action('ctrl_act4792')
def ctrl_nm4792():
    return 'ret4792' 

@action('ctrl_act4793')
def ctrl_nm4793():
    return 'ret4793' 

@action('ctrl_act4794')
def ctrl_nm4794():
    return 'ret4794' 

@action('ctrl_act4795')
def ctrl_nm4795():
    return 'ret4795' 

@action('ctrl_act4796')
def ctrl_nm4796():
    return 'ret4796' 

@action('ctrl_act4797')
def ctrl_nm4797():
    return 'ret4797' 

@action('ctrl_act4798')
def ctrl_nm4798():
    return 'ret4798' 

@action('ctrl_act4799')
def ctrl_nm4799():
    return 'ret4799' 

@action('ctrl_act4800')
def ctrl_nm4800():
    return 'ret4800' 

@action('ctrl_act4801')
def ctrl_nm4801():
    return 'ret4801' 

@action('ctrl_act4802')
def ctrl_nm4802():
    return 'ret4802' 

@action('ctrl_act4803')
def ctrl_nm4803():
    return 'ret4803' 

@action('ctrl_act4804')
def ctrl_nm4804():
    return 'ret4804' 

@action('ctrl_act4805')
def ctrl_nm4805():
    return 'ret4805' 

@action('ctrl_act4806')
def ctrl_nm4806():
    return 'ret4806' 

@action('ctrl_act4807')
def ctrl_nm4807():
    return 'ret4807' 

@action('ctrl_act4808')
def ctrl_nm4808():
    return 'ret4808' 

@action('ctrl_act4809')
def ctrl_nm4809():
    return 'ret4809' 

@action('ctrl_act4810')
def ctrl_nm4810():
    return 'ret4810' 

@action('ctrl_act4811')
def ctrl_nm4811():
    return 'ret4811' 

@action('ctrl_act4812')
def ctrl_nm4812():
    return 'ret4812' 

@action('ctrl_act4813')
def ctrl_nm4813():
    return 'ret4813' 

@action('ctrl_act4814')
def ctrl_nm4814():
    return 'ret4814' 

@action('ctrl_act4815')
def ctrl_nm4815():
    return 'ret4815' 

@action('ctrl_act4816')
def ctrl_nm4816():
    return 'ret4816' 

@action('ctrl_act4817')
def ctrl_nm4817():
    return 'ret4817' 

@action('ctrl_act4818')
def ctrl_nm4818():
    return 'ret4818' 

@action('ctrl_act4819')
def ctrl_nm4819():
    return 'ret4819' 

@action('ctrl_act4820')
def ctrl_nm4820():
    return 'ret4820' 

@action('ctrl_act4821')
def ctrl_nm4821():
    return 'ret4821' 

@action('ctrl_act4822')
def ctrl_nm4822():
    return 'ret4822' 

@action('ctrl_act4823')
def ctrl_nm4823():
    return 'ret4823' 

@action('ctrl_act4824')
def ctrl_nm4824():
    return 'ret4824' 

@action('ctrl_act4825')
def ctrl_nm4825():
    return 'ret4825' 

@action('ctrl_act4826')
def ctrl_nm4826():
    return 'ret4826' 

@action('ctrl_act4827')
def ctrl_nm4827():
    return 'ret4827' 

@action('ctrl_act4828')
def ctrl_nm4828():
    return 'ret4828' 

@action('ctrl_act4829')
def ctrl_nm4829():
    return 'ret4829' 

@action('ctrl_act4830')
def ctrl_nm4830():
    return 'ret4830' 

@action('ctrl_act4831')
def ctrl_nm4831():
    return 'ret4831' 

@action('ctrl_act4832')
def ctrl_nm4832():
    return 'ret4832' 

@action('ctrl_act4833')
def ctrl_nm4833():
    return 'ret4833' 

@action('ctrl_act4834')
def ctrl_nm4834():
    return 'ret4834' 

@action('ctrl_act4835')
def ctrl_nm4835():
    return 'ret4835' 

@action('ctrl_act4836')
def ctrl_nm4836():
    return 'ret4836' 

@action('ctrl_act4837')
def ctrl_nm4837():
    return 'ret4837' 

@action('ctrl_act4838')
def ctrl_nm4838():
    return 'ret4838' 

@action('ctrl_act4839')
def ctrl_nm4839():
    return 'ret4839' 

@action('ctrl_act4840')
def ctrl_nm4840():
    return 'ret4840' 

@action('ctrl_act4841')
def ctrl_nm4841():
    return 'ret4841' 

@action('ctrl_act4842')
def ctrl_nm4842():
    return 'ret4842' 

@action('ctrl_act4843')
def ctrl_nm4843():
    return 'ret4843' 

@action('ctrl_act4844')
def ctrl_nm4844():
    return 'ret4844' 

@action('ctrl_act4845')
def ctrl_nm4845():
    return 'ret4845' 

@action('ctrl_act4846')
def ctrl_nm4846():
    return 'ret4846' 

@action('ctrl_act4847')
def ctrl_nm4847():
    return 'ret4847' 

@action('ctrl_act4848')
def ctrl_nm4848():
    return 'ret4848' 

@action('ctrl_act4849')
def ctrl_nm4849():
    return 'ret4849' 

@action('ctrl_act4850')
def ctrl_nm4850():
    return 'ret4850' 

@action('ctrl_act4851')
def ctrl_nm4851():
    return 'ret4851' 

@action('ctrl_act4852')
def ctrl_nm4852():
    return 'ret4852' 

@action('ctrl_act4853')
def ctrl_nm4853():
    return 'ret4853' 

@action('ctrl_act4854')
def ctrl_nm4854():
    return 'ret4854' 

@action('ctrl_act4855')
def ctrl_nm4855():
    return 'ret4855' 

@action('ctrl_act4856')
def ctrl_nm4856():
    return 'ret4856' 

@action('ctrl_act4857')
def ctrl_nm4857():
    return 'ret4857' 

@action('ctrl_act4858')
def ctrl_nm4858():
    return 'ret4858' 

@action('ctrl_act4859')
def ctrl_nm4859():
    return 'ret4859' 

@action('ctrl_act4860')
def ctrl_nm4860():
    return 'ret4860' 

@action('ctrl_act4861')
def ctrl_nm4861():
    return 'ret4861' 

@action('ctrl_act4862')
def ctrl_nm4862():
    return 'ret4862' 

@action('ctrl_act4863')
def ctrl_nm4863():
    return 'ret4863' 

@action('ctrl_act4864')
def ctrl_nm4864():
    return 'ret4864' 

@action('ctrl_act4865')
def ctrl_nm4865():
    return 'ret4865' 

@action('ctrl_act4866')
def ctrl_nm4866():
    return 'ret4866' 

@action('ctrl_act4867')
def ctrl_nm4867():
    return 'ret4867' 

@action('ctrl_act4868')
def ctrl_nm4868():
    return 'ret4868' 

@action('ctrl_act4869')
def ctrl_nm4869():
    return 'ret4869' 

@action('ctrl_act4870')
def ctrl_nm4870():
    return 'ret4870' 

@action('ctrl_act4871')
def ctrl_nm4871():
    return 'ret4871' 

@action('ctrl_act4872')
def ctrl_nm4872():
    return 'ret4872' 

@action('ctrl_act4873')
def ctrl_nm4873():
    return 'ret4873' 

@action('ctrl_act4874')
def ctrl_nm4874():
    return 'ret4874' 

@action('ctrl_act4875')
def ctrl_nm4875():
    return 'ret4875' 

@action('ctrl_act4876')
def ctrl_nm4876():
    return 'ret4876' 

@action('ctrl_act4877')
def ctrl_nm4877():
    return 'ret4877' 

@action('ctrl_act4878')
def ctrl_nm4878():
    return 'ret4878' 

@action('ctrl_act4879')
def ctrl_nm4879():
    return 'ret4879' 

@action('ctrl_act4880')
def ctrl_nm4880():
    return 'ret4880' 

@action('ctrl_act4881')
def ctrl_nm4881():
    return 'ret4881' 

@action('ctrl_act4882')
def ctrl_nm4882():
    return 'ret4882' 

@action('ctrl_act4883')
def ctrl_nm4883():
    return 'ret4883' 

@action('ctrl_act4884')
def ctrl_nm4884():
    return 'ret4884' 

@action('ctrl_act4885')
def ctrl_nm4885():
    return 'ret4885' 

@action('ctrl_act4886')
def ctrl_nm4886():
    return 'ret4886' 

@action('ctrl_act4887')
def ctrl_nm4887():
    return 'ret4887' 

@action('ctrl_act4888')
def ctrl_nm4888():
    return 'ret4888' 

@action('ctrl_act4889')
def ctrl_nm4889():
    return 'ret4889' 

@action('ctrl_act4890')
def ctrl_nm4890():
    return 'ret4890' 

@action('ctrl_act4891')
def ctrl_nm4891():
    return 'ret4891' 

@action('ctrl_act4892')
def ctrl_nm4892():
    return 'ret4892' 

@action('ctrl_act4893')
def ctrl_nm4893():
    return 'ret4893' 

@action('ctrl_act4894')
def ctrl_nm4894():
    return 'ret4894' 

@action('ctrl_act4895')
def ctrl_nm4895():
    return 'ret4895' 

@action('ctrl_act4896')
def ctrl_nm4896():
    return 'ret4896' 

@action('ctrl_act4897')
def ctrl_nm4897():
    return 'ret4897' 

@action('ctrl_act4898')
def ctrl_nm4898():
    return 'ret4898' 

@action('ctrl_act4899')
def ctrl_nm4899():
    return 'ret4899' 

@action('ctrl_act4900')
def ctrl_nm4900():
    return 'ret4900' 

@action('ctrl_act4901')
def ctrl_nm4901():
    return 'ret4901' 

@action('ctrl_act4902')
def ctrl_nm4902():
    return 'ret4902' 

@action('ctrl_act4903')
def ctrl_nm4903():
    return 'ret4903' 

@action('ctrl_act4904')
def ctrl_nm4904():
    return 'ret4904' 

@action('ctrl_act4905')
def ctrl_nm4905():
    return 'ret4905' 

@action('ctrl_act4906')
def ctrl_nm4906():
    return 'ret4906' 

@action('ctrl_act4907')
def ctrl_nm4907():
    return 'ret4907' 

@action('ctrl_act4908')
def ctrl_nm4908():
    return 'ret4908' 

@action('ctrl_act4909')
def ctrl_nm4909():
    return 'ret4909' 

@action('ctrl_act4910')
def ctrl_nm4910():
    return 'ret4910' 

@action('ctrl_act4911')
def ctrl_nm4911():
    return 'ret4911' 

@action('ctrl_act4912')
def ctrl_nm4912():
    return 'ret4912' 

@action('ctrl_act4913')
def ctrl_nm4913():
    return 'ret4913' 

@action('ctrl_act4914')
def ctrl_nm4914():
    return 'ret4914' 

@action('ctrl_act4915')
def ctrl_nm4915():
    return 'ret4915' 

@action('ctrl_act4916')
def ctrl_nm4916():
    return 'ret4916' 

@action('ctrl_act4917')
def ctrl_nm4917():
    return 'ret4917' 

@action('ctrl_act4918')
def ctrl_nm4918():
    return 'ret4918' 

@action('ctrl_act4919')
def ctrl_nm4919():
    return 'ret4919' 

@action('ctrl_act4920')
def ctrl_nm4920():
    return 'ret4920' 

@action('ctrl_act4921')
def ctrl_nm4921():
    return 'ret4921' 

@action('ctrl_act4922')
def ctrl_nm4922():
    return 'ret4922' 

@action('ctrl_act4923')
def ctrl_nm4923():
    return 'ret4923' 

@action('ctrl_act4924')
def ctrl_nm4924():
    return 'ret4924' 

@action('ctrl_act4925')
def ctrl_nm4925():
    return 'ret4925' 

@action('ctrl_act4926')
def ctrl_nm4926():
    return 'ret4926' 

@action('ctrl_act4927')
def ctrl_nm4927():
    return 'ret4927' 

@action('ctrl_act4928')
def ctrl_nm4928():
    return 'ret4928' 

@action('ctrl_act4929')
def ctrl_nm4929():
    return 'ret4929' 

@action('ctrl_act4930')
def ctrl_nm4930():
    return 'ret4930' 

@action('ctrl_act4931')
def ctrl_nm4931():
    return 'ret4931' 

@action('ctrl_act4932')
def ctrl_nm4932():
    return 'ret4932' 

@action('ctrl_act4933')
def ctrl_nm4933():
    return 'ret4933' 

@action('ctrl_act4934')
def ctrl_nm4934():
    return 'ret4934' 

@action('ctrl_act4935')
def ctrl_nm4935():
    return 'ret4935' 

@action('ctrl_act4936')
def ctrl_nm4936():
    return 'ret4936' 

@action('ctrl_act4937')
def ctrl_nm4937():
    return 'ret4937' 

@action('ctrl_act4938')
def ctrl_nm4938():
    return 'ret4938' 

@action('ctrl_act4939')
def ctrl_nm4939():
    return 'ret4939' 

@action('ctrl_act4940')
def ctrl_nm4940():
    return 'ret4940' 

@action('ctrl_act4941')
def ctrl_nm4941():
    return 'ret4941' 

@action('ctrl_act4942')
def ctrl_nm4942():
    return 'ret4942' 

@action('ctrl_act4943')
def ctrl_nm4943():
    return 'ret4943' 

@action('ctrl_act4944')
def ctrl_nm4944():
    return 'ret4944' 

@action('ctrl_act4945')
def ctrl_nm4945():
    return 'ret4945' 

@action('ctrl_act4946')
def ctrl_nm4946():
    return 'ret4946' 

@action('ctrl_act4947')
def ctrl_nm4947():
    return 'ret4947' 

@action('ctrl_act4948')
def ctrl_nm4948():
    return 'ret4948' 

@action('ctrl_act4949')
def ctrl_nm4949():
    return 'ret4949' 

@action('ctrl_act4950')
def ctrl_nm4950():
    return 'ret4950' 

@action('ctrl_act4951')
def ctrl_nm4951():
    return 'ret4951' 

@action('ctrl_act4952')
def ctrl_nm4952():
    return 'ret4952' 

@action('ctrl_act4953')
def ctrl_nm4953():
    return 'ret4953' 

@action('ctrl_act4954')
def ctrl_nm4954():
    return 'ret4954' 

@action('ctrl_act4955')
def ctrl_nm4955():
    return 'ret4955' 

@action('ctrl_act4956')
def ctrl_nm4956():
    return 'ret4956' 

@action('ctrl_act4957')
def ctrl_nm4957():
    return 'ret4957' 

@action('ctrl_act4958')
def ctrl_nm4958():
    return 'ret4958' 

@action('ctrl_act4959')
def ctrl_nm4959():
    return 'ret4959' 

@action('ctrl_act4960')
def ctrl_nm4960():
    return 'ret4960' 

@action('ctrl_act4961')
def ctrl_nm4961():
    return 'ret4961' 

@action('ctrl_act4962')
def ctrl_nm4962():
    return 'ret4962' 

@action('ctrl_act4963')
def ctrl_nm4963():
    return 'ret4963' 

@action('ctrl_act4964')
def ctrl_nm4964():
    return 'ret4964' 

@action('ctrl_act4965')
def ctrl_nm4965():
    return 'ret4965' 

@action('ctrl_act4966')
def ctrl_nm4966():
    return 'ret4966' 

@action('ctrl_act4967')
def ctrl_nm4967():
    return 'ret4967' 

@action('ctrl_act4968')
def ctrl_nm4968():
    return 'ret4968' 

@action('ctrl_act4969')
def ctrl_nm4969():
    return 'ret4969' 

@action('ctrl_act4970')
def ctrl_nm4970():
    return 'ret4970' 

@action('ctrl_act4971')
def ctrl_nm4971():
    return 'ret4971' 

@action('ctrl_act4972')
def ctrl_nm4972():
    return 'ret4972' 

@action('ctrl_act4973')
def ctrl_nm4973():
    return 'ret4973' 

@action('ctrl_act4974')
def ctrl_nm4974():
    return 'ret4974' 

@action('ctrl_act4975')
def ctrl_nm4975():
    return 'ret4975' 

@action('ctrl_act4976')
def ctrl_nm4976():
    return 'ret4976' 

@action('ctrl_act4977')
def ctrl_nm4977():
    return 'ret4977' 

@action('ctrl_act4978')
def ctrl_nm4978():
    return 'ret4978' 

@action('ctrl_act4979')
def ctrl_nm4979():
    return 'ret4979' 

@action('ctrl_act4980')
def ctrl_nm4980():
    return 'ret4980' 

@action('ctrl_act4981')
def ctrl_nm4981():
    return 'ret4981' 

@action('ctrl_act4982')
def ctrl_nm4982():
    return 'ret4982' 

@action('ctrl_act4983')
def ctrl_nm4983():
    return 'ret4983' 

@action('ctrl_act4984')
def ctrl_nm4984():
    return 'ret4984' 

@action('ctrl_act4985')
def ctrl_nm4985():
    return 'ret4985' 

@action('ctrl_act4986')
def ctrl_nm4986():
    return 'ret4986' 

@action('ctrl_act4987')
def ctrl_nm4987():
    return 'ret4987' 

@action('ctrl_act4988')
def ctrl_nm4988():
    return 'ret4988' 

@action('ctrl_act4989')
def ctrl_nm4989():
    return 'ret4989' 

@action('ctrl_act4990')
def ctrl_nm4990():
    return 'ret4990' 

@action('ctrl_act4991')
def ctrl_nm4991():
    return 'ret4991' 

@action('ctrl_act4992')
def ctrl_nm4992():
    return 'ret4992' 

@action('ctrl_act4993')
def ctrl_nm4993():
    return 'ret4993' 

@action('ctrl_act4994')
def ctrl_nm4994():
    return 'ret4994' 

@action('ctrl_act4995')
def ctrl_nm4995():
    return 'ret4995' 

@action('ctrl_act4996')
def ctrl_nm4996():
    return 'ret4996' 

@action('ctrl_act4997')
def ctrl_nm4997():
    return 'ret4997' 

@action('ctrl_act4998')
def ctrl_nm4998():
    return 'ret4998' 

@action('ctrl_act4999')
def ctrl_nm4999():
    return 'ret4999' 

@action('ctrl_act5000')
def ctrl_nm5000():
    return 'ret5000' 

@action('ctrl_act5001')
def ctrl_nm5001():
    return 'ret5001' 

@action('ctrl_act5002')
def ctrl_nm5002():
    return 'ret5002' 

@action('ctrl_act5003')
def ctrl_nm5003():
    return 'ret5003' 

@action('ctrl_act5004')
def ctrl_nm5004():
    return 'ret5004' 

@action('ctrl_act5005')
def ctrl_nm5005():
    return 'ret5005' 

@action('ctrl_act5006')
def ctrl_nm5006():
    return 'ret5006' 

@action('ctrl_act5007')
def ctrl_nm5007():
    return 'ret5007' 

@action('ctrl_act5008')
def ctrl_nm5008():
    return 'ret5008' 

@action('ctrl_act5009')
def ctrl_nm5009():
    return 'ret5009' 

@action('ctrl_act5010')
def ctrl_nm5010():
    return 'ret5010' 

@action('ctrl_act5011')
def ctrl_nm5011():
    return 'ret5011' 

@action('ctrl_act5012')
def ctrl_nm5012():
    return 'ret5012' 

@action('ctrl_act5013')
def ctrl_nm5013():
    return 'ret5013' 

@action('ctrl_act5014')
def ctrl_nm5014():
    return 'ret5014' 

@action('ctrl_act5015')
def ctrl_nm5015():
    return 'ret5015' 

@action('ctrl_act5016')
def ctrl_nm5016():
    return 'ret5016' 

@action('ctrl_act5017')
def ctrl_nm5017():
    return 'ret5017' 

@action('ctrl_act5018')
def ctrl_nm5018():
    return 'ret5018' 

@action('ctrl_act5019')
def ctrl_nm5019():
    return 'ret5019' 

@action('ctrl_act5020')
def ctrl_nm5020():
    return 'ret5020' 

@action('ctrl_act5021')
def ctrl_nm5021():
    return 'ret5021' 

@action('ctrl_act5022')
def ctrl_nm5022():
    return 'ret5022' 

@action('ctrl_act5023')
def ctrl_nm5023():
    return 'ret5023' 

@action('ctrl_act5024')
def ctrl_nm5024():
    return 'ret5024' 

@action('ctrl_act5025')
def ctrl_nm5025():
    return 'ret5025' 

@action('ctrl_act5026')
def ctrl_nm5026():
    return 'ret5026' 

@action('ctrl_act5027')
def ctrl_nm5027():
    return 'ret5027' 

@action('ctrl_act5028')
def ctrl_nm5028():
    return 'ret5028' 

@action('ctrl_act5029')
def ctrl_nm5029():
    return 'ret5029' 

@action('ctrl_act5030')
def ctrl_nm5030():
    return 'ret5030' 

@action('ctrl_act5031')
def ctrl_nm5031():
    return 'ret5031' 

@action('ctrl_act5032')
def ctrl_nm5032():
    return 'ret5032' 

@action('ctrl_act5033')
def ctrl_nm5033():
    return 'ret5033' 

@action('ctrl_act5034')
def ctrl_nm5034():
    return 'ret5034' 

@action('ctrl_act5035')
def ctrl_nm5035():
    return 'ret5035' 

@action('ctrl_act5036')
def ctrl_nm5036():
    return 'ret5036' 

@action('ctrl_act5037')
def ctrl_nm5037():
    return 'ret5037' 

@action('ctrl_act5038')
def ctrl_nm5038():
    return 'ret5038' 

@action('ctrl_act5039')
def ctrl_nm5039():
    return 'ret5039' 

@action('ctrl_act5040')
def ctrl_nm5040():
    return 'ret5040' 

@action('ctrl_act5041')
def ctrl_nm5041():
    return 'ret5041' 

@action('ctrl_act5042')
def ctrl_nm5042():
    return 'ret5042' 

@action('ctrl_act5043')
def ctrl_nm5043():
    return 'ret5043' 

@action('ctrl_act5044')
def ctrl_nm5044():
    return 'ret5044' 

@action('ctrl_act5045')
def ctrl_nm5045():
    return 'ret5045' 

@action('ctrl_act5046')
def ctrl_nm5046():
    return 'ret5046' 

@action('ctrl_act5047')
def ctrl_nm5047():
    return 'ret5047' 

@action('ctrl_act5048')
def ctrl_nm5048():
    return 'ret5048' 

@action('ctrl_act5049')
def ctrl_nm5049():
    return 'ret5049' 

@action('ctrl_act5050')
def ctrl_nm5050():
    return 'ret5050' 

@action('ctrl_act5051')
def ctrl_nm5051():
    return 'ret5051' 

@action('ctrl_act5052')
def ctrl_nm5052():
    return 'ret5052' 

@action('ctrl_act5053')
def ctrl_nm5053():
    return 'ret5053' 

@action('ctrl_act5054')
def ctrl_nm5054():
    return 'ret5054' 

@action('ctrl_act5055')
def ctrl_nm5055():
    return 'ret5055' 

@action('ctrl_act5056')
def ctrl_nm5056():
    return 'ret5056' 

@action('ctrl_act5057')
def ctrl_nm5057():
    return 'ret5057' 

@action('ctrl_act5058')
def ctrl_nm5058():
    return 'ret5058' 

@action('ctrl_act5059')
def ctrl_nm5059():
    return 'ret5059' 

@action('ctrl_act5060')
def ctrl_nm5060():
    return 'ret5060' 

@action('ctrl_act5061')
def ctrl_nm5061():
    return 'ret5061' 

@action('ctrl_act5062')
def ctrl_nm5062():
    return 'ret5062' 

@action('ctrl_act5063')
def ctrl_nm5063():
    return 'ret5063' 

@action('ctrl_act5064')
def ctrl_nm5064():
    return 'ret5064' 

@action('ctrl_act5065')
def ctrl_nm5065():
    return 'ret5065' 

@action('ctrl_act5066')
def ctrl_nm5066():
    return 'ret5066' 

@action('ctrl_act5067')
def ctrl_nm5067():
    return 'ret5067' 

@action('ctrl_act5068')
def ctrl_nm5068():
    return 'ret5068' 

@action('ctrl_act5069')
def ctrl_nm5069():
    return 'ret5069' 

@action('ctrl_act5070')
def ctrl_nm5070():
    return 'ret5070' 

@action('ctrl_act5071')
def ctrl_nm5071():
    return 'ret5071' 

@action('ctrl_act5072')
def ctrl_nm5072():
    return 'ret5072' 

@action('ctrl_act5073')
def ctrl_nm5073():
    return 'ret5073' 

@action('ctrl_act5074')
def ctrl_nm5074():
    return 'ret5074' 

@action('ctrl_act5075')
def ctrl_nm5075():
    return 'ret5075' 

@action('ctrl_act5076')
def ctrl_nm5076():
    return 'ret5076' 

@action('ctrl_act5077')
def ctrl_nm5077():
    return 'ret5077' 

@action('ctrl_act5078')
def ctrl_nm5078():
    return 'ret5078' 

@action('ctrl_act5079')
def ctrl_nm5079():
    return 'ret5079' 

@action('ctrl_act5080')
def ctrl_nm5080():
    return 'ret5080' 

@action('ctrl_act5081')
def ctrl_nm5081():
    return 'ret5081' 

@action('ctrl_act5082')
def ctrl_nm5082():
    return 'ret5082' 

@action('ctrl_act5083')
def ctrl_nm5083():
    return 'ret5083' 

@action('ctrl_act5084')
def ctrl_nm5084():
    return 'ret5084' 

@action('ctrl_act5085')
def ctrl_nm5085():
    return 'ret5085' 

@action('ctrl_act5086')
def ctrl_nm5086():
    return 'ret5086' 

@action('ctrl_act5087')
def ctrl_nm5087():
    return 'ret5087' 

@action('ctrl_act5088')
def ctrl_nm5088():
    return 'ret5088' 

@action('ctrl_act5089')
def ctrl_nm5089():
    return 'ret5089' 

@action('ctrl_act5090')
def ctrl_nm5090():
    return 'ret5090' 

@action('ctrl_act5091')
def ctrl_nm5091():
    return 'ret5091' 

@action('ctrl_act5092')
def ctrl_nm5092():
    return 'ret5092' 

@action('ctrl_act5093')
def ctrl_nm5093():
    return 'ret5093' 

@action('ctrl_act5094')
def ctrl_nm5094():
    return 'ret5094' 

@action('ctrl_act5095')
def ctrl_nm5095():
    return 'ret5095' 

@action('ctrl_act5096')
def ctrl_nm5096():
    return 'ret5096' 

@action('ctrl_act5097')
def ctrl_nm5097():
    return 'ret5097' 

@action('ctrl_act5098')
def ctrl_nm5098():
    return 'ret5098' 

@action('ctrl_act5099')
def ctrl_nm5099():
    return 'ret5099' 

@action('ctrl_act5100')
def ctrl_nm5100():
    return 'ret5100' 

@action('ctrl_act5101')
def ctrl_nm5101():
    return 'ret5101' 

@action('ctrl_act5102')
def ctrl_nm5102():
    return 'ret5102' 

@action('ctrl_act5103')
def ctrl_nm5103():
    return 'ret5103' 

@action('ctrl_act5104')
def ctrl_nm5104():
    return 'ret5104' 

@action('ctrl_act5105')
def ctrl_nm5105():
    return 'ret5105' 

@action('ctrl_act5106')
def ctrl_nm5106():
    return 'ret5106' 

@action('ctrl_act5107')
def ctrl_nm5107():
    return 'ret5107' 

@action('ctrl_act5108')
def ctrl_nm5108():
    return 'ret5108' 

@action('ctrl_act5109')
def ctrl_nm5109():
    return 'ret5109' 

@action('ctrl_act5110')
def ctrl_nm5110():
    return 'ret5110' 

@action('ctrl_act5111')
def ctrl_nm5111():
    return 'ret5111' 

@action('ctrl_act5112')
def ctrl_nm5112():
    return 'ret5112' 

@action('ctrl_act5113')
def ctrl_nm5113():
    return 'ret5113' 

@action('ctrl_act5114')
def ctrl_nm5114():
    return 'ret5114' 

@action('ctrl_act5115')
def ctrl_nm5115():
    return 'ret5115' 

@action('ctrl_act5116')
def ctrl_nm5116():
    return 'ret5116' 

@action('ctrl_act5117')
def ctrl_nm5117():
    return 'ret5117' 

@action('ctrl_act5118')
def ctrl_nm5118():
    return 'ret5118' 

@action('ctrl_act5119')
def ctrl_nm5119():
    return 'ret5119' 

@action('ctrl_act5120')
def ctrl_nm5120():
    return 'ret5120' 

@action('ctrl_act5121')
def ctrl_nm5121():
    return 'ret5121' 

@action('ctrl_act5122')
def ctrl_nm5122():
    return 'ret5122' 

@action('ctrl_act5123')
def ctrl_nm5123():
    return 'ret5123' 

@action('ctrl_act5124')
def ctrl_nm5124():
    return 'ret5124' 

@action('ctrl_act5125')
def ctrl_nm5125():
    return 'ret5125' 

@action('ctrl_act5126')
def ctrl_nm5126():
    return 'ret5126' 

@action('ctrl_act5127')
def ctrl_nm5127():
    return 'ret5127' 

@action('ctrl_act5128')
def ctrl_nm5128():
    return 'ret5128' 

@action('ctrl_act5129')
def ctrl_nm5129():
    return 'ret5129' 

@action('ctrl_act5130')
def ctrl_nm5130():
    return 'ret5130' 

@action('ctrl_act5131')
def ctrl_nm5131():
    return 'ret5131' 

@action('ctrl_act5132')
def ctrl_nm5132():
    return 'ret5132' 

@action('ctrl_act5133')
def ctrl_nm5133():
    return 'ret5133' 

@action('ctrl_act5134')
def ctrl_nm5134():
    return 'ret5134' 

@action('ctrl_act5135')
def ctrl_nm5135():
    return 'ret5135' 

@action('ctrl_act5136')
def ctrl_nm5136():
    return 'ret5136' 

@action('ctrl_act5137')
def ctrl_nm5137():
    return 'ret5137' 

@action('ctrl_act5138')
def ctrl_nm5138():
    return 'ret5138' 

@action('ctrl_act5139')
def ctrl_nm5139():
    return 'ret5139' 

@action('ctrl_act5140')
def ctrl_nm5140():
    return 'ret5140' 

@action('ctrl_act5141')
def ctrl_nm5141():
    return 'ret5141' 

@action('ctrl_act5142')
def ctrl_nm5142():
    return 'ret5142' 

@action('ctrl_act5143')
def ctrl_nm5143():
    return 'ret5143' 

@action('ctrl_act5144')
def ctrl_nm5144():
    return 'ret5144' 

@action('ctrl_act5145')
def ctrl_nm5145():
    return 'ret5145' 

@action('ctrl_act5146')
def ctrl_nm5146():
    return 'ret5146' 

@action('ctrl_act5147')
def ctrl_nm5147():
    return 'ret5147' 

@action('ctrl_act5148')
def ctrl_nm5148():
    return 'ret5148' 

@action('ctrl_act5149')
def ctrl_nm5149():
    return 'ret5149' 

@action('ctrl_act5150')
def ctrl_nm5150():
    return 'ret5150' 

@action('ctrl_act5151')
def ctrl_nm5151():
    return 'ret5151' 

@action('ctrl_act5152')
def ctrl_nm5152():
    return 'ret5152' 

@action('ctrl_act5153')
def ctrl_nm5153():
    return 'ret5153' 

@action('ctrl_act5154')
def ctrl_nm5154():
    return 'ret5154' 

@action('ctrl_act5155')
def ctrl_nm5155():
    return 'ret5155' 

@action('ctrl_act5156')
def ctrl_nm5156():
    return 'ret5156' 

@action('ctrl_act5157')
def ctrl_nm5157():
    return 'ret5157' 

@action('ctrl_act5158')
def ctrl_nm5158():
    return 'ret5158' 

@action('ctrl_act5159')
def ctrl_nm5159():
    return 'ret5159' 

@action('ctrl_act5160')
def ctrl_nm5160():
    return 'ret5160' 

@action('ctrl_act5161')
def ctrl_nm5161():
    return 'ret5161' 

@action('ctrl_act5162')
def ctrl_nm5162():
    return 'ret5162' 

@action('ctrl_act5163')
def ctrl_nm5163():
    return 'ret5163' 

@action('ctrl_act5164')
def ctrl_nm5164():
    return 'ret5164' 

@action('ctrl_act5165')
def ctrl_nm5165():
    return 'ret5165' 

@action('ctrl_act5166')
def ctrl_nm5166():
    return 'ret5166' 

@action('ctrl_act5167')
def ctrl_nm5167():
    return 'ret5167' 

@action('ctrl_act5168')
def ctrl_nm5168():
    return 'ret5168' 

@action('ctrl_act5169')
def ctrl_nm5169():
    return 'ret5169' 

@action('ctrl_act5170')
def ctrl_nm5170():
    return 'ret5170' 

@action('ctrl_act5171')
def ctrl_nm5171():
    return 'ret5171' 

@action('ctrl_act5172')
def ctrl_nm5172():
    return 'ret5172' 

@action('ctrl_act5173')
def ctrl_nm5173():
    return 'ret5173' 

@action('ctrl_act5174')
def ctrl_nm5174():
    return 'ret5174' 

@action('ctrl_act5175')
def ctrl_nm5175():
    return 'ret5175' 

@action('ctrl_act5176')
def ctrl_nm5176():
    return 'ret5176' 

@action('ctrl_act5177')
def ctrl_nm5177():
    return 'ret5177' 

@action('ctrl_act5178')
def ctrl_nm5178():
    return 'ret5178' 

@action('ctrl_act5179')
def ctrl_nm5179():
    return 'ret5179' 

@action('ctrl_act5180')
def ctrl_nm5180():
    return 'ret5180' 

@action('ctrl_act5181')
def ctrl_nm5181():
    return 'ret5181' 

@action('ctrl_act5182')
def ctrl_nm5182():
    return 'ret5182' 

@action('ctrl_act5183')
def ctrl_nm5183():
    return 'ret5183' 

@action('ctrl_act5184')
def ctrl_nm5184():
    return 'ret5184' 

@action('ctrl_act5185')
def ctrl_nm5185():
    return 'ret5185' 

@action('ctrl_act5186')
def ctrl_nm5186():
    return 'ret5186' 

@action('ctrl_act5187')
def ctrl_nm5187():
    return 'ret5187' 

@action('ctrl_act5188')
def ctrl_nm5188():
    return 'ret5188' 

@action('ctrl_act5189')
def ctrl_nm5189():
    return 'ret5189' 

@action('ctrl_act5190')
def ctrl_nm5190():
    return 'ret5190' 

@action('ctrl_act5191')
def ctrl_nm5191():
    return 'ret5191' 

@action('ctrl_act5192')
def ctrl_nm5192():
    return 'ret5192' 

@action('ctrl_act5193')
def ctrl_nm5193():
    return 'ret5193' 

@action('ctrl_act5194')
def ctrl_nm5194():
    return 'ret5194' 

@action('ctrl_act5195')
def ctrl_nm5195():
    return 'ret5195' 

@action('ctrl_act5196')
def ctrl_nm5196():
    return 'ret5196' 

@action('ctrl_act5197')
def ctrl_nm5197():
    return 'ret5197' 

@action('ctrl_act5198')
def ctrl_nm5198():
    return 'ret5198' 

@action('ctrl_act5199')
def ctrl_nm5199():
    return 'ret5199' 

@action('ctrl_act5200')
def ctrl_nm5200():
    return 'ret5200' 

@action('ctrl_act5201')
def ctrl_nm5201():
    return 'ret5201' 

@action('ctrl_act5202')
def ctrl_nm5202():
    return 'ret5202' 

@action('ctrl_act5203')
def ctrl_nm5203():
    return 'ret5203' 

@action('ctrl_act5204')
def ctrl_nm5204():
    return 'ret5204' 

@action('ctrl_act5205')
def ctrl_nm5205():
    return 'ret5205' 

@action('ctrl_act5206')
def ctrl_nm5206():
    return 'ret5206' 

@action('ctrl_act5207')
def ctrl_nm5207():
    return 'ret5207' 

@action('ctrl_act5208')
def ctrl_nm5208():
    return 'ret5208' 

@action('ctrl_act5209')
def ctrl_nm5209():
    return 'ret5209' 

@action('ctrl_act5210')
def ctrl_nm5210():
    return 'ret5210' 

@action('ctrl_act5211')
def ctrl_nm5211():
    return 'ret5211' 

@action('ctrl_act5212')
def ctrl_nm5212():
    return 'ret5212' 

@action('ctrl_act5213')
def ctrl_nm5213():
    return 'ret5213' 

@action('ctrl_act5214')
def ctrl_nm5214():
    return 'ret5214' 

@action('ctrl_act5215')
def ctrl_nm5215():
    return 'ret5215' 

@action('ctrl_act5216')
def ctrl_nm5216():
    return 'ret5216' 

@action('ctrl_act5217')
def ctrl_nm5217():
    return 'ret5217' 

@action('ctrl_act5218')
def ctrl_nm5218():
    return 'ret5218' 

@action('ctrl_act5219')
def ctrl_nm5219():
    return 'ret5219' 

@action('ctrl_act5220')
def ctrl_nm5220():
    return 'ret5220' 

@action('ctrl_act5221')
def ctrl_nm5221():
    return 'ret5221' 

@action('ctrl_act5222')
def ctrl_nm5222():
    return 'ret5222' 

@action('ctrl_act5223')
def ctrl_nm5223():
    return 'ret5223' 

@action('ctrl_act5224')
def ctrl_nm5224():
    return 'ret5224' 

@action('ctrl_act5225')
def ctrl_nm5225():
    return 'ret5225' 

@action('ctrl_act5226')
def ctrl_nm5226():
    return 'ret5226' 

@action('ctrl_act5227')
def ctrl_nm5227():
    return 'ret5227' 

@action('ctrl_act5228')
def ctrl_nm5228():
    return 'ret5228' 

@action('ctrl_act5229')
def ctrl_nm5229():
    return 'ret5229' 

@action('ctrl_act5230')
def ctrl_nm5230():
    return 'ret5230' 

@action('ctrl_act5231')
def ctrl_nm5231():
    return 'ret5231' 

@action('ctrl_act5232')
def ctrl_nm5232():
    return 'ret5232' 

@action('ctrl_act5233')
def ctrl_nm5233():
    return 'ret5233' 

@action('ctrl_act5234')
def ctrl_nm5234():
    return 'ret5234' 

@action('ctrl_act5235')
def ctrl_nm5235():
    return 'ret5235' 

@action('ctrl_act5236')
def ctrl_nm5236():
    return 'ret5236' 

@action('ctrl_act5237')
def ctrl_nm5237():
    return 'ret5237' 

@action('ctrl_act5238')
def ctrl_nm5238():
    return 'ret5238' 

@action('ctrl_act5239')
def ctrl_nm5239():
    return 'ret5239' 

@action('ctrl_act5240')
def ctrl_nm5240():
    return 'ret5240' 

@action('ctrl_act5241')
def ctrl_nm5241():
    return 'ret5241' 

@action('ctrl_act5242')
def ctrl_nm5242():
    return 'ret5242' 

@action('ctrl_act5243')
def ctrl_nm5243():
    return 'ret5243' 

@action('ctrl_act5244')
def ctrl_nm5244():
    return 'ret5244' 

@action('ctrl_act5245')
def ctrl_nm5245():
    return 'ret5245' 

@action('ctrl_act5246')
def ctrl_nm5246():
    return 'ret5246' 

@action('ctrl_act5247')
def ctrl_nm5247():
    return 'ret5247' 

@action('ctrl_act5248')
def ctrl_nm5248():
    return 'ret5248' 

@action('ctrl_act5249')
def ctrl_nm5249():
    return 'ret5249' 

@action('ctrl_act5250')
def ctrl_nm5250():
    return 'ret5250' 

@action('ctrl_act5251')
def ctrl_nm5251():
    return 'ret5251' 

@action('ctrl_act5252')
def ctrl_nm5252():
    return 'ret5252' 

@action('ctrl_act5253')
def ctrl_nm5253():
    return 'ret5253' 

@action('ctrl_act5254')
def ctrl_nm5254():
    return 'ret5254' 

@action('ctrl_act5255')
def ctrl_nm5255():
    return 'ret5255' 

@action('ctrl_act5256')
def ctrl_nm5256():
    return 'ret5256' 

@action('ctrl_act5257')
def ctrl_nm5257():
    return 'ret5257' 

@action('ctrl_act5258')
def ctrl_nm5258():
    return 'ret5258' 

@action('ctrl_act5259')
def ctrl_nm5259():
    return 'ret5259' 

@action('ctrl_act5260')
def ctrl_nm5260():
    return 'ret5260' 

@action('ctrl_act5261')
def ctrl_nm5261():
    return 'ret5261' 

@action('ctrl_act5262')
def ctrl_nm5262():
    return 'ret5262' 

@action('ctrl_act5263')
def ctrl_nm5263():
    return 'ret5263' 

@action('ctrl_act5264')
def ctrl_nm5264():
    return 'ret5264' 

@action('ctrl_act5265')
def ctrl_nm5265():
    return 'ret5265' 

@action('ctrl_act5266')
def ctrl_nm5266():
    return 'ret5266' 

@action('ctrl_act5267')
def ctrl_nm5267():
    return 'ret5267' 

@action('ctrl_act5268')
def ctrl_nm5268():
    return 'ret5268' 

@action('ctrl_act5269')
def ctrl_nm5269():
    return 'ret5269' 

@action('ctrl_act5270')
def ctrl_nm5270():
    return 'ret5270' 

@action('ctrl_act5271')
def ctrl_nm5271():
    return 'ret5271' 

@action('ctrl_act5272')
def ctrl_nm5272():
    return 'ret5272' 

@action('ctrl_act5273')
def ctrl_nm5273():
    return 'ret5273' 

@action('ctrl_act5274')
def ctrl_nm5274():
    return 'ret5274' 

@action('ctrl_act5275')
def ctrl_nm5275():
    return 'ret5275' 

@action('ctrl_act5276')
def ctrl_nm5276():
    return 'ret5276' 

@action('ctrl_act5277')
def ctrl_nm5277():
    return 'ret5277' 

@action('ctrl_act5278')
def ctrl_nm5278():
    return 'ret5278' 

@action('ctrl_act5279')
def ctrl_nm5279():
    return 'ret5279' 

@action('ctrl_act5280')
def ctrl_nm5280():
    return 'ret5280' 

@action('ctrl_act5281')
def ctrl_nm5281():
    return 'ret5281' 

@action('ctrl_act5282')
def ctrl_nm5282():
    return 'ret5282' 

@action('ctrl_act5283')
def ctrl_nm5283():
    return 'ret5283' 

@action('ctrl_act5284')
def ctrl_nm5284():
    return 'ret5284' 

@action('ctrl_act5285')
def ctrl_nm5285():
    return 'ret5285' 

@action('ctrl_act5286')
def ctrl_nm5286():
    return 'ret5286' 

@action('ctrl_act5287')
def ctrl_nm5287():
    return 'ret5287' 

@action('ctrl_act5288')
def ctrl_nm5288():
    return 'ret5288' 

@action('ctrl_act5289')
def ctrl_nm5289():
    return 'ret5289' 

@action('ctrl_act5290')
def ctrl_nm5290():
    return 'ret5290' 

@action('ctrl_act5291')
def ctrl_nm5291():
    return 'ret5291' 

@action('ctrl_act5292')
def ctrl_nm5292():
    return 'ret5292' 

@action('ctrl_act5293')
def ctrl_nm5293():
    return 'ret5293' 

@action('ctrl_act5294')
def ctrl_nm5294():
    return 'ret5294' 

@action('ctrl_act5295')
def ctrl_nm5295():
    return 'ret5295' 

@action('ctrl_act5296')
def ctrl_nm5296():
    return 'ret5296' 

@action('ctrl_act5297')
def ctrl_nm5297():
    return 'ret5297' 

@action('ctrl_act5298')
def ctrl_nm5298():
    return 'ret5298' 

@action('ctrl_act5299')
def ctrl_nm5299():
    return 'ret5299' 

@action('ctrl_act5300')
def ctrl_nm5300():
    return 'ret5300' 

@action('ctrl_act5301')
def ctrl_nm5301():
    return 'ret5301' 

@action('ctrl_act5302')
def ctrl_nm5302():
    return 'ret5302' 

@action('ctrl_act5303')
def ctrl_nm5303():
    return 'ret5303' 

@action('ctrl_act5304')
def ctrl_nm5304():
    return 'ret5304' 

@action('ctrl_act5305')
def ctrl_nm5305():
    return 'ret5305' 

@action('ctrl_act5306')
def ctrl_nm5306():
    return 'ret5306' 

@action('ctrl_act5307')
def ctrl_nm5307():
    return 'ret5307' 

@action('ctrl_act5308')
def ctrl_nm5308():
    return 'ret5308' 

@action('ctrl_act5309')
def ctrl_nm5309():
    return 'ret5309' 

@action('ctrl_act5310')
def ctrl_nm5310():
    return 'ret5310' 

@action('ctrl_act5311')
def ctrl_nm5311():
    return 'ret5311' 

@action('ctrl_act5312')
def ctrl_nm5312():
    return 'ret5312' 

@action('ctrl_act5313')
def ctrl_nm5313():
    return 'ret5313' 

@action('ctrl_act5314')
def ctrl_nm5314():
    return 'ret5314' 

@action('ctrl_act5315')
def ctrl_nm5315():
    return 'ret5315' 

@action('ctrl_act5316')
def ctrl_nm5316():
    return 'ret5316' 

@action('ctrl_act5317')
def ctrl_nm5317():
    return 'ret5317' 

@action('ctrl_act5318')
def ctrl_nm5318():
    return 'ret5318' 

@action('ctrl_act5319')
def ctrl_nm5319():
    return 'ret5319' 

@action('ctrl_act5320')
def ctrl_nm5320():
    return 'ret5320' 

@action('ctrl_act5321')
def ctrl_nm5321():
    return 'ret5321' 

@action('ctrl_act5322')
def ctrl_nm5322():
    return 'ret5322' 

@action('ctrl_act5323')
def ctrl_nm5323():
    return 'ret5323' 

@action('ctrl_act5324')
def ctrl_nm5324():
    return 'ret5324' 

@action('ctrl_act5325')
def ctrl_nm5325():
    return 'ret5325' 

@action('ctrl_act5326')
def ctrl_nm5326():
    return 'ret5326' 

@action('ctrl_act5327')
def ctrl_nm5327():
    return 'ret5327' 

@action('ctrl_act5328')
def ctrl_nm5328():
    return 'ret5328' 

@action('ctrl_act5329')
def ctrl_nm5329():
    return 'ret5329' 

@action('ctrl_act5330')
def ctrl_nm5330():
    return 'ret5330' 

@action('ctrl_act5331')
def ctrl_nm5331():
    return 'ret5331' 

@action('ctrl_act5332')
def ctrl_nm5332():
    return 'ret5332' 

@action('ctrl_act5333')
def ctrl_nm5333():
    return 'ret5333' 

@action('ctrl_act5334')
def ctrl_nm5334():
    return 'ret5334' 

@action('ctrl_act5335')
def ctrl_nm5335():
    return 'ret5335' 

@action('ctrl_act5336')
def ctrl_nm5336():
    return 'ret5336' 

@action('ctrl_act5337')
def ctrl_nm5337():
    return 'ret5337' 

@action('ctrl_act5338')
def ctrl_nm5338():
    return 'ret5338' 

@action('ctrl_act5339')
def ctrl_nm5339():
    return 'ret5339' 

@action('ctrl_act5340')
def ctrl_nm5340():
    return 'ret5340' 

@action('ctrl_act5341')
def ctrl_nm5341():
    return 'ret5341' 

@action('ctrl_act5342')
def ctrl_nm5342():
    return 'ret5342' 

@action('ctrl_act5343')
def ctrl_nm5343():
    return 'ret5343' 

@action('ctrl_act5344')
def ctrl_nm5344():
    return 'ret5344' 

@action('ctrl_act5345')
def ctrl_nm5345():
    return 'ret5345' 

@action('ctrl_act5346')
def ctrl_nm5346():
    return 'ret5346' 

@action('ctrl_act5347')
def ctrl_nm5347():
    return 'ret5347' 

@action('ctrl_act5348')
def ctrl_nm5348():
    return 'ret5348' 

@action('ctrl_act5349')
def ctrl_nm5349():
    return 'ret5349' 

@action('ctrl_act5350')
def ctrl_nm5350():
    return 'ret5350' 

@action('ctrl_act5351')
def ctrl_nm5351():
    return 'ret5351' 

@action('ctrl_act5352')
def ctrl_nm5352():
    return 'ret5352' 

@action('ctrl_act5353')
def ctrl_nm5353():
    return 'ret5353' 

@action('ctrl_act5354')
def ctrl_nm5354():
    return 'ret5354' 

@action('ctrl_act5355')
def ctrl_nm5355():
    return 'ret5355' 

@action('ctrl_act5356')
def ctrl_nm5356():
    return 'ret5356' 

@action('ctrl_act5357')
def ctrl_nm5357():
    return 'ret5357' 

@action('ctrl_act5358')
def ctrl_nm5358():
    return 'ret5358' 

@action('ctrl_act5359')
def ctrl_nm5359():
    return 'ret5359' 

@action('ctrl_act5360')
def ctrl_nm5360():
    return 'ret5360' 

@action('ctrl_act5361')
def ctrl_nm5361():
    return 'ret5361' 

@action('ctrl_act5362')
def ctrl_nm5362():
    return 'ret5362' 

@action('ctrl_act5363')
def ctrl_nm5363():
    return 'ret5363' 

@action('ctrl_act5364')
def ctrl_nm5364():
    return 'ret5364' 

@action('ctrl_act5365')
def ctrl_nm5365():
    return 'ret5365' 

@action('ctrl_act5366')
def ctrl_nm5366():
    return 'ret5366' 

@action('ctrl_act5367')
def ctrl_nm5367():
    return 'ret5367' 

@action('ctrl_act5368')
def ctrl_nm5368():
    return 'ret5368' 

@action('ctrl_act5369')
def ctrl_nm5369():
    return 'ret5369' 

@action('ctrl_act5370')
def ctrl_nm5370():
    return 'ret5370' 

@action('ctrl_act5371')
def ctrl_nm5371():
    return 'ret5371' 

@action('ctrl_act5372')
def ctrl_nm5372():
    return 'ret5372' 

@action('ctrl_act5373')
def ctrl_nm5373():
    return 'ret5373' 

@action('ctrl_act5374')
def ctrl_nm5374():
    return 'ret5374' 

@action('ctrl_act5375')
def ctrl_nm5375():
    return 'ret5375' 

@action('ctrl_act5376')
def ctrl_nm5376():
    return 'ret5376' 

@action('ctrl_act5377')
def ctrl_nm5377():
    return 'ret5377' 

@action('ctrl_act5378')
def ctrl_nm5378():
    return 'ret5378' 

@action('ctrl_act5379')
def ctrl_nm5379():
    return 'ret5379' 

@action('ctrl_act5380')
def ctrl_nm5380():
    return 'ret5380' 

@action('ctrl_act5381')
def ctrl_nm5381():
    return 'ret5381' 

@action('ctrl_act5382')
def ctrl_nm5382():
    return 'ret5382' 

@action('ctrl_act5383')
def ctrl_nm5383():
    return 'ret5383' 

@action('ctrl_act5384')
def ctrl_nm5384():
    return 'ret5384' 

@action('ctrl_act5385')
def ctrl_nm5385():
    return 'ret5385' 

@action('ctrl_act5386')
def ctrl_nm5386():
    return 'ret5386' 

@action('ctrl_act5387')
def ctrl_nm5387():
    return 'ret5387' 

@action('ctrl_act5388')
def ctrl_nm5388():
    return 'ret5388' 

@action('ctrl_act5389')
def ctrl_nm5389():
    return 'ret5389' 

@action('ctrl_act5390')
def ctrl_nm5390():
    return 'ret5390' 

@action('ctrl_act5391')
def ctrl_nm5391():
    return 'ret5391' 

@action('ctrl_act5392')
def ctrl_nm5392():
    return 'ret5392' 

@action('ctrl_act5393')
def ctrl_nm5393():
    return 'ret5393' 

@action('ctrl_act5394')
def ctrl_nm5394():
    return 'ret5394' 

@action('ctrl_act5395')
def ctrl_nm5395():
    return 'ret5395' 

@action('ctrl_act5396')
def ctrl_nm5396():
    return 'ret5396' 

@action('ctrl_act5397')
def ctrl_nm5397():
    return 'ret5397' 

@action('ctrl_act5398')
def ctrl_nm5398():
    return 'ret5398' 

@action('ctrl_act5399')
def ctrl_nm5399():
    return 'ret5399' 

@action('ctrl_act5400')
def ctrl_nm5400():
    return 'ret5400' 

@action('ctrl_act5401')
def ctrl_nm5401():
    return 'ret5401' 

@action('ctrl_act5402')
def ctrl_nm5402():
    return 'ret5402' 

@action('ctrl_act5403')
def ctrl_nm5403():
    return 'ret5403' 

@action('ctrl_act5404')
def ctrl_nm5404():
    return 'ret5404' 

@action('ctrl_act5405')
def ctrl_nm5405():
    return 'ret5405' 

@action('ctrl_act5406')
def ctrl_nm5406():
    return 'ret5406' 

@action('ctrl_act5407')
def ctrl_nm5407():
    return 'ret5407' 

@action('ctrl_act5408')
def ctrl_nm5408():
    return 'ret5408' 

@action('ctrl_act5409')
def ctrl_nm5409():
    return 'ret5409' 

@action('ctrl_act5410')
def ctrl_nm5410():
    return 'ret5410' 

@action('ctrl_act5411')
def ctrl_nm5411():
    return 'ret5411' 

@action('ctrl_act5412')
def ctrl_nm5412():
    return 'ret5412' 

@action('ctrl_act5413')
def ctrl_nm5413():
    return 'ret5413' 

@action('ctrl_act5414')
def ctrl_nm5414():
    return 'ret5414' 

@action('ctrl_act5415')
def ctrl_nm5415():
    return 'ret5415' 

@action('ctrl_act5416')
def ctrl_nm5416():
    return 'ret5416' 

@action('ctrl_act5417')
def ctrl_nm5417():
    return 'ret5417' 

@action('ctrl_act5418')
def ctrl_nm5418():
    return 'ret5418' 

@action('ctrl_act5419')
def ctrl_nm5419():
    return 'ret5419' 

@action('ctrl_act5420')
def ctrl_nm5420():
    return 'ret5420' 

@action('ctrl_act5421')
def ctrl_nm5421():
    return 'ret5421' 

@action('ctrl_act5422')
def ctrl_nm5422():
    return 'ret5422' 

@action('ctrl_act5423')
def ctrl_nm5423():
    return 'ret5423' 

@action('ctrl_act5424')
def ctrl_nm5424():
    return 'ret5424' 

@action('ctrl_act5425')
def ctrl_nm5425():
    return 'ret5425' 

@action('ctrl_act5426')
def ctrl_nm5426():
    return 'ret5426' 

@action('ctrl_act5427')
def ctrl_nm5427():
    return 'ret5427' 

@action('ctrl_act5428')
def ctrl_nm5428():
    return 'ret5428' 

@action('ctrl_act5429')
def ctrl_nm5429():
    return 'ret5429' 

@action('ctrl_act5430')
def ctrl_nm5430():
    return 'ret5430' 

@action('ctrl_act5431')
def ctrl_nm5431():
    return 'ret5431' 

@action('ctrl_act5432')
def ctrl_nm5432():
    return 'ret5432' 

@action('ctrl_act5433')
def ctrl_nm5433():
    return 'ret5433' 

@action('ctrl_act5434')
def ctrl_nm5434():
    return 'ret5434' 

@action('ctrl_act5435')
def ctrl_nm5435():
    return 'ret5435' 

@action('ctrl_act5436')
def ctrl_nm5436():
    return 'ret5436' 

@action('ctrl_act5437')
def ctrl_nm5437():
    return 'ret5437' 

@action('ctrl_act5438')
def ctrl_nm5438():
    return 'ret5438' 

@action('ctrl_act5439')
def ctrl_nm5439():
    return 'ret5439' 

@action('ctrl_act5440')
def ctrl_nm5440():
    return 'ret5440' 

@action('ctrl_act5441')
def ctrl_nm5441():
    return 'ret5441' 

@action('ctrl_act5442')
def ctrl_nm5442():
    return 'ret5442' 

@action('ctrl_act5443')
def ctrl_nm5443():
    return 'ret5443' 

@action('ctrl_act5444')
def ctrl_nm5444():
    return 'ret5444' 

@action('ctrl_act5445')
def ctrl_nm5445():
    return 'ret5445' 

@action('ctrl_act5446')
def ctrl_nm5446():
    return 'ret5446' 

@action('ctrl_act5447')
def ctrl_nm5447():
    return 'ret5447' 

@action('ctrl_act5448')
def ctrl_nm5448():
    return 'ret5448' 

@action('ctrl_act5449')
def ctrl_nm5449():
    return 'ret5449' 

@action('ctrl_act5450')
def ctrl_nm5450():
    return 'ret5450' 

@action('ctrl_act5451')
def ctrl_nm5451():
    return 'ret5451' 

@action('ctrl_act5452')
def ctrl_nm5452():
    return 'ret5452' 

@action('ctrl_act5453')
def ctrl_nm5453():
    return 'ret5453' 

@action('ctrl_act5454')
def ctrl_nm5454():
    return 'ret5454' 

@action('ctrl_act5455')
def ctrl_nm5455():
    return 'ret5455' 

@action('ctrl_act5456')
def ctrl_nm5456():
    return 'ret5456' 

@action('ctrl_act5457')
def ctrl_nm5457():
    return 'ret5457' 

@action('ctrl_act5458')
def ctrl_nm5458():
    return 'ret5458' 

@action('ctrl_act5459')
def ctrl_nm5459():
    return 'ret5459' 

@action('ctrl_act5460')
def ctrl_nm5460():
    return 'ret5460' 

@action('ctrl_act5461')
def ctrl_nm5461():
    return 'ret5461' 

@action('ctrl_act5462')
def ctrl_nm5462():
    return 'ret5462' 

@action('ctrl_act5463')
def ctrl_nm5463():
    return 'ret5463' 

@action('ctrl_act5464')
def ctrl_nm5464():
    return 'ret5464' 

@action('ctrl_act5465')
def ctrl_nm5465():
    return 'ret5465' 

@action('ctrl_act5466')
def ctrl_nm5466():
    return 'ret5466' 

@action('ctrl_act5467')
def ctrl_nm5467():
    return 'ret5467' 

@action('ctrl_act5468')
def ctrl_nm5468():
    return 'ret5468' 

@action('ctrl_act5469')
def ctrl_nm5469():
    return 'ret5469' 

@action('ctrl_act5470')
def ctrl_nm5470():
    return 'ret5470' 

@action('ctrl_act5471')
def ctrl_nm5471():
    return 'ret5471' 

@action('ctrl_act5472')
def ctrl_nm5472():
    return 'ret5472' 

@action('ctrl_act5473')
def ctrl_nm5473():
    return 'ret5473' 

@action('ctrl_act5474')
def ctrl_nm5474():
    return 'ret5474' 

@action('ctrl_act5475')
def ctrl_nm5475():
    return 'ret5475' 

@action('ctrl_act5476')
def ctrl_nm5476():
    return 'ret5476' 

@action('ctrl_act5477')
def ctrl_nm5477():
    return 'ret5477' 

@action('ctrl_act5478')
def ctrl_nm5478():
    return 'ret5478' 

@action('ctrl_act5479')
def ctrl_nm5479():
    return 'ret5479' 

@action('ctrl_act5480')
def ctrl_nm5480():
    return 'ret5480' 

@action('ctrl_act5481')
def ctrl_nm5481():
    return 'ret5481' 

@action('ctrl_act5482')
def ctrl_nm5482():
    return 'ret5482' 

@action('ctrl_act5483')
def ctrl_nm5483():
    return 'ret5483' 

@action('ctrl_act5484')
def ctrl_nm5484():
    return 'ret5484' 

@action('ctrl_act5485')
def ctrl_nm5485():
    return 'ret5485' 

@action('ctrl_act5486')
def ctrl_nm5486():
    return 'ret5486' 

@action('ctrl_act5487')
def ctrl_nm5487():
    return 'ret5487' 

@action('ctrl_act5488')
def ctrl_nm5488():
    return 'ret5488' 

@action('ctrl_act5489')
def ctrl_nm5489():
    return 'ret5489' 

@action('ctrl_act5490')
def ctrl_nm5490():
    return 'ret5490' 

@action('ctrl_act5491')
def ctrl_nm5491():
    return 'ret5491' 

@action('ctrl_act5492')
def ctrl_nm5492():
    return 'ret5492' 

@action('ctrl_act5493')
def ctrl_nm5493():
    return 'ret5493' 

@action('ctrl_act5494')
def ctrl_nm5494():
    return 'ret5494' 

@action('ctrl_act5495')
def ctrl_nm5495():
    return 'ret5495' 

@action('ctrl_act5496')
def ctrl_nm5496():
    return 'ret5496' 

@action('ctrl_act5497')
def ctrl_nm5497():
    return 'ret5497' 

@action('ctrl_act5498')
def ctrl_nm5498():
    return 'ret5498' 

@action('ctrl_act5499')
def ctrl_nm5499():
    return 'ret5499' 

@action('ctrl_act5500')
def ctrl_nm5500():
    return 'ret5500' 

@action('ctrl_act5501')
def ctrl_nm5501():
    return 'ret5501' 

@action('ctrl_act5502')
def ctrl_nm5502():
    return 'ret5502' 

@action('ctrl_act5503')
def ctrl_nm5503():
    return 'ret5503' 

@action('ctrl_act5504')
def ctrl_nm5504():
    return 'ret5504' 

@action('ctrl_act5505')
def ctrl_nm5505():
    return 'ret5505' 

@action('ctrl_act5506')
def ctrl_nm5506():
    return 'ret5506' 

@action('ctrl_act5507')
def ctrl_nm5507():
    return 'ret5507' 

@action('ctrl_act5508')
def ctrl_nm5508():
    return 'ret5508' 

@action('ctrl_act5509')
def ctrl_nm5509():
    return 'ret5509' 

@action('ctrl_act5510')
def ctrl_nm5510():
    return 'ret5510' 

@action('ctrl_act5511')
def ctrl_nm5511():
    return 'ret5511' 

@action('ctrl_act5512')
def ctrl_nm5512():
    return 'ret5512' 

@action('ctrl_act5513')
def ctrl_nm5513():
    return 'ret5513' 

@action('ctrl_act5514')
def ctrl_nm5514():
    return 'ret5514' 

@action('ctrl_act5515')
def ctrl_nm5515():
    return 'ret5515' 

@action('ctrl_act5516')
def ctrl_nm5516():
    return 'ret5516' 

@action('ctrl_act5517')
def ctrl_nm5517():
    return 'ret5517' 

@action('ctrl_act5518')
def ctrl_nm5518():
    return 'ret5518' 

@action('ctrl_act5519')
def ctrl_nm5519():
    return 'ret5519' 

@action('ctrl_act5520')
def ctrl_nm5520():
    return 'ret5520' 

@action('ctrl_act5521')
def ctrl_nm5521():
    return 'ret5521' 

@action('ctrl_act5522')
def ctrl_nm5522():
    return 'ret5522' 

@action('ctrl_act5523')
def ctrl_nm5523():
    return 'ret5523' 

@action('ctrl_act5524')
def ctrl_nm5524():
    return 'ret5524' 

@action('ctrl_act5525')
def ctrl_nm5525():
    return 'ret5525' 

@action('ctrl_act5526')
def ctrl_nm5526():
    return 'ret5526' 

@action('ctrl_act5527')
def ctrl_nm5527():
    return 'ret5527' 

@action('ctrl_act5528')
def ctrl_nm5528():
    return 'ret5528' 

@action('ctrl_act5529')
def ctrl_nm5529():
    return 'ret5529' 

@action('ctrl_act5530')
def ctrl_nm5530():
    return 'ret5530' 

@action('ctrl_act5531')
def ctrl_nm5531():
    return 'ret5531' 

@action('ctrl_act5532')
def ctrl_nm5532():
    return 'ret5532' 

@action('ctrl_act5533')
def ctrl_nm5533():
    return 'ret5533' 

@action('ctrl_act5534')
def ctrl_nm5534():
    return 'ret5534' 

@action('ctrl_act5535')
def ctrl_nm5535():
    return 'ret5535' 

@action('ctrl_act5536')
def ctrl_nm5536():
    return 'ret5536' 

@action('ctrl_act5537')
def ctrl_nm5537():
    return 'ret5537' 

@action('ctrl_act5538')
def ctrl_nm5538():
    return 'ret5538' 

@action('ctrl_act5539')
def ctrl_nm5539():
    return 'ret5539' 

@action('ctrl_act5540')
def ctrl_nm5540():
    return 'ret5540' 

@action('ctrl_act5541')
def ctrl_nm5541():
    return 'ret5541' 

@action('ctrl_act5542')
def ctrl_nm5542():
    return 'ret5542' 

@action('ctrl_act5543')
def ctrl_nm5543():
    return 'ret5543' 

@action('ctrl_act5544')
def ctrl_nm5544():
    return 'ret5544' 

@action('ctrl_act5545')
def ctrl_nm5545():
    return 'ret5545' 

@action('ctrl_act5546')
def ctrl_nm5546():
    return 'ret5546' 

@action('ctrl_act5547')
def ctrl_nm5547():
    return 'ret5547' 

@action('ctrl_act5548')
def ctrl_nm5548():
    return 'ret5548' 

@action('ctrl_act5549')
def ctrl_nm5549():
    return 'ret5549' 

@action('ctrl_act5550')
def ctrl_nm5550():
    return 'ret5550' 

@action('ctrl_act5551')
def ctrl_nm5551():
    return 'ret5551' 

@action('ctrl_act5552')
def ctrl_nm5552():
    return 'ret5552' 

@action('ctrl_act5553')
def ctrl_nm5553():
    return 'ret5553' 

@action('ctrl_act5554')
def ctrl_nm5554():
    return 'ret5554' 

@action('ctrl_act5555')
def ctrl_nm5555():
    return 'ret5555' 

@action('ctrl_act5556')
def ctrl_nm5556():
    return 'ret5556' 

@action('ctrl_act5557')
def ctrl_nm5557():
    return 'ret5557' 

@action('ctrl_act5558')
def ctrl_nm5558():
    return 'ret5558' 

@action('ctrl_act5559')
def ctrl_nm5559():
    return 'ret5559' 

@action('ctrl_act5560')
def ctrl_nm5560():
    return 'ret5560' 

@action('ctrl_act5561')
def ctrl_nm5561():
    return 'ret5561' 

@action('ctrl_act5562')
def ctrl_nm5562():
    return 'ret5562' 

@action('ctrl_act5563')
def ctrl_nm5563():
    return 'ret5563' 

@action('ctrl_act5564')
def ctrl_nm5564():
    return 'ret5564' 

@action('ctrl_act5565')
def ctrl_nm5565():
    return 'ret5565' 

@action('ctrl_act5566')
def ctrl_nm5566():
    return 'ret5566' 

@action('ctrl_act5567')
def ctrl_nm5567():
    return 'ret5567' 

@action('ctrl_act5568')
def ctrl_nm5568():
    return 'ret5568' 

@action('ctrl_act5569')
def ctrl_nm5569():
    return 'ret5569' 

@action('ctrl_act5570')
def ctrl_nm5570():
    return 'ret5570' 

@action('ctrl_act5571')
def ctrl_nm5571():
    return 'ret5571' 

@action('ctrl_act5572')
def ctrl_nm5572():
    return 'ret5572' 

@action('ctrl_act5573')
def ctrl_nm5573():
    return 'ret5573' 

@action('ctrl_act5574')
def ctrl_nm5574():
    return 'ret5574' 

@action('ctrl_act5575')
def ctrl_nm5575():
    return 'ret5575' 

@action('ctrl_act5576')
def ctrl_nm5576():
    return 'ret5576' 

@action('ctrl_act5577')
def ctrl_nm5577():
    return 'ret5577' 

@action('ctrl_act5578')
def ctrl_nm5578():
    return 'ret5578' 

@action('ctrl_act5579')
def ctrl_nm5579():
    return 'ret5579' 

@action('ctrl_act5580')
def ctrl_nm5580():
    return 'ret5580' 

@action('ctrl_act5581')
def ctrl_nm5581():
    return 'ret5581' 

@action('ctrl_act5582')
def ctrl_nm5582():
    return 'ret5582' 

@action('ctrl_act5583')
def ctrl_nm5583():
    return 'ret5583' 

@action('ctrl_act5584')
def ctrl_nm5584():
    return 'ret5584' 

@action('ctrl_act5585')
def ctrl_nm5585():
    return 'ret5585' 

@action('ctrl_act5586')
def ctrl_nm5586():
    return 'ret5586' 

@action('ctrl_act5587')
def ctrl_nm5587():
    return 'ret5587' 

@action('ctrl_act5588')
def ctrl_nm5588():
    return 'ret5588' 

@action('ctrl_act5589')
def ctrl_nm5589():
    return 'ret5589' 

@action('ctrl_act5590')
def ctrl_nm5590():
    return 'ret5590' 

@action('ctrl_act5591')
def ctrl_nm5591():
    return 'ret5591' 

@action('ctrl_act5592')
def ctrl_nm5592():
    return 'ret5592' 

@action('ctrl_act5593')
def ctrl_nm5593():
    return 'ret5593' 

@action('ctrl_act5594')
def ctrl_nm5594():
    return 'ret5594' 

@action('ctrl_act5595')
def ctrl_nm5595():
    return 'ret5595' 

@action('ctrl_act5596')
def ctrl_nm5596():
    return 'ret5596' 

@action('ctrl_act5597')
def ctrl_nm5597():
    return 'ret5597' 

@action('ctrl_act5598')
def ctrl_nm5598():
    return 'ret5598' 

@action('ctrl_act5599')
def ctrl_nm5599():
    return 'ret5599' 

@action('ctrl_act5600')
def ctrl_nm5600():
    return 'ret5600' 

@action('ctrl_act5601')
def ctrl_nm5601():
    return 'ret5601' 

@action('ctrl_act5602')
def ctrl_nm5602():
    return 'ret5602' 

@action('ctrl_act5603')
def ctrl_nm5603():
    return 'ret5603' 

@action('ctrl_act5604')
def ctrl_nm5604():
    return 'ret5604' 

@action('ctrl_act5605')
def ctrl_nm5605():
    return 'ret5605' 

@action('ctrl_act5606')
def ctrl_nm5606():
    return 'ret5606' 

@action('ctrl_act5607')
def ctrl_nm5607():
    return 'ret5607' 

@action('ctrl_act5608')
def ctrl_nm5608():
    return 'ret5608' 

@action('ctrl_act5609')
def ctrl_nm5609():
    return 'ret5609' 

@action('ctrl_act5610')
def ctrl_nm5610():
    return 'ret5610' 

@action('ctrl_act5611')
def ctrl_nm5611():
    return 'ret5611' 

@action('ctrl_act5612')
def ctrl_nm5612():
    return 'ret5612' 

@action('ctrl_act5613')
def ctrl_nm5613():
    return 'ret5613' 

@action('ctrl_act5614')
def ctrl_nm5614():
    return 'ret5614' 

@action('ctrl_act5615')
def ctrl_nm5615():
    return 'ret5615' 

@action('ctrl_act5616')
def ctrl_nm5616():
    return 'ret5616' 

@action('ctrl_act5617')
def ctrl_nm5617():
    return 'ret5617' 

@action('ctrl_act5618')
def ctrl_nm5618():
    return 'ret5618' 

@action('ctrl_act5619')
def ctrl_nm5619():
    return 'ret5619' 

@action('ctrl_act5620')
def ctrl_nm5620():
    return 'ret5620' 

@action('ctrl_act5621')
def ctrl_nm5621():
    return 'ret5621' 

@action('ctrl_act5622')
def ctrl_nm5622():
    return 'ret5622' 

@action('ctrl_act5623')
def ctrl_nm5623():
    return 'ret5623' 

@action('ctrl_act5624')
def ctrl_nm5624():
    return 'ret5624' 

@action('ctrl_act5625')
def ctrl_nm5625():
    return 'ret5625' 

@action('ctrl_act5626')
def ctrl_nm5626():
    return 'ret5626' 

@action('ctrl_act5627')
def ctrl_nm5627():
    return 'ret5627' 

@action('ctrl_act5628')
def ctrl_nm5628():
    return 'ret5628' 

@action('ctrl_act5629')
def ctrl_nm5629():
    return 'ret5629' 

@action('ctrl_act5630')
def ctrl_nm5630():
    return 'ret5630' 

@action('ctrl_act5631')
def ctrl_nm5631():
    return 'ret5631' 

@action('ctrl_act5632')
def ctrl_nm5632():
    return 'ret5632' 

@action('ctrl_act5633')
def ctrl_nm5633():
    return 'ret5633' 

@action('ctrl_act5634')
def ctrl_nm5634():
    return 'ret5634' 

@action('ctrl_act5635')
def ctrl_nm5635():
    return 'ret5635' 

@action('ctrl_act5636')
def ctrl_nm5636():
    return 'ret5636' 

@action('ctrl_act5637')
def ctrl_nm5637():
    return 'ret5637' 

@action('ctrl_act5638')
def ctrl_nm5638():
    return 'ret5638' 

@action('ctrl_act5639')
def ctrl_nm5639():
    return 'ret5639' 

@action('ctrl_act5640')
def ctrl_nm5640():
    return 'ret5640' 

@action('ctrl_act5641')
def ctrl_nm5641():
    return 'ret5641' 

@action('ctrl_act5642')
def ctrl_nm5642():
    return 'ret5642' 

@action('ctrl_act5643')
def ctrl_nm5643():
    return 'ret5643' 

@action('ctrl_act5644')
def ctrl_nm5644():
    return 'ret5644' 

@action('ctrl_act5645')
def ctrl_nm5645():
    return 'ret5645' 

@action('ctrl_act5646')
def ctrl_nm5646():
    return 'ret5646' 

@action('ctrl_act5647')
def ctrl_nm5647():
    return 'ret5647' 

@action('ctrl_act5648')
def ctrl_nm5648():
    return 'ret5648' 

@action('ctrl_act5649')
def ctrl_nm5649():
    return 'ret5649' 

@action('ctrl_act5650')
def ctrl_nm5650():
    return 'ret5650' 

@action('ctrl_act5651')
def ctrl_nm5651():
    return 'ret5651' 

@action('ctrl_act5652')
def ctrl_nm5652():
    return 'ret5652' 

@action('ctrl_act5653')
def ctrl_nm5653():
    return 'ret5653' 

@action('ctrl_act5654')
def ctrl_nm5654():
    return 'ret5654' 

@action('ctrl_act5655')
def ctrl_nm5655():
    return 'ret5655' 

@action('ctrl_act5656')
def ctrl_nm5656():
    return 'ret5656' 

@action('ctrl_act5657')
def ctrl_nm5657():
    return 'ret5657' 

@action('ctrl_act5658')
def ctrl_nm5658():
    return 'ret5658' 

@action('ctrl_act5659')
def ctrl_nm5659():
    return 'ret5659' 

@action('ctrl_act5660')
def ctrl_nm5660():
    return 'ret5660' 

@action('ctrl_act5661')
def ctrl_nm5661():
    return 'ret5661' 

@action('ctrl_act5662')
def ctrl_nm5662():
    return 'ret5662' 

@action('ctrl_act5663')
def ctrl_nm5663():
    return 'ret5663' 

@action('ctrl_act5664')
def ctrl_nm5664():
    return 'ret5664' 

@action('ctrl_act5665')
def ctrl_nm5665():
    return 'ret5665' 

@action('ctrl_act5666')
def ctrl_nm5666():
    return 'ret5666' 

@action('ctrl_act5667')
def ctrl_nm5667():
    return 'ret5667' 

@action('ctrl_act5668')
def ctrl_nm5668():
    return 'ret5668' 

@action('ctrl_act5669')
def ctrl_nm5669():
    return 'ret5669' 

@action('ctrl_act5670')
def ctrl_nm5670():
    return 'ret5670' 

@action('ctrl_act5671')
def ctrl_nm5671():
    return 'ret5671' 

@action('ctrl_act5672')
def ctrl_nm5672():
    return 'ret5672' 

@action('ctrl_act5673')
def ctrl_nm5673():
    return 'ret5673' 

@action('ctrl_act5674')
def ctrl_nm5674():
    return 'ret5674' 

@action('ctrl_act5675')
def ctrl_nm5675():
    return 'ret5675' 

@action('ctrl_act5676')
def ctrl_nm5676():
    return 'ret5676' 

@action('ctrl_act5677')
def ctrl_nm5677():
    return 'ret5677' 

@action('ctrl_act5678')
def ctrl_nm5678():
    return 'ret5678' 

@action('ctrl_act5679')
def ctrl_nm5679():
    return 'ret5679' 

@action('ctrl_act5680')
def ctrl_nm5680():
    return 'ret5680' 

@action('ctrl_act5681')
def ctrl_nm5681():
    return 'ret5681' 

@action('ctrl_act5682')
def ctrl_nm5682():
    return 'ret5682' 

@action('ctrl_act5683')
def ctrl_nm5683():
    return 'ret5683' 

@action('ctrl_act5684')
def ctrl_nm5684():
    return 'ret5684' 

@action('ctrl_act5685')
def ctrl_nm5685():
    return 'ret5685' 

@action('ctrl_act5686')
def ctrl_nm5686():
    return 'ret5686' 

@action('ctrl_act5687')
def ctrl_nm5687():
    return 'ret5687' 

@action('ctrl_act5688')
def ctrl_nm5688():
    return 'ret5688' 

@action('ctrl_act5689')
def ctrl_nm5689():
    return 'ret5689' 

@action('ctrl_act5690')
def ctrl_nm5690():
    return 'ret5690' 

@action('ctrl_act5691')
def ctrl_nm5691():
    return 'ret5691' 

@action('ctrl_act5692')
def ctrl_nm5692():
    return 'ret5692' 

@action('ctrl_act5693')
def ctrl_nm5693():
    return 'ret5693' 

@action('ctrl_act5694')
def ctrl_nm5694():
    return 'ret5694' 

@action('ctrl_act5695')
def ctrl_nm5695():
    return 'ret5695' 

@action('ctrl_act5696')
def ctrl_nm5696():
    return 'ret5696' 

@action('ctrl_act5697')
def ctrl_nm5697():
    return 'ret5697' 

@action('ctrl_act5698')
def ctrl_nm5698():
    return 'ret5698' 

@action('ctrl_act5699')
def ctrl_nm5699():
    return 'ret5699' 

@action('ctrl_act5700')
def ctrl_nm5700():
    return 'ret5700' 

@action('ctrl_act5701')
def ctrl_nm5701():
    return 'ret5701' 

@action('ctrl_act5702')
def ctrl_nm5702():
    return 'ret5702' 

@action('ctrl_act5703')
def ctrl_nm5703():
    return 'ret5703' 

@action('ctrl_act5704')
def ctrl_nm5704():
    return 'ret5704' 

@action('ctrl_act5705')
def ctrl_nm5705():
    return 'ret5705' 

@action('ctrl_act5706')
def ctrl_nm5706():
    return 'ret5706' 

@action('ctrl_act5707')
def ctrl_nm5707():
    return 'ret5707' 

@action('ctrl_act5708')
def ctrl_nm5708():
    return 'ret5708' 

@action('ctrl_act5709')
def ctrl_nm5709():
    return 'ret5709' 

@action('ctrl_act5710')
def ctrl_nm5710():
    return 'ret5710' 

@action('ctrl_act5711')
def ctrl_nm5711():
    return 'ret5711' 

@action('ctrl_act5712')
def ctrl_nm5712():
    return 'ret5712' 

@action('ctrl_act5713')
def ctrl_nm5713():
    return 'ret5713' 

@action('ctrl_act5714')
def ctrl_nm5714():
    return 'ret5714' 

@action('ctrl_act5715')
def ctrl_nm5715():
    return 'ret5715' 

@action('ctrl_act5716')
def ctrl_nm5716():
    return 'ret5716' 

@action('ctrl_act5717')
def ctrl_nm5717():
    return 'ret5717' 

@action('ctrl_act5718')
def ctrl_nm5718():
    return 'ret5718' 

@action('ctrl_act5719')
def ctrl_nm5719():
    return 'ret5719' 

@action('ctrl_act5720')
def ctrl_nm5720():
    return 'ret5720' 

@action('ctrl_act5721')
def ctrl_nm5721():
    return 'ret5721' 

@action('ctrl_act5722')
def ctrl_nm5722():
    return 'ret5722' 

@action('ctrl_act5723')
def ctrl_nm5723():
    return 'ret5723' 

@action('ctrl_act5724')
def ctrl_nm5724():
    return 'ret5724' 

@action('ctrl_act5725')
def ctrl_nm5725():
    return 'ret5725' 

@action('ctrl_act5726')
def ctrl_nm5726():
    return 'ret5726' 

@action('ctrl_act5727')
def ctrl_nm5727():
    return 'ret5727' 

@action('ctrl_act5728')
def ctrl_nm5728():
    return 'ret5728' 

@action('ctrl_act5729')
def ctrl_nm5729():
    return 'ret5729' 

@action('ctrl_act5730')
def ctrl_nm5730():
    return 'ret5730' 

@action('ctrl_act5731')
def ctrl_nm5731():
    return 'ret5731' 

@action('ctrl_act5732')
def ctrl_nm5732():
    return 'ret5732' 

@action('ctrl_act5733')
def ctrl_nm5733():
    return 'ret5733' 

@action('ctrl_act5734')
def ctrl_nm5734():
    return 'ret5734' 

@action('ctrl_act5735')
def ctrl_nm5735():
    return 'ret5735' 

@action('ctrl_act5736')
def ctrl_nm5736():
    return 'ret5736' 

@action('ctrl_act5737')
def ctrl_nm5737():
    return 'ret5737' 

@action('ctrl_act5738')
def ctrl_nm5738():
    return 'ret5738' 

@action('ctrl_act5739')
def ctrl_nm5739():
    return 'ret5739' 

@action('ctrl_act5740')
def ctrl_nm5740():
    return 'ret5740' 

@action('ctrl_act5741')
def ctrl_nm5741():
    return 'ret5741' 

@action('ctrl_act5742')
def ctrl_nm5742():
    return 'ret5742' 

@action('ctrl_act5743')
def ctrl_nm5743():
    return 'ret5743' 

@action('ctrl_act5744')
def ctrl_nm5744():
    return 'ret5744' 

@action('ctrl_act5745')
def ctrl_nm5745():
    return 'ret5745' 

@action('ctrl_act5746')
def ctrl_nm5746():
    return 'ret5746' 

@action('ctrl_act5747')
def ctrl_nm5747():
    return 'ret5747' 

@action('ctrl_act5748')
def ctrl_nm5748():
    return 'ret5748' 

@action('ctrl_act5749')
def ctrl_nm5749():
    return 'ret5749' 

@action('ctrl_act5750')
def ctrl_nm5750():
    return 'ret5750' 

@action('ctrl_act5751')
def ctrl_nm5751():
    return 'ret5751' 

@action('ctrl_act5752')
def ctrl_nm5752():
    return 'ret5752' 

@action('ctrl_act5753')
def ctrl_nm5753():
    return 'ret5753' 

@action('ctrl_act5754')
def ctrl_nm5754():
    return 'ret5754' 

@action('ctrl_act5755')
def ctrl_nm5755():
    return 'ret5755' 

@action('ctrl_act5756')
def ctrl_nm5756():
    return 'ret5756' 

@action('ctrl_act5757')
def ctrl_nm5757():
    return 'ret5757' 

@action('ctrl_act5758')
def ctrl_nm5758():
    return 'ret5758' 

@action('ctrl_act5759')
def ctrl_nm5759():
    return 'ret5759' 

@action('ctrl_act5760')
def ctrl_nm5760():
    return 'ret5760' 

@action('ctrl_act5761')
def ctrl_nm5761():
    return 'ret5761' 

@action('ctrl_act5762')
def ctrl_nm5762():
    return 'ret5762' 

@action('ctrl_act5763')
def ctrl_nm5763():
    return 'ret5763' 

@action('ctrl_act5764')
def ctrl_nm5764():
    return 'ret5764' 

@action('ctrl_act5765')
def ctrl_nm5765():
    return 'ret5765' 

@action('ctrl_act5766')
def ctrl_nm5766():
    return 'ret5766' 

@action('ctrl_act5767')
def ctrl_nm5767():
    return 'ret5767' 

@action('ctrl_act5768')
def ctrl_nm5768():
    return 'ret5768' 

@action('ctrl_act5769')
def ctrl_nm5769():
    return 'ret5769' 

@action('ctrl_act5770')
def ctrl_nm5770():
    return 'ret5770' 

@action('ctrl_act5771')
def ctrl_nm5771():
    return 'ret5771' 

@action('ctrl_act5772')
def ctrl_nm5772():
    return 'ret5772' 

@action('ctrl_act5773')
def ctrl_nm5773():
    return 'ret5773' 

@action('ctrl_act5774')
def ctrl_nm5774():
    return 'ret5774' 

@action('ctrl_act5775')
def ctrl_nm5775():
    return 'ret5775' 

@action('ctrl_act5776')
def ctrl_nm5776():
    return 'ret5776' 

@action('ctrl_act5777')
def ctrl_nm5777():
    return 'ret5777' 

@action('ctrl_act5778')
def ctrl_nm5778():
    return 'ret5778' 

@action('ctrl_act5779')
def ctrl_nm5779():
    return 'ret5779' 

@action('ctrl_act5780')
def ctrl_nm5780():
    return 'ret5780' 

@action('ctrl_act5781')
def ctrl_nm5781():
    return 'ret5781' 

@action('ctrl_act5782')
def ctrl_nm5782():
    return 'ret5782' 

@action('ctrl_act5783')
def ctrl_nm5783():
    return 'ret5783' 

@action('ctrl_act5784')
def ctrl_nm5784():
    return 'ret5784' 

@action('ctrl_act5785')
def ctrl_nm5785():
    return 'ret5785' 

@action('ctrl_act5786')
def ctrl_nm5786():
    return 'ret5786' 

@action('ctrl_act5787')
def ctrl_nm5787():
    return 'ret5787' 

@action('ctrl_act5788')
def ctrl_nm5788():
    return 'ret5788' 

@action('ctrl_act5789')
def ctrl_nm5789():
    return 'ret5789' 

@action('ctrl_act5790')
def ctrl_nm5790():
    return 'ret5790' 

@action('ctrl_act5791')
def ctrl_nm5791():
    return 'ret5791' 

@action('ctrl_act5792')
def ctrl_nm5792():
    return 'ret5792' 

@action('ctrl_act5793')
def ctrl_nm5793():
    return 'ret5793' 

@action('ctrl_act5794')
def ctrl_nm5794():
    return 'ret5794' 

@action('ctrl_act5795')
def ctrl_nm5795():
    return 'ret5795' 

@action('ctrl_act5796')
def ctrl_nm5796():
    return 'ret5796' 

@action('ctrl_act5797')
def ctrl_nm5797():
    return 'ret5797' 

@action('ctrl_act5798')
def ctrl_nm5798():
    return 'ret5798' 

@action('ctrl_act5799')
def ctrl_nm5799():
    return 'ret5799' 

@action('ctrl_act5800')
def ctrl_nm5800():
    return 'ret5800' 

@action('ctrl_act5801')
def ctrl_nm5801():
    return 'ret5801' 

@action('ctrl_act5802')
def ctrl_nm5802():
    return 'ret5802' 

@action('ctrl_act5803')
def ctrl_nm5803():
    return 'ret5803' 

@action('ctrl_act5804')
def ctrl_nm5804():
    return 'ret5804' 

@action('ctrl_act5805')
def ctrl_nm5805():
    return 'ret5805' 

@action('ctrl_act5806')
def ctrl_nm5806():
    return 'ret5806' 

@action('ctrl_act5807')
def ctrl_nm5807():
    return 'ret5807' 

@action('ctrl_act5808')
def ctrl_nm5808():
    return 'ret5808' 

@action('ctrl_act5809')
def ctrl_nm5809():
    return 'ret5809' 

@action('ctrl_act5810')
def ctrl_nm5810():
    return 'ret5810' 

@action('ctrl_act5811')
def ctrl_nm5811():
    return 'ret5811' 

@action('ctrl_act5812')
def ctrl_nm5812():
    return 'ret5812' 

@action('ctrl_act5813')
def ctrl_nm5813():
    return 'ret5813' 

@action('ctrl_act5814')
def ctrl_nm5814():
    return 'ret5814' 

@action('ctrl_act5815')
def ctrl_nm5815():
    return 'ret5815' 

@action('ctrl_act5816')
def ctrl_nm5816():
    return 'ret5816' 

@action('ctrl_act5817')
def ctrl_nm5817():
    return 'ret5817' 

@action('ctrl_act5818')
def ctrl_nm5818():
    return 'ret5818' 

@action('ctrl_act5819')
def ctrl_nm5819():
    return 'ret5819' 

@action('ctrl_act5820')
def ctrl_nm5820():
    return 'ret5820' 

@action('ctrl_act5821')
def ctrl_nm5821():
    return 'ret5821' 

@action('ctrl_act5822')
def ctrl_nm5822():
    return 'ret5822' 

@action('ctrl_act5823')
def ctrl_nm5823():
    return 'ret5823' 

@action('ctrl_act5824')
def ctrl_nm5824():
    return 'ret5824' 

@action('ctrl_act5825')
def ctrl_nm5825():
    return 'ret5825' 

@action('ctrl_act5826')
def ctrl_nm5826():
    return 'ret5826' 

@action('ctrl_act5827')
def ctrl_nm5827():
    return 'ret5827' 

@action('ctrl_act5828')
def ctrl_nm5828():
    return 'ret5828' 

@action('ctrl_act5829')
def ctrl_nm5829():
    return 'ret5829' 

@action('ctrl_act5830')
def ctrl_nm5830():
    return 'ret5830' 

@action('ctrl_act5831')
def ctrl_nm5831():
    return 'ret5831' 

@action('ctrl_act5832')
def ctrl_nm5832():
    return 'ret5832' 

@action('ctrl_act5833')
def ctrl_nm5833():
    return 'ret5833' 

@action('ctrl_act5834')
def ctrl_nm5834():
    return 'ret5834' 

@action('ctrl_act5835')
def ctrl_nm5835():
    return 'ret5835' 

@action('ctrl_act5836')
def ctrl_nm5836():
    return 'ret5836' 

@action('ctrl_act5837')
def ctrl_nm5837():
    return 'ret5837' 

@action('ctrl_act5838')
def ctrl_nm5838():
    return 'ret5838' 

@action('ctrl_act5839')
def ctrl_nm5839():
    return 'ret5839' 

@action('ctrl_act5840')
def ctrl_nm5840():
    return 'ret5840' 

@action('ctrl_act5841')
def ctrl_nm5841():
    return 'ret5841' 

@action('ctrl_act5842')
def ctrl_nm5842():
    return 'ret5842' 

@action('ctrl_act5843')
def ctrl_nm5843():
    return 'ret5843' 

@action('ctrl_act5844')
def ctrl_nm5844():
    return 'ret5844' 

@action('ctrl_act5845')
def ctrl_nm5845():
    return 'ret5845' 

@action('ctrl_act5846')
def ctrl_nm5846():
    return 'ret5846' 

@action('ctrl_act5847')
def ctrl_nm5847():
    return 'ret5847' 

@action('ctrl_act5848')
def ctrl_nm5848():
    return 'ret5848' 

@action('ctrl_act5849')
def ctrl_nm5849():
    return 'ret5849' 

@action('ctrl_act5850')
def ctrl_nm5850():
    return 'ret5850' 

@action('ctrl_act5851')
def ctrl_nm5851():
    return 'ret5851' 

@action('ctrl_act5852')
def ctrl_nm5852():
    return 'ret5852' 

@action('ctrl_act5853')
def ctrl_nm5853():
    return 'ret5853' 

@action('ctrl_act5854')
def ctrl_nm5854():
    return 'ret5854' 

@action('ctrl_act5855')
def ctrl_nm5855():
    return 'ret5855' 

@action('ctrl_act5856')
def ctrl_nm5856():
    return 'ret5856' 

@action('ctrl_act5857')
def ctrl_nm5857():
    return 'ret5857' 

@action('ctrl_act5858')
def ctrl_nm5858():
    return 'ret5858' 

@action('ctrl_act5859')
def ctrl_nm5859():
    return 'ret5859' 

@action('ctrl_act5860')
def ctrl_nm5860():
    return 'ret5860' 

@action('ctrl_act5861')
def ctrl_nm5861():
    return 'ret5861' 

@action('ctrl_act5862')
def ctrl_nm5862():
    return 'ret5862' 

@action('ctrl_act5863')
def ctrl_nm5863():
    return 'ret5863' 

@action('ctrl_act5864')
def ctrl_nm5864():
    return 'ret5864' 

@action('ctrl_act5865')
def ctrl_nm5865():
    return 'ret5865' 

@action('ctrl_act5866')
def ctrl_nm5866():
    return 'ret5866' 

@action('ctrl_act5867')
def ctrl_nm5867():
    return 'ret5867' 

@action('ctrl_act5868')
def ctrl_nm5868():
    return 'ret5868' 

@action('ctrl_act5869')
def ctrl_nm5869():
    return 'ret5869' 

@action('ctrl_act5870')
def ctrl_nm5870():
    return 'ret5870' 

@action('ctrl_act5871')
def ctrl_nm5871():
    return 'ret5871' 

@action('ctrl_act5872')
def ctrl_nm5872():
    return 'ret5872' 

@action('ctrl_act5873')
def ctrl_nm5873():
    return 'ret5873' 

@action('ctrl_act5874')
def ctrl_nm5874():
    return 'ret5874' 

@action('ctrl_act5875')
def ctrl_nm5875():
    return 'ret5875' 

@action('ctrl_act5876')
def ctrl_nm5876():
    return 'ret5876' 

@action('ctrl_act5877')
def ctrl_nm5877():
    return 'ret5877' 

@action('ctrl_act5878')
def ctrl_nm5878():
    return 'ret5878' 

@action('ctrl_act5879')
def ctrl_nm5879():
    return 'ret5879' 

@action('ctrl_act5880')
def ctrl_nm5880():
    return 'ret5880' 

@action('ctrl_act5881')
def ctrl_nm5881():
    return 'ret5881' 

@action('ctrl_act5882')
def ctrl_nm5882():
    return 'ret5882' 

@action('ctrl_act5883')
def ctrl_nm5883():
    return 'ret5883' 

@action('ctrl_act5884')
def ctrl_nm5884():
    return 'ret5884' 

@action('ctrl_act5885')
def ctrl_nm5885():
    return 'ret5885' 

@action('ctrl_act5886')
def ctrl_nm5886():
    return 'ret5886' 

@action('ctrl_act5887')
def ctrl_nm5887():
    return 'ret5887' 

@action('ctrl_act5888')
def ctrl_nm5888():
    return 'ret5888' 

@action('ctrl_act5889')
def ctrl_nm5889():
    return 'ret5889' 

@action('ctrl_act5890')
def ctrl_nm5890():
    return 'ret5890' 

@action('ctrl_act5891')
def ctrl_nm5891():
    return 'ret5891' 

@action('ctrl_act5892')
def ctrl_nm5892():
    return 'ret5892' 

@action('ctrl_act5893')
def ctrl_nm5893():
    return 'ret5893' 

@action('ctrl_act5894')
def ctrl_nm5894():
    return 'ret5894' 

@action('ctrl_act5895')
def ctrl_nm5895():
    return 'ret5895' 

@action('ctrl_act5896')
def ctrl_nm5896():
    return 'ret5896' 

@action('ctrl_act5897')
def ctrl_nm5897():
    return 'ret5897' 

@action('ctrl_act5898')
def ctrl_nm5898():
    return 'ret5898' 

@action('ctrl_act5899')
def ctrl_nm5899():
    return 'ret5899' 

@action('ctrl_act5900')
def ctrl_nm5900():
    return 'ret5900' 

@action('ctrl_act5901')
def ctrl_nm5901():
    return 'ret5901' 

@action('ctrl_act5902')
def ctrl_nm5902():
    return 'ret5902' 

@action('ctrl_act5903')
def ctrl_nm5903():
    return 'ret5903' 

@action('ctrl_act5904')
def ctrl_nm5904():
    return 'ret5904' 

@action('ctrl_act5905')
def ctrl_nm5905():
    return 'ret5905' 

@action('ctrl_act5906')
def ctrl_nm5906():
    return 'ret5906' 

@action('ctrl_act5907')
def ctrl_nm5907():
    return 'ret5907' 

@action('ctrl_act5908')
def ctrl_nm5908():
    return 'ret5908' 

@action('ctrl_act5909')
def ctrl_nm5909():
    return 'ret5909' 

@action('ctrl_act5910')
def ctrl_nm5910():
    return 'ret5910' 

@action('ctrl_act5911')
def ctrl_nm5911():
    return 'ret5911' 

@action('ctrl_act5912')
def ctrl_nm5912():
    return 'ret5912' 

@action('ctrl_act5913')
def ctrl_nm5913():
    return 'ret5913' 

@action('ctrl_act5914')
def ctrl_nm5914():
    return 'ret5914' 

@action('ctrl_act5915')
def ctrl_nm5915():
    return 'ret5915' 

@action('ctrl_act5916')
def ctrl_nm5916():
    return 'ret5916' 

@action('ctrl_act5917')
def ctrl_nm5917():
    return 'ret5917' 

@action('ctrl_act5918')
def ctrl_nm5918():
    return 'ret5918' 

@action('ctrl_act5919')
def ctrl_nm5919():
    return 'ret5919' 

@action('ctrl_act5920')
def ctrl_nm5920():
    return 'ret5920' 

@action('ctrl_act5921')
def ctrl_nm5921():
    return 'ret5921' 

@action('ctrl_act5922')
def ctrl_nm5922():
    return 'ret5922' 

@action('ctrl_act5923')
def ctrl_nm5923():
    return 'ret5923' 

@action('ctrl_act5924')
def ctrl_nm5924():
    return 'ret5924' 

@action('ctrl_act5925')
def ctrl_nm5925():
    return 'ret5925' 

@action('ctrl_act5926')
def ctrl_nm5926():
    return 'ret5926' 

@action('ctrl_act5927')
def ctrl_nm5927():
    return 'ret5927' 

@action('ctrl_act5928')
def ctrl_nm5928():
    return 'ret5928' 

@action('ctrl_act5929')
def ctrl_nm5929():
    return 'ret5929' 

@action('ctrl_act5930')
def ctrl_nm5930():
    return 'ret5930' 

@action('ctrl_act5931')
def ctrl_nm5931():
    return 'ret5931' 

@action('ctrl_act5932')
def ctrl_nm5932():
    return 'ret5932' 

@action('ctrl_act5933')
def ctrl_nm5933():
    return 'ret5933' 

@action('ctrl_act5934')
def ctrl_nm5934():
    return 'ret5934' 

@action('ctrl_act5935')
def ctrl_nm5935():
    return 'ret5935' 

@action('ctrl_act5936')
def ctrl_nm5936():
    return 'ret5936' 

@action('ctrl_act5937')
def ctrl_nm5937():
    return 'ret5937' 

@action('ctrl_act5938')
def ctrl_nm5938():
    return 'ret5938' 

@action('ctrl_act5939')
def ctrl_nm5939():
    return 'ret5939' 

@action('ctrl_act5940')
def ctrl_nm5940():
    return 'ret5940' 

@action('ctrl_act5941')
def ctrl_nm5941():
    return 'ret5941' 

@action('ctrl_act5942')
def ctrl_nm5942():
    return 'ret5942' 

@action('ctrl_act5943')
def ctrl_nm5943():
    return 'ret5943' 

@action('ctrl_act5944')
def ctrl_nm5944():
    return 'ret5944' 

@action('ctrl_act5945')
def ctrl_nm5945():
    return 'ret5945' 

@action('ctrl_act5946')
def ctrl_nm5946():
    return 'ret5946' 

@action('ctrl_act5947')
def ctrl_nm5947():
    return 'ret5947' 

@action('ctrl_act5948')
def ctrl_nm5948():
    return 'ret5948' 

@action('ctrl_act5949')
def ctrl_nm5949():
    return 'ret5949' 

@action('ctrl_act5950')
def ctrl_nm5950():
    return 'ret5950' 

@action('ctrl_act5951')
def ctrl_nm5951():
    return 'ret5951' 

@action('ctrl_act5952')
def ctrl_nm5952():
    return 'ret5952' 

@action('ctrl_act5953')
def ctrl_nm5953():
    return 'ret5953' 

@action('ctrl_act5954')
def ctrl_nm5954():
    return 'ret5954' 

@action('ctrl_act5955')
def ctrl_nm5955():
    return 'ret5955' 

@action('ctrl_act5956')
def ctrl_nm5956():
    return 'ret5956' 

@action('ctrl_act5957')
def ctrl_nm5957():
    return 'ret5957' 

@action('ctrl_act5958')
def ctrl_nm5958():
    return 'ret5958' 

@action('ctrl_act5959')
def ctrl_nm5959():
    return 'ret5959' 

@action('ctrl_act5960')
def ctrl_nm5960():
    return 'ret5960' 

@action('ctrl_act5961')
def ctrl_nm5961():
    return 'ret5961' 

@action('ctrl_act5962')
def ctrl_nm5962():
    return 'ret5962' 

@action('ctrl_act5963')
def ctrl_nm5963():
    return 'ret5963' 

@action('ctrl_act5964')
def ctrl_nm5964():
    return 'ret5964' 

@action('ctrl_act5965')
def ctrl_nm5965():
    return 'ret5965' 

@action('ctrl_act5966')
def ctrl_nm5966():
    return 'ret5966' 

@action('ctrl_act5967')
def ctrl_nm5967():
    return 'ret5967' 

@action('ctrl_act5968')
def ctrl_nm5968():
    return 'ret5968' 

@action('ctrl_act5969')
def ctrl_nm5969():
    return 'ret5969' 

@action('ctrl_act5970')
def ctrl_nm5970():
    return 'ret5970' 

@action('ctrl_act5971')
def ctrl_nm5971():
    return 'ret5971' 

@action('ctrl_act5972')
def ctrl_nm5972():
    return 'ret5972' 

@action('ctrl_act5973')
def ctrl_nm5973():
    return 'ret5973' 

@action('ctrl_act5974')
def ctrl_nm5974():
    return 'ret5974' 

@action('ctrl_act5975')
def ctrl_nm5975():
    return 'ret5975' 

@action('ctrl_act5976')
def ctrl_nm5976():
    return 'ret5976' 

@action('ctrl_act5977')
def ctrl_nm5977():
    return 'ret5977' 

@action('ctrl_act5978')
def ctrl_nm5978():
    return 'ret5978' 

@action('ctrl_act5979')
def ctrl_nm5979():
    return 'ret5979' 

@action('ctrl_act5980')
def ctrl_nm5980():
    return 'ret5980' 

@action('ctrl_act5981')
def ctrl_nm5981():
    return 'ret5981' 

@action('ctrl_act5982')
def ctrl_nm5982():
    return 'ret5982' 

@action('ctrl_act5983')
def ctrl_nm5983():
    return 'ret5983' 

@action('ctrl_act5984')
def ctrl_nm5984():
    return 'ret5984' 

@action('ctrl_act5985')
def ctrl_nm5985():
    return 'ret5985' 

@action('ctrl_act5986')
def ctrl_nm5986():
    return 'ret5986' 

@action('ctrl_act5987')
def ctrl_nm5987():
    return 'ret5987' 

@action('ctrl_act5988')
def ctrl_nm5988():
    return 'ret5988' 

@action('ctrl_act5989')
def ctrl_nm5989():
    return 'ret5989' 

@action('ctrl_act5990')
def ctrl_nm5990():
    return 'ret5990' 

@action('ctrl_act5991')
def ctrl_nm5991():
    return 'ret5991' 

@action('ctrl_act5992')
def ctrl_nm5992():
    return 'ret5992' 

@action('ctrl_act5993')
def ctrl_nm5993():
    return 'ret5993' 

@action('ctrl_act5994')
def ctrl_nm5994():
    return 'ret5994' 

@action('ctrl_act5995')
def ctrl_nm5995():
    return 'ret5995' 

@action('ctrl_act5996')
def ctrl_nm5996():
    return 'ret5996' 

@action('ctrl_act5997')
def ctrl_nm5997():
    return 'ret5997' 

@action('ctrl_act5998')
def ctrl_nm5998():
    return 'ret5998' 

@action('ctrl_act5999')
def ctrl_nm5999():
    return 'ret5999' 

@action('ctrl_act6000')
def ctrl_nm6000():
    return 'ret6000' 

@action('ctrl_act6001')
def ctrl_nm6001():
    return 'ret6001' 

@action('ctrl_act6002')
def ctrl_nm6002():
    return 'ret6002' 

@action('ctrl_act6003')
def ctrl_nm6003():
    return 'ret6003' 

@action('ctrl_act6004')
def ctrl_nm6004():
    return 'ret6004' 

@action('ctrl_act6005')
def ctrl_nm6005():
    return 'ret6005' 

@action('ctrl_act6006')
def ctrl_nm6006():
    return 'ret6006' 

@action('ctrl_act6007')
def ctrl_nm6007():
    return 'ret6007' 

@action('ctrl_act6008')
def ctrl_nm6008():
    return 'ret6008' 

@action('ctrl_act6009')
def ctrl_nm6009():
    return 'ret6009' 

@action('ctrl_act6010')
def ctrl_nm6010():
    return 'ret6010' 

@action('ctrl_act6011')
def ctrl_nm6011():
    return 'ret6011' 

@action('ctrl_act6012')
def ctrl_nm6012():
    return 'ret6012' 

@action('ctrl_act6013')
def ctrl_nm6013():
    return 'ret6013' 

@action('ctrl_act6014')
def ctrl_nm6014():
    return 'ret6014' 

@action('ctrl_act6015')
def ctrl_nm6015():
    return 'ret6015' 

@action('ctrl_act6016')
def ctrl_nm6016():
    return 'ret6016' 

@action('ctrl_act6017')
def ctrl_nm6017():
    return 'ret6017' 

@action('ctrl_act6018')
def ctrl_nm6018():
    return 'ret6018' 

@action('ctrl_act6019')
def ctrl_nm6019():
    return 'ret6019' 

@action('ctrl_act6020')
def ctrl_nm6020():
    return 'ret6020' 

@action('ctrl_act6021')
def ctrl_nm6021():
    return 'ret6021' 

@action('ctrl_act6022')
def ctrl_nm6022():
    return 'ret6022' 

@action('ctrl_act6023')
def ctrl_nm6023():
    return 'ret6023' 

@action('ctrl_act6024')
def ctrl_nm6024():
    return 'ret6024' 

@action('ctrl_act6025')
def ctrl_nm6025():
    return 'ret6025' 

@action('ctrl_act6026')
def ctrl_nm6026():
    return 'ret6026' 

@action('ctrl_act6027')
def ctrl_nm6027():
    return 'ret6027' 

@action('ctrl_act6028')
def ctrl_nm6028():
    return 'ret6028' 

@action('ctrl_act6029')
def ctrl_nm6029():
    return 'ret6029' 

@action('ctrl_act6030')
def ctrl_nm6030():
    return 'ret6030' 

@action('ctrl_act6031')
def ctrl_nm6031():
    return 'ret6031' 

@action('ctrl_act6032')
def ctrl_nm6032():
    return 'ret6032' 

@action('ctrl_act6033')
def ctrl_nm6033():
    return 'ret6033' 

@action('ctrl_act6034')
def ctrl_nm6034():
    return 'ret6034' 

@action('ctrl_act6035')
def ctrl_nm6035():
    return 'ret6035' 

@action('ctrl_act6036')
def ctrl_nm6036():
    return 'ret6036' 

@action('ctrl_act6037')
def ctrl_nm6037():
    return 'ret6037' 

@action('ctrl_act6038')
def ctrl_nm6038():
    return 'ret6038' 

@action('ctrl_act6039')
def ctrl_nm6039():
    return 'ret6039' 

@action('ctrl_act6040')
def ctrl_nm6040():
    return 'ret6040' 

@action('ctrl_act6041')
def ctrl_nm6041():
    return 'ret6041' 

@action('ctrl_act6042')
def ctrl_nm6042():
    return 'ret6042' 

@action('ctrl_act6043')
def ctrl_nm6043():
    return 'ret6043' 

@action('ctrl_act6044')
def ctrl_nm6044():
    return 'ret6044' 

@action('ctrl_act6045')
def ctrl_nm6045():
    return 'ret6045' 

@action('ctrl_act6046')
def ctrl_nm6046():
    return 'ret6046' 

@action('ctrl_act6047')
def ctrl_nm6047():
    return 'ret6047' 

@action('ctrl_act6048')
def ctrl_nm6048():
    return 'ret6048' 

@action('ctrl_act6049')
def ctrl_nm6049():
    return 'ret6049' 

@action('ctrl_act6050')
def ctrl_nm6050():
    return 'ret6050' 

@action('ctrl_act6051')
def ctrl_nm6051():
    return 'ret6051' 

@action('ctrl_act6052')
def ctrl_nm6052():
    return 'ret6052' 

@action('ctrl_act6053')
def ctrl_nm6053():
    return 'ret6053' 

@action('ctrl_act6054')
def ctrl_nm6054():
    return 'ret6054' 

@action('ctrl_act6055')
def ctrl_nm6055():
    return 'ret6055' 

@action('ctrl_act6056')
def ctrl_nm6056():
    return 'ret6056' 

@action('ctrl_act6057')
def ctrl_nm6057():
    return 'ret6057' 

@action('ctrl_act6058')
def ctrl_nm6058():
    return 'ret6058' 

@action('ctrl_act6059')
def ctrl_nm6059():
    return 'ret6059' 

@action('ctrl_act6060')
def ctrl_nm6060():
    return 'ret6060' 

@action('ctrl_act6061')
def ctrl_nm6061():
    return 'ret6061' 

@action('ctrl_act6062')
def ctrl_nm6062():
    return 'ret6062' 

@action('ctrl_act6063')
def ctrl_nm6063():
    return 'ret6063' 

@action('ctrl_act6064')
def ctrl_nm6064():
    return 'ret6064' 

@action('ctrl_act6065')
def ctrl_nm6065():
    return 'ret6065' 

@action('ctrl_act6066')
def ctrl_nm6066():
    return 'ret6066' 

@action('ctrl_act6067')
def ctrl_nm6067():
    return 'ret6067' 

@action('ctrl_act6068')
def ctrl_nm6068():
    return 'ret6068' 

@action('ctrl_act6069')
def ctrl_nm6069():
    return 'ret6069' 

@action('ctrl_act6070')
def ctrl_nm6070():
    return 'ret6070' 

@action('ctrl_act6071')
def ctrl_nm6071():
    return 'ret6071' 

@action('ctrl_act6072')
def ctrl_nm6072():
    return 'ret6072' 

@action('ctrl_act6073')
def ctrl_nm6073():
    return 'ret6073' 

@action('ctrl_act6074')
def ctrl_nm6074():
    return 'ret6074' 

@action('ctrl_act6075')
def ctrl_nm6075():
    return 'ret6075' 

@action('ctrl_act6076')
def ctrl_nm6076():
    return 'ret6076' 

@action('ctrl_act6077')
def ctrl_nm6077():
    return 'ret6077' 

@action('ctrl_act6078')
def ctrl_nm6078():
    return 'ret6078' 

@action('ctrl_act6079')
def ctrl_nm6079():
    return 'ret6079' 

@action('ctrl_act6080')
def ctrl_nm6080():
    return 'ret6080' 

@action('ctrl_act6081')
def ctrl_nm6081():
    return 'ret6081' 

@action('ctrl_act6082')
def ctrl_nm6082():
    return 'ret6082' 

@action('ctrl_act6083')
def ctrl_nm6083():
    return 'ret6083' 

@action('ctrl_act6084')
def ctrl_nm6084():
    return 'ret6084' 

@action('ctrl_act6085')
def ctrl_nm6085():
    return 'ret6085' 

@action('ctrl_act6086')
def ctrl_nm6086():
    return 'ret6086' 

@action('ctrl_act6087')
def ctrl_nm6087():
    return 'ret6087' 

@action('ctrl_act6088')
def ctrl_nm6088():
    return 'ret6088' 

@action('ctrl_act6089')
def ctrl_nm6089():
    return 'ret6089' 

@action('ctrl_act6090')
def ctrl_nm6090():
    return 'ret6090' 

@action('ctrl_act6091')
def ctrl_nm6091():
    return 'ret6091' 

@action('ctrl_act6092')
def ctrl_nm6092():
    return 'ret6092' 

@action('ctrl_act6093')
def ctrl_nm6093():
    return 'ret6093' 

@action('ctrl_act6094')
def ctrl_nm6094():
    return 'ret6094' 

@action('ctrl_act6095')
def ctrl_nm6095():
    return 'ret6095' 

@action('ctrl_act6096')
def ctrl_nm6096():
    return 'ret6096' 

@action('ctrl_act6097')
def ctrl_nm6097():
    return 'ret6097' 

@action('ctrl_act6098')
def ctrl_nm6098():
    return 'ret6098' 

@action('ctrl_act6099')
def ctrl_nm6099():
    return 'ret6099' 

@action('ctrl_act6100')
def ctrl_nm6100():
    return 'ret6100' 

@action('ctrl_act6101')
def ctrl_nm6101():
    return 'ret6101' 

@action('ctrl_act6102')
def ctrl_nm6102():
    return 'ret6102' 

@action('ctrl_act6103')
def ctrl_nm6103():
    return 'ret6103' 

@action('ctrl_act6104')
def ctrl_nm6104():
    return 'ret6104' 

@action('ctrl_act6105')
def ctrl_nm6105():
    return 'ret6105' 

@action('ctrl_act6106')
def ctrl_nm6106():
    return 'ret6106' 

@action('ctrl_act6107')
def ctrl_nm6107():
    return 'ret6107' 

@action('ctrl_act6108')
def ctrl_nm6108():
    return 'ret6108' 

@action('ctrl_act6109')
def ctrl_nm6109():
    return 'ret6109' 

@action('ctrl_act6110')
def ctrl_nm6110():
    return 'ret6110' 

@action('ctrl_act6111')
def ctrl_nm6111():
    return 'ret6111' 

@action('ctrl_act6112')
def ctrl_nm6112():
    return 'ret6112' 

@action('ctrl_act6113')
def ctrl_nm6113():
    return 'ret6113' 

@action('ctrl_act6114')
def ctrl_nm6114():
    return 'ret6114' 

@action('ctrl_act6115')
def ctrl_nm6115():
    return 'ret6115' 

@action('ctrl_act6116')
def ctrl_nm6116():
    return 'ret6116' 

@action('ctrl_act6117')
def ctrl_nm6117():
    return 'ret6117' 

@action('ctrl_act6118')
def ctrl_nm6118():
    return 'ret6118' 

@action('ctrl_act6119')
def ctrl_nm6119():
    return 'ret6119' 

@action('ctrl_act6120')
def ctrl_nm6120():
    return 'ret6120' 

@action('ctrl_act6121')
def ctrl_nm6121():
    return 'ret6121' 

@action('ctrl_act6122')
def ctrl_nm6122():
    return 'ret6122' 

@action('ctrl_act6123')
def ctrl_nm6123():
    return 'ret6123' 

@action('ctrl_act6124')
def ctrl_nm6124():
    return 'ret6124' 

@action('ctrl_act6125')
def ctrl_nm6125():
    return 'ret6125' 

@action('ctrl_act6126')
def ctrl_nm6126():
    return 'ret6126' 

@action('ctrl_act6127')
def ctrl_nm6127():
    return 'ret6127' 

@action('ctrl_act6128')
def ctrl_nm6128():
    return 'ret6128' 

@action('ctrl_act6129')
def ctrl_nm6129():
    return 'ret6129' 

@action('ctrl_act6130')
def ctrl_nm6130():
    return 'ret6130' 

@action('ctrl_act6131')
def ctrl_nm6131():
    return 'ret6131' 

@action('ctrl_act6132')
def ctrl_nm6132():
    return 'ret6132' 

@action('ctrl_act6133')
def ctrl_nm6133():
    return 'ret6133' 

@action('ctrl_act6134')
def ctrl_nm6134():
    return 'ret6134' 

@action('ctrl_act6135')
def ctrl_nm6135():
    return 'ret6135' 

@action('ctrl_act6136')
def ctrl_nm6136():
    return 'ret6136' 

@action('ctrl_act6137')
def ctrl_nm6137():
    return 'ret6137' 

@action('ctrl_act6138')
def ctrl_nm6138():
    return 'ret6138' 

@action('ctrl_act6139')
def ctrl_nm6139():
    return 'ret6139' 

@action('ctrl_act6140')
def ctrl_nm6140():
    return 'ret6140' 

@action('ctrl_act6141')
def ctrl_nm6141():
    return 'ret6141' 

@action('ctrl_act6142')
def ctrl_nm6142():
    return 'ret6142' 

@action('ctrl_act6143')
def ctrl_nm6143():
    return 'ret6143' 

@action('ctrl_act6144')
def ctrl_nm6144():
    return 'ret6144' 

@action('ctrl_act6145')
def ctrl_nm6145():
    return 'ret6145' 

@action('ctrl_act6146')
def ctrl_nm6146():
    return 'ret6146' 

@action('ctrl_act6147')
def ctrl_nm6147():
    return 'ret6147' 

@action('ctrl_act6148')
def ctrl_nm6148():
    return 'ret6148' 

@action('ctrl_act6149')
def ctrl_nm6149():
    return 'ret6149' 

@action('ctrl_act6150')
def ctrl_nm6150():
    return 'ret6150' 

@action('ctrl_act6151')
def ctrl_nm6151():
    return 'ret6151' 

@action('ctrl_act6152')
def ctrl_nm6152():
    return 'ret6152' 

@action('ctrl_act6153')
def ctrl_nm6153():
    return 'ret6153' 

@action('ctrl_act6154')
def ctrl_nm6154():
    return 'ret6154' 

@action('ctrl_act6155')
def ctrl_nm6155():
    return 'ret6155' 

@action('ctrl_act6156')
def ctrl_nm6156():
    return 'ret6156' 

@action('ctrl_act6157')
def ctrl_nm6157():
    return 'ret6157' 

@action('ctrl_act6158')
def ctrl_nm6158():
    return 'ret6158' 

@action('ctrl_act6159')
def ctrl_nm6159():
    return 'ret6159' 

@action('ctrl_act6160')
def ctrl_nm6160():
    return 'ret6160' 

@action('ctrl_act6161')
def ctrl_nm6161():
    return 'ret6161' 

@action('ctrl_act6162')
def ctrl_nm6162():
    return 'ret6162' 

@action('ctrl_act6163')
def ctrl_nm6163():
    return 'ret6163' 

@action('ctrl_act6164')
def ctrl_nm6164():
    return 'ret6164' 

@action('ctrl_act6165')
def ctrl_nm6165():
    return 'ret6165' 

@action('ctrl_act6166')
def ctrl_nm6166():
    return 'ret6166' 

@action('ctrl_act6167')
def ctrl_nm6167():
    return 'ret6167' 

@action('ctrl_act6168')
def ctrl_nm6168():
    return 'ret6168' 

@action('ctrl_act6169')
def ctrl_nm6169():
    return 'ret6169' 

@action('ctrl_act6170')
def ctrl_nm6170():
    return 'ret6170' 

@action('ctrl_act6171')
def ctrl_nm6171():
    return 'ret6171' 

@action('ctrl_act6172')
def ctrl_nm6172():
    return 'ret6172' 

@action('ctrl_act6173')
def ctrl_nm6173():
    return 'ret6173' 

@action('ctrl_act6174')
def ctrl_nm6174():
    return 'ret6174' 

@action('ctrl_act6175')
def ctrl_nm6175():
    return 'ret6175' 

@action('ctrl_act6176')
def ctrl_nm6176():
    return 'ret6176' 

@action('ctrl_act6177')
def ctrl_nm6177():
    return 'ret6177' 

@action('ctrl_act6178')
def ctrl_nm6178():
    return 'ret6178' 

@action('ctrl_act6179')
def ctrl_nm6179():
    return 'ret6179' 

@action('ctrl_act6180')
def ctrl_nm6180():
    return 'ret6180' 

@action('ctrl_act6181')
def ctrl_nm6181():
    return 'ret6181' 

@action('ctrl_act6182')
def ctrl_nm6182():
    return 'ret6182' 

@action('ctrl_act6183')
def ctrl_nm6183():
    return 'ret6183' 

@action('ctrl_act6184')
def ctrl_nm6184():
    return 'ret6184' 

@action('ctrl_act6185')
def ctrl_nm6185():
    return 'ret6185' 

@action('ctrl_act6186')
def ctrl_nm6186():
    return 'ret6186' 

@action('ctrl_act6187')
def ctrl_nm6187():
    return 'ret6187' 

@action('ctrl_act6188')
def ctrl_nm6188():
    return 'ret6188' 

@action('ctrl_act6189')
def ctrl_nm6189():
    return 'ret6189' 

@action('ctrl_act6190')
def ctrl_nm6190():
    return 'ret6190' 

@action('ctrl_act6191')
def ctrl_nm6191():
    return 'ret6191' 

@action('ctrl_act6192')
def ctrl_nm6192():
    return 'ret6192' 

@action('ctrl_act6193')
def ctrl_nm6193():
    return 'ret6193' 

@action('ctrl_act6194')
def ctrl_nm6194():
    return 'ret6194' 

@action('ctrl_act6195')
def ctrl_nm6195():
    return 'ret6195' 

@action('ctrl_act6196')
def ctrl_nm6196():
    return 'ret6196' 

@action('ctrl_act6197')
def ctrl_nm6197():
    return 'ret6197' 

@action('ctrl_act6198')
def ctrl_nm6198():
    return 'ret6198' 

@action('ctrl_act6199')
def ctrl_nm6199():
    return 'ret6199' 

@action('ctrl_act6200')
def ctrl_nm6200():
    return 'ret6200' 

@action('ctrl_act6201')
def ctrl_nm6201():
    return 'ret6201' 

@action('ctrl_act6202')
def ctrl_nm6202():
    return 'ret6202' 

@action('ctrl_act6203')
def ctrl_nm6203():
    return 'ret6203' 

@action('ctrl_act6204')
def ctrl_nm6204():
    return 'ret6204' 

@action('ctrl_act6205')
def ctrl_nm6205():
    return 'ret6205' 

@action('ctrl_act6206')
def ctrl_nm6206():
    return 'ret6206' 

@action('ctrl_act6207')
def ctrl_nm6207():
    return 'ret6207' 

@action('ctrl_act6208')
def ctrl_nm6208():
    return 'ret6208' 

@action('ctrl_act6209')
def ctrl_nm6209():
    return 'ret6209' 

@action('ctrl_act6210')
def ctrl_nm6210():
    return 'ret6210' 

@action('ctrl_act6211')
def ctrl_nm6211():
    return 'ret6211' 

@action('ctrl_act6212')
def ctrl_nm6212():
    return 'ret6212' 

@action('ctrl_act6213')
def ctrl_nm6213():
    return 'ret6213' 

@action('ctrl_act6214')
def ctrl_nm6214():
    return 'ret6214' 

@action('ctrl_act6215')
def ctrl_nm6215():
    return 'ret6215' 

@action('ctrl_act6216')
def ctrl_nm6216():
    return 'ret6216' 

@action('ctrl_act6217')
def ctrl_nm6217():
    return 'ret6217' 

@action('ctrl_act6218')
def ctrl_nm6218():
    return 'ret6218' 

@action('ctrl_act6219')
def ctrl_nm6219():
    return 'ret6219' 

@action('ctrl_act6220')
def ctrl_nm6220():
    return 'ret6220' 

@action('ctrl_act6221')
def ctrl_nm6221():
    return 'ret6221' 

@action('ctrl_act6222')
def ctrl_nm6222():
    return 'ret6222' 

@action('ctrl_act6223')
def ctrl_nm6223():
    return 'ret6223' 

@action('ctrl_act6224')
def ctrl_nm6224():
    return 'ret6224' 

@action('ctrl_act6225')
def ctrl_nm6225():
    return 'ret6225' 

@action('ctrl_act6226')
def ctrl_nm6226():
    return 'ret6226' 

@action('ctrl_act6227')
def ctrl_nm6227():
    return 'ret6227' 

@action('ctrl_act6228')
def ctrl_nm6228():
    return 'ret6228' 

@action('ctrl_act6229')
def ctrl_nm6229():
    return 'ret6229' 

@action('ctrl_act6230')
def ctrl_nm6230():
    return 'ret6230' 

@action('ctrl_act6231')
def ctrl_nm6231():
    return 'ret6231' 

@action('ctrl_act6232')
def ctrl_nm6232():
    return 'ret6232' 

@action('ctrl_act6233')
def ctrl_nm6233():
    return 'ret6233' 

@action('ctrl_act6234')
def ctrl_nm6234():
    return 'ret6234' 

@action('ctrl_act6235')
def ctrl_nm6235():
    return 'ret6235' 

@action('ctrl_act6236')
def ctrl_nm6236():
    return 'ret6236' 

@action('ctrl_act6237')
def ctrl_nm6237():
    return 'ret6237' 

@action('ctrl_act6238')
def ctrl_nm6238():
    return 'ret6238' 

@action('ctrl_act6239')
def ctrl_nm6239():
    return 'ret6239' 

@action('ctrl_act6240')
def ctrl_nm6240():
    return 'ret6240' 

@action('ctrl_act6241')
def ctrl_nm6241():
    return 'ret6241' 

@action('ctrl_act6242')
def ctrl_nm6242():
    return 'ret6242' 

@action('ctrl_act6243')
def ctrl_nm6243():
    return 'ret6243' 

@action('ctrl_act6244')
def ctrl_nm6244():
    return 'ret6244' 

@action('ctrl_act6245')
def ctrl_nm6245():
    return 'ret6245' 

@action('ctrl_act6246')
def ctrl_nm6246():
    return 'ret6246' 

@action('ctrl_act6247')
def ctrl_nm6247():
    return 'ret6247' 

@action('ctrl_act6248')
def ctrl_nm6248():
    return 'ret6248' 

@action('ctrl_act6249')
def ctrl_nm6249():
    return 'ret6249' 

@action('ctrl_act6250')
def ctrl_nm6250():
    return 'ret6250' 

@action('ctrl_act6251')
def ctrl_nm6251():
    return 'ret6251' 

@action('ctrl_act6252')
def ctrl_nm6252():
    return 'ret6252' 

@action('ctrl_act6253')
def ctrl_nm6253():
    return 'ret6253' 

@action('ctrl_act6254')
def ctrl_nm6254():
    return 'ret6254' 

@action('ctrl_act6255')
def ctrl_nm6255():
    return 'ret6255' 

@action('ctrl_act6256')
def ctrl_nm6256():
    return 'ret6256' 

@action('ctrl_act6257')
def ctrl_nm6257():
    return 'ret6257' 

@action('ctrl_act6258')
def ctrl_nm6258():
    return 'ret6258' 

@action('ctrl_act6259')
def ctrl_nm6259():
    return 'ret6259' 

@action('ctrl_act6260')
def ctrl_nm6260():
    return 'ret6260' 

@action('ctrl_act6261')
def ctrl_nm6261():
    return 'ret6261' 

@action('ctrl_act6262')
def ctrl_nm6262():
    return 'ret6262' 

@action('ctrl_act6263')
def ctrl_nm6263():
    return 'ret6263' 

@action('ctrl_act6264')
def ctrl_nm6264():
    return 'ret6264' 

@action('ctrl_act6265')
def ctrl_nm6265():
    return 'ret6265' 

@action('ctrl_act6266')
def ctrl_nm6266():
    return 'ret6266' 

@action('ctrl_act6267')
def ctrl_nm6267():
    return 'ret6267' 

@action('ctrl_act6268')
def ctrl_nm6268():
    return 'ret6268' 

@action('ctrl_act6269')
def ctrl_nm6269():
    return 'ret6269' 

@action('ctrl_act6270')
def ctrl_nm6270():
    return 'ret6270' 

@action('ctrl_act6271')
def ctrl_nm6271():
    return 'ret6271' 

@action('ctrl_act6272')
def ctrl_nm6272():
    return 'ret6272' 

@action('ctrl_act6273')
def ctrl_nm6273():
    return 'ret6273' 

@action('ctrl_act6274')
def ctrl_nm6274():
    return 'ret6274' 

@action('ctrl_act6275')
def ctrl_nm6275():
    return 'ret6275' 

@action('ctrl_act6276')
def ctrl_nm6276():
    return 'ret6276' 

@action('ctrl_act6277')
def ctrl_nm6277():
    return 'ret6277' 

@action('ctrl_act6278')
def ctrl_nm6278():
    return 'ret6278' 

@action('ctrl_act6279')
def ctrl_nm6279():
    return 'ret6279' 

@action('ctrl_act6280')
def ctrl_nm6280():
    return 'ret6280' 

@action('ctrl_act6281')
def ctrl_nm6281():
    return 'ret6281' 

@action('ctrl_act6282')
def ctrl_nm6282():
    return 'ret6282' 

@action('ctrl_act6283')
def ctrl_nm6283():
    return 'ret6283' 

@action('ctrl_act6284')
def ctrl_nm6284():
    return 'ret6284' 

@action('ctrl_act6285')
def ctrl_nm6285():
    return 'ret6285' 

@action('ctrl_act6286')
def ctrl_nm6286():
    return 'ret6286' 

@action('ctrl_act6287')
def ctrl_nm6287():
    return 'ret6287' 

@action('ctrl_act6288')
def ctrl_nm6288():
    return 'ret6288' 

@action('ctrl_act6289')
def ctrl_nm6289():
    return 'ret6289' 

@action('ctrl_act6290')
def ctrl_nm6290():
    return 'ret6290' 

@action('ctrl_act6291')
def ctrl_nm6291():
    return 'ret6291' 

@action('ctrl_act6292')
def ctrl_nm6292():
    return 'ret6292' 

@action('ctrl_act6293')
def ctrl_nm6293():
    return 'ret6293' 

@action('ctrl_act6294')
def ctrl_nm6294():
    return 'ret6294' 

@action('ctrl_act6295')
def ctrl_nm6295():
    return 'ret6295' 

@action('ctrl_act6296')
def ctrl_nm6296():
    return 'ret6296' 

@action('ctrl_act6297')
def ctrl_nm6297():
    return 'ret6297' 

@action('ctrl_act6298')
def ctrl_nm6298():
    return 'ret6298' 

@action('ctrl_act6299')
def ctrl_nm6299():
    return 'ret6299' 

@action('ctrl_act6300')
def ctrl_nm6300():
    return 'ret6300' 

@action('ctrl_act6301')
def ctrl_nm6301():
    return 'ret6301' 

@action('ctrl_act6302')
def ctrl_nm6302():
    return 'ret6302' 

@action('ctrl_act6303')
def ctrl_nm6303():
    return 'ret6303' 

@action('ctrl_act6304')
def ctrl_nm6304():
    return 'ret6304' 

@action('ctrl_act6305')
def ctrl_nm6305():
    return 'ret6305' 

@action('ctrl_act6306')
def ctrl_nm6306():
    return 'ret6306' 

@action('ctrl_act6307')
def ctrl_nm6307():
    return 'ret6307' 

@action('ctrl_act6308')
def ctrl_nm6308():
    return 'ret6308' 

@action('ctrl_act6309')
def ctrl_nm6309():
    return 'ret6309' 

@action('ctrl_act6310')
def ctrl_nm6310():
    return 'ret6310' 

@action('ctrl_act6311')
def ctrl_nm6311():
    return 'ret6311' 

@action('ctrl_act6312')
def ctrl_nm6312():
    return 'ret6312' 

@action('ctrl_act6313')
def ctrl_nm6313():
    return 'ret6313' 

@action('ctrl_act6314')
def ctrl_nm6314():
    return 'ret6314' 

@action('ctrl_act6315')
def ctrl_nm6315():
    return 'ret6315' 

@action('ctrl_act6316')
def ctrl_nm6316():
    return 'ret6316' 

@action('ctrl_act6317')
def ctrl_nm6317():
    return 'ret6317' 

@action('ctrl_act6318')
def ctrl_nm6318():
    return 'ret6318' 

@action('ctrl_act6319')
def ctrl_nm6319():
    return 'ret6319' 

@action('ctrl_act6320')
def ctrl_nm6320():
    return 'ret6320' 

@action('ctrl_act6321')
def ctrl_nm6321():
    return 'ret6321' 

@action('ctrl_act6322')
def ctrl_nm6322():
    return 'ret6322' 

@action('ctrl_act6323')
def ctrl_nm6323():
    return 'ret6323' 

@action('ctrl_act6324')
def ctrl_nm6324():
    return 'ret6324' 

@action('ctrl_act6325')
def ctrl_nm6325():
    return 'ret6325' 

@action('ctrl_act6326')
def ctrl_nm6326():
    return 'ret6326' 

@action('ctrl_act6327')
def ctrl_nm6327():
    return 'ret6327' 

@action('ctrl_act6328')
def ctrl_nm6328():
    return 'ret6328' 

@action('ctrl_act6329')
def ctrl_nm6329():
    return 'ret6329' 

@action('ctrl_act6330')
def ctrl_nm6330():
    return 'ret6330' 

@action('ctrl_act6331')
def ctrl_nm6331():
    return 'ret6331' 

@action('ctrl_act6332')
def ctrl_nm6332():
    return 'ret6332' 

@action('ctrl_act6333')
def ctrl_nm6333():
    return 'ret6333' 

@action('ctrl_act6334')
def ctrl_nm6334():
    return 'ret6334' 

@action('ctrl_act6335')
def ctrl_nm6335():
    return 'ret6335' 

@action('ctrl_act6336')
def ctrl_nm6336():
    return 'ret6336' 

@action('ctrl_act6337')
def ctrl_nm6337():
    return 'ret6337' 

@action('ctrl_act6338')
def ctrl_nm6338():
    return 'ret6338' 

@action('ctrl_act6339')
def ctrl_nm6339():
    return 'ret6339' 

@action('ctrl_act6340')
def ctrl_nm6340():
    return 'ret6340' 

@action('ctrl_act6341')
def ctrl_nm6341():
    return 'ret6341' 

@action('ctrl_act6342')
def ctrl_nm6342():
    return 'ret6342' 

@action('ctrl_act6343')
def ctrl_nm6343():
    return 'ret6343' 

@action('ctrl_act6344')
def ctrl_nm6344():
    return 'ret6344' 

@action('ctrl_act6345')
def ctrl_nm6345():
    return 'ret6345' 

@action('ctrl_act6346')
def ctrl_nm6346():
    return 'ret6346' 

@action('ctrl_act6347')
def ctrl_nm6347():
    return 'ret6347' 

@action('ctrl_act6348')
def ctrl_nm6348():
    return 'ret6348' 

@action('ctrl_act6349')
def ctrl_nm6349():
    return 'ret6349' 

@action('ctrl_act6350')
def ctrl_nm6350():
    return 'ret6350' 

@action('ctrl_act6351')
def ctrl_nm6351():
    return 'ret6351' 

@action('ctrl_act6352')
def ctrl_nm6352():
    return 'ret6352' 

@action('ctrl_act6353')
def ctrl_nm6353():
    return 'ret6353' 

@action('ctrl_act6354')
def ctrl_nm6354():
    return 'ret6354' 

@action('ctrl_act6355')
def ctrl_nm6355():
    return 'ret6355' 

@action('ctrl_act6356')
def ctrl_nm6356():
    return 'ret6356' 

@action('ctrl_act6357')
def ctrl_nm6357():
    return 'ret6357' 

@action('ctrl_act6358')
def ctrl_nm6358():
    return 'ret6358' 

@action('ctrl_act6359')
def ctrl_nm6359():
    return 'ret6359' 

@action('ctrl_act6360')
def ctrl_nm6360():
    return 'ret6360' 

@action('ctrl_act6361')
def ctrl_nm6361():
    return 'ret6361' 

@action('ctrl_act6362')
def ctrl_nm6362():
    return 'ret6362' 

@action('ctrl_act6363')
def ctrl_nm6363():
    return 'ret6363' 

@action('ctrl_act6364')
def ctrl_nm6364():
    return 'ret6364' 

@action('ctrl_act6365')
def ctrl_nm6365():
    return 'ret6365' 

@action('ctrl_act6366')
def ctrl_nm6366():
    return 'ret6366' 

@action('ctrl_act6367')
def ctrl_nm6367():
    return 'ret6367' 

@action('ctrl_act6368')
def ctrl_nm6368():
    return 'ret6368' 

@action('ctrl_act6369')
def ctrl_nm6369():
    return 'ret6369' 

@action('ctrl_act6370')
def ctrl_nm6370():
    return 'ret6370' 

@action('ctrl_act6371')
def ctrl_nm6371():
    return 'ret6371' 

@action('ctrl_act6372')
def ctrl_nm6372():
    return 'ret6372' 

@action('ctrl_act6373')
def ctrl_nm6373():
    return 'ret6373' 

@action('ctrl_act6374')
def ctrl_nm6374():
    return 'ret6374' 

@action('ctrl_act6375')
def ctrl_nm6375():
    return 'ret6375' 

@action('ctrl_act6376')
def ctrl_nm6376():
    return 'ret6376' 

@action('ctrl_act6377')
def ctrl_nm6377():
    return 'ret6377' 

@action('ctrl_act6378')
def ctrl_nm6378():
    return 'ret6378' 

@action('ctrl_act6379')
def ctrl_nm6379():
    return 'ret6379' 

@action('ctrl_act6380')
def ctrl_nm6380():
    return 'ret6380' 

@action('ctrl_act6381')
def ctrl_nm6381():
    return 'ret6381' 

@action('ctrl_act6382')
def ctrl_nm6382():
    return 'ret6382' 

@action('ctrl_act6383')
def ctrl_nm6383():
    return 'ret6383' 

@action('ctrl_act6384')
def ctrl_nm6384():
    return 'ret6384' 

@action('ctrl_act6385')
def ctrl_nm6385():
    return 'ret6385' 

@action('ctrl_act6386')
def ctrl_nm6386():
    return 'ret6386' 

@action('ctrl_act6387')
def ctrl_nm6387():
    return 'ret6387' 

@action('ctrl_act6388')
def ctrl_nm6388():
    return 'ret6388' 

@action('ctrl_act6389')
def ctrl_nm6389():
    return 'ret6389' 

@action('ctrl_act6390')
def ctrl_nm6390():
    return 'ret6390' 

@action('ctrl_act6391')
def ctrl_nm6391():
    return 'ret6391' 

@action('ctrl_act6392')
def ctrl_nm6392():
    return 'ret6392' 

@action('ctrl_act6393')
def ctrl_nm6393():
    return 'ret6393' 

@action('ctrl_act6394')
def ctrl_nm6394():
    return 'ret6394' 

@action('ctrl_act6395')
def ctrl_nm6395():
    return 'ret6395' 

@action('ctrl_act6396')
def ctrl_nm6396():
    return 'ret6396' 

@action('ctrl_act6397')
def ctrl_nm6397():
    return 'ret6397' 

@action('ctrl_act6398')
def ctrl_nm6398():
    return 'ret6398' 

@action('ctrl_act6399')
def ctrl_nm6399():
    return 'ret6399' 

@action('ctrl_act6400')
def ctrl_nm6400():
    return 'ret6400' 

@action('ctrl_act6401')
def ctrl_nm6401():
    return 'ret6401' 

@action('ctrl_act6402')
def ctrl_nm6402():
    return 'ret6402' 

@action('ctrl_act6403')
def ctrl_nm6403():
    return 'ret6403' 

@action('ctrl_act6404')
def ctrl_nm6404():
    return 'ret6404' 

@action('ctrl_act6405')
def ctrl_nm6405():
    return 'ret6405' 

@action('ctrl_act6406')
def ctrl_nm6406():
    return 'ret6406' 

@action('ctrl_act6407')
def ctrl_nm6407():
    return 'ret6407' 

@action('ctrl_act6408')
def ctrl_nm6408():
    return 'ret6408' 

@action('ctrl_act6409')
def ctrl_nm6409():
    return 'ret6409' 

@action('ctrl_act6410')
def ctrl_nm6410():
    return 'ret6410' 

@action('ctrl_act6411')
def ctrl_nm6411():
    return 'ret6411' 

@action('ctrl_act6412')
def ctrl_nm6412():
    return 'ret6412' 

@action('ctrl_act6413')
def ctrl_nm6413():
    return 'ret6413' 

@action('ctrl_act6414')
def ctrl_nm6414():
    return 'ret6414' 

@action('ctrl_act6415')
def ctrl_nm6415():
    return 'ret6415' 

@action('ctrl_act6416')
def ctrl_nm6416():
    return 'ret6416' 

@action('ctrl_act6417')
def ctrl_nm6417():
    return 'ret6417' 

@action('ctrl_act6418')
def ctrl_nm6418():
    return 'ret6418' 

@action('ctrl_act6419')
def ctrl_nm6419():
    return 'ret6419' 

@action('ctrl_act6420')
def ctrl_nm6420():
    return 'ret6420' 

@action('ctrl_act6421')
def ctrl_nm6421():
    return 'ret6421' 

@action('ctrl_act6422')
def ctrl_nm6422():
    return 'ret6422' 

@action('ctrl_act6423')
def ctrl_nm6423():
    return 'ret6423' 

@action('ctrl_act6424')
def ctrl_nm6424():
    return 'ret6424' 

@action('ctrl_act6425')
def ctrl_nm6425():
    return 'ret6425' 

@action('ctrl_act6426')
def ctrl_nm6426():
    return 'ret6426' 

@action('ctrl_act6427')
def ctrl_nm6427():
    return 'ret6427' 

@action('ctrl_act6428')
def ctrl_nm6428():
    return 'ret6428' 

@action('ctrl_act6429')
def ctrl_nm6429():
    return 'ret6429' 

@action('ctrl_act6430')
def ctrl_nm6430():
    return 'ret6430' 

@action('ctrl_act6431')
def ctrl_nm6431():
    return 'ret6431' 

@action('ctrl_act6432')
def ctrl_nm6432():
    return 'ret6432' 

@action('ctrl_act6433')
def ctrl_nm6433():
    return 'ret6433' 

@action('ctrl_act6434')
def ctrl_nm6434():
    return 'ret6434' 

@action('ctrl_act6435')
def ctrl_nm6435():
    return 'ret6435' 

@action('ctrl_act6436')
def ctrl_nm6436():
    return 'ret6436' 

@action('ctrl_act6437')
def ctrl_nm6437():
    return 'ret6437' 

@action('ctrl_act6438')
def ctrl_nm6438():
    return 'ret6438' 

@action('ctrl_act6439')
def ctrl_nm6439():
    return 'ret6439' 

@action('ctrl_act6440')
def ctrl_nm6440():
    return 'ret6440' 

@action('ctrl_act6441')
def ctrl_nm6441():
    return 'ret6441' 

@action('ctrl_act6442')
def ctrl_nm6442():
    return 'ret6442' 

@action('ctrl_act6443')
def ctrl_nm6443():
    return 'ret6443' 

@action('ctrl_act6444')
def ctrl_nm6444():
    return 'ret6444' 

@action('ctrl_act6445')
def ctrl_nm6445():
    return 'ret6445' 

@action('ctrl_act6446')
def ctrl_nm6446():
    return 'ret6446' 

@action('ctrl_act6447')
def ctrl_nm6447():
    return 'ret6447' 

@action('ctrl_act6448')
def ctrl_nm6448():
    return 'ret6448' 

@action('ctrl_act6449')
def ctrl_nm6449():
    return 'ret6449' 

@action('ctrl_act6450')
def ctrl_nm6450():
    return 'ret6450' 

@action('ctrl_act6451')
def ctrl_nm6451():
    return 'ret6451' 

@action('ctrl_act6452')
def ctrl_nm6452():
    return 'ret6452' 

@action('ctrl_act6453')
def ctrl_nm6453():
    return 'ret6453' 

@action('ctrl_act6454')
def ctrl_nm6454():
    return 'ret6454' 

@action('ctrl_act6455')
def ctrl_nm6455():
    return 'ret6455' 

@action('ctrl_act6456')
def ctrl_nm6456():
    return 'ret6456' 

@action('ctrl_act6457')
def ctrl_nm6457():
    return 'ret6457' 

@action('ctrl_act6458')
def ctrl_nm6458():
    return 'ret6458' 

@action('ctrl_act6459')
def ctrl_nm6459():
    return 'ret6459' 

@action('ctrl_act6460')
def ctrl_nm6460():
    return 'ret6460' 

@action('ctrl_act6461')
def ctrl_nm6461():
    return 'ret6461' 

@action('ctrl_act6462')
def ctrl_nm6462():
    return 'ret6462' 

@action('ctrl_act6463')
def ctrl_nm6463():
    return 'ret6463' 

@action('ctrl_act6464')
def ctrl_nm6464():
    return 'ret6464' 

@action('ctrl_act6465')
def ctrl_nm6465():
    return 'ret6465' 

@action('ctrl_act6466')
def ctrl_nm6466():
    return 'ret6466' 

@action('ctrl_act6467')
def ctrl_nm6467():
    return 'ret6467' 

@action('ctrl_act6468')
def ctrl_nm6468():
    return 'ret6468' 

@action('ctrl_act6469')
def ctrl_nm6469():
    return 'ret6469' 

@action('ctrl_act6470')
def ctrl_nm6470():
    return 'ret6470' 

@action('ctrl_act6471')
def ctrl_nm6471():
    return 'ret6471' 

@action('ctrl_act6472')
def ctrl_nm6472():
    return 'ret6472' 

@action('ctrl_act6473')
def ctrl_nm6473():
    return 'ret6473' 

@action('ctrl_act6474')
def ctrl_nm6474():
    return 'ret6474' 

@action('ctrl_act6475')
def ctrl_nm6475():
    return 'ret6475' 

@action('ctrl_act6476')
def ctrl_nm6476():
    return 'ret6476' 

@action('ctrl_act6477')
def ctrl_nm6477():
    return 'ret6477' 

@action('ctrl_act6478')
def ctrl_nm6478():
    return 'ret6478' 

@action('ctrl_act6479')
def ctrl_nm6479():
    return 'ret6479' 

@action('ctrl_act6480')
def ctrl_nm6480():
    return 'ret6480' 

@action('ctrl_act6481')
def ctrl_nm6481():
    return 'ret6481' 

@action('ctrl_act6482')
def ctrl_nm6482():
    return 'ret6482' 

@action('ctrl_act6483')
def ctrl_nm6483():
    return 'ret6483' 

@action('ctrl_act6484')
def ctrl_nm6484():
    return 'ret6484' 

@action('ctrl_act6485')
def ctrl_nm6485():
    return 'ret6485' 

@action('ctrl_act6486')
def ctrl_nm6486():
    return 'ret6486' 

@action('ctrl_act6487')
def ctrl_nm6487():
    return 'ret6487' 

@action('ctrl_act6488')
def ctrl_nm6488():
    return 'ret6488' 

@action('ctrl_act6489')
def ctrl_nm6489():
    return 'ret6489' 

@action('ctrl_act6490')
def ctrl_nm6490():
    return 'ret6490' 

@action('ctrl_act6491')
def ctrl_nm6491():
    return 'ret6491' 

@action('ctrl_act6492')
def ctrl_nm6492():
    return 'ret6492' 

@action('ctrl_act6493')
def ctrl_nm6493():
    return 'ret6493' 

@action('ctrl_act6494')
def ctrl_nm6494():
    return 'ret6494' 

@action('ctrl_act6495')
def ctrl_nm6495():
    return 'ret6495' 

@action('ctrl_act6496')
def ctrl_nm6496():
    return 'ret6496' 

@action('ctrl_act6497')
def ctrl_nm6497():
    return 'ret6497' 

@action('ctrl_act6498')
def ctrl_nm6498():
    return 'ret6498' 

@action('ctrl_act6499')
def ctrl_nm6499():
    return 'ret6499' 

@action('ctrl_act6500')
def ctrl_nm6500():
    return 'ret6500' 

@action('ctrl_act6501')
def ctrl_nm6501():
    return 'ret6501' 

@action('ctrl_act6502')
def ctrl_nm6502():
    return 'ret6502' 

@action('ctrl_act6503')
def ctrl_nm6503():
    return 'ret6503' 

@action('ctrl_act6504')
def ctrl_nm6504():
    return 'ret6504' 

@action('ctrl_act6505')
def ctrl_nm6505():
    return 'ret6505' 

@action('ctrl_act6506')
def ctrl_nm6506():
    return 'ret6506' 

@action('ctrl_act6507')
def ctrl_nm6507():
    return 'ret6507' 

@action('ctrl_act6508')
def ctrl_nm6508():
    return 'ret6508' 

@action('ctrl_act6509')
def ctrl_nm6509():
    return 'ret6509' 

@action('ctrl_act6510')
def ctrl_nm6510():
    return 'ret6510' 

@action('ctrl_act6511')
def ctrl_nm6511():
    return 'ret6511' 

@action('ctrl_act6512')
def ctrl_nm6512():
    return 'ret6512' 

@action('ctrl_act6513')
def ctrl_nm6513():
    return 'ret6513' 

@action('ctrl_act6514')
def ctrl_nm6514():
    return 'ret6514' 

@action('ctrl_act6515')
def ctrl_nm6515():
    return 'ret6515' 

@action('ctrl_act6516')
def ctrl_nm6516():
    return 'ret6516' 

@action('ctrl_act6517')
def ctrl_nm6517():
    return 'ret6517' 

@action('ctrl_act6518')
def ctrl_nm6518():
    return 'ret6518' 

@action('ctrl_act6519')
def ctrl_nm6519():
    return 'ret6519' 

@action('ctrl_act6520')
def ctrl_nm6520():
    return 'ret6520' 

@action('ctrl_act6521')
def ctrl_nm6521():
    return 'ret6521' 

@action('ctrl_act6522')
def ctrl_nm6522():
    return 'ret6522' 

@action('ctrl_act6523')
def ctrl_nm6523():
    return 'ret6523' 

@action('ctrl_act6524')
def ctrl_nm6524():
    return 'ret6524' 

@action('ctrl_act6525')
def ctrl_nm6525():
    return 'ret6525' 

@action('ctrl_act6526')
def ctrl_nm6526():
    return 'ret6526' 

@action('ctrl_act6527')
def ctrl_nm6527():
    return 'ret6527' 

@action('ctrl_act6528')
def ctrl_nm6528():
    return 'ret6528' 

@action('ctrl_act6529')
def ctrl_nm6529():
    return 'ret6529' 

@action('ctrl_act6530')
def ctrl_nm6530():
    return 'ret6530' 

@action('ctrl_act6531')
def ctrl_nm6531():
    return 'ret6531' 

@action('ctrl_act6532')
def ctrl_nm6532():
    return 'ret6532' 

@action('ctrl_act6533')
def ctrl_nm6533():
    return 'ret6533' 

@action('ctrl_act6534')
def ctrl_nm6534():
    return 'ret6534' 

@action('ctrl_act6535')
def ctrl_nm6535():
    return 'ret6535' 

@action('ctrl_act6536')
def ctrl_nm6536():
    return 'ret6536' 

@action('ctrl_act6537')
def ctrl_nm6537():
    return 'ret6537' 

@action('ctrl_act6538')
def ctrl_nm6538():
    return 'ret6538' 

@action('ctrl_act6539')
def ctrl_nm6539():
    return 'ret6539' 

@action('ctrl_act6540')
def ctrl_nm6540():
    return 'ret6540' 

@action('ctrl_act6541')
def ctrl_nm6541():
    return 'ret6541' 

@action('ctrl_act6542')
def ctrl_nm6542():
    return 'ret6542' 

@action('ctrl_act6543')
def ctrl_nm6543():
    return 'ret6543' 

@action('ctrl_act6544')
def ctrl_nm6544():
    return 'ret6544' 

@action('ctrl_act6545')
def ctrl_nm6545():
    return 'ret6545' 

@action('ctrl_act6546')
def ctrl_nm6546():
    return 'ret6546' 

@action('ctrl_act6547')
def ctrl_nm6547():
    return 'ret6547' 

@action('ctrl_act6548')
def ctrl_nm6548():
    return 'ret6548' 

@action('ctrl_act6549')
def ctrl_nm6549():
    return 'ret6549' 

@action('ctrl_act6550')
def ctrl_nm6550():
    return 'ret6550' 

@action('ctrl_act6551')
def ctrl_nm6551():
    return 'ret6551' 

@action('ctrl_act6552')
def ctrl_nm6552():
    return 'ret6552' 

@action('ctrl_act6553')
def ctrl_nm6553():
    return 'ret6553' 

@action('ctrl_act6554')
def ctrl_nm6554():
    return 'ret6554' 

@action('ctrl_act6555')
def ctrl_nm6555():
    return 'ret6555' 

@action('ctrl_act6556')
def ctrl_nm6556():
    return 'ret6556' 

@action('ctrl_act6557')
def ctrl_nm6557():
    return 'ret6557' 

@action('ctrl_act6558')
def ctrl_nm6558():
    return 'ret6558' 

@action('ctrl_act6559')
def ctrl_nm6559():
    return 'ret6559' 

@action('ctrl_act6560')
def ctrl_nm6560():
    return 'ret6560' 

@action('ctrl_act6561')
def ctrl_nm6561():
    return 'ret6561' 

@action('ctrl_act6562')
def ctrl_nm6562():
    return 'ret6562' 

@action('ctrl_act6563')
def ctrl_nm6563():
    return 'ret6563' 

@action('ctrl_act6564')
def ctrl_nm6564():
    return 'ret6564' 

@action('ctrl_act6565')
def ctrl_nm6565():
    return 'ret6565' 

@action('ctrl_act6566')
def ctrl_nm6566():
    return 'ret6566' 

@action('ctrl_act6567')
def ctrl_nm6567():
    return 'ret6567' 

@action('ctrl_act6568')
def ctrl_nm6568():
    return 'ret6568' 

@action('ctrl_act6569')
def ctrl_nm6569():
    return 'ret6569' 

@action('ctrl_act6570')
def ctrl_nm6570():
    return 'ret6570' 

@action('ctrl_act6571')
def ctrl_nm6571():
    return 'ret6571' 

@action('ctrl_act6572')
def ctrl_nm6572():
    return 'ret6572' 

@action('ctrl_act6573')
def ctrl_nm6573():
    return 'ret6573' 

@action('ctrl_act6574')
def ctrl_nm6574():
    return 'ret6574' 

@action('ctrl_act6575')
def ctrl_nm6575():
    return 'ret6575' 

@action('ctrl_act6576')
def ctrl_nm6576():
    return 'ret6576' 

@action('ctrl_act6577')
def ctrl_nm6577():
    return 'ret6577' 

@action('ctrl_act6578')
def ctrl_nm6578():
    return 'ret6578' 

@action('ctrl_act6579')
def ctrl_nm6579():
    return 'ret6579' 

@action('ctrl_act6580')
def ctrl_nm6580():
    return 'ret6580' 

@action('ctrl_act6581')
def ctrl_nm6581():
    return 'ret6581' 

@action('ctrl_act6582')
def ctrl_nm6582():
    return 'ret6582' 

@action('ctrl_act6583')
def ctrl_nm6583():
    return 'ret6583' 

@action('ctrl_act6584')
def ctrl_nm6584():
    return 'ret6584' 

@action('ctrl_act6585')
def ctrl_nm6585():
    return 'ret6585' 

@action('ctrl_act6586')
def ctrl_nm6586():
    return 'ret6586' 

@action('ctrl_act6587')
def ctrl_nm6587():
    return 'ret6587' 

@action('ctrl_act6588')
def ctrl_nm6588():
    return 'ret6588' 

@action('ctrl_act6589')
def ctrl_nm6589():
    return 'ret6589' 

@action('ctrl_act6590')
def ctrl_nm6590():
    return 'ret6590' 

@action('ctrl_act6591')
def ctrl_nm6591():
    return 'ret6591' 

@action('ctrl_act6592')
def ctrl_nm6592():
    return 'ret6592' 

@action('ctrl_act6593')
def ctrl_nm6593():
    return 'ret6593' 

@action('ctrl_act6594')
def ctrl_nm6594():
    return 'ret6594' 

@action('ctrl_act6595')
def ctrl_nm6595():
    return 'ret6595' 

@action('ctrl_act6596')
def ctrl_nm6596():
    return 'ret6596' 

@action('ctrl_act6597')
def ctrl_nm6597():
    return 'ret6597' 

@action('ctrl_act6598')
def ctrl_nm6598():
    return 'ret6598' 

@action('ctrl_act6599')
def ctrl_nm6599():
    return 'ret6599' 

@action('ctrl_act6600')
def ctrl_nm6600():
    return 'ret6600' 

@action('ctrl_act6601')
def ctrl_nm6601():
    return 'ret6601' 

@action('ctrl_act6602')
def ctrl_nm6602():
    return 'ret6602' 

@action('ctrl_act6603')
def ctrl_nm6603():
    return 'ret6603' 

@action('ctrl_act6604')
def ctrl_nm6604():
    return 'ret6604' 

@action('ctrl_act6605')
def ctrl_nm6605():
    return 'ret6605' 

@action('ctrl_act6606')
def ctrl_nm6606():
    return 'ret6606' 

@action('ctrl_act6607')
def ctrl_nm6607():
    return 'ret6607' 

@action('ctrl_act6608')
def ctrl_nm6608():
    return 'ret6608' 

@action('ctrl_act6609')
def ctrl_nm6609():
    return 'ret6609' 

@action('ctrl_act6610')
def ctrl_nm6610():
    return 'ret6610' 

@action('ctrl_act6611')
def ctrl_nm6611():
    return 'ret6611' 

@action('ctrl_act6612')
def ctrl_nm6612():
    return 'ret6612' 

@action('ctrl_act6613')
def ctrl_nm6613():
    return 'ret6613' 

@action('ctrl_act6614')
def ctrl_nm6614():
    return 'ret6614' 

@action('ctrl_act6615')
def ctrl_nm6615():
    return 'ret6615' 

@action('ctrl_act6616')
def ctrl_nm6616():
    return 'ret6616' 

@action('ctrl_act6617')
def ctrl_nm6617():
    return 'ret6617' 

@action('ctrl_act6618')
def ctrl_nm6618():
    return 'ret6618' 

@action('ctrl_act6619')
def ctrl_nm6619():
    return 'ret6619' 

@action('ctrl_act6620')
def ctrl_nm6620():
    return 'ret6620' 

@action('ctrl_act6621')
def ctrl_nm6621():
    return 'ret6621' 

@action('ctrl_act6622')
def ctrl_nm6622():
    return 'ret6622' 

@action('ctrl_act6623')
def ctrl_nm6623():
    return 'ret6623' 

@action('ctrl_act6624')
def ctrl_nm6624():
    return 'ret6624' 

@action('ctrl_act6625')
def ctrl_nm6625():
    return 'ret6625' 

@action('ctrl_act6626')
def ctrl_nm6626():
    return 'ret6626' 

@action('ctrl_act6627')
def ctrl_nm6627():
    return 'ret6627' 

@action('ctrl_act6628')
def ctrl_nm6628():
    return 'ret6628' 

@action('ctrl_act6629')
def ctrl_nm6629():
    return 'ret6629' 

@action('ctrl_act6630')
def ctrl_nm6630():
    return 'ret6630' 

@action('ctrl_act6631')
def ctrl_nm6631():
    return 'ret6631' 

@action('ctrl_act6632')
def ctrl_nm6632():
    return 'ret6632' 

@action('ctrl_act6633')
def ctrl_nm6633():
    return 'ret6633' 

@action('ctrl_act6634')
def ctrl_nm6634():
    return 'ret6634' 

@action('ctrl_act6635')
def ctrl_nm6635():
    return 'ret6635' 

@action('ctrl_act6636')
def ctrl_nm6636():
    return 'ret6636' 

@action('ctrl_act6637')
def ctrl_nm6637():
    return 'ret6637' 

@action('ctrl_act6638')
def ctrl_nm6638():
    return 'ret6638' 

@action('ctrl_act6639')
def ctrl_nm6639():
    return 'ret6639' 

@action('ctrl_act6640')
def ctrl_nm6640():
    return 'ret6640' 

@action('ctrl_act6641')
def ctrl_nm6641():
    return 'ret6641' 

@action('ctrl_act6642')
def ctrl_nm6642():
    return 'ret6642' 

@action('ctrl_act6643')
def ctrl_nm6643():
    return 'ret6643' 

@action('ctrl_act6644')
def ctrl_nm6644():
    return 'ret6644' 

@action('ctrl_act6645')
def ctrl_nm6645():
    return 'ret6645' 

@action('ctrl_act6646')
def ctrl_nm6646():
    return 'ret6646' 

@action('ctrl_act6647')
def ctrl_nm6647():
    return 'ret6647' 

@action('ctrl_act6648')
def ctrl_nm6648():
    return 'ret6648' 

@action('ctrl_act6649')
def ctrl_nm6649():
    return 'ret6649' 

@action('ctrl_act6650')
def ctrl_nm6650():
    return 'ret6650' 

@action('ctrl_act6651')
def ctrl_nm6651():
    return 'ret6651' 

@action('ctrl_act6652')
def ctrl_nm6652():
    return 'ret6652' 

@action('ctrl_act6653')
def ctrl_nm6653():
    return 'ret6653' 

@action('ctrl_act6654')
def ctrl_nm6654():
    return 'ret6654' 

@action('ctrl_act6655')
def ctrl_nm6655():
    return 'ret6655' 

@action('ctrl_act6656')
def ctrl_nm6656():
    return 'ret6656' 

@action('ctrl_act6657')
def ctrl_nm6657():
    return 'ret6657' 

@action('ctrl_act6658')
def ctrl_nm6658():
    return 'ret6658' 

@action('ctrl_act6659')
def ctrl_nm6659():
    return 'ret6659' 

@action('ctrl_act6660')
def ctrl_nm6660():
    return 'ret6660' 

@action('ctrl_act6661')
def ctrl_nm6661():
    return 'ret6661' 

@action('ctrl_act6662')
def ctrl_nm6662():
    return 'ret6662' 

@action('ctrl_act6663')
def ctrl_nm6663():
    return 'ret6663' 

@action('ctrl_act6664')
def ctrl_nm6664():
    return 'ret6664' 

@action('ctrl_act6665')
def ctrl_nm6665():
    return 'ret6665' 

@action('ctrl_act6666')
def ctrl_nm6666():
    return 'ret6666' 

@action('ctrl_act6667')
def ctrl_nm6667():
    return 'ret6667' 

@action('ctrl_act6668')
def ctrl_nm6668():
    return 'ret6668' 

@action('ctrl_act6669')
def ctrl_nm6669():
    return 'ret6669' 

@action('ctrl_act6670')
def ctrl_nm6670():
    return 'ret6670' 

@action('ctrl_act6671')
def ctrl_nm6671():
    return 'ret6671' 

@action('ctrl_act6672')
def ctrl_nm6672():
    return 'ret6672' 

@action('ctrl_act6673')
def ctrl_nm6673():
    return 'ret6673' 

@action('ctrl_act6674')
def ctrl_nm6674():
    return 'ret6674' 

@action('ctrl_act6675')
def ctrl_nm6675():
    return 'ret6675' 

@action('ctrl_act6676')
def ctrl_nm6676():
    return 'ret6676' 

@action('ctrl_act6677')
def ctrl_nm6677():
    return 'ret6677' 

@action('ctrl_act6678')
def ctrl_nm6678():
    return 'ret6678' 

@action('ctrl_act6679')
def ctrl_nm6679():
    return 'ret6679' 

@action('ctrl_act6680')
def ctrl_nm6680():
    return 'ret6680' 

@action('ctrl_act6681')
def ctrl_nm6681():
    return 'ret6681' 

@action('ctrl_act6682')
def ctrl_nm6682():
    return 'ret6682' 

@action('ctrl_act6683')
def ctrl_nm6683():
    return 'ret6683' 

@action('ctrl_act6684')
def ctrl_nm6684():
    return 'ret6684' 

@action('ctrl_act6685')
def ctrl_nm6685():
    return 'ret6685' 

@action('ctrl_act6686')
def ctrl_nm6686():
    return 'ret6686' 

@action('ctrl_act6687')
def ctrl_nm6687():
    return 'ret6687' 

@action('ctrl_act6688')
def ctrl_nm6688():
    return 'ret6688' 

@action('ctrl_act6689')
def ctrl_nm6689():
    return 'ret6689' 

@action('ctrl_act6690')
def ctrl_nm6690():
    return 'ret6690' 

@action('ctrl_act6691')
def ctrl_nm6691():
    return 'ret6691' 

@action('ctrl_act6692')
def ctrl_nm6692():
    return 'ret6692' 

@action('ctrl_act6693')
def ctrl_nm6693():
    return 'ret6693' 

@action('ctrl_act6694')
def ctrl_nm6694():
    return 'ret6694' 

@action('ctrl_act6695')
def ctrl_nm6695():
    return 'ret6695' 

@action('ctrl_act6696')
def ctrl_nm6696():
    return 'ret6696' 

@action('ctrl_act6697')
def ctrl_nm6697():
    return 'ret6697' 

@action('ctrl_act6698')
def ctrl_nm6698():
    return 'ret6698' 

@action('ctrl_act6699')
def ctrl_nm6699():
    return 'ret6699' 

@action('ctrl_act6700')
def ctrl_nm6700():
    return 'ret6700' 

@action('ctrl_act6701')
def ctrl_nm6701():
    return 'ret6701' 

@action('ctrl_act6702')
def ctrl_nm6702():
    return 'ret6702' 

@action('ctrl_act6703')
def ctrl_nm6703():
    return 'ret6703' 

@action('ctrl_act6704')
def ctrl_nm6704():
    return 'ret6704' 

@action('ctrl_act6705')
def ctrl_nm6705():
    return 'ret6705' 

@action('ctrl_act6706')
def ctrl_nm6706():
    return 'ret6706' 

@action('ctrl_act6707')
def ctrl_nm6707():
    return 'ret6707' 

@action('ctrl_act6708')
def ctrl_nm6708():
    return 'ret6708' 

@action('ctrl_act6709')
def ctrl_nm6709():
    return 'ret6709' 

@action('ctrl_act6710')
def ctrl_nm6710():
    return 'ret6710' 

@action('ctrl_act6711')
def ctrl_nm6711():
    return 'ret6711' 

@action('ctrl_act6712')
def ctrl_nm6712():
    return 'ret6712' 

@action('ctrl_act6713')
def ctrl_nm6713():
    return 'ret6713' 

@action('ctrl_act6714')
def ctrl_nm6714():
    return 'ret6714' 

@action('ctrl_act6715')
def ctrl_nm6715():
    return 'ret6715' 

@action('ctrl_act6716')
def ctrl_nm6716():
    return 'ret6716' 

@action('ctrl_act6717')
def ctrl_nm6717():
    return 'ret6717' 

@action('ctrl_act6718')
def ctrl_nm6718():
    return 'ret6718' 

@action('ctrl_act6719')
def ctrl_nm6719():
    return 'ret6719' 

@action('ctrl_act6720')
def ctrl_nm6720():
    return 'ret6720' 

@action('ctrl_act6721')
def ctrl_nm6721():
    return 'ret6721' 

@action('ctrl_act6722')
def ctrl_nm6722():
    return 'ret6722' 

@action('ctrl_act6723')
def ctrl_nm6723():
    return 'ret6723' 

@action('ctrl_act6724')
def ctrl_nm6724():
    return 'ret6724' 

@action('ctrl_act6725')
def ctrl_nm6725():
    return 'ret6725' 

@action('ctrl_act6726')
def ctrl_nm6726():
    return 'ret6726' 

@action('ctrl_act6727')
def ctrl_nm6727():
    return 'ret6727' 

@action('ctrl_act6728')
def ctrl_nm6728():
    return 'ret6728' 

@action('ctrl_act6729')
def ctrl_nm6729():
    return 'ret6729' 

@action('ctrl_act6730')
def ctrl_nm6730():
    return 'ret6730' 

@action('ctrl_act6731')
def ctrl_nm6731():
    return 'ret6731' 

@action('ctrl_act6732')
def ctrl_nm6732():
    return 'ret6732' 

@action('ctrl_act6733')
def ctrl_nm6733():
    return 'ret6733' 

@action('ctrl_act6734')
def ctrl_nm6734():
    return 'ret6734' 

@action('ctrl_act6735')
def ctrl_nm6735():
    return 'ret6735' 

@action('ctrl_act6736')
def ctrl_nm6736():
    return 'ret6736' 

@action('ctrl_act6737')
def ctrl_nm6737():
    return 'ret6737' 

@action('ctrl_act6738')
def ctrl_nm6738():
    return 'ret6738' 

@action('ctrl_act6739')
def ctrl_nm6739():
    return 'ret6739' 

@action('ctrl_act6740')
def ctrl_nm6740():
    return 'ret6740' 

@action('ctrl_act6741')
def ctrl_nm6741():
    return 'ret6741' 

@action('ctrl_act6742')
def ctrl_nm6742():
    return 'ret6742' 

@action('ctrl_act6743')
def ctrl_nm6743():
    return 'ret6743' 

@action('ctrl_act6744')
def ctrl_nm6744():
    return 'ret6744' 

@action('ctrl_act6745')
def ctrl_nm6745():
    return 'ret6745' 

@action('ctrl_act6746')
def ctrl_nm6746():
    return 'ret6746' 

@action('ctrl_act6747')
def ctrl_nm6747():
    return 'ret6747' 

@action('ctrl_act6748')
def ctrl_nm6748():
    return 'ret6748' 

@action('ctrl_act6749')
def ctrl_nm6749():
    return 'ret6749' 

@action('ctrl_act6750')
def ctrl_nm6750():
    return 'ret6750' 

@action('ctrl_act6751')
def ctrl_nm6751():
    return 'ret6751' 

@action('ctrl_act6752')
def ctrl_nm6752():
    return 'ret6752' 

@action('ctrl_act6753')
def ctrl_nm6753():
    return 'ret6753' 

@action('ctrl_act6754')
def ctrl_nm6754():
    return 'ret6754' 

@action('ctrl_act6755')
def ctrl_nm6755():
    return 'ret6755' 

@action('ctrl_act6756')
def ctrl_nm6756():
    return 'ret6756' 

@action('ctrl_act6757')
def ctrl_nm6757():
    return 'ret6757' 

@action('ctrl_act6758')
def ctrl_nm6758():
    return 'ret6758' 

@action('ctrl_act6759')
def ctrl_nm6759():
    return 'ret6759' 

@action('ctrl_act6760')
def ctrl_nm6760():
    return 'ret6760' 

@action('ctrl_act6761')
def ctrl_nm6761():
    return 'ret6761' 

@action('ctrl_act6762')
def ctrl_nm6762():
    return 'ret6762' 

@action('ctrl_act6763')
def ctrl_nm6763():
    return 'ret6763' 

@action('ctrl_act6764')
def ctrl_nm6764():
    return 'ret6764' 

@action('ctrl_act6765')
def ctrl_nm6765():
    return 'ret6765' 

@action('ctrl_act6766')
def ctrl_nm6766():
    return 'ret6766' 

@action('ctrl_act6767')
def ctrl_nm6767():
    return 'ret6767' 

@action('ctrl_act6768')
def ctrl_nm6768():
    return 'ret6768' 

@action('ctrl_act6769')
def ctrl_nm6769():
    return 'ret6769' 

@action('ctrl_act6770')
def ctrl_nm6770():
    return 'ret6770' 

@action('ctrl_act6771')
def ctrl_nm6771():
    return 'ret6771' 

@action('ctrl_act6772')
def ctrl_nm6772():
    return 'ret6772' 

@action('ctrl_act6773')
def ctrl_nm6773():
    return 'ret6773' 

@action('ctrl_act6774')
def ctrl_nm6774():
    return 'ret6774' 

@action('ctrl_act6775')
def ctrl_nm6775():
    return 'ret6775' 

@action('ctrl_act6776')
def ctrl_nm6776():
    return 'ret6776' 

@action('ctrl_act6777')
def ctrl_nm6777():
    return 'ret6777' 

@action('ctrl_act6778')
def ctrl_nm6778():
    return 'ret6778' 

@action('ctrl_act6779')
def ctrl_nm6779():
    return 'ret6779' 

@action('ctrl_act6780')
def ctrl_nm6780():
    return 'ret6780' 

@action('ctrl_act6781')
def ctrl_nm6781():
    return 'ret6781' 

@action('ctrl_act6782')
def ctrl_nm6782():
    return 'ret6782' 

@action('ctrl_act6783')
def ctrl_nm6783():
    return 'ret6783' 

@action('ctrl_act6784')
def ctrl_nm6784():
    return 'ret6784' 

@action('ctrl_act6785')
def ctrl_nm6785():
    return 'ret6785' 

@action('ctrl_act6786')
def ctrl_nm6786():
    return 'ret6786' 

@action('ctrl_act6787')
def ctrl_nm6787():
    return 'ret6787' 

@action('ctrl_act6788')
def ctrl_nm6788():
    return 'ret6788' 

@action('ctrl_act6789')
def ctrl_nm6789():
    return 'ret6789' 

@action('ctrl_act6790')
def ctrl_nm6790():
    return 'ret6790' 

@action('ctrl_act6791')
def ctrl_nm6791():
    return 'ret6791' 

@action('ctrl_act6792')
def ctrl_nm6792():
    return 'ret6792' 

@action('ctrl_act6793')
def ctrl_nm6793():
    return 'ret6793' 

@action('ctrl_act6794')
def ctrl_nm6794():
    return 'ret6794' 

@action('ctrl_act6795')
def ctrl_nm6795():
    return 'ret6795' 

@action('ctrl_act6796')
def ctrl_nm6796():
    return 'ret6796' 

@action('ctrl_act6797')
def ctrl_nm6797():
    return 'ret6797' 

@action('ctrl_act6798')
def ctrl_nm6798():
    return 'ret6798' 

@action('ctrl_act6799')
def ctrl_nm6799():
    return 'ret6799' 

@action('ctrl_act6800')
def ctrl_nm6800():
    return 'ret6800' 

@action('ctrl_act6801')
def ctrl_nm6801():
    return 'ret6801' 

@action('ctrl_act6802')
def ctrl_nm6802():
    return 'ret6802' 

@action('ctrl_act6803')
def ctrl_nm6803():
    return 'ret6803' 

@action('ctrl_act6804')
def ctrl_nm6804():
    return 'ret6804' 

@action('ctrl_act6805')
def ctrl_nm6805():
    return 'ret6805' 

@action('ctrl_act6806')
def ctrl_nm6806():
    return 'ret6806' 

@action('ctrl_act6807')
def ctrl_nm6807():
    return 'ret6807' 

@action('ctrl_act6808')
def ctrl_nm6808():
    return 'ret6808' 

@action('ctrl_act6809')
def ctrl_nm6809():
    return 'ret6809' 

@action('ctrl_act6810')
def ctrl_nm6810():
    return 'ret6810' 

@action('ctrl_act6811')
def ctrl_nm6811():
    return 'ret6811' 

@action('ctrl_act6812')
def ctrl_nm6812():
    return 'ret6812' 

@action('ctrl_act6813')
def ctrl_nm6813():
    return 'ret6813' 

@action('ctrl_act6814')
def ctrl_nm6814():
    return 'ret6814' 

@action('ctrl_act6815')
def ctrl_nm6815():
    return 'ret6815' 

@action('ctrl_act6816')
def ctrl_nm6816():
    return 'ret6816' 

@action('ctrl_act6817')
def ctrl_nm6817():
    return 'ret6817' 

@action('ctrl_act6818')
def ctrl_nm6818():
    return 'ret6818' 

@action('ctrl_act6819')
def ctrl_nm6819():
    return 'ret6819' 

@action('ctrl_act6820')
def ctrl_nm6820():
    return 'ret6820' 

@action('ctrl_act6821')
def ctrl_nm6821():
    return 'ret6821' 

@action('ctrl_act6822')
def ctrl_nm6822():
    return 'ret6822' 

@action('ctrl_act6823')
def ctrl_nm6823():
    return 'ret6823' 

@action('ctrl_act6824')
def ctrl_nm6824():
    return 'ret6824' 

@action('ctrl_act6825')
def ctrl_nm6825():
    return 'ret6825' 

@action('ctrl_act6826')
def ctrl_nm6826():
    return 'ret6826' 

@action('ctrl_act6827')
def ctrl_nm6827():
    return 'ret6827' 

@action('ctrl_act6828')
def ctrl_nm6828():
    return 'ret6828' 

@action('ctrl_act6829')
def ctrl_nm6829():
    return 'ret6829' 

@action('ctrl_act6830')
def ctrl_nm6830():
    return 'ret6830' 

@action('ctrl_act6831')
def ctrl_nm6831():
    return 'ret6831' 

@action('ctrl_act6832')
def ctrl_nm6832():
    return 'ret6832' 

@action('ctrl_act6833')
def ctrl_nm6833():
    return 'ret6833' 

@action('ctrl_act6834')
def ctrl_nm6834():
    return 'ret6834' 

@action('ctrl_act6835')
def ctrl_nm6835():
    return 'ret6835' 

@action('ctrl_act6836')
def ctrl_nm6836():
    return 'ret6836' 

@action('ctrl_act6837')
def ctrl_nm6837():
    return 'ret6837' 

@action('ctrl_act6838')
def ctrl_nm6838():
    return 'ret6838' 

@action('ctrl_act6839')
def ctrl_nm6839():
    return 'ret6839' 

@action('ctrl_act6840')
def ctrl_nm6840():
    return 'ret6840' 

@action('ctrl_act6841')
def ctrl_nm6841():
    return 'ret6841' 

@action('ctrl_act6842')
def ctrl_nm6842():
    return 'ret6842' 

@action('ctrl_act6843')
def ctrl_nm6843():
    return 'ret6843' 

@action('ctrl_act6844')
def ctrl_nm6844():
    return 'ret6844' 

@action('ctrl_act6845')
def ctrl_nm6845():
    return 'ret6845' 

@action('ctrl_act6846')
def ctrl_nm6846():
    return 'ret6846' 

@action('ctrl_act6847')
def ctrl_nm6847():
    return 'ret6847' 

@action('ctrl_act6848')
def ctrl_nm6848():
    return 'ret6848' 

@action('ctrl_act6849')
def ctrl_nm6849():
    return 'ret6849' 

@action('ctrl_act6850')
def ctrl_nm6850():
    return 'ret6850' 

@action('ctrl_act6851')
def ctrl_nm6851():
    return 'ret6851' 

@action('ctrl_act6852')
def ctrl_nm6852():
    return 'ret6852' 

@action('ctrl_act6853')
def ctrl_nm6853():
    return 'ret6853' 

@action('ctrl_act6854')
def ctrl_nm6854():
    return 'ret6854' 

@action('ctrl_act6855')
def ctrl_nm6855():
    return 'ret6855' 

@action('ctrl_act6856')
def ctrl_nm6856():
    return 'ret6856' 

@action('ctrl_act6857')
def ctrl_nm6857():
    return 'ret6857' 

@action('ctrl_act6858')
def ctrl_nm6858():
    return 'ret6858' 

@action('ctrl_act6859')
def ctrl_nm6859():
    return 'ret6859' 

@action('ctrl_act6860')
def ctrl_nm6860():
    return 'ret6860' 

@action('ctrl_act6861')
def ctrl_nm6861():
    return 'ret6861' 

@action('ctrl_act6862')
def ctrl_nm6862():
    return 'ret6862' 

@action('ctrl_act6863')
def ctrl_nm6863():
    return 'ret6863' 

@action('ctrl_act6864')
def ctrl_nm6864():
    return 'ret6864' 

@action('ctrl_act6865')
def ctrl_nm6865():
    return 'ret6865' 

@action('ctrl_act6866')
def ctrl_nm6866():
    return 'ret6866' 

@action('ctrl_act6867')
def ctrl_nm6867():
    return 'ret6867' 

@action('ctrl_act6868')
def ctrl_nm6868():
    return 'ret6868' 

@action('ctrl_act6869')
def ctrl_nm6869():
    return 'ret6869' 

@action('ctrl_act6870')
def ctrl_nm6870():
    return 'ret6870' 

@action('ctrl_act6871')
def ctrl_nm6871():
    return 'ret6871' 

@action('ctrl_act6872')
def ctrl_nm6872():
    return 'ret6872' 

@action('ctrl_act6873')
def ctrl_nm6873():
    return 'ret6873' 

@action('ctrl_act6874')
def ctrl_nm6874():
    return 'ret6874' 

@action('ctrl_act6875')
def ctrl_nm6875():
    return 'ret6875' 

@action('ctrl_act6876')
def ctrl_nm6876():
    return 'ret6876' 

@action('ctrl_act6877')
def ctrl_nm6877():
    return 'ret6877' 

@action('ctrl_act6878')
def ctrl_nm6878():
    return 'ret6878' 

@action('ctrl_act6879')
def ctrl_nm6879():
    return 'ret6879' 

@action('ctrl_act6880')
def ctrl_nm6880():
    return 'ret6880' 

@action('ctrl_act6881')
def ctrl_nm6881():
    return 'ret6881' 

@action('ctrl_act6882')
def ctrl_nm6882():
    return 'ret6882' 

@action('ctrl_act6883')
def ctrl_nm6883():
    return 'ret6883' 

@action('ctrl_act6884')
def ctrl_nm6884():
    return 'ret6884' 

@action('ctrl_act6885')
def ctrl_nm6885():
    return 'ret6885' 

@action('ctrl_act6886')
def ctrl_nm6886():
    return 'ret6886' 

@action('ctrl_act6887')
def ctrl_nm6887():
    return 'ret6887' 

@action('ctrl_act6888')
def ctrl_nm6888():
    return 'ret6888' 

@action('ctrl_act6889')
def ctrl_nm6889():
    return 'ret6889' 

@action('ctrl_act6890')
def ctrl_nm6890():
    return 'ret6890' 

@action('ctrl_act6891')
def ctrl_nm6891():
    return 'ret6891' 

@action('ctrl_act6892')
def ctrl_nm6892():
    return 'ret6892' 

@action('ctrl_act6893')
def ctrl_nm6893():
    return 'ret6893' 

@action('ctrl_act6894')
def ctrl_nm6894():
    return 'ret6894' 

@action('ctrl_act6895')
def ctrl_nm6895():
    return 'ret6895' 

@action('ctrl_act6896')
def ctrl_nm6896():
    return 'ret6896' 

@action('ctrl_act6897')
def ctrl_nm6897():
    return 'ret6897' 

@action('ctrl_act6898')
def ctrl_nm6898():
    return 'ret6898' 

@action('ctrl_act6899')
def ctrl_nm6899():
    return 'ret6899' 

@action('ctrl_act6900')
def ctrl_nm6900():
    return 'ret6900' 

@action('ctrl_act6901')
def ctrl_nm6901():
    return 'ret6901' 

@action('ctrl_act6902')
def ctrl_nm6902():
    return 'ret6902' 

@action('ctrl_act6903')
def ctrl_nm6903():
    return 'ret6903' 

@action('ctrl_act6904')
def ctrl_nm6904():
    return 'ret6904' 

@action('ctrl_act6905')
def ctrl_nm6905():
    return 'ret6905' 

@action('ctrl_act6906')
def ctrl_nm6906():
    return 'ret6906' 

@action('ctrl_act6907')
def ctrl_nm6907():
    return 'ret6907' 

@action('ctrl_act6908')
def ctrl_nm6908():
    return 'ret6908' 

@action('ctrl_act6909')
def ctrl_nm6909():
    return 'ret6909' 

@action('ctrl_act6910')
def ctrl_nm6910():
    return 'ret6910' 

@action('ctrl_act6911')
def ctrl_nm6911():
    return 'ret6911' 

@action('ctrl_act6912')
def ctrl_nm6912():
    return 'ret6912' 

@action('ctrl_act6913')
def ctrl_nm6913():
    return 'ret6913' 

@action('ctrl_act6914')
def ctrl_nm6914():
    return 'ret6914' 

@action('ctrl_act6915')
def ctrl_nm6915():
    return 'ret6915' 

@action('ctrl_act6916')
def ctrl_nm6916():
    return 'ret6916' 

@action('ctrl_act6917')
def ctrl_nm6917():
    return 'ret6917' 

@action('ctrl_act6918')
def ctrl_nm6918():
    return 'ret6918' 

@action('ctrl_act6919')
def ctrl_nm6919():
    return 'ret6919' 

@action('ctrl_act6920')
def ctrl_nm6920():
    return 'ret6920' 

@action('ctrl_act6921')
def ctrl_nm6921():
    return 'ret6921' 

@action('ctrl_act6922')
def ctrl_nm6922():
    return 'ret6922' 

@action('ctrl_act6923')
def ctrl_nm6923():
    return 'ret6923' 

@action('ctrl_act6924')
def ctrl_nm6924():
    return 'ret6924' 

@action('ctrl_act6925')
def ctrl_nm6925():
    return 'ret6925' 

@action('ctrl_act6926')
def ctrl_nm6926():
    return 'ret6926' 

@action('ctrl_act6927')
def ctrl_nm6927():
    return 'ret6927' 

@action('ctrl_act6928')
def ctrl_nm6928():
    return 'ret6928' 

@action('ctrl_act6929')
def ctrl_nm6929():
    return 'ret6929' 

@action('ctrl_act6930')
def ctrl_nm6930():
    return 'ret6930' 

@action('ctrl_act6931')
def ctrl_nm6931():
    return 'ret6931' 

@action('ctrl_act6932')
def ctrl_nm6932():
    return 'ret6932' 

@action('ctrl_act6933')
def ctrl_nm6933():
    return 'ret6933' 

@action('ctrl_act6934')
def ctrl_nm6934():
    return 'ret6934' 

@action('ctrl_act6935')
def ctrl_nm6935():
    return 'ret6935' 

@action('ctrl_act6936')
def ctrl_nm6936():
    return 'ret6936' 

@action('ctrl_act6937')
def ctrl_nm6937():
    return 'ret6937' 

@action('ctrl_act6938')
def ctrl_nm6938():
    return 'ret6938' 

@action('ctrl_act6939')
def ctrl_nm6939():
    return 'ret6939' 

@action('ctrl_act6940')
def ctrl_nm6940():
    return 'ret6940' 

@action('ctrl_act6941')
def ctrl_nm6941():
    return 'ret6941' 

@action('ctrl_act6942')
def ctrl_nm6942():
    return 'ret6942' 

@action('ctrl_act6943')
def ctrl_nm6943():
    return 'ret6943' 

@action('ctrl_act6944')
def ctrl_nm6944():
    return 'ret6944' 

@action('ctrl_act6945')
def ctrl_nm6945():
    return 'ret6945' 

@action('ctrl_act6946')
def ctrl_nm6946():
    return 'ret6946' 

@action('ctrl_act6947')
def ctrl_nm6947():
    return 'ret6947' 

@action('ctrl_act6948')
def ctrl_nm6948():
    return 'ret6948' 

@action('ctrl_act6949')
def ctrl_nm6949():
    return 'ret6949' 

@action('ctrl_act6950')
def ctrl_nm6950():
    return 'ret6950' 

@action('ctrl_act6951')
def ctrl_nm6951():
    return 'ret6951' 

@action('ctrl_act6952')
def ctrl_nm6952():
    return 'ret6952' 

@action('ctrl_act6953')
def ctrl_nm6953():
    return 'ret6953' 

@action('ctrl_act6954')
def ctrl_nm6954():
    return 'ret6954' 

@action('ctrl_act6955')
def ctrl_nm6955():
    return 'ret6955' 

@action('ctrl_act6956')
def ctrl_nm6956():
    return 'ret6956' 

@action('ctrl_act6957')
def ctrl_nm6957():
    return 'ret6957' 

@action('ctrl_act6958')
def ctrl_nm6958():
    return 'ret6958' 

@action('ctrl_act6959')
def ctrl_nm6959():
    return 'ret6959' 

@action('ctrl_act6960')
def ctrl_nm6960():
    return 'ret6960' 

@action('ctrl_act6961')
def ctrl_nm6961():
    return 'ret6961' 

@action('ctrl_act6962')
def ctrl_nm6962():
    return 'ret6962' 

@action('ctrl_act6963')
def ctrl_nm6963():
    return 'ret6963' 

@action('ctrl_act6964')
def ctrl_nm6964():
    return 'ret6964' 

@action('ctrl_act6965')
def ctrl_nm6965():
    return 'ret6965' 

@action('ctrl_act6966')
def ctrl_nm6966():
    return 'ret6966' 

@action('ctrl_act6967')
def ctrl_nm6967():
    return 'ret6967' 

@action('ctrl_act6968')
def ctrl_nm6968():
    return 'ret6968' 

@action('ctrl_act6969')
def ctrl_nm6969():
    return 'ret6969' 

@action('ctrl_act6970')
def ctrl_nm6970():
    return 'ret6970' 

@action('ctrl_act6971')
def ctrl_nm6971():
    return 'ret6971' 

@action('ctrl_act6972')
def ctrl_nm6972():
    return 'ret6972' 

@action('ctrl_act6973')
def ctrl_nm6973():
    return 'ret6973' 

@action('ctrl_act6974')
def ctrl_nm6974():
    return 'ret6974' 

@action('ctrl_act6975')
def ctrl_nm6975():
    return 'ret6975' 

@action('ctrl_act6976')
def ctrl_nm6976():
    return 'ret6976' 

@action('ctrl_act6977')
def ctrl_nm6977():
    return 'ret6977' 

@action('ctrl_act6978')
def ctrl_nm6978():
    return 'ret6978' 

@action('ctrl_act6979')
def ctrl_nm6979():
    return 'ret6979' 

@action('ctrl_act6980')
def ctrl_nm6980():
    return 'ret6980' 

@action('ctrl_act6981')
def ctrl_nm6981():
    return 'ret6981' 

@action('ctrl_act6982')
def ctrl_nm6982():
    return 'ret6982' 

@action('ctrl_act6983')
def ctrl_nm6983():
    return 'ret6983' 

@action('ctrl_act6984')
def ctrl_nm6984():
    return 'ret6984' 

@action('ctrl_act6985')
def ctrl_nm6985():
    return 'ret6985' 

@action('ctrl_act6986')
def ctrl_nm6986():
    return 'ret6986' 

@action('ctrl_act6987')
def ctrl_nm6987():
    return 'ret6987' 

@action('ctrl_act6988')
def ctrl_nm6988():
    return 'ret6988' 

@action('ctrl_act6989')
def ctrl_nm6989():
    return 'ret6989' 

@action('ctrl_act6990')
def ctrl_nm6990():
    return 'ret6990' 

@action('ctrl_act6991')
def ctrl_nm6991():
    return 'ret6991' 

@action('ctrl_act6992')
def ctrl_nm6992():
    return 'ret6992' 

@action('ctrl_act6993')
def ctrl_nm6993():
    return 'ret6993' 

@action('ctrl_act6994')
def ctrl_nm6994():
    return 'ret6994' 

@action('ctrl_act6995')
def ctrl_nm6995():
    return 'ret6995' 

@action('ctrl_act6996')
def ctrl_nm6996():
    return 'ret6996' 

@action('ctrl_act6997')
def ctrl_nm6997():
    return 'ret6997' 

@action('ctrl_act6998')
def ctrl_nm6998():
    return 'ret6998' 

@action('ctrl_act6999')
def ctrl_nm6999():
    return 'ret6999' 

@action('ctrl_act7000')
def ctrl_nm7000():
    return 'ret7000' 

@action('ctrl_act7001')
def ctrl_nm7001():
    return 'ret7001' 

@action('ctrl_act7002')
def ctrl_nm7002():
    return 'ret7002' 

@action('ctrl_act7003')
def ctrl_nm7003():
    return 'ret7003' 

@action('ctrl_act7004')
def ctrl_nm7004():
    return 'ret7004' 

@action('ctrl_act7005')
def ctrl_nm7005():
    return 'ret7005' 

@action('ctrl_act7006')
def ctrl_nm7006():
    return 'ret7006' 

@action('ctrl_act7007')
def ctrl_nm7007():
    return 'ret7007' 

@action('ctrl_act7008')
def ctrl_nm7008():
    return 'ret7008' 

@action('ctrl_act7009')
def ctrl_nm7009():
    return 'ret7009' 

@action('ctrl_act7010')
def ctrl_nm7010():
    return 'ret7010' 

@action('ctrl_act7011')
def ctrl_nm7011():
    return 'ret7011' 

@action('ctrl_act7012')
def ctrl_nm7012():
    return 'ret7012' 

@action('ctrl_act7013')
def ctrl_nm7013():
    return 'ret7013' 

@action('ctrl_act7014')
def ctrl_nm7014():
    return 'ret7014' 

@action('ctrl_act7015')
def ctrl_nm7015():
    return 'ret7015' 

@action('ctrl_act7016')
def ctrl_nm7016():
    return 'ret7016' 

@action('ctrl_act7017')
def ctrl_nm7017():
    return 'ret7017' 

@action('ctrl_act7018')
def ctrl_nm7018():
    return 'ret7018' 

@action('ctrl_act7019')
def ctrl_nm7019():
    return 'ret7019' 

@action('ctrl_act7020')
def ctrl_nm7020():
    return 'ret7020' 

@action('ctrl_act7021')
def ctrl_nm7021():
    return 'ret7021' 

@action('ctrl_act7022')
def ctrl_nm7022():
    return 'ret7022' 

@action('ctrl_act7023')
def ctrl_nm7023():
    return 'ret7023' 

@action('ctrl_act7024')
def ctrl_nm7024():
    return 'ret7024' 

@action('ctrl_act7025')
def ctrl_nm7025():
    return 'ret7025' 

@action('ctrl_act7026')
def ctrl_nm7026():
    return 'ret7026' 

@action('ctrl_act7027')
def ctrl_nm7027():
    return 'ret7027' 

@action('ctrl_act7028')
def ctrl_nm7028():
    return 'ret7028' 

@action('ctrl_act7029')
def ctrl_nm7029():
    return 'ret7029' 

@action('ctrl_act7030')
def ctrl_nm7030():
    return 'ret7030' 

@action('ctrl_act7031')
def ctrl_nm7031():
    return 'ret7031' 

@action('ctrl_act7032')
def ctrl_nm7032():
    return 'ret7032' 

@action('ctrl_act7033')
def ctrl_nm7033():
    return 'ret7033' 

@action('ctrl_act7034')
def ctrl_nm7034():
    return 'ret7034' 

@action('ctrl_act7035')
def ctrl_nm7035():
    return 'ret7035' 

@action('ctrl_act7036')
def ctrl_nm7036():
    return 'ret7036' 

@action('ctrl_act7037')
def ctrl_nm7037():
    return 'ret7037' 

@action('ctrl_act7038')
def ctrl_nm7038():
    return 'ret7038' 

@action('ctrl_act7039')
def ctrl_nm7039():
    return 'ret7039' 

@action('ctrl_act7040')
def ctrl_nm7040():
    return 'ret7040' 

@action('ctrl_act7041')
def ctrl_nm7041():
    return 'ret7041' 

@action('ctrl_act7042')
def ctrl_nm7042():
    return 'ret7042' 

@action('ctrl_act7043')
def ctrl_nm7043():
    return 'ret7043' 

@action('ctrl_act7044')
def ctrl_nm7044():
    return 'ret7044' 

@action('ctrl_act7045')
def ctrl_nm7045():
    return 'ret7045' 

@action('ctrl_act7046')
def ctrl_nm7046():
    return 'ret7046' 

@action('ctrl_act7047')
def ctrl_nm7047():
    return 'ret7047' 

@action('ctrl_act7048')
def ctrl_nm7048():
    return 'ret7048' 

@action('ctrl_act7049')
def ctrl_nm7049():
    return 'ret7049' 

@action('ctrl_act7050')
def ctrl_nm7050():
    return 'ret7050' 

@action('ctrl_act7051')
def ctrl_nm7051():
    return 'ret7051' 

@action('ctrl_act7052')
def ctrl_nm7052():
    return 'ret7052' 

@action('ctrl_act7053')
def ctrl_nm7053():
    return 'ret7053' 

@action('ctrl_act7054')
def ctrl_nm7054():
    return 'ret7054' 

@action('ctrl_act7055')
def ctrl_nm7055():
    return 'ret7055' 

@action('ctrl_act7056')
def ctrl_nm7056():
    return 'ret7056' 

@action('ctrl_act7057')
def ctrl_nm7057():
    return 'ret7057' 

@action('ctrl_act7058')
def ctrl_nm7058():
    return 'ret7058' 

@action('ctrl_act7059')
def ctrl_nm7059():
    return 'ret7059' 

@action('ctrl_act7060')
def ctrl_nm7060():
    return 'ret7060' 

@action('ctrl_act7061')
def ctrl_nm7061():
    return 'ret7061' 

@action('ctrl_act7062')
def ctrl_nm7062():
    return 'ret7062' 

@action('ctrl_act7063')
def ctrl_nm7063():
    return 'ret7063' 

@action('ctrl_act7064')
def ctrl_nm7064():
    return 'ret7064' 

@action('ctrl_act7065')
def ctrl_nm7065():
    return 'ret7065' 

@action('ctrl_act7066')
def ctrl_nm7066():
    return 'ret7066' 

@action('ctrl_act7067')
def ctrl_nm7067():
    return 'ret7067' 

@action('ctrl_act7068')
def ctrl_nm7068():
    return 'ret7068' 

@action('ctrl_act7069')
def ctrl_nm7069():
    return 'ret7069' 

@action('ctrl_act7070')
def ctrl_nm7070():
    return 'ret7070' 

@action('ctrl_act7071')
def ctrl_nm7071():
    return 'ret7071' 

@action('ctrl_act7072')
def ctrl_nm7072():
    return 'ret7072' 

@action('ctrl_act7073')
def ctrl_nm7073():
    return 'ret7073' 

@action('ctrl_act7074')
def ctrl_nm7074():
    return 'ret7074' 

@action('ctrl_act7075')
def ctrl_nm7075():
    return 'ret7075' 

@action('ctrl_act7076')
def ctrl_nm7076():
    return 'ret7076' 

@action('ctrl_act7077')
def ctrl_nm7077():
    return 'ret7077' 

@action('ctrl_act7078')
def ctrl_nm7078():
    return 'ret7078' 

@action('ctrl_act7079')
def ctrl_nm7079():
    return 'ret7079' 

@action('ctrl_act7080')
def ctrl_nm7080():
    return 'ret7080' 

@action('ctrl_act7081')
def ctrl_nm7081():
    return 'ret7081' 

@action('ctrl_act7082')
def ctrl_nm7082():
    return 'ret7082' 

@action('ctrl_act7083')
def ctrl_nm7083():
    return 'ret7083' 

@action('ctrl_act7084')
def ctrl_nm7084():
    return 'ret7084' 

@action('ctrl_act7085')
def ctrl_nm7085():
    return 'ret7085' 

@action('ctrl_act7086')
def ctrl_nm7086():
    return 'ret7086' 

@action('ctrl_act7087')
def ctrl_nm7087():
    return 'ret7087' 

@action('ctrl_act7088')
def ctrl_nm7088():
    return 'ret7088' 

@action('ctrl_act7089')
def ctrl_nm7089():
    return 'ret7089' 

@action('ctrl_act7090')
def ctrl_nm7090():
    return 'ret7090' 

@action('ctrl_act7091')
def ctrl_nm7091():
    return 'ret7091' 

@action('ctrl_act7092')
def ctrl_nm7092():
    return 'ret7092' 

@action('ctrl_act7093')
def ctrl_nm7093():
    return 'ret7093' 

@action('ctrl_act7094')
def ctrl_nm7094():
    return 'ret7094' 

@action('ctrl_act7095')
def ctrl_nm7095():
    return 'ret7095' 

@action('ctrl_act7096')
def ctrl_nm7096():
    return 'ret7096' 

@action('ctrl_act7097')
def ctrl_nm7097():
    return 'ret7097' 

@action('ctrl_act7098')
def ctrl_nm7098():
    return 'ret7098' 

@action('ctrl_act7099')
def ctrl_nm7099():
    return 'ret7099' 

@action('ctrl_act7100')
def ctrl_nm7100():
    return 'ret7100' 

@action('ctrl_act7101')
def ctrl_nm7101():
    return 'ret7101' 

@action('ctrl_act7102')
def ctrl_nm7102():
    return 'ret7102' 

@action('ctrl_act7103')
def ctrl_nm7103():
    return 'ret7103' 

@action('ctrl_act7104')
def ctrl_nm7104():
    return 'ret7104' 

@action('ctrl_act7105')
def ctrl_nm7105():
    return 'ret7105' 

@action('ctrl_act7106')
def ctrl_nm7106():
    return 'ret7106' 

@action('ctrl_act7107')
def ctrl_nm7107():
    return 'ret7107' 

@action('ctrl_act7108')
def ctrl_nm7108():
    return 'ret7108' 

@action('ctrl_act7109')
def ctrl_nm7109():
    return 'ret7109' 

@action('ctrl_act7110')
def ctrl_nm7110():
    return 'ret7110' 

@action('ctrl_act7111')
def ctrl_nm7111():
    return 'ret7111' 

@action('ctrl_act7112')
def ctrl_nm7112():
    return 'ret7112' 

@action('ctrl_act7113')
def ctrl_nm7113():
    return 'ret7113' 

@action('ctrl_act7114')
def ctrl_nm7114():
    return 'ret7114' 

@action('ctrl_act7115')
def ctrl_nm7115():
    return 'ret7115' 

@action('ctrl_act7116')
def ctrl_nm7116():
    return 'ret7116' 

@action('ctrl_act7117')
def ctrl_nm7117():
    return 'ret7117' 

@action('ctrl_act7118')
def ctrl_nm7118():
    return 'ret7118' 

@action('ctrl_act7119')
def ctrl_nm7119():
    return 'ret7119' 

@action('ctrl_act7120')
def ctrl_nm7120():
    return 'ret7120' 

@action('ctrl_act7121')
def ctrl_nm7121():
    return 'ret7121' 

@action('ctrl_act7122')
def ctrl_nm7122():
    return 'ret7122' 

@action('ctrl_act7123')
def ctrl_nm7123():
    return 'ret7123' 

@action('ctrl_act7124')
def ctrl_nm7124():
    return 'ret7124' 

@action('ctrl_act7125')
def ctrl_nm7125():
    return 'ret7125' 

@action('ctrl_act7126')
def ctrl_nm7126():
    return 'ret7126' 

@action('ctrl_act7127')
def ctrl_nm7127():
    return 'ret7127' 

@action('ctrl_act7128')
def ctrl_nm7128():
    return 'ret7128' 

@action('ctrl_act7129')
def ctrl_nm7129():
    return 'ret7129' 

@action('ctrl_act7130')
def ctrl_nm7130():
    return 'ret7130' 

@action('ctrl_act7131')
def ctrl_nm7131():
    return 'ret7131' 

@action('ctrl_act7132')
def ctrl_nm7132():
    return 'ret7132' 

@action('ctrl_act7133')
def ctrl_nm7133():
    return 'ret7133' 

@action('ctrl_act7134')
def ctrl_nm7134():
    return 'ret7134' 

@action('ctrl_act7135')
def ctrl_nm7135():
    return 'ret7135' 

@action('ctrl_act7136')
def ctrl_nm7136():
    return 'ret7136' 

@action('ctrl_act7137')
def ctrl_nm7137():
    return 'ret7137' 

@action('ctrl_act7138')
def ctrl_nm7138():
    return 'ret7138' 

@action('ctrl_act7139')
def ctrl_nm7139():
    return 'ret7139' 

@action('ctrl_act7140')
def ctrl_nm7140():
    return 'ret7140' 

@action('ctrl_act7141')
def ctrl_nm7141():
    return 'ret7141' 

@action('ctrl_act7142')
def ctrl_nm7142():
    return 'ret7142' 

@action('ctrl_act7143')
def ctrl_nm7143():
    return 'ret7143' 

@action('ctrl_act7144')
def ctrl_nm7144():
    return 'ret7144' 

@action('ctrl_act7145')
def ctrl_nm7145():
    return 'ret7145' 

@action('ctrl_act7146')
def ctrl_nm7146():
    return 'ret7146' 

@action('ctrl_act7147')
def ctrl_nm7147():
    return 'ret7147' 

@action('ctrl_act7148')
def ctrl_nm7148():
    return 'ret7148' 

@action('ctrl_act7149')
def ctrl_nm7149():
    return 'ret7149' 

@action('ctrl_act7150')
def ctrl_nm7150():
    return 'ret7150' 

@action('ctrl_act7151')
def ctrl_nm7151():
    return 'ret7151' 

@action('ctrl_act7152')
def ctrl_nm7152():
    return 'ret7152' 

@action('ctrl_act7153')
def ctrl_nm7153():
    return 'ret7153' 

@action('ctrl_act7154')
def ctrl_nm7154():
    return 'ret7154' 

@action('ctrl_act7155')
def ctrl_nm7155():
    return 'ret7155' 

@action('ctrl_act7156')
def ctrl_nm7156():
    return 'ret7156' 

@action('ctrl_act7157')
def ctrl_nm7157():
    return 'ret7157' 

@action('ctrl_act7158')
def ctrl_nm7158():
    return 'ret7158' 

@action('ctrl_act7159')
def ctrl_nm7159():
    return 'ret7159' 

@action('ctrl_act7160')
def ctrl_nm7160():
    return 'ret7160' 

@action('ctrl_act7161')
def ctrl_nm7161():
    return 'ret7161' 

@action('ctrl_act7162')
def ctrl_nm7162():
    return 'ret7162' 

@action('ctrl_act7163')
def ctrl_nm7163():
    return 'ret7163' 

@action('ctrl_act7164')
def ctrl_nm7164():
    return 'ret7164' 

@action('ctrl_act7165')
def ctrl_nm7165():
    return 'ret7165' 

@action('ctrl_act7166')
def ctrl_nm7166():
    return 'ret7166' 

@action('ctrl_act7167')
def ctrl_nm7167():
    return 'ret7167' 

@action('ctrl_act7168')
def ctrl_nm7168():
    return 'ret7168' 

@action('ctrl_act7169')
def ctrl_nm7169():
    return 'ret7169' 

@action('ctrl_act7170')
def ctrl_nm7170():
    return 'ret7170' 

@action('ctrl_act7171')
def ctrl_nm7171():
    return 'ret7171' 

@action('ctrl_act7172')
def ctrl_nm7172():
    return 'ret7172' 

@action('ctrl_act7173')
def ctrl_nm7173():
    return 'ret7173' 

@action('ctrl_act7174')
def ctrl_nm7174():
    return 'ret7174' 

@action('ctrl_act7175')
def ctrl_nm7175():
    return 'ret7175' 

@action('ctrl_act7176')
def ctrl_nm7176():
    return 'ret7176' 

@action('ctrl_act7177')
def ctrl_nm7177():
    return 'ret7177' 

@action('ctrl_act7178')
def ctrl_nm7178():
    return 'ret7178' 

@action('ctrl_act7179')
def ctrl_nm7179():
    return 'ret7179' 

@action('ctrl_act7180')
def ctrl_nm7180():
    return 'ret7180' 

@action('ctrl_act7181')
def ctrl_nm7181():
    return 'ret7181' 

@action('ctrl_act7182')
def ctrl_nm7182():
    return 'ret7182' 

@action('ctrl_act7183')
def ctrl_nm7183():
    return 'ret7183' 

@action('ctrl_act7184')
def ctrl_nm7184():
    return 'ret7184' 

@action('ctrl_act7185')
def ctrl_nm7185():
    return 'ret7185' 

@action('ctrl_act7186')
def ctrl_nm7186():
    return 'ret7186' 

@action('ctrl_act7187')
def ctrl_nm7187():
    return 'ret7187' 

@action('ctrl_act7188')
def ctrl_nm7188():
    return 'ret7188' 

@action('ctrl_act7189')
def ctrl_nm7189():
    return 'ret7189' 

@action('ctrl_act7190')
def ctrl_nm7190():
    return 'ret7190' 

@action('ctrl_act7191')
def ctrl_nm7191():
    return 'ret7191' 

@action('ctrl_act7192')
def ctrl_nm7192():
    return 'ret7192' 

@action('ctrl_act7193')
def ctrl_nm7193():
    return 'ret7193' 

@action('ctrl_act7194')
def ctrl_nm7194():
    return 'ret7194' 

@action('ctrl_act7195')
def ctrl_nm7195():
    return 'ret7195' 

@action('ctrl_act7196')
def ctrl_nm7196():
    return 'ret7196' 

@action('ctrl_act7197')
def ctrl_nm7197():
    return 'ret7197' 

@action('ctrl_act7198')
def ctrl_nm7198():
    return 'ret7198' 

@action('ctrl_act7199')
def ctrl_nm7199():
    return 'ret7199' 

@action('ctrl_act7200')
def ctrl_nm7200():
    return 'ret7200' 

@action('ctrl_act7201')
def ctrl_nm7201():
    return 'ret7201' 

@action('ctrl_act7202')
def ctrl_nm7202():
    return 'ret7202' 

@action('ctrl_act7203')
def ctrl_nm7203():
    return 'ret7203' 

@action('ctrl_act7204')
def ctrl_nm7204():
    return 'ret7204' 

@action('ctrl_act7205')
def ctrl_nm7205():
    return 'ret7205' 

@action('ctrl_act7206')
def ctrl_nm7206():
    return 'ret7206' 

@action('ctrl_act7207')
def ctrl_nm7207():
    return 'ret7207' 

@action('ctrl_act7208')
def ctrl_nm7208():
    return 'ret7208' 

@action('ctrl_act7209')
def ctrl_nm7209():
    return 'ret7209' 

@action('ctrl_act7210')
def ctrl_nm7210():
    return 'ret7210' 

@action('ctrl_act7211')
def ctrl_nm7211():
    return 'ret7211' 

@action('ctrl_act7212')
def ctrl_nm7212():
    return 'ret7212' 

@action('ctrl_act7213')
def ctrl_nm7213():
    return 'ret7213' 

@action('ctrl_act7214')
def ctrl_nm7214():
    return 'ret7214' 

@action('ctrl_act7215')
def ctrl_nm7215():
    return 'ret7215' 

@action('ctrl_act7216')
def ctrl_nm7216():
    return 'ret7216' 

@action('ctrl_act7217')
def ctrl_nm7217():
    return 'ret7217' 

@action('ctrl_act7218')
def ctrl_nm7218():
    return 'ret7218' 

@action('ctrl_act7219')
def ctrl_nm7219():
    return 'ret7219' 

@action('ctrl_act7220')
def ctrl_nm7220():
    return 'ret7220' 

@action('ctrl_act7221')
def ctrl_nm7221():
    return 'ret7221' 

@action('ctrl_act7222')
def ctrl_nm7222():
    return 'ret7222' 

@action('ctrl_act7223')
def ctrl_nm7223():
    return 'ret7223' 

@action('ctrl_act7224')
def ctrl_nm7224():
    return 'ret7224' 

@action('ctrl_act7225')
def ctrl_nm7225():
    return 'ret7225' 

@action('ctrl_act7226')
def ctrl_nm7226():
    return 'ret7226' 

@action('ctrl_act7227')
def ctrl_nm7227():
    return 'ret7227' 

@action('ctrl_act7228')
def ctrl_nm7228():
    return 'ret7228' 

@action('ctrl_act7229')
def ctrl_nm7229():
    return 'ret7229' 

@action('ctrl_act7230')
def ctrl_nm7230():
    return 'ret7230' 

@action('ctrl_act7231')
def ctrl_nm7231():
    return 'ret7231' 

@action('ctrl_act7232')
def ctrl_nm7232():
    return 'ret7232' 

@action('ctrl_act7233')
def ctrl_nm7233():
    return 'ret7233' 

@action('ctrl_act7234')
def ctrl_nm7234():
    return 'ret7234' 

@action('ctrl_act7235')
def ctrl_nm7235():
    return 'ret7235' 

@action('ctrl_act7236')
def ctrl_nm7236():
    return 'ret7236' 

@action('ctrl_act7237')
def ctrl_nm7237():
    return 'ret7237' 

@action('ctrl_act7238')
def ctrl_nm7238():
    return 'ret7238' 

@action('ctrl_act7239')
def ctrl_nm7239():
    return 'ret7239' 

@action('ctrl_act7240')
def ctrl_nm7240():
    return 'ret7240' 

@action('ctrl_act7241')
def ctrl_nm7241():
    return 'ret7241' 

@action('ctrl_act7242')
def ctrl_nm7242():
    return 'ret7242' 

@action('ctrl_act7243')
def ctrl_nm7243():
    return 'ret7243' 

@action('ctrl_act7244')
def ctrl_nm7244():
    return 'ret7244' 

@action('ctrl_act7245')
def ctrl_nm7245():
    return 'ret7245' 

@action('ctrl_act7246')
def ctrl_nm7246():
    return 'ret7246' 

@action('ctrl_act7247')
def ctrl_nm7247():
    return 'ret7247' 

@action('ctrl_act7248')
def ctrl_nm7248():
    return 'ret7248' 

@action('ctrl_act7249')
def ctrl_nm7249():
    return 'ret7249' 

@action('ctrl_act7250')
def ctrl_nm7250():
    return 'ret7250' 

@action('ctrl_act7251')
def ctrl_nm7251():
    return 'ret7251' 

@action('ctrl_act7252')
def ctrl_nm7252():
    return 'ret7252' 

@action('ctrl_act7253')
def ctrl_nm7253():
    return 'ret7253' 

@action('ctrl_act7254')
def ctrl_nm7254():
    return 'ret7254' 

@action('ctrl_act7255')
def ctrl_nm7255():
    return 'ret7255' 

@action('ctrl_act7256')
def ctrl_nm7256():
    return 'ret7256' 

@action('ctrl_act7257')
def ctrl_nm7257():
    return 'ret7257' 

@action('ctrl_act7258')
def ctrl_nm7258():
    return 'ret7258' 

@action('ctrl_act7259')
def ctrl_nm7259():
    return 'ret7259' 

@action('ctrl_act7260')
def ctrl_nm7260():
    return 'ret7260' 

@action('ctrl_act7261')
def ctrl_nm7261():
    return 'ret7261' 

@action('ctrl_act7262')
def ctrl_nm7262():
    return 'ret7262' 

@action('ctrl_act7263')
def ctrl_nm7263():
    return 'ret7263' 

@action('ctrl_act7264')
def ctrl_nm7264():
    return 'ret7264' 

@action('ctrl_act7265')
def ctrl_nm7265():
    return 'ret7265' 

@action('ctrl_act7266')
def ctrl_nm7266():
    return 'ret7266' 

@action('ctrl_act7267')
def ctrl_nm7267():
    return 'ret7267' 

@action('ctrl_act7268')
def ctrl_nm7268():
    return 'ret7268' 

@action('ctrl_act7269')
def ctrl_nm7269():
    return 'ret7269' 

@action('ctrl_act7270')
def ctrl_nm7270():
    return 'ret7270' 

@action('ctrl_act7271')
def ctrl_nm7271():
    return 'ret7271' 

@action('ctrl_act7272')
def ctrl_nm7272():
    return 'ret7272' 

@action('ctrl_act7273')
def ctrl_nm7273():
    return 'ret7273' 

@action('ctrl_act7274')
def ctrl_nm7274():
    return 'ret7274' 

@action('ctrl_act7275')
def ctrl_nm7275():
    return 'ret7275' 

@action('ctrl_act7276')
def ctrl_nm7276():
    return 'ret7276' 

@action('ctrl_act7277')
def ctrl_nm7277():
    return 'ret7277' 

@action('ctrl_act7278')
def ctrl_nm7278():
    return 'ret7278' 

@action('ctrl_act7279')
def ctrl_nm7279():
    return 'ret7279' 

@action('ctrl_act7280')
def ctrl_nm7280():
    return 'ret7280' 

@action('ctrl_act7281')
def ctrl_nm7281():
    return 'ret7281' 

@action('ctrl_act7282')
def ctrl_nm7282():
    return 'ret7282' 

@action('ctrl_act7283')
def ctrl_nm7283():
    return 'ret7283' 

@action('ctrl_act7284')
def ctrl_nm7284():
    return 'ret7284' 

@action('ctrl_act7285')
def ctrl_nm7285():
    return 'ret7285' 

@action('ctrl_act7286')
def ctrl_nm7286():
    return 'ret7286' 

@action('ctrl_act7287')
def ctrl_nm7287():
    return 'ret7287' 

@action('ctrl_act7288')
def ctrl_nm7288():
    return 'ret7288' 

@action('ctrl_act7289')
def ctrl_nm7289():
    return 'ret7289' 

@action('ctrl_act7290')
def ctrl_nm7290():
    return 'ret7290' 

@action('ctrl_act7291')
def ctrl_nm7291():
    return 'ret7291' 

@action('ctrl_act7292')
def ctrl_nm7292():
    return 'ret7292' 

@action('ctrl_act7293')
def ctrl_nm7293():
    return 'ret7293' 

@action('ctrl_act7294')
def ctrl_nm7294():
    return 'ret7294' 

@action('ctrl_act7295')
def ctrl_nm7295():
    return 'ret7295' 

@action('ctrl_act7296')
def ctrl_nm7296():
    return 'ret7296' 

@action('ctrl_act7297')
def ctrl_nm7297():
    return 'ret7297' 

@action('ctrl_act7298')
def ctrl_nm7298():
    return 'ret7298' 

@action('ctrl_act7299')
def ctrl_nm7299():
    return 'ret7299' 

@action('ctrl_act7300')
def ctrl_nm7300():
    return 'ret7300' 

@action('ctrl_act7301')
def ctrl_nm7301():
    return 'ret7301' 

@action('ctrl_act7302')
def ctrl_nm7302():
    return 'ret7302' 

@action('ctrl_act7303')
def ctrl_nm7303():
    return 'ret7303' 

@action('ctrl_act7304')
def ctrl_nm7304():
    return 'ret7304' 

@action('ctrl_act7305')
def ctrl_nm7305():
    return 'ret7305' 

@action('ctrl_act7306')
def ctrl_nm7306():
    return 'ret7306' 

@action('ctrl_act7307')
def ctrl_nm7307():
    return 'ret7307' 

@action('ctrl_act7308')
def ctrl_nm7308():
    return 'ret7308' 

@action('ctrl_act7309')
def ctrl_nm7309():
    return 'ret7309' 

@action('ctrl_act7310')
def ctrl_nm7310():
    return 'ret7310' 

@action('ctrl_act7311')
def ctrl_nm7311():
    return 'ret7311' 

@action('ctrl_act7312')
def ctrl_nm7312():
    return 'ret7312' 

@action('ctrl_act7313')
def ctrl_nm7313():
    return 'ret7313' 

@action('ctrl_act7314')
def ctrl_nm7314():
    return 'ret7314' 

@action('ctrl_act7315')
def ctrl_nm7315():
    return 'ret7315' 

@action('ctrl_act7316')
def ctrl_nm7316():
    return 'ret7316' 

@action('ctrl_act7317')
def ctrl_nm7317():
    return 'ret7317' 

@action('ctrl_act7318')
def ctrl_nm7318():
    return 'ret7318' 

@action('ctrl_act7319')
def ctrl_nm7319():
    return 'ret7319' 

@action('ctrl_act7320')
def ctrl_nm7320():
    return 'ret7320' 

@action('ctrl_act7321')
def ctrl_nm7321():
    return 'ret7321' 

@action('ctrl_act7322')
def ctrl_nm7322():
    return 'ret7322' 

@action('ctrl_act7323')
def ctrl_nm7323():
    return 'ret7323' 

@action('ctrl_act7324')
def ctrl_nm7324():
    return 'ret7324' 

@action('ctrl_act7325')
def ctrl_nm7325():
    return 'ret7325' 

@action('ctrl_act7326')
def ctrl_nm7326():
    return 'ret7326' 

@action('ctrl_act7327')
def ctrl_nm7327():
    return 'ret7327' 

@action('ctrl_act7328')
def ctrl_nm7328():
    return 'ret7328' 

@action('ctrl_act7329')
def ctrl_nm7329():
    return 'ret7329' 

@action('ctrl_act7330')
def ctrl_nm7330():
    return 'ret7330' 

@action('ctrl_act7331')
def ctrl_nm7331():
    return 'ret7331' 

@action('ctrl_act7332')
def ctrl_nm7332():
    return 'ret7332' 

@action('ctrl_act7333')
def ctrl_nm7333():
    return 'ret7333' 

@action('ctrl_act7334')
def ctrl_nm7334():
    return 'ret7334' 

@action('ctrl_act7335')
def ctrl_nm7335():
    return 'ret7335' 

@action('ctrl_act7336')
def ctrl_nm7336():
    return 'ret7336' 

@action('ctrl_act7337')
def ctrl_nm7337():
    return 'ret7337' 

@action('ctrl_act7338')
def ctrl_nm7338():
    return 'ret7338' 

@action('ctrl_act7339')
def ctrl_nm7339():
    return 'ret7339' 

@action('ctrl_act7340')
def ctrl_nm7340():
    return 'ret7340' 

@action('ctrl_act7341')
def ctrl_nm7341():
    return 'ret7341' 

@action('ctrl_act7342')
def ctrl_nm7342():
    return 'ret7342' 

@action('ctrl_act7343')
def ctrl_nm7343():
    return 'ret7343' 

@action('ctrl_act7344')
def ctrl_nm7344():
    return 'ret7344' 

@action('ctrl_act7345')
def ctrl_nm7345():
    return 'ret7345' 

@action('ctrl_act7346')
def ctrl_nm7346():
    return 'ret7346' 

@action('ctrl_act7347')
def ctrl_nm7347():
    return 'ret7347' 

@action('ctrl_act7348')
def ctrl_nm7348():
    return 'ret7348' 

@action('ctrl_act7349')
def ctrl_nm7349():
    return 'ret7349' 

@action('ctrl_act7350')
def ctrl_nm7350():
    return 'ret7350' 

@action('ctrl_act7351')
def ctrl_nm7351():
    return 'ret7351' 

@action('ctrl_act7352')
def ctrl_nm7352():
    return 'ret7352' 

@action('ctrl_act7353')
def ctrl_nm7353():
    return 'ret7353' 

@action('ctrl_act7354')
def ctrl_nm7354():
    return 'ret7354' 

@action('ctrl_act7355')
def ctrl_nm7355():
    return 'ret7355' 

@action('ctrl_act7356')
def ctrl_nm7356():
    return 'ret7356' 

@action('ctrl_act7357')
def ctrl_nm7357():
    return 'ret7357' 

@action('ctrl_act7358')
def ctrl_nm7358():
    return 'ret7358' 

@action('ctrl_act7359')
def ctrl_nm7359():
    return 'ret7359' 

@action('ctrl_act7360')
def ctrl_nm7360():
    return 'ret7360' 

@action('ctrl_act7361')
def ctrl_nm7361():
    return 'ret7361' 

@action('ctrl_act7362')
def ctrl_nm7362():
    return 'ret7362' 

@action('ctrl_act7363')
def ctrl_nm7363():
    return 'ret7363' 

@action('ctrl_act7364')
def ctrl_nm7364():
    return 'ret7364' 

@action('ctrl_act7365')
def ctrl_nm7365():
    return 'ret7365' 

@action('ctrl_act7366')
def ctrl_nm7366():
    return 'ret7366' 

@action('ctrl_act7367')
def ctrl_nm7367():
    return 'ret7367' 

@action('ctrl_act7368')
def ctrl_nm7368():
    return 'ret7368' 

@action('ctrl_act7369')
def ctrl_nm7369():
    return 'ret7369' 

@action('ctrl_act7370')
def ctrl_nm7370():
    return 'ret7370' 

@action('ctrl_act7371')
def ctrl_nm7371():
    return 'ret7371' 

@action('ctrl_act7372')
def ctrl_nm7372():
    return 'ret7372' 

@action('ctrl_act7373')
def ctrl_nm7373():
    return 'ret7373' 

@action('ctrl_act7374')
def ctrl_nm7374():
    return 'ret7374' 

@action('ctrl_act7375')
def ctrl_nm7375():
    return 'ret7375' 

@action('ctrl_act7376')
def ctrl_nm7376():
    return 'ret7376' 

@action('ctrl_act7377')
def ctrl_nm7377():
    return 'ret7377' 

@action('ctrl_act7378')
def ctrl_nm7378():
    return 'ret7378' 

@action('ctrl_act7379')
def ctrl_nm7379():
    return 'ret7379' 

@action('ctrl_act7380')
def ctrl_nm7380():
    return 'ret7380' 

@action('ctrl_act7381')
def ctrl_nm7381():
    return 'ret7381' 

@action('ctrl_act7382')
def ctrl_nm7382():
    return 'ret7382' 

@action('ctrl_act7383')
def ctrl_nm7383():
    return 'ret7383' 

@action('ctrl_act7384')
def ctrl_nm7384():
    return 'ret7384' 

@action('ctrl_act7385')
def ctrl_nm7385():
    return 'ret7385' 

@action('ctrl_act7386')
def ctrl_nm7386():
    return 'ret7386' 

@action('ctrl_act7387')
def ctrl_nm7387():
    return 'ret7387' 

@action('ctrl_act7388')
def ctrl_nm7388():
    return 'ret7388' 

@action('ctrl_act7389')
def ctrl_nm7389():
    return 'ret7389' 

@action('ctrl_act7390')
def ctrl_nm7390():
    return 'ret7390' 

@action('ctrl_act7391')
def ctrl_nm7391():
    return 'ret7391' 

@action('ctrl_act7392')
def ctrl_nm7392():
    return 'ret7392' 

@action('ctrl_act7393')
def ctrl_nm7393():
    return 'ret7393' 

@action('ctrl_act7394')
def ctrl_nm7394():
    return 'ret7394' 

@action('ctrl_act7395')
def ctrl_nm7395():
    return 'ret7395' 

@action('ctrl_act7396')
def ctrl_nm7396():
    return 'ret7396' 

@action('ctrl_act7397')
def ctrl_nm7397():
    return 'ret7397' 

@action('ctrl_act7398')
def ctrl_nm7398():
    return 'ret7398' 

@action('ctrl_act7399')
def ctrl_nm7399():
    return 'ret7399' 

@action('ctrl_act7400')
def ctrl_nm7400():
    return 'ret7400' 

@action('ctrl_act7401')
def ctrl_nm7401():
    return 'ret7401' 

@action('ctrl_act7402')
def ctrl_nm7402():
    return 'ret7402' 

@action('ctrl_act7403')
def ctrl_nm7403():
    return 'ret7403' 

@action('ctrl_act7404')
def ctrl_nm7404():
    return 'ret7404' 

@action('ctrl_act7405')
def ctrl_nm7405():
    return 'ret7405' 

@action('ctrl_act7406')
def ctrl_nm7406():
    return 'ret7406' 

@action('ctrl_act7407')
def ctrl_nm7407():
    return 'ret7407' 

@action('ctrl_act7408')
def ctrl_nm7408():
    return 'ret7408' 

@action('ctrl_act7409')
def ctrl_nm7409():
    return 'ret7409' 

@action('ctrl_act7410')
def ctrl_nm7410():
    return 'ret7410' 

@action('ctrl_act7411')
def ctrl_nm7411():
    return 'ret7411' 

@action('ctrl_act7412')
def ctrl_nm7412():
    return 'ret7412' 

@action('ctrl_act7413')
def ctrl_nm7413():
    return 'ret7413' 

@action('ctrl_act7414')
def ctrl_nm7414():
    return 'ret7414' 

@action('ctrl_act7415')
def ctrl_nm7415():
    return 'ret7415' 

@action('ctrl_act7416')
def ctrl_nm7416():
    return 'ret7416' 

@action('ctrl_act7417')
def ctrl_nm7417():
    return 'ret7417' 

@action('ctrl_act7418')
def ctrl_nm7418():
    return 'ret7418' 

@action('ctrl_act7419')
def ctrl_nm7419():
    return 'ret7419' 

@action('ctrl_act7420')
def ctrl_nm7420():
    return 'ret7420' 

@action('ctrl_act7421')
def ctrl_nm7421():
    return 'ret7421' 

@action('ctrl_act7422')
def ctrl_nm7422():
    return 'ret7422' 

@action('ctrl_act7423')
def ctrl_nm7423():
    return 'ret7423' 

@action('ctrl_act7424')
def ctrl_nm7424():
    return 'ret7424' 

@action('ctrl_act7425')
def ctrl_nm7425():
    return 'ret7425' 

@action('ctrl_act7426')
def ctrl_nm7426():
    return 'ret7426' 

@action('ctrl_act7427')
def ctrl_nm7427():
    return 'ret7427' 

@action('ctrl_act7428')
def ctrl_nm7428():
    return 'ret7428' 

@action('ctrl_act7429')
def ctrl_nm7429():
    return 'ret7429' 

@action('ctrl_act7430')
def ctrl_nm7430():
    return 'ret7430' 

@action('ctrl_act7431')
def ctrl_nm7431():
    return 'ret7431' 

@action('ctrl_act7432')
def ctrl_nm7432():
    return 'ret7432' 

@action('ctrl_act7433')
def ctrl_nm7433():
    return 'ret7433' 

@action('ctrl_act7434')
def ctrl_nm7434():
    return 'ret7434' 

@action('ctrl_act7435')
def ctrl_nm7435():
    return 'ret7435' 

@action('ctrl_act7436')
def ctrl_nm7436():
    return 'ret7436' 

@action('ctrl_act7437')
def ctrl_nm7437():
    return 'ret7437' 

@action('ctrl_act7438')
def ctrl_nm7438():
    return 'ret7438' 

@action('ctrl_act7439')
def ctrl_nm7439():
    return 'ret7439' 

@action('ctrl_act7440')
def ctrl_nm7440():
    return 'ret7440' 

@action('ctrl_act7441')
def ctrl_nm7441():
    return 'ret7441' 

@action('ctrl_act7442')
def ctrl_nm7442():
    return 'ret7442' 

@action('ctrl_act7443')
def ctrl_nm7443():
    return 'ret7443' 

@action('ctrl_act7444')
def ctrl_nm7444():
    return 'ret7444' 

@action('ctrl_act7445')
def ctrl_nm7445():
    return 'ret7445' 

@action('ctrl_act7446')
def ctrl_nm7446():
    return 'ret7446' 

@action('ctrl_act7447')
def ctrl_nm7447():
    return 'ret7447' 

@action('ctrl_act7448')
def ctrl_nm7448():
    return 'ret7448' 

@action('ctrl_act7449')
def ctrl_nm7449():
    return 'ret7449' 

@action('ctrl_act7450')
def ctrl_nm7450():
    return 'ret7450' 

@action('ctrl_act7451')
def ctrl_nm7451():
    return 'ret7451' 

@action('ctrl_act7452')
def ctrl_nm7452():
    return 'ret7452' 

@action('ctrl_act7453')
def ctrl_nm7453():
    return 'ret7453' 

@action('ctrl_act7454')
def ctrl_nm7454():
    return 'ret7454' 

@action('ctrl_act7455')
def ctrl_nm7455():
    return 'ret7455' 

@action('ctrl_act7456')
def ctrl_nm7456():
    return 'ret7456' 

@action('ctrl_act7457')
def ctrl_nm7457():
    return 'ret7457' 

@action('ctrl_act7458')
def ctrl_nm7458():
    return 'ret7458' 

@action('ctrl_act7459')
def ctrl_nm7459():
    return 'ret7459' 

@action('ctrl_act7460')
def ctrl_nm7460():
    return 'ret7460' 

@action('ctrl_act7461')
def ctrl_nm7461():
    return 'ret7461' 

@action('ctrl_act7462')
def ctrl_nm7462():
    return 'ret7462' 

@action('ctrl_act7463')
def ctrl_nm7463():
    return 'ret7463' 

@action('ctrl_act7464')
def ctrl_nm7464():
    return 'ret7464' 

@action('ctrl_act7465')
def ctrl_nm7465():
    return 'ret7465' 

@action('ctrl_act7466')
def ctrl_nm7466():
    return 'ret7466' 

@action('ctrl_act7467')
def ctrl_nm7467():
    return 'ret7467' 

@action('ctrl_act7468')
def ctrl_nm7468():
    return 'ret7468' 

@action('ctrl_act7469')
def ctrl_nm7469():
    return 'ret7469' 

@action('ctrl_act7470')
def ctrl_nm7470():
    return 'ret7470' 

@action('ctrl_act7471')
def ctrl_nm7471():
    return 'ret7471' 

@action('ctrl_act7472')
def ctrl_nm7472():
    return 'ret7472' 

@action('ctrl_act7473')
def ctrl_nm7473():
    return 'ret7473' 

@action('ctrl_act7474')
def ctrl_nm7474():
    return 'ret7474' 

@action('ctrl_act7475')
def ctrl_nm7475():
    return 'ret7475' 

@action('ctrl_act7476')
def ctrl_nm7476():
    return 'ret7476' 

@action('ctrl_act7477')
def ctrl_nm7477():
    return 'ret7477' 

@action('ctrl_act7478')
def ctrl_nm7478():
    return 'ret7478' 

@action('ctrl_act7479')
def ctrl_nm7479():
    return 'ret7479' 

@action('ctrl_act7480')
def ctrl_nm7480():
    return 'ret7480' 

@action('ctrl_act7481')
def ctrl_nm7481():
    return 'ret7481' 

@action('ctrl_act7482')
def ctrl_nm7482():
    return 'ret7482' 

@action('ctrl_act7483')
def ctrl_nm7483():
    return 'ret7483' 

@action('ctrl_act7484')
def ctrl_nm7484():
    return 'ret7484' 

@action('ctrl_act7485')
def ctrl_nm7485():
    return 'ret7485' 

@action('ctrl_act7486')
def ctrl_nm7486():
    return 'ret7486' 

@action('ctrl_act7487')
def ctrl_nm7487():
    return 'ret7487' 

@action('ctrl_act7488')
def ctrl_nm7488():
    return 'ret7488' 

@action('ctrl_act7489')
def ctrl_nm7489():
    return 'ret7489' 

@action('ctrl_act7490')
def ctrl_nm7490():
    return 'ret7490' 

@action('ctrl_act7491')
def ctrl_nm7491():
    return 'ret7491' 

@action('ctrl_act7492')
def ctrl_nm7492():
    return 'ret7492' 

@action('ctrl_act7493')
def ctrl_nm7493():
    return 'ret7493' 

@action('ctrl_act7494')
def ctrl_nm7494():
    return 'ret7494' 

@action('ctrl_act7495')
def ctrl_nm7495():
    return 'ret7495' 

@action('ctrl_act7496')
def ctrl_nm7496():
    return 'ret7496' 

@action('ctrl_act7497')
def ctrl_nm7497():
    return 'ret7497' 

@action('ctrl_act7498')
def ctrl_nm7498():
    return 'ret7498' 

@action('ctrl_act7499')
def ctrl_nm7499():
    return 'ret7499' 

@action('ctrl_act7500')
def ctrl_nm7500():
    return 'ret7500' 

@action('ctrl_act7501')
def ctrl_nm7501():
    return 'ret7501' 

@action('ctrl_act7502')
def ctrl_nm7502():
    return 'ret7502' 

@action('ctrl_act7503')
def ctrl_nm7503():
    return 'ret7503' 

@action('ctrl_act7504')
def ctrl_nm7504():
    return 'ret7504' 

@action('ctrl_act7505')
def ctrl_nm7505():
    return 'ret7505' 

@action('ctrl_act7506')
def ctrl_nm7506():
    return 'ret7506' 

@action('ctrl_act7507')
def ctrl_nm7507():
    return 'ret7507' 

@action('ctrl_act7508')
def ctrl_nm7508():
    return 'ret7508' 

@action('ctrl_act7509')
def ctrl_nm7509():
    return 'ret7509' 

@action('ctrl_act7510')
def ctrl_nm7510():
    return 'ret7510' 

@action('ctrl_act7511')
def ctrl_nm7511():
    return 'ret7511' 

@action('ctrl_act7512')
def ctrl_nm7512():
    return 'ret7512' 

@action('ctrl_act7513')
def ctrl_nm7513():
    return 'ret7513' 

@action('ctrl_act7514')
def ctrl_nm7514():
    return 'ret7514' 

@action('ctrl_act7515')
def ctrl_nm7515():
    return 'ret7515' 

@action('ctrl_act7516')
def ctrl_nm7516():
    return 'ret7516' 

@action('ctrl_act7517')
def ctrl_nm7517():
    return 'ret7517' 

@action('ctrl_act7518')
def ctrl_nm7518():
    return 'ret7518' 

@action('ctrl_act7519')
def ctrl_nm7519():
    return 'ret7519' 

@action('ctrl_act7520')
def ctrl_nm7520():
    return 'ret7520' 

@action('ctrl_act7521')
def ctrl_nm7521():
    return 'ret7521' 

@action('ctrl_act7522')
def ctrl_nm7522():
    return 'ret7522' 

@action('ctrl_act7523')
def ctrl_nm7523():
    return 'ret7523' 

@action('ctrl_act7524')
def ctrl_nm7524():
    return 'ret7524' 

@action('ctrl_act7525')
def ctrl_nm7525():
    return 'ret7525' 

@action('ctrl_act7526')
def ctrl_nm7526():
    return 'ret7526' 

@action('ctrl_act7527')
def ctrl_nm7527():
    return 'ret7527' 

@action('ctrl_act7528')
def ctrl_nm7528():
    return 'ret7528' 

@action('ctrl_act7529')
def ctrl_nm7529():
    return 'ret7529' 

@action('ctrl_act7530')
def ctrl_nm7530():
    return 'ret7530' 

@action('ctrl_act7531')
def ctrl_nm7531():
    return 'ret7531' 

@action('ctrl_act7532')
def ctrl_nm7532():
    return 'ret7532' 

@action('ctrl_act7533')
def ctrl_nm7533():
    return 'ret7533' 

@action('ctrl_act7534')
def ctrl_nm7534():
    return 'ret7534' 

@action('ctrl_act7535')
def ctrl_nm7535():
    return 'ret7535' 

@action('ctrl_act7536')
def ctrl_nm7536():
    return 'ret7536' 

@action('ctrl_act7537')
def ctrl_nm7537():
    return 'ret7537' 

@action('ctrl_act7538')
def ctrl_nm7538():
    return 'ret7538' 

@action('ctrl_act7539')
def ctrl_nm7539():
    return 'ret7539' 

@action('ctrl_act7540')
def ctrl_nm7540():
    return 'ret7540' 

@action('ctrl_act7541')
def ctrl_nm7541():
    return 'ret7541' 

@action('ctrl_act7542')
def ctrl_nm7542():
    return 'ret7542' 

@action('ctrl_act7543')
def ctrl_nm7543():
    return 'ret7543' 

@action('ctrl_act7544')
def ctrl_nm7544():
    return 'ret7544' 

@action('ctrl_act7545')
def ctrl_nm7545():
    return 'ret7545' 

@action('ctrl_act7546')
def ctrl_nm7546():
    return 'ret7546' 

@action('ctrl_act7547')
def ctrl_nm7547():
    return 'ret7547' 

@action('ctrl_act7548')
def ctrl_nm7548():
    return 'ret7548' 

@action('ctrl_act7549')
def ctrl_nm7549():
    return 'ret7549' 

@action('ctrl_act7550')
def ctrl_nm7550():
    return 'ret7550' 

@action('ctrl_act7551')
def ctrl_nm7551():
    return 'ret7551' 

@action('ctrl_act7552')
def ctrl_nm7552():
    return 'ret7552' 

@action('ctrl_act7553')
def ctrl_nm7553():
    return 'ret7553' 

@action('ctrl_act7554')
def ctrl_nm7554():
    return 'ret7554' 

@action('ctrl_act7555')
def ctrl_nm7555():
    return 'ret7555' 

@action('ctrl_act7556')
def ctrl_nm7556():
    return 'ret7556' 

@action('ctrl_act7557')
def ctrl_nm7557():
    return 'ret7557' 

@action('ctrl_act7558')
def ctrl_nm7558():
    return 'ret7558' 

@action('ctrl_act7559')
def ctrl_nm7559():
    return 'ret7559' 

@action('ctrl_act7560')
def ctrl_nm7560():
    return 'ret7560' 

@action('ctrl_act7561')
def ctrl_nm7561():
    return 'ret7561' 

@action('ctrl_act7562')
def ctrl_nm7562():
    return 'ret7562' 

@action('ctrl_act7563')
def ctrl_nm7563():
    return 'ret7563' 

@action('ctrl_act7564')
def ctrl_nm7564():
    return 'ret7564' 

@action('ctrl_act7565')
def ctrl_nm7565():
    return 'ret7565' 

@action('ctrl_act7566')
def ctrl_nm7566():
    return 'ret7566' 

@action('ctrl_act7567')
def ctrl_nm7567():
    return 'ret7567' 

@action('ctrl_act7568')
def ctrl_nm7568():
    return 'ret7568' 

@action('ctrl_act7569')
def ctrl_nm7569():
    return 'ret7569' 

@action('ctrl_act7570')
def ctrl_nm7570():
    return 'ret7570' 

@action('ctrl_act7571')
def ctrl_nm7571():
    return 'ret7571' 

@action('ctrl_act7572')
def ctrl_nm7572():
    return 'ret7572' 

@action('ctrl_act7573')
def ctrl_nm7573():
    return 'ret7573' 

@action('ctrl_act7574')
def ctrl_nm7574():
    return 'ret7574' 

@action('ctrl_act7575')
def ctrl_nm7575():
    return 'ret7575' 

@action('ctrl_act7576')
def ctrl_nm7576():
    return 'ret7576' 

@action('ctrl_act7577')
def ctrl_nm7577():
    return 'ret7577' 

@action('ctrl_act7578')
def ctrl_nm7578():
    return 'ret7578' 

@action('ctrl_act7579')
def ctrl_nm7579():
    return 'ret7579' 

@action('ctrl_act7580')
def ctrl_nm7580():
    return 'ret7580' 

@action('ctrl_act7581')
def ctrl_nm7581():
    return 'ret7581' 

@action('ctrl_act7582')
def ctrl_nm7582():
    return 'ret7582' 

@action('ctrl_act7583')
def ctrl_nm7583():
    return 'ret7583' 

@action('ctrl_act7584')
def ctrl_nm7584():
    return 'ret7584' 

@action('ctrl_act7585')
def ctrl_nm7585():
    return 'ret7585' 

@action('ctrl_act7586')
def ctrl_nm7586():
    return 'ret7586' 

@action('ctrl_act7587')
def ctrl_nm7587():
    return 'ret7587' 

@action('ctrl_act7588')
def ctrl_nm7588():
    return 'ret7588' 

@action('ctrl_act7589')
def ctrl_nm7589():
    return 'ret7589' 

@action('ctrl_act7590')
def ctrl_nm7590():
    return 'ret7590' 

@action('ctrl_act7591')
def ctrl_nm7591():
    return 'ret7591' 

@action('ctrl_act7592')
def ctrl_nm7592():
    return 'ret7592' 

@action('ctrl_act7593')
def ctrl_nm7593():
    return 'ret7593' 

@action('ctrl_act7594')
def ctrl_nm7594():
    return 'ret7594' 

@action('ctrl_act7595')
def ctrl_nm7595():
    return 'ret7595' 

@action('ctrl_act7596')
def ctrl_nm7596():
    return 'ret7596' 

@action('ctrl_act7597')
def ctrl_nm7597():
    return 'ret7597' 

@action('ctrl_act7598')
def ctrl_nm7598():
    return 'ret7598' 

@action('ctrl_act7599')
def ctrl_nm7599():
    return 'ret7599' 

@action('ctrl_act7600')
def ctrl_nm7600():
    return 'ret7600' 

@action('ctrl_act7601')
def ctrl_nm7601():
    return 'ret7601' 

@action('ctrl_act7602')
def ctrl_nm7602():
    return 'ret7602' 

@action('ctrl_act7603')
def ctrl_nm7603():
    return 'ret7603' 

@action('ctrl_act7604')
def ctrl_nm7604():
    return 'ret7604' 

@action('ctrl_act7605')
def ctrl_nm7605():
    return 'ret7605' 

@action('ctrl_act7606')
def ctrl_nm7606():
    return 'ret7606' 

@action('ctrl_act7607')
def ctrl_nm7607():
    return 'ret7607' 

@action('ctrl_act7608')
def ctrl_nm7608():
    return 'ret7608' 

@action('ctrl_act7609')
def ctrl_nm7609():
    return 'ret7609' 

@action('ctrl_act7610')
def ctrl_nm7610():
    return 'ret7610' 

@action('ctrl_act7611')
def ctrl_nm7611():
    return 'ret7611' 

@action('ctrl_act7612')
def ctrl_nm7612():
    return 'ret7612' 

@action('ctrl_act7613')
def ctrl_nm7613():
    return 'ret7613' 

@action('ctrl_act7614')
def ctrl_nm7614():
    return 'ret7614' 

@action('ctrl_act7615')
def ctrl_nm7615():
    return 'ret7615' 

@action('ctrl_act7616')
def ctrl_nm7616():
    return 'ret7616' 

@action('ctrl_act7617')
def ctrl_nm7617():
    return 'ret7617' 

@action('ctrl_act7618')
def ctrl_nm7618():
    return 'ret7618' 

@action('ctrl_act7619')
def ctrl_nm7619():
    return 'ret7619' 

@action('ctrl_act7620')
def ctrl_nm7620():
    return 'ret7620' 

@action('ctrl_act7621')
def ctrl_nm7621():
    return 'ret7621' 

@action('ctrl_act7622')
def ctrl_nm7622():
    return 'ret7622' 

@action('ctrl_act7623')
def ctrl_nm7623():
    return 'ret7623' 

@action('ctrl_act7624')
def ctrl_nm7624():
    return 'ret7624' 

@action('ctrl_act7625')
def ctrl_nm7625():
    return 'ret7625' 

@action('ctrl_act7626')
def ctrl_nm7626():
    return 'ret7626' 

@action('ctrl_act7627')
def ctrl_nm7627():
    return 'ret7627' 

@action('ctrl_act7628')
def ctrl_nm7628():
    return 'ret7628' 

@action('ctrl_act7629')
def ctrl_nm7629():
    return 'ret7629' 

@action('ctrl_act7630')
def ctrl_nm7630():
    return 'ret7630' 

@action('ctrl_act7631')
def ctrl_nm7631():
    return 'ret7631' 

@action('ctrl_act7632')
def ctrl_nm7632():
    return 'ret7632' 

@action('ctrl_act7633')
def ctrl_nm7633():
    return 'ret7633' 

@action('ctrl_act7634')
def ctrl_nm7634():
    return 'ret7634' 

@action('ctrl_act7635')
def ctrl_nm7635():
    return 'ret7635' 

@action('ctrl_act7636')
def ctrl_nm7636():
    return 'ret7636' 

@action('ctrl_act7637')
def ctrl_nm7637():
    return 'ret7637' 

@action('ctrl_act7638')
def ctrl_nm7638():
    return 'ret7638' 

@action('ctrl_act7639')
def ctrl_nm7639():
    return 'ret7639' 

@action('ctrl_act7640')
def ctrl_nm7640():
    return 'ret7640' 

@action('ctrl_act7641')
def ctrl_nm7641():
    return 'ret7641' 

@action('ctrl_act7642')
def ctrl_nm7642():
    return 'ret7642' 

@action('ctrl_act7643')
def ctrl_nm7643():
    return 'ret7643' 

@action('ctrl_act7644')
def ctrl_nm7644():
    return 'ret7644' 

@action('ctrl_act7645')
def ctrl_nm7645():
    return 'ret7645' 

@action('ctrl_act7646')
def ctrl_nm7646():
    return 'ret7646' 

@action('ctrl_act7647')
def ctrl_nm7647():
    return 'ret7647' 

@action('ctrl_act7648')
def ctrl_nm7648():
    return 'ret7648' 

@action('ctrl_act7649')
def ctrl_nm7649():
    return 'ret7649' 

@action('ctrl_act7650')
def ctrl_nm7650():
    return 'ret7650' 

@action('ctrl_act7651')
def ctrl_nm7651():
    return 'ret7651' 

@action('ctrl_act7652')
def ctrl_nm7652():
    return 'ret7652' 

@action('ctrl_act7653')
def ctrl_nm7653():
    return 'ret7653' 

@action('ctrl_act7654')
def ctrl_nm7654():
    return 'ret7654' 

@action('ctrl_act7655')
def ctrl_nm7655():
    return 'ret7655' 

@action('ctrl_act7656')
def ctrl_nm7656():
    return 'ret7656' 

@action('ctrl_act7657')
def ctrl_nm7657():
    return 'ret7657' 

@action('ctrl_act7658')
def ctrl_nm7658():
    return 'ret7658' 

@action('ctrl_act7659')
def ctrl_nm7659():
    return 'ret7659' 

@action('ctrl_act7660')
def ctrl_nm7660():
    return 'ret7660' 

@action('ctrl_act7661')
def ctrl_nm7661():
    return 'ret7661' 

@action('ctrl_act7662')
def ctrl_nm7662():
    return 'ret7662' 

@action('ctrl_act7663')
def ctrl_nm7663():
    return 'ret7663' 

@action('ctrl_act7664')
def ctrl_nm7664():
    return 'ret7664' 

@action('ctrl_act7665')
def ctrl_nm7665():
    return 'ret7665' 

@action('ctrl_act7666')
def ctrl_nm7666():
    return 'ret7666' 

@action('ctrl_act7667')
def ctrl_nm7667():
    return 'ret7667' 

@action('ctrl_act7668')
def ctrl_nm7668():
    return 'ret7668' 

@action('ctrl_act7669')
def ctrl_nm7669():
    return 'ret7669' 

@action('ctrl_act7670')
def ctrl_nm7670():
    return 'ret7670' 

@action('ctrl_act7671')
def ctrl_nm7671():
    return 'ret7671' 

@action('ctrl_act7672')
def ctrl_nm7672():
    return 'ret7672' 

@action('ctrl_act7673')
def ctrl_nm7673():
    return 'ret7673' 

@action('ctrl_act7674')
def ctrl_nm7674():
    return 'ret7674' 

@action('ctrl_act7675')
def ctrl_nm7675():
    return 'ret7675' 

@action('ctrl_act7676')
def ctrl_nm7676():
    return 'ret7676' 

@action('ctrl_act7677')
def ctrl_nm7677():
    return 'ret7677' 

@action('ctrl_act7678')
def ctrl_nm7678():
    return 'ret7678' 

@action('ctrl_act7679')
def ctrl_nm7679():
    return 'ret7679' 

@action('ctrl_act7680')
def ctrl_nm7680():
    return 'ret7680' 

@action('ctrl_act7681')
def ctrl_nm7681():
    return 'ret7681' 

@action('ctrl_act7682')
def ctrl_nm7682():
    return 'ret7682' 

@action('ctrl_act7683')
def ctrl_nm7683():
    return 'ret7683' 

@action('ctrl_act7684')
def ctrl_nm7684():
    return 'ret7684' 

@action('ctrl_act7685')
def ctrl_nm7685():
    return 'ret7685' 

@action('ctrl_act7686')
def ctrl_nm7686():
    return 'ret7686' 

@action('ctrl_act7687')
def ctrl_nm7687():
    return 'ret7687' 

@action('ctrl_act7688')
def ctrl_nm7688():
    return 'ret7688' 

@action('ctrl_act7689')
def ctrl_nm7689():
    return 'ret7689' 

@action('ctrl_act7690')
def ctrl_nm7690():
    return 'ret7690' 

@action('ctrl_act7691')
def ctrl_nm7691():
    return 'ret7691' 

@action('ctrl_act7692')
def ctrl_nm7692():
    return 'ret7692' 

@action('ctrl_act7693')
def ctrl_nm7693():
    return 'ret7693' 

@action('ctrl_act7694')
def ctrl_nm7694():
    return 'ret7694' 

@action('ctrl_act7695')
def ctrl_nm7695():
    return 'ret7695' 

@action('ctrl_act7696')
def ctrl_nm7696():
    return 'ret7696' 

@action('ctrl_act7697')
def ctrl_nm7697():
    return 'ret7697' 

@action('ctrl_act7698')
def ctrl_nm7698():
    return 'ret7698' 

@action('ctrl_act7699')
def ctrl_nm7699():
    return 'ret7699' 

@action('ctrl_act7700')
def ctrl_nm7700():
    return 'ret7700' 

@action('ctrl_act7701')
def ctrl_nm7701():
    return 'ret7701' 

@action('ctrl_act7702')
def ctrl_nm7702():
    return 'ret7702' 

@action('ctrl_act7703')
def ctrl_nm7703():
    return 'ret7703' 

@action('ctrl_act7704')
def ctrl_nm7704():
    return 'ret7704' 

@action('ctrl_act7705')
def ctrl_nm7705():
    return 'ret7705' 

@action('ctrl_act7706')
def ctrl_nm7706():
    return 'ret7706' 

@action('ctrl_act7707')
def ctrl_nm7707():
    return 'ret7707' 

@action('ctrl_act7708')
def ctrl_nm7708():
    return 'ret7708' 

@action('ctrl_act7709')
def ctrl_nm7709():
    return 'ret7709' 

@action('ctrl_act7710')
def ctrl_nm7710():
    return 'ret7710' 

@action('ctrl_act7711')
def ctrl_nm7711():
    return 'ret7711' 

@action('ctrl_act7712')
def ctrl_nm7712():
    return 'ret7712' 

@action('ctrl_act7713')
def ctrl_nm7713():
    return 'ret7713' 

@action('ctrl_act7714')
def ctrl_nm7714():
    return 'ret7714' 

@action('ctrl_act7715')
def ctrl_nm7715():
    return 'ret7715' 

@action('ctrl_act7716')
def ctrl_nm7716():
    return 'ret7716' 

@action('ctrl_act7717')
def ctrl_nm7717():
    return 'ret7717' 

@action('ctrl_act7718')
def ctrl_nm7718():
    return 'ret7718' 

@action('ctrl_act7719')
def ctrl_nm7719():
    return 'ret7719' 

@action('ctrl_act7720')
def ctrl_nm7720():
    return 'ret7720' 

@action('ctrl_act7721')
def ctrl_nm7721():
    return 'ret7721' 

@action('ctrl_act7722')
def ctrl_nm7722():
    return 'ret7722' 

@action('ctrl_act7723')
def ctrl_nm7723():
    return 'ret7723' 

@action('ctrl_act7724')
def ctrl_nm7724():
    return 'ret7724' 

@action('ctrl_act7725')
def ctrl_nm7725():
    return 'ret7725' 

@action('ctrl_act7726')
def ctrl_nm7726():
    return 'ret7726' 

@action('ctrl_act7727')
def ctrl_nm7727():
    return 'ret7727' 

@action('ctrl_act7728')
def ctrl_nm7728():
    return 'ret7728' 

@action('ctrl_act7729')
def ctrl_nm7729():
    return 'ret7729' 

@action('ctrl_act7730')
def ctrl_nm7730():
    return 'ret7730' 

@action('ctrl_act7731')
def ctrl_nm7731():
    return 'ret7731' 

@action('ctrl_act7732')
def ctrl_nm7732():
    return 'ret7732' 

@action('ctrl_act7733')
def ctrl_nm7733():
    return 'ret7733' 

@action('ctrl_act7734')
def ctrl_nm7734():
    return 'ret7734' 

@action('ctrl_act7735')
def ctrl_nm7735():
    return 'ret7735' 

@action('ctrl_act7736')
def ctrl_nm7736():
    return 'ret7736' 

@action('ctrl_act7737')
def ctrl_nm7737():
    return 'ret7737' 

@action('ctrl_act7738')
def ctrl_nm7738():
    return 'ret7738' 

@action('ctrl_act7739')
def ctrl_nm7739():
    return 'ret7739' 

@action('ctrl_act7740')
def ctrl_nm7740():
    return 'ret7740' 

@action('ctrl_act7741')
def ctrl_nm7741():
    return 'ret7741' 

@action('ctrl_act7742')
def ctrl_nm7742():
    return 'ret7742' 

@action('ctrl_act7743')
def ctrl_nm7743():
    return 'ret7743' 

@action('ctrl_act7744')
def ctrl_nm7744():
    return 'ret7744' 

@action('ctrl_act7745')
def ctrl_nm7745():
    return 'ret7745' 

@action('ctrl_act7746')
def ctrl_nm7746():
    return 'ret7746' 

@action('ctrl_act7747')
def ctrl_nm7747():
    return 'ret7747' 

@action('ctrl_act7748')
def ctrl_nm7748():
    return 'ret7748' 

@action('ctrl_act7749')
def ctrl_nm7749():
    return 'ret7749' 

@action('ctrl_act7750')
def ctrl_nm7750():
    return 'ret7750' 

@action('ctrl_act7751')
def ctrl_nm7751():
    return 'ret7751' 

@action('ctrl_act7752')
def ctrl_nm7752():
    return 'ret7752' 

@action('ctrl_act7753')
def ctrl_nm7753():
    return 'ret7753' 

@action('ctrl_act7754')
def ctrl_nm7754():
    return 'ret7754' 

@action('ctrl_act7755')
def ctrl_nm7755():
    return 'ret7755' 

@action('ctrl_act7756')
def ctrl_nm7756():
    return 'ret7756' 

@action('ctrl_act7757')
def ctrl_nm7757():
    return 'ret7757' 

@action('ctrl_act7758')
def ctrl_nm7758():
    return 'ret7758' 

@action('ctrl_act7759')
def ctrl_nm7759():
    return 'ret7759' 

@action('ctrl_act7760')
def ctrl_nm7760():
    return 'ret7760' 

@action('ctrl_act7761')
def ctrl_nm7761():
    return 'ret7761' 

@action('ctrl_act7762')
def ctrl_nm7762():
    return 'ret7762' 

@action('ctrl_act7763')
def ctrl_nm7763():
    return 'ret7763' 

@action('ctrl_act7764')
def ctrl_nm7764():
    return 'ret7764' 

@action('ctrl_act7765')
def ctrl_nm7765():
    return 'ret7765' 

@action('ctrl_act7766')
def ctrl_nm7766():
    return 'ret7766' 

@action('ctrl_act7767')
def ctrl_nm7767():
    return 'ret7767' 

@action('ctrl_act7768')
def ctrl_nm7768():
    return 'ret7768' 

@action('ctrl_act7769')
def ctrl_nm7769():
    return 'ret7769' 

@action('ctrl_act7770')
def ctrl_nm7770():
    return 'ret7770' 

@action('ctrl_act7771')
def ctrl_nm7771():
    return 'ret7771' 

@action('ctrl_act7772')
def ctrl_nm7772():
    return 'ret7772' 

@action('ctrl_act7773')
def ctrl_nm7773():
    return 'ret7773' 

@action('ctrl_act7774')
def ctrl_nm7774():
    return 'ret7774' 

@action('ctrl_act7775')
def ctrl_nm7775():
    return 'ret7775' 

@action('ctrl_act7776')
def ctrl_nm7776():
    return 'ret7776' 

@action('ctrl_act7777')
def ctrl_nm7777():
    return 'ret7777' 

@action('ctrl_act7778')
def ctrl_nm7778():
    return 'ret7778' 

@action('ctrl_act7779')
def ctrl_nm7779():
    return 'ret7779' 

@action('ctrl_act7780')
def ctrl_nm7780():
    return 'ret7780' 

@action('ctrl_act7781')
def ctrl_nm7781():
    return 'ret7781' 

@action('ctrl_act7782')
def ctrl_nm7782():
    return 'ret7782' 

@action('ctrl_act7783')
def ctrl_nm7783():
    return 'ret7783' 

@action('ctrl_act7784')
def ctrl_nm7784():
    return 'ret7784' 

@action('ctrl_act7785')
def ctrl_nm7785():
    return 'ret7785' 

@action('ctrl_act7786')
def ctrl_nm7786():
    return 'ret7786' 

@action('ctrl_act7787')
def ctrl_nm7787():
    return 'ret7787' 

@action('ctrl_act7788')
def ctrl_nm7788():
    return 'ret7788' 

@action('ctrl_act7789')
def ctrl_nm7789():
    return 'ret7789' 

@action('ctrl_act7790')
def ctrl_nm7790():
    return 'ret7790' 

@action('ctrl_act7791')
def ctrl_nm7791():
    return 'ret7791' 

@action('ctrl_act7792')
def ctrl_nm7792():
    return 'ret7792' 

@action('ctrl_act7793')
def ctrl_nm7793():
    return 'ret7793' 

@action('ctrl_act7794')
def ctrl_nm7794():
    return 'ret7794' 

@action('ctrl_act7795')
def ctrl_nm7795():
    return 'ret7795' 

@action('ctrl_act7796')
def ctrl_nm7796():
    return 'ret7796' 

@action('ctrl_act7797')
def ctrl_nm7797():
    return 'ret7797' 

@action('ctrl_act7798')
def ctrl_nm7798():
    return 'ret7798' 

@action('ctrl_act7799')
def ctrl_nm7799():
    return 'ret7799' 

@action('ctrl_act7800')
def ctrl_nm7800():
    return 'ret7800' 

@action('ctrl_act7801')
def ctrl_nm7801():
    return 'ret7801' 

@action('ctrl_act7802')
def ctrl_nm7802():
    return 'ret7802' 

@action('ctrl_act7803')
def ctrl_nm7803():
    return 'ret7803' 

@action('ctrl_act7804')
def ctrl_nm7804():
    return 'ret7804' 

@action('ctrl_act7805')
def ctrl_nm7805():
    return 'ret7805' 

@action('ctrl_act7806')
def ctrl_nm7806():
    return 'ret7806' 

@action('ctrl_act7807')
def ctrl_nm7807():
    return 'ret7807' 

@action('ctrl_act7808')
def ctrl_nm7808():
    return 'ret7808' 

@action('ctrl_act7809')
def ctrl_nm7809():
    return 'ret7809' 

@action('ctrl_act7810')
def ctrl_nm7810():
    return 'ret7810' 

@action('ctrl_act7811')
def ctrl_nm7811():
    return 'ret7811' 

@action('ctrl_act7812')
def ctrl_nm7812():
    return 'ret7812' 

@action('ctrl_act7813')
def ctrl_nm7813():
    return 'ret7813' 

@action('ctrl_act7814')
def ctrl_nm7814():
    return 'ret7814' 

@action('ctrl_act7815')
def ctrl_nm7815():
    return 'ret7815' 

@action('ctrl_act7816')
def ctrl_nm7816():
    return 'ret7816' 

@action('ctrl_act7817')
def ctrl_nm7817():
    return 'ret7817' 

@action('ctrl_act7818')
def ctrl_nm7818():
    return 'ret7818' 

@action('ctrl_act7819')
def ctrl_nm7819():
    return 'ret7819' 

@action('ctrl_act7820')
def ctrl_nm7820():
    return 'ret7820' 

@action('ctrl_act7821')
def ctrl_nm7821():
    return 'ret7821' 

@action('ctrl_act7822')
def ctrl_nm7822():
    return 'ret7822' 

@action('ctrl_act7823')
def ctrl_nm7823():
    return 'ret7823' 

@action('ctrl_act7824')
def ctrl_nm7824():
    return 'ret7824' 

@action('ctrl_act7825')
def ctrl_nm7825():
    return 'ret7825' 

@action('ctrl_act7826')
def ctrl_nm7826():
    return 'ret7826' 

@action('ctrl_act7827')
def ctrl_nm7827():
    return 'ret7827' 

@action('ctrl_act7828')
def ctrl_nm7828():
    return 'ret7828' 

@action('ctrl_act7829')
def ctrl_nm7829():
    return 'ret7829' 

@action('ctrl_act7830')
def ctrl_nm7830():
    return 'ret7830' 

@action('ctrl_act7831')
def ctrl_nm7831():
    return 'ret7831' 

@action('ctrl_act7832')
def ctrl_nm7832():
    return 'ret7832' 

@action('ctrl_act7833')
def ctrl_nm7833():
    return 'ret7833' 

@action('ctrl_act7834')
def ctrl_nm7834():
    return 'ret7834' 

@action('ctrl_act7835')
def ctrl_nm7835():
    return 'ret7835' 

@action('ctrl_act7836')
def ctrl_nm7836():
    return 'ret7836' 

@action('ctrl_act7837')
def ctrl_nm7837():
    return 'ret7837' 

@action('ctrl_act7838')
def ctrl_nm7838():
    return 'ret7838' 

@action('ctrl_act7839')
def ctrl_nm7839():
    return 'ret7839' 

@action('ctrl_act7840')
def ctrl_nm7840():
    return 'ret7840' 

@action('ctrl_act7841')
def ctrl_nm7841():
    return 'ret7841' 

@action('ctrl_act7842')
def ctrl_nm7842():
    return 'ret7842' 

@action('ctrl_act7843')
def ctrl_nm7843():
    return 'ret7843' 

@action('ctrl_act7844')
def ctrl_nm7844():
    return 'ret7844' 

@action('ctrl_act7845')
def ctrl_nm7845():
    return 'ret7845' 

@action('ctrl_act7846')
def ctrl_nm7846():
    return 'ret7846' 

@action('ctrl_act7847')
def ctrl_nm7847():
    return 'ret7847' 

@action('ctrl_act7848')
def ctrl_nm7848():
    return 'ret7848' 

@action('ctrl_act7849')
def ctrl_nm7849():
    return 'ret7849' 

@action('ctrl_act7850')
def ctrl_nm7850():
    return 'ret7850' 

@action('ctrl_act7851')
def ctrl_nm7851():
    return 'ret7851' 

@action('ctrl_act7852')
def ctrl_nm7852():
    return 'ret7852' 

@action('ctrl_act7853')
def ctrl_nm7853():
    return 'ret7853' 

@action('ctrl_act7854')
def ctrl_nm7854():
    return 'ret7854' 

@action('ctrl_act7855')
def ctrl_nm7855():
    return 'ret7855' 

@action('ctrl_act7856')
def ctrl_nm7856():
    return 'ret7856' 

@action('ctrl_act7857')
def ctrl_nm7857():
    return 'ret7857' 

@action('ctrl_act7858')
def ctrl_nm7858():
    return 'ret7858' 

@action('ctrl_act7859')
def ctrl_nm7859():
    return 'ret7859' 

@action('ctrl_act7860')
def ctrl_nm7860():
    return 'ret7860' 

@action('ctrl_act7861')
def ctrl_nm7861():
    return 'ret7861' 

@action('ctrl_act7862')
def ctrl_nm7862():
    return 'ret7862' 

@action('ctrl_act7863')
def ctrl_nm7863():
    return 'ret7863' 

@action('ctrl_act7864')
def ctrl_nm7864():
    return 'ret7864' 

@action('ctrl_act7865')
def ctrl_nm7865():
    return 'ret7865' 

@action('ctrl_act7866')
def ctrl_nm7866():
    return 'ret7866' 

@action('ctrl_act7867')
def ctrl_nm7867():
    return 'ret7867' 

@action('ctrl_act7868')
def ctrl_nm7868():
    return 'ret7868' 

@action('ctrl_act7869')
def ctrl_nm7869():
    return 'ret7869' 

@action('ctrl_act7870')
def ctrl_nm7870():
    return 'ret7870' 

@action('ctrl_act7871')
def ctrl_nm7871():
    return 'ret7871' 

@action('ctrl_act7872')
def ctrl_nm7872():
    return 'ret7872' 

@action('ctrl_act7873')
def ctrl_nm7873():
    return 'ret7873' 

@action('ctrl_act7874')
def ctrl_nm7874():
    return 'ret7874' 

@action('ctrl_act7875')
def ctrl_nm7875():
    return 'ret7875' 

@action('ctrl_act7876')
def ctrl_nm7876():
    return 'ret7876' 

@action('ctrl_act7877')
def ctrl_nm7877():
    return 'ret7877' 

@action('ctrl_act7878')
def ctrl_nm7878():
    return 'ret7878' 

@action('ctrl_act7879')
def ctrl_nm7879():
    return 'ret7879' 

@action('ctrl_act7880')
def ctrl_nm7880():
    return 'ret7880' 

@action('ctrl_act7881')
def ctrl_nm7881():
    return 'ret7881' 

@action('ctrl_act7882')
def ctrl_nm7882():
    return 'ret7882' 

@action('ctrl_act7883')
def ctrl_nm7883():
    return 'ret7883' 

@action('ctrl_act7884')
def ctrl_nm7884():
    return 'ret7884' 

@action('ctrl_act7885')
def ctrl_nm7885():
    return 'ret7885' 

@action('ctrl_act7886')
def ctrl_nm7886():
    return 'ret7886' 

@action('ctrl_act7887')
def ctrl_nm7887():
    return 'ret7887' 

@action('ctrl_act7888')
def ctrl_nm7888():
    return 'ret7888' 

@action('ctrl_act7889')
def ctrl_nm7889():
    return 'ret7889' 

@action('ctrl_act7890')
def ctrl_nm7890():
    return 'ret7890' 

@action('ctrl_act7891')
def ctrl_nm7891():
    return 'ret7891' 

@action('ctrl_act7892')
def ctrl_nm7892():
    return 'ret7892' 

@action('ctrl_act7893')
def ctrl_nm7893():
    return 'ret7893' 

@action('ctrl_act7894')
def ctrl_nm7894():
    return 'ret7894' 

@action('ctrl_act7895')
def ctrl_nm7895():
    return 'ret7895' 

@action('ctrl_act7896')
def ctrl_nm7896():
    return 'ret7896' 

@action('ctrl_act7897')
def ctrl_nm7897():
    return 'ret7897' 

@action('ctrl_act7898')
def ctrl_nm7898():
    return 'ret7898' 

@action('ctrl_act7899')
def ctrl_nm7899():
    return 'ret7899' 

@action('ctrl_act7900')
def ctrl_nm7900():
    return 'ret7900' 

@action('ctrl_act7901')
def ctrl_nm7901():
    return 'ret7901' 

@action('ctrl_act7902')
def ctrl_nm7902():
    return 'ret7902' 

@action('ctrl_act7903')
def ctrl_nm7903():
    return 'ret7903' 

@action('ctrl_act7904')
def ctrl_nm7904():
    return 'ret7904' 

@action('ctrl_act7905')
def ctrl_nm7905():
    return 'ret7905' 

@action('ctrl_act7906')
def ctrl_nm7906():
    return 'ret7906' 

@action('ctrl_act7907')
def ctrl_nm7907():
    return 'ret7907' 

@action('ctrl_act7908')
def ctrl_nm7908():
    return 'ret7908' 

@action('ctrl_act7909')
def ctrl_nm7909():
    return 'ret7909' 

@action('ctrl_act7910')
def ctrl_nm7910():
    return 'ret7910' 

@action('ctrl_act7911')
def ctrl_nm7911():
    return 'ret7911' 

@action('ctrl_act7912')
def ctrl_nm7912():
    return 'ret7912' 

@action('ctrl_act7913')
def ctrl_nm7913():
    return 'ret7913' 

@action('ctrl_act7914')
def ctrl_nm7914():
    return 'ret7914' 

@action('ctrl_act7915')
def ctrl_nm7915():
    return 'ret7915' 

@action('ctrl_act7916')
def ctrl_nm7916():
    return 'ret7916' 

@action('ctrl_act7917')
def ctrl_nm7917():
    return 'ret7917' 

@action('ctrl_act7918')
def ctrl_nm7918():
    return 'ret7918' 

@action('ctrl_act7919')
def ctrl_nm7919():
    return 'ret7919' 

@action('ctrl_act7920')
def ctrl_nm7920():
    return 'ret7920' 

@action('ctrl_act7921')
def ctrl_nm7921():
    return 'ret7921' 

@action('ctrl_act7922')
def ctrl_nm7922():
    return 'ret7922' 

@action('ctrl_act7923')
def ctrl_nm7923():
    return 'ret7923' 

@action('ctrl_act7924')
def ctrl_nm7924():
    return 'ret7924' 

@action('ctrl_act7925')
def ctrl_nm7925():
    return 'ret7925' 

@action('ctrl_act7926')
def ctrl_nm7926():
    return 'ret7926' 

@action('ctrl_act7927')
def ctrl_nm7927():
    return 'ret7927' 

@action('ctrl_act7928')
def ctrl_nm7928():
    return 'ret7928' 

@action('ctrl_act7929')
def ctrl_nm7929():
    return 'ret7929' 

@action('ctrl_act7930')
def ctrl_nm7930():
    return 'ret7930' 

@action('ctrl_act7931')
def ctrl_nm7931():
    return 'ret7931' 

@action('ctrl_act7932')
def ctrl_nm7932():
    return 'ret7932' 

@action('ctrl_act7933')
def ctrl_nm7933():
    return 'ret7933' 

@action('ctrl_act7934')
def ctrl_nm7934():
    return 'ret7934' 

@action('ctrl_act7935')
def ctrl_nm7935():
    return 'ret7935' 

@action('ctrl_act7936')
def ctrl_nm7936():
    return 'ret7936' 

@action('ctrl_act7937')
def ctrl_nm7937():
    return 'ret7937' 

@action('ctrl_act7938')
def ctrl_nm7938():
    return 'ret7938' 

@action('ctrl_act7939')
def ctrl_nm7939():
    return 'ret7939' 

@action('ctrl_act7940')
def ctrl_nm7940():
    return 'ret7940' 

@action('ctrl_act7941')
def ctrl_nm7941():
    return 'ret7941' 

@action('ctrl_act7942')
def ctrl_nm7942():
    return 'ret7942' 

@action('ctrl_act7943')
def ctrl_nm7943():
    return 'ret7943' 

@action('ctrl_act7944')
def ctrl_nm7944():
    return 'ret7944' 

@action('ctrl_act7945')
def ctrl_nm7945():
    return 'ret7945' 

@action('ctrl_act7946')
def ctrl_nm7946():
    return 'ret7946' 

@action('ctrl_act7947')
def ctrl_nm7947():
    return 'ret7947' 

@action('ctrl_act7948')
def ctrl_nm7948():
    return 'ret7948' 

@action('ctrl_act7949')
def ctrl_nm7949():
    return 'ret7949' 

@action('ctrl_act7950')
def ctrl_nm7950():
    return 'ret7950' 

@action('ctrl_act7951')
def ctrl_nm7951():
    return 'ret7951' 

@action('ctrl_act7952')
def ctrl_nm7952():
    return 'ret7952' 

@action('ctrl_act7953')
def ctrl_nm7953():
    return 'ret7953' 

@action('ctrl_act7954')
def ctrl_nm7954():
    return 'ret7954' 

@action('ctrl_act7955')
def ctrl_nm7955():
    return 'ret7955' 

@action('ctrl_act7956')
def ctrl_nm7956():
    return 'ret7956' 

@action('ctrl_act7957')
def ctrl_nm7957():
    return 'ret7957' 

@action('ctrl_act7958')
def ctrl_nm7958():
    return 'ret7958' 

@action('ctrl_act7959')
def ctrl_nm7959():
    return 'ret7959' 

@action('ctrl_act7960')
def ctrl_nm7960():
    return 'ret7960' 

@action('ctrl_act7961')
def ctrl_nm7961():
    return 'ret7961' 

@action('ctrl_act7962')
def ctrl_nm7962():
    return 'ret7962' 

@action('ctrl_act7963')
def ctrl_nm7963():
    return 'ret7963' 

@action('ctrl_act7964')
def ctrl_nm7964():
    return 'ret7964' 

@action('ctrl_act7965')
def ctrl_nm7965():
    return 'ret7965' 

@action('ctrl_act7966')
def ctrl_nm7966():
    return 'ret7966' 

@action('ctrl_act7967')
def ctrl_nm7967():
    return 'ret7967' 

@action('ctrl_act7968')
def ctrl_nm7968():
    return 'ret7968' 

@action('ctrl_act7969')
def ctrl_nm7969():
    return 'ret7969' 

@action('ctrl_act7970')
def ctrl_nm7970():
    return 'ret7970' 

@action('ctrl_act7971')
def ctrl_nm7971():
    return 'ret7971' 

@action('ctrl_act7972')
def ctrl_nm7972():
    return 'ret7972' 

@action('ctrl_act7973')
def ctrl_nm7973():
    return 'ret7973' 

@action('ctrl_act7974')
def ctrl_nm7974():
    return 'ret7974' 

@action('ctrl_act7975')
def ctrl_nm7975():
    return 'ret7975' 

@action('ctrl_act7976')
def ctrl_nm7976():
    return 'ret7976' 

@action('ctrl_act7977')
def ctrl_nm7977():
    return 'ret7977' 

@action('ctrl_act7978')
def ctrl_nm7978():
    return 'ret7978' 

@action('ctrl_act7979')
def ctrl_nm7979():
    return 'ret7979' 

@action('ctrl_act7980')
def ctrl_nm7980():
    return 'ret7980' 

@action('ctrl_act7981')
def ctrl_nm7981():
    return 'ret7981' 

@action('ctrl_act7982')
def ctrl_nm7982():
    return 'ret7982' 

@action('ctrl_act7983')
def ctrl_nm7983():
    return 'ret7983' 

@action('ctrl_act7984')
def ctrl_nm7984():
    return 'ret7984' 

@action('ctrl_act7985')
def ctrl_nm7985():
    return 'ret7985' 

@action('ctrl_act7986')
def ctrl_nm7986():
    return 'ret7986' 

@action('ctrl_act7987')
def ctrl_nm7987():
    return 'ret7987' 

@action('ctrl_act7988')
def ctrl_nm7988():
    return 'ret7988' 

@action('ctrl_act7989')
def ctrl_nm7989():
    return 'ret7989' 

@action('ctrl_act7990')
def ctrl_nm7990():
    return 'ret7990' 

@action('ctrl_act7991')
def ctrl_nm7991():
    return 'ret7991' 

@action('ctrl_act7992')
def ctrl_nm7992():
    return 'ret7992' 

@action('ctrl_act7993')
def ctrl_nm7993():
    return 'ret7993' 

@action('ctrl_act7994')
def ctrl_nm7994():
    return 'ret7994' 

@action('ctrl_act7995')
def ctrl_nm7995():
    return 'ret7995' 

@action('ctrl_act7996')
def ctrl_nm7996():
    return 'ret7996' 

@action('ctrl_act7997')
def ctrl_nm7997():
    return 'ret7997' 

@action('ctrl_act7998')
def ctrl_nm7998():
    return 'ret7998' 

@action('ctrl_act7999')
def ctrl_nm7999():
    return 'ret7999' 

@action('ctrl_act8000')
def ctrl_nm8000():
    return 'ret8000' 

@action('ctrl_act8001')
def ctrl_nm8001():
    return 'ret8001' 

@action('ctrl_act8002')
def ctrl_nm8002():
    return 'ret8002' 

@action('ctrl_act8003')
def ctrl_nm8003():
    return 'ret8003' 

@action('ctrl_act8004')
def ctrl_nm8004():
    return 'ret8004' 

@action('ctrl_act8005')
def ctrl_nm8005():
    return 'ret8005' 

@action('ctrl_act8006')
def ctrl_nm8006():
    return 'ret8006' 

@action('ctrl_act8007')
def ctrl_nm8007():
    return 'ret8007' 

@action('ctrl_act8008')
def ctrl_nm8008():
    return 'ret8008' 

@action('ctrl_act8009')
def ctrl_nm8009():
    return 'ret8009' 

@action('ctrl_act8010')
def ctrl_nm8010():
    return 'ret8010' 

@action('ctrl_act8011')
def ctrl_nm8011():
    return 'ret8011' 

@action('ctrl_act8012')
def ctrl_nm8012():
    return 'ret8012' 

@action('ctrl_act8013')
def ctrl_nm8013():
    return 'ret8013' 

@action('ctrl_act8014')
def ctrl_nm8014():
    return 'ret8014' 

@action('ctrl_act8015')
def ctrl_nm8015():
    return 'ret8015' 

@action('ctrl_act8016')
def ctrl_nm8016():
    return 'ret8016' 

@action('ctrl_act8017')
def ctrl_nm8017():
    return 'ret8017' 

@action('ctrl_act8018')
def ctrl_nm8018():
    return 'ret8018' 

@action('ctrl_act8019')
def ctrl_nm8019():
    return 'ret8019' 

@action('ctrl_act8020')
def ctrl_nm8020():
    return 'ret8020' 

@action('ctrl_act8021')
def ctrl_nm8021():
    return 'ret8021' 

@action('ctrl_act8022')
def ctrl_nm8022():
    return 'ret8022' 

@action('ctrl_act8023')
def ctrl_nm8023():
    return 'ret8023' 

@action('ctrl_act8024')
def ctrl_nm8024():
    return 'ret8024' 

@action('ctrl_act8025')
def ctrl_nm8025():
    return 'ret8025' 

@action('ctrl_act8026')
def ctrl_nm8026():
    return 'ret8026' 

@action('ctrl_act8027')
def ctrl_nm8027():
    return 'ret8027' 

@action('ctrl_act8028')
def ctrl_nm8028():
    return 'ret8028' 

@action('ctrl_act8029')
def ctrl_nm8029():
    return 'ret8029' 

@action('ctrl_act8030')
def ctrl_nm8030():
    return 'ret8030' 

@action('ctrl_act8031')
def ctrl_nm8031():
    return 'ret8031' 

@action('ctrl_act8032')
def ctrl_nm8032():
    return 'ret8032' 

@action('ctrl_act8033')
def ctrl_nm8033():
    return 'ret8033' 

@action('ctrl_act8034')
def ctrl_nm8034():
    return 'ret8034' 

@action('ctrl_act8035')
def ctrl_nm8035():
    return 'ret8035' 

@action('ctrl_act8036')
def ctrl_nm8036():
    return 'ret8036' 

@action('ctrl_act8037')
def ctrl_nm8037():
    return 'ret8037' 

@action('ctrl_act8038')
def ctrl_nm8038():
    return 'ret8038' 

@action('ctrl_act8039')
def ctrl_nm8039():
    return 'ret8039' 

@action('ctrl_act8040')
def ctrl_nm8040():
    return 'ret8040' 

@action('ctrl_act8041')
def ctrl_nm8041():
    return 'ret8041' 

@action('ctrl_act8042')
def ctrl_nm8042():
    return 'ret8042' 

@action('ctrl_act8043')
def ctrl_nm8043():
    return 'ret8043' 

@action('ctrl_act8044')
def ctrl_nm8044():
    return 'ret8044' 

@action('ctrl_act8045')
def ctrl_nm8045():
    return 'ret8045' 

@action('ctrl_act8046')
def ctrl_nm8046():
    return 'ret8046' 

@action('ctrl_act8047')
def ctrl_nm8047():
    return 'ret8047' 

@action('ctrl_act8048')
def ctrl_nm8048():
    return 'ret8048' 

@action('ctrl_act8049')
def ctrl_nm8049():
    return 'ret8049' 

@action('ctrl_act8050')
def ctrl_nm8050():
    return 'ret8050' 

@action('ctrl_act8051')
def ctrl_nm8051():
    return 'ret8051' 

@action('ctrl_act8052')
def ctrl_nm8052():
    return 'ret8052' 

@action('ctrl_act8053')
def ctrl_nm8053():
    return 'ret8053' 

@action('ctrl_act8054')
def ctrl_nm8054():
    return 'ret8054' 

@action('ctrl_act8055')
def ctrl_nm8055():
    return 'ret8055' 

@action('ctrl_act8056')
def ctrl_nm8056():
    return 'ret8056' 

@action('ctrl_act8057')
def ctrl_nm8057():
    return 'ret8057' 

@action('ctrl_act8058')
def ctrl_nm8058():
    return 'ret8058' 

@action('ctrl_act8059')
def ctrl_nm8059():
    return 'ret8059' 

@action('ctrl_act8060')
def ctrl_nm8060():
    return 'ret8060' 

@action('ctrl_act8061')
def ctrl_nm8061():
    return 'ret8061' 

@action('ctrl_act8062')
def ctrl_nm8062():
    return 'ret8062' 

@action('ctrl_act8063')
def ctrl_nm8063():
    return 'ret8063' 

@action('ctrl_act8064')
def ctrl_nm8064():
    return 'ret8064' 

@action('ctrl_act8065')
def ctrl_nm8065():
    return 'ret8065' 

@action('ctrl_act8066')
def ctrl_nm8066():
    return 'ret8066' 

@action('ctrl_act8067')
def ctrl_nm8067():
    return 'ret8067' 

@action('ctrl_act8068')
def ctrl_nm8068():
    return 'ret8068' 

@action('ctrl_act8069')
def ctrl_nm8069():
    return 'ret8069' 

@action('ctrl_act8070')
def ctrl_nm8070():
    return 'ret8070' 

@action('ctrl_act8071')
def ctrl_nm8071():
    return 'ret8071' 

@action('ctrl_act8072')
def ctrl_nm8072():
    return 'ret8072' 

@action('ctrl_act8073')
def ctrl_nm8073():
    return 'ret8073' 

@action('ctrl_act8074')
def ctrl_nm8074():
    return 'ret8074' 

@action('ctrl_act8075')
def ctrl_nm8075():
    return 'ret8075' 

@action('ctrl_act8076')
def ctrl_nm8076():
    return 'ret8076' 

@action('ctrl_act8077')
def ctrl_nm8077():
    return 'ret8077' 

@action('ctrl_act8078')
def ctrl_nm8078():
    return 'ret8078' 

@action('ctrl_act8079')
def ctrl_nm8079():
    return 'ret8079' 

@action('ctrl_act8080')
def ctrl_nm8080():
    return 'ret8080' 

@action('ctrl_act8081')
def ctrl_nm8081():
    return 'ret8081' 

@action('ctrl_act8082')
def ctrl_nm8082():
    return 'ret8082' 

@action('ctrl_act8083')
def ctrl_nm8083():
    return 'ret8083' 

@action('ctrl_act8084')
def ctrl_nm8084():
    return 'ret8084' 

@action('ctrl_act8085')
def ctrl_nm8085():
    return 'ret8085' 

@action('ctrl_act8086')
def ctrl_nm8086():
    return 'ret8086' 

@action('ctrl_act8087')
def ctrl_nm8087():
    return 'ret8087' 

@action('ctrl_act8088')
def ctrl_nm8088():
    return 'ret8088' 

@action('ctrl_act8089')
def ctrl_nm8089():
    return 'ret8089' 

@action('ctrl_act8090')
def ctrl_nm8090():
    return 'ret8090' 

@action('ctrl_act8091')
def ctrl_nm8091():
    return 'ret8091' 

@action('ctrl_act8092')
def ctrl_nm8092():
    return 'ret8092' 

@action('ctrl_act8093')
def ctrl_nm8093():
    return 'ret8093' 

@action('ctrl_act8094')
def ctrl_nm8094():
    return 'ret8094' 

@action('ctrl_act8095')
def ctrl_nm8095():
    return 'ret8095' 

@action('ctrl_act8096')
def ctrl_nm8096():
    return 'ret8096' 

@action('ctrl_act8097')
def ctrl_nm8097():
    return 'ret8097' 

@action('ctrl_act8098')
def ctrl_nm8098():
    return 'ret8098' 

@action('ctrl_act8099')
def ctrl_nm8099():
    return 'ret8099' 

@action('ctrl_act8100')
def ctrl_nm8100():
    return 'ret8100' 

@action('ctrl_act8101')
def ctrl_nm8101():
    return 'ret8101' 

@action('ctrl_act8102')
def ctrl_nm8102():
    return 'ret8102' 

@action('ctrl_act8103')
def ctrl_nm8103():
    return 'ret8103' 

@action('ctrl_act8104')
def ctrl_nm8104():
    return 'ret8104' 

@action('ctrl_act8105')
def ctrl_nm8105():
    return 'ret8105' 

@action('ctrl_act8106')
def ctrl_nm8106():
    return 'ret8106' 

@action('ctrl_act8107')
def ctrl_nm8107():
    return 'ret8107' 

@action('ctrl_act8108')
def ctrl_nm8108():
    return 'ret8108' 

@action('ctrl_act8109')
def ctrl_nm8109():
    return 'ret8109' 

@action('ctrl_act8110')
def ctrl_nm8110():
    return 'ret8110' 

@action('ctrl_act8111')
def ctrl_nm8111():
    return 'ret8111' 

@action('ctrl_act8112')
def ctrl_nm8112():
    return 'ret8112' 

@action('ctrl_act8113')
def ctrl_nm8113():
    return 'ret8113' 

@action('ctrl_act8114')
def ctrl_nm8114():
    return 'ret8114' 

@action('ctrl_act8115')
def ctrl_nm8115():
    return 'ret8115' 

@action('ctrl_act8116')
def ctrl_nm8116():
    return 'ret8116' 

@action('ctrl_act8117')
def ctrl_nm8117():
    return 'ret8117' 

@action('ctrl_act8118')
def ctrl_nm8118():
    return 'ret8118' 

@action('ctrl_act8119')
def ctrl_nm8119():
    return 'ret8119' 

@action('ctrl_act8120')
def ctrl_nm8120():
    return 'ret8120' 

@action('ctrl_act8121')
def ctrl_nm8121():
    return 'ret8121' 

@action('ctrl_act8122')
def ctrl_nm8122():
    return 'ret8122' 

@action('ctrl_act8123')
def ctrl_nm8123():
    return 'ret8123' 

@action('ctrl_act8124')
def ctrl_nm8124():
    return 'ret8124' 

@action('ctrl_act8125')
def ctrl_nm8125():
    return 'ret8125' 

@action('ctrl_act8126')
def ctrl_nm8126():
    return 'ret8126' 

@action('ctrl_act8127')
def ctrl_nm8127():
    return 'ret8127' 

@action('ctrl_act8128')
def ctrl_nm8128():
    return 'ret8128' 

@action('ctrl_act8129')
def ctrl_nm8129():
    return 'ret8129' 

@action('ctrl_act8130')
def ctrl_nm8130():
    return 'ret8130' 

@action('ctrl_act8131')
def ctrl_nm8131():
    return 'ret8131' 

@action('ctrl_act8132')
def ctrl_nm8132():
    return 'ret8132' 

@action('ctrl_act8133')
def ctrl_nm8133():
    return 'ret8133' 

@action('ctrl_act8134')
def ctrl_nm8134():
    return 'ret8134' 

@action('ctrl_act8135')
def ctrl_nm8135():
    return 'ret8135' 

@action('ctrl_act8136')
def ctrl_nm8136():
    return 'ret8136' 

@action('ctrl_act8137')
def ctrl_nm8137():
    return 'ret8137' 

@action('ctrl_act8138')
def ctrl_nm8138():
    return 'ret8138' 

@action('ctrl_act8139')
def ctrl_nm8139():
    return 'ret8139' 

@action('ctrl_act8140')
def ctrl_nm8140():
    return 'ret8140' 

@action('ctrl_act8141')
def ctrl_nm8141():
    return 'ret8141' 

@action('ctrl_act8142')
def ctrl_nm8142():
    return 'ret8142' 

@action('ctrl_act8143')
def ctrl_nm8143():
    return 'ret8143' 

@action('ctrl_act8144')
def ctrl_nm8144():
    return 'ret8144' 

@action('ctrl_act8145')
def ctrl_nm8145():
    return 'ret8145' 

@action('ctrl_act8146')
def ctrl_nm8146():
    return 'ret8146' 

@action('ctrl_act8147')
def ctrl_nm8147():
    return 'ret8147' 

@action('ctrl_act8148')
def ctrl_nm8148():
    return 'ret8148' 

@action('ctrl_act8149')
def ctrl_nm8149():
    return 'ret8149' 

@action('ctrl_act8150')
def ctrl_nm8150():
    return 'ret8150' 

@action('ctrl_act8151')
def ctrl_nm8151():
    return 'ret8151' 

@action('ctrl_act8152')
def ctrl_nm8152():
    return 'ret8152' 

@action('ctrl_act8153')
def ctrl_nm8153():
    return 'ret8153' 

@action('ctrl_act8154')
def ctrl_nm8154():
    return 'ret8154' 

@action('ctrl_act8155')
def ctrl_nm8155():
    return 'ret8155' 

@action('ctrl_act8156')
def ctrl_nm8156():
    return 'ret8156' 

@action('ctrl_act8157')
def ctrl_nm8157():
    return 'ret8157' 

@action('ctrl_act8158')
def ctrl_nm8158():
    return 'ret8158' 

@action('ctrl_act8159')
def ctrl_nm8159():
    return 'ret8159' 

@action('ctrl_act8160')
def ctrl_nm8160():
    return 'ret8160' 

@action('ctrl_act8161')
def ctrl_nm8161():
    return 'ret8161' 

@action('ctrl_act8162')
def ctrl_nm8162():
    return 'ret8162' 

@action('ctrl_act8163')
def ctrl_nm8163():
    return 'ret8163' 

@action('ctrl_act8164')
def ctrl_nm8164():
    return 'ret8164' 

@action('ctrl_act8165')
def ctrl_nm8165():
    return 'ret8165' 

@action('ctrl_act8166')
def ctrl_nm8166():
    return 'ret8166' 

@action('ctrl_act8167')
def ctrl_nm8167():
    return 'ret8167' 

@action('ctrl_act8168')
def ctrl_nm8168():
    return 'ret8168' 

@action('ctrl_act8169')
def ctrl_nm8169():
    return 'ret8169' 

@action('ctrl_act8170')
def ctrl_nm8170():
    return 'ret8170' 

@action('ctrl_act8171')
def ctrl_nm8171():
    return 'ret8171' 

@action('ctrl_act8172')
def ctrl_nm8172():
    return 'ret8172' 

@action('ctrl_act8173')
def ctrl_nm8173():
    return 'ret8173' 

@action('ctrl_act8174')
def ctrl_nm8174():
    return 'ret8174' 

@action('ctrl_act8175')
def ctrl_nm8175():
    return 'ret8175' 

@action('ctrl_act8176')
def ctrl_nm8176():
    return 'ret8176' 

@action('ctrl_act8177')
def ctrl_nm8177():
    return 'ret8177' 

@action('ctrl_act8178')
def ctrl_nm8178():
    return 'ret8178' 

@action('ctrl_act8179')
def ctrl_nm8179():
    return 'ret8179' 

@action('ctrl_act8180')
def ctrl_nm8180():
    return 'ret8180' 

@action('ctrl_act8181')
def ctrl_nm8181():
    return 'ret8181' 

@action('ctrl_act8182')
def ctrl_nm8182():
    return 'ret8182' 

@action('ctrl_act8183')
def ctrl_nm8183():
    return 'ret8183' 

@action('ctrl_act8184')
def ctrl_nm8184():
    return 'ret8184' 

@action('ctrl_act8185')
def ctrl_nm8185():
    return 'ret8185' 

@action('ctrl_act8186')
def ctrl_nm8186():
    return 'ret8186' 

@action('ctrl_act8187')
def ctrl_nm8187():
    return 'ret8187' 

@action('ctrl_act8188')
def ctrl_nm8188():
    return 'ret8188' 

@action('ctrl_act8189')
def ctrl_nm8189():
    return 'ret8189' 

@action('ctrl_act8190')
def ctrl_nm8190():
    return 'ret8190' 

@action('ctrl_act8191')
def ctrl_nm8191():
    return 'ret8191' 

@action('ctrl_act8192')
def ctrl_nm8192():
    return 'ret8192' 

@action('ctrl_act8193')
def ctrl_nm8193():
    return 'ret8193' 

@action('ctrl_act8194')
def ctrl_nm8194():
    return 'ret8194' 

@action('ctrl_act8195')
def ctrl_nm8195():
    return 'ret8195' 

@action('ctrl_act8196')
def ctrl_nm8196():
    return 'ret8196' 

@action('ctrl_act8197')
def ctrl_nm8197():
    return 'ret8197' 

@action('ctrl_act8198')
def ctrl_nm8198():
    return 'ret8198' 

@action('ctrl_act8199')
def ctrl_nm8199():
    return 'ret8199' 

@action('ctrl_act8200')
def ctrl_nm8200():
    return 'ret8200' 

@action('ctrl_act8201')
def ctrl_nm8201():
    return 'ret8201' 

@action('ctrl_act8202')
def ctrl_nm8202():
    return 'ret8202' 

@action('ctrl_act8203')
def ctrl_nm8203():
    return 'ret8203' 

@action('ctrl_act8204')
def ctrl_nm8204():
    return 'ret8204' 

@action('ctrl_act8205')
def ctrl_nm8205():
    return 'ret8205' 

@action('ctrl_act8206')
def ctrl_nm8206():
    return 'ret8206' 

@action('ctrl_act8207')
def ctrl_nm8207():
    return 'ret8207' 

@action('ctrl_act8208')
def ctrl_nm8208():
    return 'ret8208' 

@action('ctrl_act8209')
def ctrl_nm8209():
    return 'ret8209' 

@action('ctrl_act8210')
def ctrl_nm8210():
    return 'ret8210' 

@action('ctrl_act8211')
def ctrl_nm8211():
    return 'ret8211' 

@action('ctrl_act8212')
def ctrl_nm8212():
    return 'ret8212' 

@action('ctrl_act8213')
def ctrl_nm8213():
    return 'ret8213' 

@action('ctrl_act8214')
def ctrl_nm8214():
    return 'ret8214' 

@action('ctrl_act8215')
def ctrl_nm8215():
    return 'ret8215' 

@action('ctrl_act8216')
def ctrl_nm8216():
    return 'ret8216' 

@action('ctrl_act8217')
def ctrl_nm8217():
    return 'ret8217' 

@action('ctrl_act8218')
def ctrl_nm8218():
    return 'ret8218' 

@action('ctrl_act8219')
def ctrl_nm8219():
    return 'ret8219' 

@action('ctrl_act8220')
def ctrl_nm8220():
    return 'ret8220' 

@action('ctrl_act8221')
def ctrl_nm8221():
    return 'ret8221' 

@action('ctrl_act8222')
def ctrl_nm8222():
    return 'ret8222' 

@action('ctrl_act8223')
def ctrl_nm8223():
    return 'ret8223' 

@action('ctrl_act8224')
def ctrl_nm8224():
    return 'ret8224' 

@action('ctrl_act8225')
def ctrl_nm8225():
    return 'ret8225' 

@action('ctrl_act8226')
def ctrl_nm8226():
    return 'ret8226' 

@action('ctrl_act8227')
def ctrl_nm8227():
    return 'ret8227' 

@action('ctrl_act8228')
def ctrl_nm8228():
    return 'ret8228' 

@action('ctrl_act8229')
def ctrl_nm8229():
    return 'ret8229' 

@action('ctrl_act8230')
def ctrl_nm8230():
    return 'ret8230' 

@action('ctrl_act8231')
def ctrl_nm8231():
    return 'ret8231' 

@action('ctrl_act8232')
def ctrl_nm8232():
    return 'ret8232' 

@action('ctrl_act8233')
def ctrl_nm8233():
    return 'ret8233' 

@action('ctrl_act8234')
def ctrl_nm8234():
    return 'ret8234' 

@action('ctrl_act8235')
def ctrl_nm8235():
    return 'ret8235' 

@action('ctrl_act8236')
def ctrl_nm8236():
    return 'ret8236' 

@action('ctrl_act8237')
def ctrl_nm8237():
    return 'ret8237' 

@action('ctrl_act8238')
def ctrl_nm8238():
    return 'ret8238' 

@action('ctrl_act8239')
def ctrl_nm8239():
    return 'ret8239' 

@action('ctrl_act8240')
def ctrl_nm8240():
    return 'ret8240' 

@action('ctrl_act8241')
def ctrl_nm8241():
    return 'ret8241' 

@action('ctrl_act8242')
def ctrl_nm8242():
    return 'ret8242' 

@action('ctrl_act8243')
def ctrl_nm8243():
    return 'ret8243' 

@action('ctrl_act8244')
def ctrl_nm8244():
    return 'ret8244' 

@action('ctrl_act8245')
def ctrl_nm8245():
    return 'ret8245' 

@action('ctrl_act8246')
def ctrl_nm8246():
    return 'ret8246' 

@action('ctrl_act8247')
def ctrl_nm8247():
    return 'ret8247' 

@action('ctrl_act8248')
def ctrl_nm8248():
    return 'ret8248' 

@action('ctrl_act8249')
def ctrl_nm8249():
    return 'ret8249' 

@action('ctrl_act8250')
def ctrl_nm8250():
    return 'ret8250' 

@action('ctrl_act8251')
def ctrl_nm8251():
    return 'ret8251' 

@action('ctrl_act8252')
def ctrl_nm8252():
    return 'ret8252' 

@action('ctrl_act8253')
def ctrl_nm8253():
    return 'ret8253' 

@action('ctrl_act8254')
def ctrl_nm8254():
    return 'ret8254' 

@action('ctrl_act8255')
def ctrl_nm8255():
    return 'ret8255' 

@action('ctrl_act8256')
def ctrl_nm8256():
    return 'ret8256' 

@action('ctrl_act8257')
def ctrl_nm8257():
    return 'ret8257' 

@action('ctrl_act8258')
def ctrl_nm8258():
    return 'ret8258' 

@action('ctrl_act8259')
def ctrl_nm8259():
    return 'ret8259' 

@action('ctrl_act8260')
def ctrl_nm8260():
    return 'ret8260' 

@action('ctrl_act8261')
def ctrl_nm8261():
    return 'ret8261' 

@action('ctrl_act8262')
def ctrl_nm8262():
    return 'ret8262' 

@action('ctrl_act8263')
def ctrl_nm8263():
    return 'ret8263' 

@action('ctrl_act8264')
def ctrl_nm8264():
    return 'ret8264' 

@action('ctrl_act8265')
def ctrl_nm8265():
    return 'ret8265' 

@action('ctrl_act8266')
def ctrl_nm8266():
    return 'ret8266' 

@action('ctrl_act8267')
def ctrl_nm8267():
    return 'ret8267' 

@action('ctrl_act8268')
def ctrl_nm8268():
    return 'ret8268' 

@action('ctrl_act8269')
def ctrl_nm8269():
    return 'ret8269' 

@action('ctrl_act8270')
def ctrl_nm8270():
    return 'ret8270' 

@action('ctrl_act8271')
def ctrl_nm8271():
    return 'ret8271' 

@action('ctrl_act8272')
def ctrl_nm8272():
    return 'ret8272' 

@action('ctrl_act8273')
def ctrl_nm8273():
    return 'ret8273' 

@action('ctrl_act8274')
def ctrl_nm8274():
    return 'ret8274' 

@action('ctrl_act8275')
def ctrl_nm8275():
    return 'ret8275' 

@action('ctrl_act8276')
def ctrl_nm8276():
    return 'ret8276' 

@action('ctrl_act8277')
def ctrl_nm8277():
    return 'ret8277' 

@action('ctrl_act8278')
def ctrl_nm8278():
    return 'ret8278' 

@action('ctrl_act8279')
def ctrl_nm8279():
    return 'ret8279' 

@action('ctrl_act8280')
def ctrl_nm8280():
    return 'ret8280' 

@action('ctrl_act8281')
def ctrl_nm8281():
    return 'ret8281' 

@action('ctrl_act8282')
def ctrl_nm8282():
    return 'ret8282' 

@action('ctrl_act8283')
def ctrl_nm8283():
    return 'ret8283' 

@action('ctrl_act8284')
def ctrl_nm8284():
    return 'ret8284' 

@action('ctrl_act8285')
def ctrl_nm8285():
    return 'ret8285' 

@action('ctrl_act8286')
def ctrl_nm8286():
    return 'ret8286' 

@action('ctrl_act8287')
def ctrl_nm8287():
    return 'ret8287' 

@action('ctrl_act8288')
def ctrl_nm8288():
    return 'ret8288' 

@action('ctrl_act8289')
def ctrl_nm8289():
    return 'ret8289' 

@action('ctrl_act8290')
def ctrl_nm8290():
    return 'ret8290' 

@action('ctrl_act8291')
def ctrl_nm8291():
    return 'ret8291' 

@action('ctrl_act8292')
def ctrl_nm8292():
    return 'ret8292' 

@action('ctrl_act8293')
def ctrl_nm8293():
    return 'ret8293' 

@action('ctrl_act8294')
def ctrl_nm8294():
    return 'ret8294' 

@action('ctrl_act8295')
def ctrl_nm8295():
    return 'ret8295' 

@action('ctrl_act8296')
def ctrl_nm8296():
    return 'ret8296' 

@action('ctrl_act8297')
def ctrl_nm8297():
    return 'ret8297' 

@action('ctrl_act8298')
def ctrl_nm8298():
    return 'ret8298' 

@action('ctrl_act8299')
def ctrl_nm8299():
    return 'ret8299' 

@action('ctrl_act8300')
def ctrl_nm8300():
    return 'ret8300' 

@action('ctrl_act8301')
def ctrl_nm8301():
    return 'ret8301' 

@action('ctrl_act8302')
def ctrl_nm8302():
    return 'ret8302' 

@action('ctrl_act8303')
def ctrl_nm8303():
    return 'ret8303' 

@action('ctrl_act8304')
def ctrl_nm8304():
    return 'ret8304' 

@action('ctrl_act8305')
def ctrl_nm8305():
    return 'ret8305' 

@action('ctrl_act8306')
def ctrl_nm8306():
    return 'ret8306' 

@action('ctrl_act8307')
def ctrl_nm8307():
    return 'ret8307' 

@action('ctrl_act8308')
def ctrl_nm8308():
    return 'ret8308' 

@action('ctrl_act8309')
def ctrl_nm8309():
    return 'ret8309' 

@action('ctrl_act8310')
def ctrl_nm8310():
    return 'ret8310' 

@action('ctrl_act8311')
def ctrl_nm8311():
    return 'ret8311' 

@action('ctrl_act8312')
def ctrl_nm8312():
    return 'ret8312' 

@action('ctrl_act8313')
def ctrl_nm8313():
    return 'ret8313' 

@action('ctrl_act8314')
def ctrl_nm8314():
    return 'ret8314' 

@action('ctrl_act8315')
def ctrl_nm8315():
    return 'ret8315' 

@action('ctrl_act8316')
def ctrl_nm8316():
    return 'ret8316' 

@action('ctrl_act8317')
def ctrl_nm8317():
    return 'ret8317' 

@action('ctrl_act8318')
def ctrl_nm8318():
    return 'ret8318' 

@action('ctrl_act8319')
def ctrl_nm8319():
    return 'ret8319' 

@action('ctrl_act8320')
def ctrl_nm8320():
    return 'ret8320' 

@action('ctrl_act8321')
def ctrl_nm8321():
    return 'ret8321' 

@action('ctrl_act8322')
def ctrl_nm8322():
    return 'ret8322' 

@action('ctrl_act8323')
def ctrl_nm8323():
    return 'ret8323' 

@action('ctrl_act8324')
def ctrl_nm8324():
    return 'ret8324' 

@action('ctrl_act8325')
def ctrl_nm8325():
    return 'ret8325' 

@action('ctrl_act8326')
def ctrl_nm8326():
    return 'ret8326' 

@action('ctrl_act8327')
def ctrl_nm8327():
    return 'ret8327' 

@action('ctrl_act8328')
def ctrl_nm8328():
    return 'ret8328' 

@action('ctrl_act8329')
def ctrl_nm8329():
    return 'ret8329' 

@action('ctrl_act8330')
def ctrl_nm8330():
    return 'ret8330' 

@action('ctrl_act8331')
def ctrl_nm8331():
    return 'ret8331' 

@action('ctrl_act8332')
def ctrl_nm8332():
    return 'ret8332' 

@action('ctrl_act8333')
def ctrl_nm8333():
    return 'ret8333' 

@action('ctrl_act8334')
def ctrl_nm8334():
    return 'ret8334' 

@action('ctrl_act8335')
def ctrl_nm8335():
    return 'ret8335' 

@action('ctrl_act8336')
def ctrl_nm8336():
    return 'ret8336' 

@action('ctrl_act8337')
def ctrl_nm8337():
    return 'ret8337' 

@action('ctrl_act8338')
def ctrl_nm8338():
    return 'ret8338' 

@action('ctrl_act8339')
def ctrl_nm8339():
    return 'ret8339' 

@action('ctrl_act8340')
def ctrl_nm8340():
    return 'ret8340' 

@action('ctrl_act8341')
def ctrl_nm8341():
    return 'ret8341' 

@action('ctrl_act8342')
def ctrl_nm8342():
    return 'ret8342' 

@action('ctrl_act8343')
def ctrl_nm8343():
    return 'ret8343' 

@action('ctrl_act8344')
def ctrl_nm8344():
    return 'ret8344' 

@action('ctrl_act8345')
def ctrl_nm8345():
    return 'ret8345' 

@action('ctrl_act8346')
def ctrl_nm8346():
    return 'ret8346' 

@action('ctrl_act8347')
def ctrl_nm8347():
    return 'ret8347' 

@action('ctrl_act8348')
def ctrl_nm8348():
    return 'ret8348' 

@action('ctrl_act8349')
def ctrl_nm8349():
    return 'ret8349' 

@action('ctrl_act8350')
def ctrl_nm8350():
    return 'ret8350' 

@action('ctrl_act8351')
def ctrl_nm8351():
    return 'ret8351' 

@action('ctrl_act8352')
def ctrl_nm8352():
    return 'ret8352' 

@action('ctrl_act8353')
def ctrl_nm8353():
    return 'ret8353' 

@action('ctrl_act8354')
def ctrl_nm8354():
    return 'ret8354' 

@action('ctrl_act8355')
def ctrl_nm8355():
    return 'ret8355' 

@action('ctrl_act8356')
def ctrl_nm8356():
    return 'ret8356' 

@action('ctrl_act8357')
def ctrl_nm8357():
    return 'ret8357' 

@action('ctrl_act8358')
def ctrl_nm8358():
    return 'ret8358' 

@action('ctrl_act8359')
def ctrl_nm8359():
    return 'ret8359' 

@action('ctrl_act8360')
def ctrl_nm8360():
    return 'ret8360' 

@action('ctrl_act8361')
def ctrl_nm8361():
    return 'ret8361' 

@action('ctrl_act8362')
def ctrl_nm8362():
    return 'ret8362' 

@action('ctrl_act8363')
def ctrl_nm8363():
    return 'ret8363' 

@action('ctrl_act8364')
def ctrl_nm8364():
    return 'ret8364' 

@action('ctrl_act8365')
def ctrl_nm8365():
    return 'ret8365' 

@action('ctrl_act8366')
def ctrl_nm8366():
    return 'ret8366' 

@action('ctrl_act8367')
def ctrl_nm8367():
    return 'ret8367' 

@action('ctrl_act8368')
def ctrl_nm8368():
    return 'ret8368' 

@action('ctrl_act8369')
def ctrl_nm8369():
    return 'ret8369' 

@action('ctrl_act8370')
def ctrl_nm8370():
    return 'ret8370' 

@action('ctrl_act8371')
def ctrl_nm8371():
    return 'ret8371' 

@action('ctrl_act8372')
def ctrl_nm8372():
    return 'ret8372' 

@action('ctrl_act8373')
def ctrl_nm8373():
    return 'ret8373' 

@action('ctrl_act8374')
def ctrl_nm8374():
    return 'ret8374' 

@action('ctrl_act8375')
def ctrl_nm8375():
    return 'ret8375' 

@action('ctrl_act8376')
def ctrl_nm8376():
    return 'ret8376' 

@action('ctrl_act8377')
def ctrl_nm8377():
    return 'ret8377' 

@action('ctrl_act8378')
def ctrl_nm8378():
    return 'ret8378' 

@action('ctrl_act8379')
def ctrl_nm8379():
    return 'ret8379' 

@action('ctrl_act8380')
def ctrl_nm8380():
    return 'ret8380' 

@action('ctrl_act8381')
def ctrl_nm8381():
    return 'ret8381' 

@action('ctrl_act8382')
def ctrl_nm8382():
    return 'ret8382' 

@action('ctrl_act8383')
def ctrl_nm8383():
    return 'ret8383' 

@action('ctrl_act8384')
def ctrl_nm8384():
    return 'ret8384' 

@action('ctrl_act8385')
def ctrl_nm8385():
    return 'ret8385' 

@action('ctrl_act8386')
def ctrl_nm8386():
    return 'ret8386' 

@action('ctrl_act8387')
def ctrl_nm8387():
    return 'ret8387' 

@action('ctrl_act8388')
def ctrl_nm8388():
    return 'ret8388' 

@action('ctrl_act8389')
def ctrl_nm8389():
    return 'ret8389' 

@action('ctrl_act8390')
def ctrl_nm8390():
    return 'ret8390' 

@action('ctrl_act8391')
def ctrl_nm8391():
    return 'ret8391' 

@action('ctrl_act8392')
def ctrl_nm8392():
    return 'ret8392' 

@action('ctrl_act8393')
def ctrl_nm8393():
    return 'ret8393' 

@action('ctrl_act8394')
def ctrl_nm8394():
    return 'ret8394' 

@action('ctrl_act8395')
def ctrl_nm8395():
    return 'ret8395' 

@action('ctrl_act8396')
def ctrl_nm8396():
    return 'ret8396' 

@action('ctrl_act8397')
def ctrl_nm8397():
    return 'ret8397' 

@action('ctrl_act8398')
def ctrl_nm8398():
    return 'ret8398' 

@action('ctrl_act8399')
def ctrl_nm8399():
    return 'ret8399' 

@action('ctrl_act8400')
def ctrl_nm8400():
    return 'ret8400' 

@action('ctrl_act8401')
def ctrl_nm8401():
    return 'ret8401' 

@action('ctrl_act8402')
def ctrl_nm8402():
    return 'ret8402' 

@action('ctrl_act8403')
def ctrl_nm8403():
    return 'ret8403' 

@action('ctrl_act8404')
def ctrl_nm8404():
    return 'ret8404' 

@action('ctrl_act8405')
def ctrl_nm8405():
    return 'ret8405' 

@action('ctrl_act8406')
def ctrl_nm8406():
    return 'ret8406' 

@action('ctrl_act8407')
def ctrl_nm8407():
    return 'ret8407' 

@action('ctrl_act8408')
def ctrl_nm8408():
    return 'ret8408' 

@action('ctrl_act8409')
def ctrl_nm8409():
    return 'ret8409' 

@action('ctrl_act8410')
def ctrl_nm8410():
    return 'ret8410' 

@action('ctrl_act8411')
def ctrl_nm8411():
    return 'ret8411' 

@action('ctrl_act8412')
def ctrl_nm8412():
    return 'ret8412' 

@action('ctrl_act8413')
def ctrl_nm8413():
    return 'ret8413' 

@action('ctrl_act8414')
def ctrl_nm8414():
    return 'ret8414' 

@action('ctrl_act8415')
def ctrl_nm8415():
    return 'ret8415' 

@action('ctrl_act8416')
def ctrl_nm8416():
    return 'ret8416' 

@action('ctrl_act8417')
def ctrl_nm8417():
    return 'ret8417' 

@action('ctrl_act8418')
def ctrl_nm8418():
    return 'ret8418' 

@action('ctrl_act8419')
def ctrl_nm8419():
    return 'ret8419' 

@action('ctrl_act8420')
def ctrl_nm8420():
    return 'ret8420' 

@action('ctrl_act8421')
def ctrl_nm8421():
    return 'ret8421' 

@action('ctrl_act8422')
def ctrl_nm8422():
    return 'ret8422' 

@action('ctrl_act8423')
def ctrl_nm8423():
    return 'ret8423' 

@action('ctrl_act8424')
def ctrl_nm8424():
    return 'ret8424' 

@action('ctrl_act8425')
def ctrl_nm8425():
    return 'ret8425' 

@action('ctrl_act8426')
def ctrl_nm8426():
    return 'ret8426' 

@action('ctrl_act8427')
def ctrl_nm8427():
    return 'ret8427' 

@action('ctrl_act8428')
def ctrl_nm8428():
    return 'ret8428' 

@action('ctrl_act8429')
def ctrl_nm8429():
    return 'ret8429' 

@action('ctrl_act8430')
def ctrl_nm8430():
    return 'ret8430' 

@action('ctrl_act8431')
def ctrl_nm8431():
    return 'ret8431' 

@action('ctrl_act8432')
def ctrl_nm8432():
    return 'ret8432' 

@action('ctrl_act8433')
def ctrl_nm8433():
    return 'ret8433' 

@action('ctrl_act8434')
def ctrl_nm8434():
    return 'ret8434' 

@action('ctrl_act8435')
def ctrl_nm8435():
    return 'ret8435' 

@action('ctrl_act8436')
def ctrl_nm8436():
    return 'ret8436' 

@action('ctrl_act8437')
def ctrl_nm8437():
    return 'ret8437' 

@action('ctrl_act8438')
def ctrl_nm8438():
    return 'ret8438' 

@action('ctrl_act8439')
def ctrl_nm8439():
    return 'ret8439' 

@action('ctrl_act8440')
def ctrl_nm8440():
    return 'ret8440' 

@action('ctrl_act8441')
def ctrl_nm8441():
    return 'ret8441' 

@action('ctrl_act8442')
def ctrl_nm8442():
    return 'ret8442' 

@action('ctrl_act8443')
def ctrl_nm8443():
    return 'ret8443' 

@action('ctrl_act8444')
def ctrl_nm8444():
    return 'ret8444' 

@action('ctrl_act8445')
def ctrl_nm8445():
    return 'ret8445' 

@action('ctrl_act8446')
def ctrl_nm8446():
    return 'ret8446' 

@action('ctrl_act8447')
def ctrl_nm8447():
    return 'ret8447' 

@action('ctrl_act8448')
def ctrl_nm8448():
    return 'ret8448' 

@action('ctrl_act8449')
def ctrl_nm8449():
    return 'ret8449' 

@action('ctrl_act8450')
def ctrl_nm8450():
    return 'ret8450' 

@action('ctrl_act8451')
def ctrl_nm8451():
    return 'ret8451' 

@action('ctrl_act8452')
def ctrl_nm8452():
    return 'ret8452' 

@action('ctrl_act8453')
def ctrl_nm8453():
    return 'ret8453' 

@action('ctrl_act8454')
def ctrl_nm8454():
    return 'ret8454' 

@action('ctrl_act8455')
def ctrl_nm8455():
    return 'ret8455' 

@action('ctrl_act8456')
def ctrl_nm8456():
    return 'ret8456' 

@action('ctrl_act8457')
def ctrl_nm8457():
    return 'ret8457' 

@action('ctrl_act8458')
def ctrl_nm8458():
    return 'ret8458' 

@action('ctrl_act8459')
def ctrl_nm8459():
    return 'ret8459' 

@action('ctrl_act8460')
def ctrl_nm8460():
    return 'ret8460' 

@action('ctrl_act8461')
def ctrl_nm8461():
    return 'ret8461' 

@action('ctrl_act8462')
def ctrl_nm8462():
    return 'ret8462' 

@action('ctrl_act8463')
def ctrl_nm8463():
    return 'ret8463' 

@action('ctrl_act8464')
def ctrl_nm8464():
    return 'ret8464' 

@action('ctrl_act8465')
def ctrl_nm8465():
    return 'ret8465' 

@action('ctrl_act8466')
def ctrl_nm8466():
    return 'ret8466' 

@action('ctrl_act8467')
def ctrl_nm8467():
    return 'ret8467' 

@action('ctrl_act8468')
def ctrl_nm8468():
    return 'ret8468' 

@action('ctrl_act8469')
def ctrl_nm8469():
    return 'ret8469' 

@action('ctrl_act8470')
def ctrl_nm8470():
    return 'ret8470' 

@action('ctrl_act8471')
def ctrl_nm8471():
    return 'ret8471' 

@action('ctrl_act8472')
def ctrl_nm8472():
    return 'ret8472' 

@action('ctrl_act8473')
def ctrl_nm8473():
    return 'ret8473' 

@action('ctrl_act8474')
def ctrl_nm8474():
    return 'ret8474' 

@action('ctrl_act8475')
def ctrl_nm8475():
    return 'ret8475' 

@action('ctrl_act8476')
def ctrl_nm8476():
    return 'ret8476' 

@action('ctrl_act8477')
def ctrl_nm8477():
    return 'ret8477' 

@action('ctrl_act8478')
def ctrl_nm8478():
    return 'ret8478' 

@action('ctrl_act8479')
def ctrl_nm8479():
    return 'ret8479' 

@action('ctrl_act8480')
def ctrl_nm8480():
    return 'ret8480' 

@action('ctrl_act8481')
def ctrl_nm8481():
    return 'ret8481' 

@action('ctrl_act8482')
def ctrl_nm8482():
    return 'ret8482' 

@action('ctrl_act8483')
def ctrl_nm8483():
    return 'ret8483' 

@action('ctrl_act8484')
def ctrl_nm8484():
    return 'ret8484' 

@action('ctrl_act8485')
def ctrl_nm8485():
    return 'ret8485' 

@action('ctrl_act8486')
def ctrl_nm8486():
    return 'ret8486' 

@action('ctrl_act8487')
def ctrl_nm8487():
    return 'ret8487' 

@action('ctrl_act8488')
def ctrl_nm8488():
    return 'ret8488' 

@action('ctrl_act8489')
def ctrl_nm8489():
    return 'ret8489' 

@action('ctrl_act8490')
def ctrl_nm8490():
    return 'ret8490' 

@action('ctrl_act8491')
def ctrl_nm8491():
    return 'ret8491' 

@action('ctrl_act8492')
def ctrl_nm8492():
    return 'ret8492' 

@action('ctrl_act8493')
def ctrl_nm8493():
    return 'ret8493' 

@action('ctrl_act8494')
def ctrl_nm8494():
    return 'ret8494' 

@action('ctrl_act8495')
def ctrl_nm8495():
    return 'ret8495' 

@action('ctrl_act8496')
def ctrl_nm8496():
    return 'ret8496' 

@action('ctrl_act8497')
def ctrl_nm8497():
    return 'ret8497' 

@action('ctrl_act8498')
def ctrl_nm8498():
    return 'ret8498' 

@action('ctrl_act8499')
def ctrl_nm8499():
    return 'ret8499' 

@action('ctrl_act8500')
def ctrl_nm8500():
    return 'ret8500' 

@action('ctrl_act8501')
def ctrl_nm8501():
    return 'ret8501' 

@action('ctrl_act8502')
def ctrl_nm8502():
    return 'ret8502' 

@action('ctrl_act8503')
def ctrl_nm8503():
    return 'ret8503' 

@action('ctrl_act8504')
def ctrl_nm8504():
    return 'ret8504' 

@action('ctrl_act8505')
def ctrl_nm8505():
    return 'ret8505' 

@action('ctrl_act8506')
def ctrl_nm8506():
    return 'ret8506' 

@action('ctrl_act8507')
def ctrl_nm8507():
    return 'ret8507' 

@action('ctrl_act8508')
def ctrl_nm8508():
    return 'ret8508' 

@action('ctrl_act8509')
def ctrl_nm8509():
    return 'ret8509' 

@action('ctrl_act8510')
def ctrl_nm8510():
    return 'ret8510' 

@action('ctrl_act8511')
def ctrl_nm8511():
    return 'ret8511' 

@action('ctrl_act8512')
def ctrl_nm8512():
    return 'ret8512' 

@action('ctrl_act8513')
def ctrl_nm8513():
    return 'ret8513' 

@action('ctrl_act8514')
def ctrl_nm8514():
    return 'ret8514' 

@action('ctrl_act8515')
def ctrl_nm8515():
    return 'ret8515' 

@action('ctrl_act8516')
def ctrl_nm8516():
    return 'ret8516' 

@action('ctrl_act8517')
def ctrl_nm8517():
    return 'ret8517' 

@action('ctrl_act8518')
def ctrl_nm8518():
    return 'ret8518' 

@action('ctrl_act8519')
def ctrl_nm8519():
    return 'ret8519' 

@action('ctrl_act8520')
def ctrl_nm8520():
    return 'ret8520' 

@action('ctrl_act8521')
def ctrl_nm8521():
    return 'ret8521' 

@action('ctrl_act8522')
def ctrl_nm8522():
    return 'ret8522' 

@action('ctrl_act8523')
def ctrl_nm8523():
    return 'ret8523' 

@action('ctrl_act8524')
def ctrl_nm8524():
    return 'ret8524' 

@action('ctrl_act8525')
def ctrl_nm8525():
    return 'ret8525' 

@action('ctrl_act8526')
def ctrl_nm8526():
    return 'ret8526' 

@action('ctrl_act8527')
def ctrl_nm8527():
    return 'ret8527' 

@action('ctrl_act8528')
def ctrl_nm8528():
    return 'ret8528' 

@action('ctrl_act8529')
def ctrl_nm8529():
    return 'ret8529' 

@action('ctrl_act8530')
def ctrl_nm8530():
    return 'ret8530' 

@action('ctrl_act8531')
def ctrl_nm8531():
    return 'ret8531' 

@action('ctrl_act8532')
def ctrl_nm8532():
    return 'ret8532' 

@action('ctrl_act8533')
def ctrl_nm8533():
    return 'ret8533' 

@action('ctrl_act8534')
def ctrl_nm8534():
    return 'ret8534' 

@action('ctrl_act8535')
def ctrl_nm8535():
    return 'ret8535' 

@action('ctrl_act8536')
def ctrl_nm8536():
    return 'ret8536' 

@action('ctrl_act8537')
def ctrl_nm8537():
    return 'ret8537' 

@action('ctrl_act8538')
def ctrl_nm8538():
    return 'ret8538' 

@action('ctrl_act8539')
def ctrl_nm8539():
    return 'ret8539' 

@action('ctrl_act8540')
def ctrl_nm8540():
    return 'ret8540' 

@action('ctrl_act8541')
def ctrl_nm8541():
    return 'ret8541' 

@action('ctrl_act8542')
def ctrl_nm8542():
    return 'ret8542' 

@action('ctrl_act8543')
def ctrl_nm8543():
    return 'ret8543' 

@action('ctrl_act8544')
def ctrl_nm8544():
    return 'ret8544' 

@action('ctrl_act8545')
def ctrl_nm8545():
    return 'ret8545' 

@action('ctrl_act8546')
def ctrl_nm8546():
    return 'ret8546' 

@action('ctrl_act8547')
def ctrl_nm8547():
    return 'ret8547' 

@action('ctrl_act8548')
def ctrl_nm8548():
    return 'ret8548' 

@action('ctrl_act8549')
def ctrl_nm8549():
    return 'ret8549' 

@action('ctrl_act8550')
def ctrl_nm8550():
    return 'ret8550' 

@action('ctrl_act8551')
def ctrl_nm8551():
    return 'ret8551' 

@action('ctrl_act8552')
def ctrl_nm8552():
    return 'ret8552' 

@action('ctrl_act8553')
def ctrl_nm8553():
    return 'ret8553' 

@action('ctrl_act8554')
def ctrl_nm8554():
    return 'ret8554' 

@action('ctrl_act8555')
def ctrl_nm8555():
    return 'ret8555' 

@action('ctrl_act8556')
def ctrl_nm8556():
    return 'ret8556' 

@action('ctrl_act8557')
def ctrl_nm8557():
    return 'ret8557' 

@action('ctrl_act8558')
def ctrl_nm8558():
    return 'ret8558' 

@action('ctrl_act8559')
def ctrl_nm8559():
    return 'ret8559' 

@action('ctrl_act8560')
def ctrl_nm8560():
    return 'ret8560' 

@action('ctrl_act8561')
def ctrl_nm8561():
    return 'ret8561' 

@action('ctrl_act8562')
def ctrl_nm8562():
    return 'ret8562' 

@action('ctrl_act8563')
def ctrl_nm8563():
    return 'ret8563' 

@action('ctrl_act8564')
def ctrl_nm8564():
    return 'ret8564' 

@action('ctrl_act8565')
def ctrl_nm8565():
    return 'ret8565' 

@action('ctrl_act8566')
def ctrl_nm8566():
    return 'ret8566' 

@action('ctrl_act8567')
def ctrl_nm8567():
    return 'ret8567' 

@action('ctrl_act8568')
def ctrl_nm8568():
    return 'ret8568' 

@action('ctrl_act8569')
def ctrl_nm8569():
    return 'ret8569' 

@action('ctrl_act8570')
def ctrl_nm8570():
    return 'ret8570' 

@action('ctrl_act8571')
def ctrl_nm8571():
    return 'ret8571' 

@action('ctrl_act8572')
def ctrl_nm8572():
    return 'ret8572' 

@action('ctrl_act8573')
def ctrl_nm8573():
    return 'ret8573' 

@action('ctrl_act8574')
def ctrl_nm8574():
    return 'ret8574' 

@action('ctrl_act8575')
def ctrl_nm8575():
    return 'ret8575' 

@action('ctrl_act8576')
def ctrl_nm8576():
    return 'ret8576' 

@action('ctrl_act8577')
def ctrl_nm8577():
    return 'ret8577' 

@action('ctrl_act8578')
def ctrl_nm8578():
    return 'ret8578' 

@action('ctrl_act8579')
def ctrl_nm8579():
    return 'ret8579' 

@action('ctrl_act8580')
def ctrl_nm8580():
    return 'ret8580' 

@action('ctrl_act8581')
def ctrl_nm8581():
    return 'ret8581' 

@action('ctrl_act8582')
def ctrl_nm8582():
    return 'ret8582' 

@action('ctrl_act8583')
def ctrl_nm8583():
    return 'ret8583' 

@action('ctrl_act8584')
def ctrl_nm8584():
    return 'ret8584' 

@action('ctrl_act8585')
def ctrl_nm8585():
    return 'ret8585' 

@action('ctrl_act8586')
def ctrl_nm8586():
    return 'ret8586' 

@action('ctrl_act8587')
def ctrl_nm8587():
    return 'ret8587' 

@action('ctrl_act8588')
def ctrl_nm8588():
    return 'ret8588' 

@action('ctrl_act8589')
def ctrl_nm8589():
    return 'ret8589' 

@action('ctrl_act8590')
def ctrl_nm8590():
    return 'ret8590' 

@action('ctrl_act8591')
def ctrl_nm8591():
    return 'ret8591' 

@action('ctrl_act8592')
def ctrl_nm8592():
    return 'ret8592' 

@action('ctrl_act8593')
def ctrl_nm8593():
    return 'ret8593' 

@action('ctrl_act8594')
def ctrl_nm8594():
    return 'ret8594' 

@action('ctrl_act8595')
def ctrl_nm8595():
    return 'ret8595' 

@action('ctrl_act8596')
def ctrl_nm8596():
    return 'ret8596' 

@action('ctrl_act8597')
def ctrl_nm8597():
    return 'ret8597' 

@action('ctrl_act8598')
def ctrl_nm8598():
    return 'ret8598' 

@action('ctrl_act8599')
def ctrl_nm8599():
    return 'ret8599' 

@action('ctrl_act8600')
def ctrl_nm8600():
    return 'ret8600' 

@action('ctrl_act8601')
def ctrl_nm8601():
    return 'ret8601' 

@action('ctrl_act8602')
def ctrl_nm8602():
    return 'ret8602' 

@action('ctrl_act8603')
def ctrl_nm8603():
    return 'ret8603' 

@action('ctrl_act8604')
def ctrl_nm8604():
    return 'ret8604' 

@action('ctrl_act8605')
def ctrl_nm8605():
    return 'ret8605' 

@action('ctrl_act8606')
def ctrl_nm8606():
    return 'ret8606' 

@action('ctrl_act8607')
def ctrl_nm8607():
    return 'ret8607' 

@action('ctrl_act8608')
def ctrl_nm8608():
    return 'ret8608' 

@action('ctrl_act8609')
def ctrl_nm8609():
    return 'ret8609' 

@action('ctrl_act8610')
def ctrl_nm8610():
    return 'ret8610' 

@action('ctrl_act8611')
def ctrl_nm8611():
    return 'ret8611' 

@action('ctrl_act8612')
def ctrl_nm8612():
    return 'ret8612' 

@action('ctrl_act8613')
def ctrl_nm8613():
    return 'ret8613' 

@action('ctrl_act8614')
def ctrl_nm8614():
    return 'ret8614' 

@action('ctrl_act8615')
def ctrl_nm8615():
    return 'ret8615' 

@action('ctrl_act8616')
def ctrl_nm8616():
    return 'ret8616' 

@action('ctrl_act8617')
def ctrl_nm8617():
    return 'ret8617' 

@action('ctrl_act8618')
def ctrl_nm8618():
    return 'ret8618' 

@action('ctrl_act8619')
def ctrl_nm8619():
    return 'ret8619' 

@action('ctrl_act8620')
def ctrl_nm8620():
    return 'ret8620' 

@action('ctrl_act8621')
def ctrl_nm8621():
    return 'ret8621' 

@action('ctrl_act8622')
def ctrl_nm8622():
    return 'ret8622' 

@action('ctrl_act8623')
def ctrl_nm8623():
    return 'ret8623' 

@action('ctrl_act8624')
def ctrl_nm8624():
    return 'ret8624' 

@action('ctrl_act8625')
def ctrl_nm8625():
    return 'ret8625' 

@action('ctrl_act8626')
def ctrl_nm8626():
    return 'ret8626' 

@action('ctrl_act8627')
def ctrl_nm8627():
    return 'ret8627' 

@action('ctrl_act8628')
def ctrl_nm8628():
    return 'ret8628' 

@action('ctrl_act8629')
def ctrl_nm8629():
    return 'ret8629' 

@action('ctrl_act8630')
def ctrl_nm8630():
    return 'ret8630' 

@action('ctrl_act8631')
def ctrl_nm8631():
    return 'ret8631' 

@action('ctrl_act8632')
def ctrl_nm8632():
    return 'ret8632' 

@action('ctrl_act8633')
def ctrl_nm8633():
    return 'ret8633' 

@action('ctrl_act8634')
def ctrl_nm8634():
    return 'ret8634' 

@action('ctrl_act8635')
def ctrl_nm8635():
    return 'ret8635' 

@action('ctrl_act8636')
def ctrl_nm8636():
    return 'ret8636' 

@action('ctrl_act8637')
def ctrl_nm8637():
    return 'ret8637' 

@action('ctrl_act8638')
def ctrl_nm8638():
    return 'ret8638' 

@action('ctrl_act8639')
def ctrl_nm8639():
    return 'ret8639' 

@action('ctrl_act8640')
def ctrl_nm8640():
    return 'ret8640' 

@action('ctrl_act8641')
def ctrl_nm8641():
    return 'ret8641' 

@action('ctrl_act8642')
def ctrl_nm8642():
    return 'ret8642' 

@action('ctrl_act8643')
def ctrl_nm8643():
    return 'ret8643' 

@action('ctrl_act8644')
def ctrl_nm8644():
    return 'ret8644' 

@action('ctrl_act8645')
def ctrl_nm8645():
    return 'ret8645' 

@action('ctrl_act8646')
def ctrl_nm8646():
    return 'ret8646' 

@action('ctrl_act8647')
def ctrl_nm8647():
    return 'ret8647' 

@action('ctrl_act8648')
def ctrl_nm8648():
    return 'ret8648' 

@action('ctrl_act8649')
def ctrl_nm8649():
    return 'ret8649' 

@action('ctrl_act8650')
def ctrl_nm8650():
    return 'ret8650' 

@action('ctrl_act8651')
def ctrl_nm8651():
    return 'ret8651' 

@action('ctrl_act8652')
def ctrl_nm8652():
    return 'ret8652' 

@action('ctrl_act8653')
def ctrl_nm8653():
    return 'ret8653' 

@action('ctrl_act8654')
def ctrl_nm8654():
    return 'ret8654' 

@action('ctrl_act8655')
def ctrl_nm8655():
    return 'ret8655' 

@action('ctrl_act8656')
def ctrl_nm8656():
    return 'ret8656' 

@action('ctrl_act8657')
def ctrl_nm8657():
    return 'ret8657' 

@action('ctrl_act8658')
def ctrl_nm8658():
    return 'ret8658' 

@action('ctrl_act8659')
def ctrl_nm8659():
    return 'ret8659' 

@action('ctrl_act8660')
def ctrl_nm8660():
    return 'ret8660' 

@action('ctrl_act8661')
def ctrl_nm8661():
    return 'ret8661' 

@action('ctrl_act8662')
def ctrl_nm8662():
    return 'ret8662' 

@action('ctrl_act8663')
def ctrl_nm8663():
    return 'ret8663' 

@action('ctrl_act8664')
def ctrl_nm8664():
    return 'ret8664' 

@action('ctrl_act8665')
def ctrl_nm8665():
    return 'ret8665' 

@action('ctrl_act8666')
def ctrl_nm8666():
    return 'ret8666' 

@action('ctrl_act8667')
def ctrl_nm8667():
    return 'ret8667' 

@action('ctrl_act8668')
def ctrl_nm8668():
    return 'ret8668' 

@action('ctrl_act8669')
def ctrl_nm8669():
    return 'ret8669' 

@action('ctrl_act8670')
def ctrl_nm8670():
    return 'ret8670' 

@action('ctrl_act8671')
def ctrl_nm8671():
    return 'ret8671' 

@action('ctrl_act8672')
def ctrl_nm8672():
    return 'ret8672' 

@action('ctrl_act8673')
def ctrl_nm8673():
    return 'ret8673' 

@action('ctrl_act8674')
def ctrl_nm8674():
    return 'ret8674' 

@action('ctrl_act8675')
def ctrl_nm8675():
    return 'ret8675' 

@action('ctrl_act8676')
def ctrl_nm8676():
    return 'ret8676' 

@action('ctrl_act8677')
def ctrl_nm8677():
    return 'ret8677' 

@action('ctrl_act8678')
def ctrl_nm8678():
    return 'ret8678' 

@action('ctrl_act8679')
def ctrl_nm8679():
    return 'ret8679' 

@action('ctrl_act8680')
def ctrl_nm8680():
    return 'ret8680' 

@action('ctrl_act8681')
def ctrl_nm8681():
    return 'ret8681' 

@action('ctrl_act8682')
def ctrl_nm8682():
    return 'ret8682' 

@action('ctrl_act8683')
def ctrl_nm8683():
    return 'ret8683' 

@action('ctrl_act8684')
def ctrl_nm8684():
    return 'ret8684' 

@action('ctrl_act8685')
def ctrl_nm8685():
    return 'ret8685' 

@action('ctrl_act8686')
def ctrl_nm8686():
    return 'ret8686' 

@action('ctrl_act8687')
def ctrl_nm8687():
    return 'ret8687' 

@action('ctrl_act8688')
def ctrl_nm8688():
    return 'ret8688' 

@action('ctrl_act8689')
def ctrl_nm8689():
    return 'ret8689' 

@action('ctrl_act8690')
def ctrl_nm8690():
    return 'ret8690' 

@action('ctrl_act8691')
def ctrl_nm8691():
    return 'ret8691' 

@action('ctrl_act8692')
def ctrl_nm8692():
    return 'ret8692' 

@action('ctrl_act8693')
def ctrl_nm8693():
    return 'ret8693' 

@action('ctrl_act8694')
def ctrl_nm8694():
    return 'ret8694' 

@action('ctrl_act8695')
def ctrl_nm8695():
    return 'ret8695' 

@action('ctrl_act8696')
def ctrl_nm8696():
    return 'ret8696' 

@action('ctrl_act8697')
def ctrl_nm8697():
    return 'ret8697' 

@action('ctrl_act8698')
def ctrl_nm8698():
    return 'ret8698' 

@action('ctrl_act8699')
def ctrl_nm8699():
    return 'ret8699' 

@action('ctrl_act8700')
def ctrl_nm8700():
    return 'ret8700' 

@action('ctrl_act8701')
def ctrl_nm8701():
    return 'ret8701' 

@action('ctrl_act8702')
def ctrl_nm8702():
    return 'ret8702' 

@action('ctrl_act8703')
def ctrl_nm8703():
    return 'ret8703' 

@action('ctrl_act8704')
def ctrl_nm8704():
    return 'ret8704' 

@action('ctrl_act8705')
def ctrl_nm8705():
    return 'ret8705' 

@action('ctrl_act8706')
def ctrl_nm8706():
    return 'ret8706' 

@action('ctrl_act8707')
def ctrl_nm8707():
    return 'ret8707' 

@action('ctrl_act8708')
def ctrl_nm8708():
    return 'ret8708' 

@action('ctrl_act8709')
def ctrl_nm8709():
    return 'ret8709' 

@action('ctrl_act8710')
def ctrl_nm8710():
    return 'ret8710' 

@action('ctrl_act8711')
def ctrl_nm8711():
    return 'ret8711' 

@action('ctrl_act8712')
def ctrl_nm8712():
    return 'ret8712' 

@action('ctrl_act8713')
def ctrl_nm8713():
    return 'ret8713' 

@action('ctrl_act8714')
def ctrl_nm8714():
    return 'ret8714' 

@action('ctrl_act8715')
def ctrl_nm8715():
    return 'ret8715' 

@action('ctrl_act8716')
def ctrl_nm8716():
    return 'ret8716' 

@action('ctrl_act8717')
def ctrl_nm8717():
    return 'ret8717' 

@action('ctrl_act8718')
def ctrl_nm8718():
    return 'ret8718' 

@action('ctrl_act8719')
def ctrl_nm8719():
    return 'ret8719' 

@action('ctrl_act8720')
def ctrl_nm8720():
    return 'ret8720' 

@action('ctrl_act8721')
def ctrl_nm8721():
    return 'ret8721' 

@action('ctrl_act8722')
def ctrl_nm8722():
    return 'ret8722' 

@action('ctrl_act8723')
def ctrl_nm8723():
    return 'ret8723' 

@action('ctrl_act8724')
def ctrl_nm8724():
    return 'ret8724' 

@action('ctrl_act8725')
def ctrl_nm8725():
    return 'ret8725' 

@action('ctrl_act8726')
def ctrl_nm8726():
    return 'ret8726' 

@action('ctrl_act8727')
def ctrl_nm8727():
    return 'ret8727' 

@action('ctrl_act8728')
def ctrl_nm8728():
    return 'ret8728' 

@action('ctrl_act8729')
def ctrl_nm8729():
    return 'ret8729' 

@action('ctrl_act8730')
def ctrl_nm8730():
    return 'ret8730' 

@action('ctrl_act8731')
def ctrl_nm8731():
    return 'ret8731' 

@action('ctrl_act8732')
def ctrl_nm8732():
    return 'ret8732' 

@action('ctrl_act8733')
def ctrl_nm8733():
    return 'ret8733' 

@action('ctrl_act8734')
def ctrl_nm8734():
    return 'ret8734' 

@action('ctrl_act8735')
def ctrl_nm8735():
    return 'ret8735' 

@action('ctrl_act8736')
def ctrl_nm8736():
    return 'ret8736' 

@action('ctrl_act8737')
def ctrl_nm8737():
    return 'ret8737' 

@action('ctrl_act8738')
def ctrl_nm8738():
    return 'ret8738' 

@action('ctrl_act8739')
def ctrl_nm8739():
    return 'ret8739' 

@action('ctrl_act8740')
def ctrl_nm8740():
    return 'ret8740' 

@action('ctrl_act8741')
def ctrl_nm8741():
    return 'ret8741' 

@action('ctrl_act8742')
def ctrl_nm8742():
    return 'ret8742' 

@action('ctrl_act8743')
def ctrl_nm8743():
    return 'ret8743' 

@action('ctrl_act8744')
def ctrl_nm8744():
    return 'ret8744' 

@action('ctrl_act8745')
def ctrl_nm8745():
    return 'ret8745' 

@action('ctrl_act8746')
def ctrl_nm8746():
    return 'ret8746' 

@action('ctrl_act8747')
def ctrl_nm8747():
    return 'ret8747' 

@action('ctrl_act8748')
def ctrl_nm8748():
    return 'ret8748' 

@action('ctrl_act8749')
def ctrl_nm8749():
    return 'ret8749' 

@action('ctrl_act8750')
def ctrl_nm8750():
    return 'ret8750' 

@action('ctrl_act8751')
def ctrl_nm8751():
    return 'ret8751' 

@action('ctrl_act8752')
def ctrl_nm8752():
    return 'ret8752' 

@action('ctrl_act8753')
def ctrl_nm8753():
    return 'ret8753' 

@action('ctrl_act8754')
def ctrl_nm8754():
    return 'ret8754' 

@action('ctrl_act8755')
def ctrl_nm8755():
    return 'ret8755' 

@action('ctrl_act8756')
def ctrl_nm8756():
    return 'ret8756' 

@action('ctrl_act8757')
def ctrl_nm8757():
    return 'ret8757' 

@action('ctrl_act8758')
def ctrl_nm8758():
    return 'ret8758' 

@action('ctrl_act8759')
def ctrl_nm8759():
    return 'ret8759' 

@action('ctrl_act8760')
def ctrl_nm8760():
    return 'ret8760' 

@action('ctrl_act8761')
def ctrl_nm8761():
    return 'ret8761' 

@action('ctrl_act8762')
def ctrl_nm8762():
    return 'ret8762' 

@action('ctrl_act8763')
def ctrl_nm8763():
    return 'ret8763' 

@action('ctrl_act8764')
def ctrl_nm8764():
    return 'ret8764' 

@action('ctrl_act8765')
def ctrl_nm8765():
    return 'ret8765' 

@action('ctrl_act8766')
def ctrl_nm8766():
    return 'ret8766' 

@action('ctrl_act8767')
def ctrl_nm8767():
    return 'ret8767' 

@action('ctrl_act8768')
def ctrl_nm8768():
    return 'ret8768' 

@action('ctrl_act8769')
def ctrl_nm8769():
    return 'ret8769' 

@action('ctrl_act8770')
def ctrl_nm8770():
    return 'ret8770' 

@action('ctrl_act8771')
def ctrl_nm8771():
    return 'ret8771' 

@action('ctrl_act8772')
def ctrl_nm8772():
    return 'ret8772' 

@action('ctrl_act8773')
def ctrl_nm8773():
    return 'ret8773' 

@action('ctrl_act8774')
def ctrl_nm8774():
    return 'ret8774' 

@action('ctrl_act8775')
def ctrl_nm8775():
    return 'ret8775' 

@action('ctrl_act8776')
def ctrl_nm8776():
    return 'ret8776' 

@action('ctrl_act8777')
def ctrl_nm8777():
    return 'ret8777' 

@action('ctrl_act8778')
def ctrl_nm8778():
    return 'ret8778' 

@action('ctrl_act8779')
def ctrl_nm8779():
    return 'ret8779' 

@action('ctrl_act8780')
def ctrl_nm8780():
    return 'ret8780' 

@action('ctrl_act8781')
def ctrl_nm8781():
    return 'ret8781' 

@action('ctrl_act8782')
def ctrl_nm8782():
    return 'ret8782' 

@action('ctrl_act8783')
def ctrl_nm8783():
    return 'ret8783' 

@action('ctrl_act8784')
def ctrl_nm8784():
    return 'ret8784' 

@action('ctrl_act8785')
def ctrl_nm8785():
    return 'ret8785' 

@action('ctrl_act8786')
def ctrl_nm8786():
    return 'ret8786' 

@action('ctrl_act8787')
def ctrl_nm8787():
    return 'ret8787' 

@action('ctrl_act8788')
def ctrl_nm8788():
    return 'ret8788' 

@action('ctrl_act8789')
def ctrl_nm8789():
    return 'ret8789' 

@action('ctrl_act8790')
def ctrl_nm8790():
    return 'ret8790' 

@action('ctrl_act8791')
def ctrl_nm8791():
    return 'ret8791' 

@action('ctrl_act8792')
def ctrl_nm8792():
    return 'ret8792' 

@action('ctrl_act8793')
def ctrl_nm8793():
    return 'ret8793' 

@action('ctrl_act8794')
def ctrl_nm8794():
    return 'ret8794' 

@action('ctrl_act8795')
def ctrl_nm8795():
    return 'ret8795' 

@action('ctrl_act8796')
def ctrl_nm8796():
    return 'ret8796' 

@action('ctrl_act8797')
def ctrl_nm8797():
    return 'ret8797' 

@action('ctrl_act8798')
def ctrl_nm8798():
    return 'ret8798' 

@action('ctrl_act8799')
def ctrl_nm8799():
    return 'ret8799' 

@action('ctrl_act8800')
def ctrl_nm8800():
    return 'ret8800' 

@action('ctrl_act8801')
def ctrl_nm8801():
    return 'ret8801' 

@action('ctrl_act8802')
def ctrl_nm8802():
    return 'ret8802' 

@action('ctrl_act8803')
def ctrl_nm8803():
    return 'ret8803' 

@action('ctrl_act8804')
def ctrl_nm8804():
    return 'ret8804' 

@action('ctrl_act8805')
def ctrl_nm8805():
    return 'ret8805' 

@action('ctrl_act8806')
def ctrl_nm8806():
    return 'ret8806' 

@action('ctrl_act8807')
def ctrl_nm8807():
    return 'ret8807' 

@action('ctrl_act8808')
def ctrl_nm8808():
    return 'ret8808' 

@action('ctrl_act8809')
def ctrl_nm8809():
    return 'ret8809' 

@action('ctrl_act8810')
def ctrl_nm8810():
    return 'ret8810' 

@action('ctrl_act8811')
def ctrl_nm8811():
    return 'ret8811' 

@action('ctrl_act8812')
def ctrl_nm8812():
    return 'ret8812' 

@action('ctrl_act8813')
def ctrl_nm8813():
    return 'ret8813' 

@action('ctrl_act8814')
def ctrl_nm8814():
    return 'ret8814' 

@action('ctrl_act8815')
def ctrl_nm8815():
    return 'ret8815' 

@action('ctrl_act8816')
def ctrl_nm8816():
    return 'ret8816' 

@action('ctrl_act8817')
def ctrl_nm8817():
    return 'ret8817' 

@action('ctrl_act8818')
def ctrl_nm8818():
    return 'ret8818' 

@action('ctrl_act8819')
def ctrl_nm8819():
    return 'ret8819' 

@action('ctrl_act8820')
def ctrl_nm8820():
    return 'ret8820' 

@action('ctrl_act8821')
def ctrl_nm8821():
    return 'ret8821' 

@action('ctrl_act8822')
def ctrl_nm8822():
    return 'ret8822' 

@action('ctrl_act8823')
def ctrl_nm8823():
    return 'ret8823' 

@action('ctrl_act8824')
def ctrl_nm8824():
    return 'ret8824' 

@action('ctrl_act8825')
def ctrl_nm8825():
    return 'ret8825' 

@action('ctrl_act8826')
def ctrl_nm8826():
    return 'ret8826' 

@action('ctrl_act8827')
def ctrl_nm8827():
    return 'ret8827' 

@action('ctrl_act8828')
def ctrl_nm8828():
    return 'ret8828' 

@action('ctrl_act8829')
def ctrl_nm8829():
    return 'ret8829' 

@action('ctrl_act8830')
def ctrl_nm8830():
    return 'ret8830' 

@action('ctrl_act8831')
def ctrl_nm8831():
    return 'ret8831' 

@action('ctrl_act8832')
def ctrl_nm8832():
    return 'ret8832' 

@action('ctrl_act8833')
def ctrl_nm8833():
    return 'ret8833' 

@action('ctrl_act8834')
def ctrl_nm8834():
    return 'ret8834' 

@action('ctrl_act8835')
def ctrl_nm8835():
    return 'ret8835' 

@action('ctrl_act8836')
def ctrl_nm8836():
    return 'ret8836' 

@action('ctrl_act8837')
def ctrl_nm8837():
    return 'ret8837' 

@action('ctrl_act8838')
def ctrl_nm8838():
    return 'ret8838' 

@action('ctrl_act8839')
def ctrl_nm8839():
    return 'ret8839' 

@action('ctrl_act8840')
def ctrl_nm8840():
    return 'ret8840' 

@action('ctrl_act8841')
def ctrl_nm8841():
    return 'ret8841' 

@action('ctrl_act8842')
def ctrl_nm8842():
    return 'ret8842' 

@action('ctrl_act8843')
def ctrl_nm8843():
    return 'ret8843' 

@action('ctrl_act8844')
def ctrl_nm8844():
    return 'ret8844' 

@action('ctrl_act8845')
def ctrl_nm8845():
    return 'ret8845' 

@action('ctrl_act8846')
def ctrl_nm8846():
    return 'ret8846' 

@action('ctrl_act8847')
def ctrl_nm8847():
    return 'ret8847' 

@action('ctrl_act8848')
def ctrl_nm8848():
    return 'ret8848' 

@action('ctrl_act8849')
def ctrl_nm8849():
    return 'ret8849' 

@action('ctrl_act8850')
def ctrl_nm8850():
    return 'ret8850' 

@action('ctrl_act8851')
def ctrl_nm8851():
    return 'ret8851' 

@action('ctrl_act8852')
def ctrl_nm8852():
    return 'ret8852' 

@action('ctrl_act8853')
def ctrl_nm8853():
    return 'ret8853' 

@action('ctrl_act8854')
def ctrl_nm8854():
    return 'ret8854' 

@action('ctrl_act8855')
def ctrl_nm8855():
    return 'ret8855' 

@action('ctrl_act8856')
def ctrl_nm8856():
    return 'ret8856' 

@action('ctrl_act8857')
def ctrl_nm8857():
    return 'ret8857' 

@action('ctrl_act8858')
def ctrl_nm8858():
    return 'ret8858' 

@action('ctrl_act8859')
def ctrl_nm8859():
    return 'ret8859' 

@action('ctrl_act8860')
def ctrl_nm8860():
    return 'ret8860' 

@action('ctrl_act8861')
def ctrl_nm8861():
    return 'ret8861' 

@action('ctrl_act8862')
def ctrl_nm8862():
    return 'ret8862' 

@action('ctrl_act8863')
def ctrl_nm8863():
    return 'ret8863' 

@action('ctrl_act8864')
def ctrl_nm8864():
    return 'ret8864' 

@action('ctrl_act8865')
def ctrl_nm8865():
    return 'ret8865' 

@action('ctrl_act8866')
def ctrl_nm8866():
    return 'ret8866' 

@action('ctrl_act8867')
def ctrl_nm8867():
    return 'ret8867' 

@action('ctrl_act8868')
def ctrl_nm8868():
    return 'ret8868' 

@action('ctrl_act8869')
def ctrl_nm8869():
    return 'ret8869' 

@action('ctrl_act8870')
def ctrl_nm8870():
    return 'ret8870' 

@action('ctrl_act8871')
def ctrl_nm8871():
    return 'ret8871' 

@action('ctrl_act8872')
def ctrl_nm8872():
    return 'ret8872' 

@action('ctrl_act8873')
def ctrl_nm8873():
    return 'ret8873' 

@action('ctrl_act8874')
def ctrl_nm8874():
    return 'ret8874' 

@action('ctrl_act8875')
def ctrl_nm8875():
    return 'ret8875' 

@action('ctrl_act8876')
def ctrl_nm8876():
    return 'ret8876' 

@action('ctrl_act8877')
def ctrl_nm8877():
    return 'ret8877' 

@action('ctrl_act8878')
def ctrl_nm8878():
    return 'ret8878' 

@action('ctrl_act8879')
def ctrl_nm8879():
    return 'ret8879' 

@action('ctrl_act8880')
def ctrl_nm8880():
    return 'ret8880' 

@action('ctrl_act8881')
def ctrl_nm8881():
    return 'ret8881' 

@action('ctrl_act8882')
def ctrl_nm8882():
    return 'ret8882' 

@action('ctrl_act8883')
def ctrl_nm8883():
    return 'ret8883' 

@action('ctrl_act8884')
def ctrl_nm8884():
    return 'ret8884' 

@action('ctrl_act8885')
def ctrl_nm8885():
    return 'ret8885' 

@action('ctrl_act8886')
def ctrl_nm8886():
    return 'ret8886' 

@action('ctrl_act8887')
def ctrl_nm8887():
    return 'ret8887' 

@action('ctrl_act8888')
def ctrl_nm8888():
    return 'ret8888' 

@action('ctrl_act8889')
def ctrl_nm8889():
    return 'ret8889' 

@action('ctrl_act8890')
def ctrl_nm8890():
    return 'ret8890' 

@action('ctrl_act8891')
def ctrl_nm8891():
    return 'ret8891' 

@action('ctrl_act8892')
def ctrl_nm8892():
    return 'ret8892' 

@action('ctrl_act8893')
def ctrl_nm8893():
    return 'ret8893' 

@action('ctrl_act8894')
def ctrl_nm8894():
    return 'ret8894' 

@action('ctrl_act8895')
def ctrl_nm8895():
    return 'ret8895' 

@action('ctrl_act8896')
def ctrl_nm8896():
    return 'ret8896' 

@action('ctrl_act8897')
def ctrl_nm8897():
    return 'ret8897' 

@action('ctrl_act8898')
def ctrl_nm8898():
    return 'ret8898' 

@action('ctrl_act8899')
def ctrl_nm8899():
    return 'ret8899' 

@action('ctrl_act8900')
def ctrl_nm8900():
    return 'ret8900' 

@action('ctrl_act8901')
def ctrl_nm8901():
    return 'ret8901' 

@action('ctrl_act8902')
def ctrl_nm8902():
    return 'ret8902' 

@action('ctrl_act8903')
def ctrl_nm8903():
    return 'ret8903' 

@action('ctrl_act8904')
def ctrl_nm8904():
    return 'ret8904' 

@action('ctrl_act8905')
def ctrl_nm8905():
    return 'ret8905' 

@action('ctrl_act8906')
def ctrl_nm8906():
    return 'ret8906' 

@action('ctrl_act8907')
def ctrl_nm8907():
    return 'ret8907' 

@action('ctrl_act8908')
def ctrl_nm8908():
    return 'ret8908' 

@action('ctrl_act8909')
def ctrl_nm8909():
    return 'ret8909' 

@action('ctrl_act8910')
def ctrl_nm8910():
    return 'ret8910' 

@action('ctrl_act8911')
def ctrl_nm8911():
    return 'ret8911' 

@action('ctrl_act8912')
def ctrl_nm8912():
    return 'ret8912' 

@action('ctrl_act8913')
def ctrl_nm8913():
    return 'ret8913' 

@action('ctrl_act8914')
def ctrl_nm8914():
    return 'ret8914' 

@action('ctrl_act8915')
def ctrl_nm8915():
    return 'ret8915' 

@action('ctrl_act8916')
def ctrl_nm8916():
    return 'ret8916' 

@action('ctrl_act8917')
def ctrl_nm8917():
    return 'ret8917' 

@action('ctrl_act8918')
def ctrl_nm8918():
    return 'ret8918' 

@action('ctrl_act8919')
def ctrl_nm8919():
    return 'ret8919' 

@action('ctrl_act8920')
def ctrl_nm8920():
    return 'ret8920' 

@action('ctrl_act8921')
def ctrl_nm8921():
    return 'ret8921' 

@action('ctrl_act8922')
def ctrl_nm8922():
    return 'ret8922' 

@action('ctrl_act8923')
def ctrl_nm8923():
    return 'ret8923' 

@action('ctrl_act8924')
def ctrl_nm8924():
    return 'ret8924' 

@action('ctrl_act8925')
def ctrl_nm8925():
    return 'ret8925' 

@action('ctrl_act8926')
def ctrl_nm8926():
    return 'ret8926' 

@action('ctrl_act8927')
def ctrl_nm8927():
    return 'ret8927' 

@action('ctrl_act8928')
def ctrl_nm8928():
    return 'ret8928' 

@action('ctrl_act8929')
def ctrl_nm8929():
    return 'ret8929' 

@action('ctrl_act8930')
def ctrl_nm8930():
    return 'ret8930' 

@action('ctrl_act8931')
def ctrl_nm8931():
    return 'ret8931' 

@action('ctrl_act8932')
def ctrl_nm8932():
    return 'ret8932' 

@action('ctrl_act8933')
def ctrl_nm8933():
    return 'ret8933' 

@action('ctrl_act8934')
def ctrl_nm8934():
    return 'ret8934' 

@action('ctrl_act8935')
def ctrl_nm8935():
    return 'ret8935' 

@action('ctrl_act8936')
def ctrl_nm8936():
    return 'ret8936' 

@action('ctrl_act8937')
def ctrl_nm8937():
    return 'ret8937' 

@action('ctrl_act8938')
def ctrl_nm8938():
    return 'ret8938' 

@action('ctrl_act8939')
def ctrl_nm8939():
    return 'ret8939' 

@action('ctrl_act8940')
def ctrl_nm8940():
    return 'ret8940' 

@action('ctrl_act8941')
def ctrl_nm8941():
    return 'ret8941' 

@action('ctrl_act8942')
def ctrl_nm8942():
    return 'ret8942' 

@action('ctrl_act8943')
def ctrl_nm8943():
    return 'ret8943' 

@action('ctrl_act8944')
def ctrl_nm8944():
    return 'ret8944' 

@action('ctrl_act8945')
def ctrl_nm8945():
    return 'ret8945' 

@action('ctrl_act8946')
def ctrl_nm8946():
    return 'ret8946' 

@action('ctrl_act8947')
def ctrl_nm8947():
    return 'ret8947' 

@action('ctrl_act8948')
def ctrl_nm8948():
    return 'ret8948' 

@action('ctrl_act8949')
def ctrl_nm8949():
    return 'ret8949' 

@action('ctrl_act8950')
def ctrl_nm8950():
    return 'ret8950' 

@action('ctrl_act8951')
def ctrl_nm8951():
    return 'ret8951' 

@action('ctrl_act8952')
def ctrl_nm8952():
    return 'ret8952' 

@action('ctrl_act8953')
def ctrl_nm8953():
    return 'ret8953' 

@action('ctrl_act8954')
def ctrl_nm8954():
    return 'ret8954' 

@action('ctrl_act8955')
def ctrl_nm8955():
    return 'ret8955' 

@action('ctrl_act8956')
def ctrl_nm8956():
    return 'ret8956' 

@action('ctrl_act8957')
def ctrl_nm8957():
    return 'ret8957' 

@action('ctrl_act8958')
def ctrl_nm8958():
    return 'ret8958' 

@action('ctrl_act8959')
def ctrl_nm8959():
    return 'ret8959' 

@action('ctrl_act8960')
def ctrl_nm8960():
    return 'ret8960' 

@action('ctrl_act8961')
def ctrl_nm8961():
    return 'ret8961' 

@action('ctrl_act8962')
def ctrl_nm8962():
    return 'ret8962' 

@action('ctrl_act8963')
def ctrl_nm8963():
    return 'ret8963' 

@action('ctrl_act8964')
def ctrl_nm8964():
    return 'ret8964' 

@action('ctrl_act8965')
def ctrl_nm8965():
    return 'ret8965' 

@action('ctrl_act8966')
def ctrl_nm8966():
    return 'ret8966' 

@action('ctrl_act8967')
def ctrl_nm8967():
    return 'ret8967' 

@action('ctrl_act8968')
def ctrl_nm8968():
    return 'ret8968' 

@action('ctrl_act8969')
def ctrl_nm8969():
    return 'ret8969' 

@action('ctrl_act8970')
def ctrl_nm8970():
    return 'ret8970' 

@action('ctrl_act8971')
def ctrl_nm8971():
    return 'ret8971' 

@action('ctrl_act8972')
def ctrl_nm8972():
    return 'ret8972' 

@action('ctrl_act8973')
def ctrl_nm8973():
    return 'ret8973' 

@action('ctrl_act8974')
def ctrl_nm8974():
    return 'ret8974' 

@action('ctrl_act8975')
def ctrl_nm8975():
    return 'ret8975' 

@action('ctrl_act8976')
def ctrl_nm8976():
    return 'ret8976' 

@action('ctrl_act8977')
def ctrl_nm8977():
    return 'ret8977' 

@action('ctrl_act8978')
def ctrl_nm8978():
    return 'ret8978' 

@action('ctrl_act8979')
def ctrl_nm8979():
    return 'ret8979' 

@action('ctrl_act8980')
def ctrl_nm8980():
    return 'ret8980' 

@action('ctrl_act8981')
def ctrl_nm8981():
    return 'ret8981' 

@action('ctrl_act8982')
def ctrl_nm8982():
    return 'ret8982' 

@action('ctrl_act8983')
def ctrl_nm8983():
    return 'ret8983' 

@action('ctrl_act8984')
def ctrl_nm8984():
    return 'ret8984' 

@action('ctrl_act8985')
def ctrl_nm8985():
    return 'ret8985' 

@action('ctrl_act8986')
def ctrl_nm8986():
    return 'ret8986' 

@action('ctrl_act8987')
def ctrl_nm8987():
    return 'ret8987' 

@action('ctrl_act8988')
def ctrl_nm8988():
    return 'ret8988' 

@action('ctrl_act8989')
def ctrl_nm8989():
    return 'ret8989' 

@action('ctrl_act8990')
def ctrl_nm8990():
    return 'ret8990' 

@action('ctrl_act8991')
def ctrl_nm8991():
    return 'ret8991' 

@action('ctrl_act8992')
def ctrl_nm8992():
    return 'ret8992' 

@action('ctrl_act8993')
def ctrl_nm8993():
    return 'ret8993' 

@action('ctrl_act8994')
def ctrl_nm8994():
    return 'ret8994' 

@action('ctrl_act8995')
def ctrl_nm8995():
    return 'ret8995' 

@action('ctrl_act8996')
def ctrl_nm8996():
    return 'ret8996' 

@action('ctrl_act8997')
def ctrl_nm8997():
    return 'ret8997' 

@action('ctrl_act8998')
def ctrl_nm8998():
    return 'ret8998' 

@action('ctrl_act8999')
def ctrl_nm8999():
    return 'ret8999' 

@action('ctrl_act9000')
def ctrl_nm9000():
    return 'ret9000' 

@action('ctrl_act9001')
def ctrl_nm9001():
    return 'ret9001' 

@action('ctrl_act9002')
def ctrl_nm9002():
    return 'ret9002' 

@action('ctrl_act9003')
def ctrl_nm9003():
    return 'ret9003' 

@action('ctrl_act9004')
def ctrl_nm9004():
    return 'ret9004' 

@action('ctrl_act9005')
def ctrl_nm9005():
    return 'ret9005' 

@action('ctrl_act9006')
def ctrl_nm9006():
    return 'ret9006' 

@action('ctrl_act9007')
def ctrl_nm9007():
    return 'ret9007' 

@action('ctrl_act9008')
def ctrl_nm9008():
    return 'ret9008' 

@action('ctrl_act9009')
def ctrl_nm9009():
    return 'ret9009' 

@action('ctrl_act9010')
def ctrl_nm9010():
    return 'ret9010' 

@action('ctrl_act9011')
def ctrl_nm9011():
    return 'ret9011' 

@action('ctrl_act9012')
def ctrl_nm9012():
    return 'ret9012' 

@action('ctrl_act9013')
def ctrl_nm9013():
    return 'ret9013' 

@action('ctrl_act9014')
def ctrl_nm9014():
    return 'ret9014' 

@action('ctrl_act9015')
def ctrl_nm9015():
    return 'ret9015' 

@action('ctrl_act9016')
def ctrl_nm9016():
    return 'ret9016' 

@action('ctrl_act9017')
def ctrl_nm9017():
    return 'ret9017' 

@action('ctrl_act9018')
def ctrl_nm9018():
    return 'ret9018' 

@action('ctrl_act9019')
def ctrl_nm9019():
    return 'ret9019' 

@action('ctrl_act9020')
def ctrl_nm9020():
    return 'ret9020' 

@action('ctrl_act9021')
def ctrl_nm9021():
    return 'ret9021' 

@action('ctrl_act9022')
def ctrl_nm9022():
    return 'ret9022' 

@action('ctrl_act9023')
def ctrl_nm9023():
    return 'ret9023' 

@action('ctrl_act9024')
def ctrl_nm9024():
    return 'ret9024' 

@action('ctrl_act9025')
def ctrl_nm9025():
    return 'ret9025' 

@action('ctrl_act9026')
def ctrl_nm9026():
    return 'ret9026' 

@action('ctrl_act9027')
def ctrl_nm9027():
    return 'ret9027' 

@action('ctrl_act9028')
def ctrl_nm9028():
    return 'ret9028' 

@action('ctrl_act9029')
def ctrl_nm9029():
    return 'ret9029' 

@action('ctrl_act9030')
def ctrl_nm9030():
    return 'ret9030' 

@action('ctrl_act9031')
def ctrl_nm9031():
    return 'ret9031' 

@action('ctrl_act9032')
def ctrl_nm9032():
    return 'ret9032' 

@action('ctrl_act9033')
def ctrl_nm9033():
    return 'ret9033' 

@action('ctrl_act9034')
def ctrl_nm9034():
    return 'ret9034' 

@action('ctrl_act9035')
def ctrl_nm9035():
    return 'ret9035' 

@action('ctrl_act9036')
def ctrl_nm9036():
    return 'ret9036' 

@action('ctrl_act9037')
def ctrl_nm9037():
    return 'ret9037' 

@action('ctrl_act9038')
def ctrl_nm9038():
    return 'ret9038' 

@action('ctrl_act9039')
def ctrl_nm9039():
    return 'ret9039' 

@action('ctrl_act9040')
def ctrl_nm9040():
    return 'ret9040' 

@action('ctrl_act9041')
def ctrl_nm9041():
    return 'ret9041' 

@action('ctrl_act9042')
def ctrl_nm9042():
    return 'ret9042' 

@action('ctrl_act9043')
def ctrl_nm9043():
    return 'ret9043' 

@action('ctrl_act9044')
def ctrl_nm9044():
    return 'ret9044' 

@action('ctrl_act9045')
def ctrl_nm9045():
    return 'ret9045' 

@action('ctrl_act9046')
def ctrl_nm9046():
    return 'ret9046' 

@action('ctrl_act9047')
def ctrl_nm9047():
    return 'ret9047' 

@action('ctrl_act9048')
def ctrl_nm9048():
    return 'ret9048' 

@action('ctrl_act9049')
def ctrl_nm9049():
    return 'ret9049' 

@action('ctrl_act9050')
def ctrl_nm9050():
    return 'ret9050' 

@action('ctrl_act9051')
def ctrl_nm9051():
    return 'ret9051' 

@action('ctrl_act9052')
def ctrl_nm9052():
    return 'ret9052' 

@action('ctrl_act9053')
def ctrl_nm9053():
    return 'ret9053' 

@action('ctrl_act9054')
def ctrl_nm9054():
    return 'ret9054' 

@action('ctrl_act9055')
def ctrl_nm9055():
    return 'ret9055' 

@action('ctrl_act9056')
def ctrl_nm9056():
    return 'ret9056' 

@action('ctrl_act9057')
def ctrl_nm9057():
    return 'ret9057' 

@action('ctrl_act9058')
def ctrl_nm9058():
    return 'ret9058' 

@action('ctrl_act9059')
def ctrl_nm9059():
    return 'ret9059' 

@action('ctrl_act9060')
def ctrl_nm9060():
    return 'ret9060' 

@action('ctrl_act9061')
def ctrl_nm9061():
    return 'ret9061' 

@action('ctrl_act9062')
def ctrl_nm9062():
    return 'ret9062' 

@action('ctrl_act9063')
def ctrl_nm9063():
    return 'ret9063' 

@action('ctrl_act9064')
def ctrl_nm9064():
    return 'ret9064' 

@action('ctrl_act9065')
def ctrl_nm9065():
    return 'ret9065' 

@action('ctrl_act9066')
def ctrl_nm9066():
    return 'ret9066' 

@action('ctrl_act9067')
def ctrl_nm9067():
    return 'ret9067' 

@action('ctrl_act9068')
def ctrl_nm9068():
    return 'ret9068' 

@action('ctrl_act9069')
def ctrl_nm9069():
    return 'ret9069' 

@action('ctrl_act9070')
def ctrl_nm9070():
    return 'ret9070' 

@action('ctrl_act9071')
def ctrl_nm9071():
    return 'ret9071' 

@action('ctrl_act9072')
def ctrl_nm9072():
    return 'ret9072' 

@action('ctrl_act9073')
def ctrl_nm9073():
    return 'ret9073' 

@action('ctrl_act9074')
def ctrl_nm9074():
    return 'ret9074' 

@action('ctrl_act9075')
def ctrl_nm9075():
    return 'ret9075' 

@action('ctrl_act9076')
def ctrl_nm9076():
    return 'ret9076' 

@action('ctrl_act9077')
def ctrl_nm9077():
    return 'ret9077' 

@action('ctrl_act9078')
def ctrl_nm9078():
    return 'ret9078' 

@action('ctrl_act9079')
def ctrl_nm9079():
    return 'ret9079' 

@action('ctrl_act9080')
def ctrl_nm9080():
    return 'ret9080' 

@action('ctrl_act9081')
def ctrl_nm9081():
    return 'ret9081' 

@action('ctrl_act9082')
def ctrl_nm9082():
    return 'ret9082' 

@action('ctrl_act9083')
def ctrl_nm9083():
    return 'ret9083' 

@action('ctrl_act9084')
def ctrl_nm9084():
    return 'ret9084' 

@action('ctrl_act9085')
def ctrl_nm9085():
    return 'ret9085' 

@action('ctrl_act9086')
def ctrl_nm9086():
    return 'ret9086' 

@action('ctrl_act9087')
def ctrl_nm9087():
    return 'ret9087' 

@action('ctrl_act9088')
def ctrl_nm9088():
    return 'ret9088' 

@action('ctrl_act9089')
def ctrl_nm9089():
    return 'ret9089' 

@action('ctrl_act9090')
def ctrl_nm9090():
    return 'ret9090' 

@action('ctrl_act9091')
def ctrl_nm9091():
    return 'ret9091' 

@action('ctrl_act9092')
def ctrl_nm9092():
    return 'ret9092' 

@action('ctrl_act9093')
def ctrl_nm9093():
    return 'ret9093' 

@action('ctrl_act9094')
def ctrl_nm9094():
    return 'ret9094' 

@action('ctrl_act9095')
def ctrl_nm9095():
    return 'ret9095' 

@action('ctrl_act9096')
def ctrl_nm9096():
    return 'ret9096' 

@action('ctrl_act9097')
def ctrl_nm9097():
    return 'ret9097' 

@action('ctrl_act9098')
def ctrl_nm9098():
    return 'ret9098' 

@action('ctrl_act9099')
def ctrl_nm9099():
    return 'ret9099' 

@action('ctrl_act9100')
def ctrl_nm9100():
    return 'ret9100' 

@action('ctrl_act9101')
def ctrl_nm9101():
    return 'ret9101' 

@action('ctrl_act9102')
def ctrl_nm9102():
    return 'ret9102' 

@action('ctrl_act9103')
def ctrl_nm9103():
    return 'ret9103' 

@action('ctrl_act9104')
def ctrl_nm9104():
    return 'ret9104' 

@action('ctrl_act9105')
def ctrl_nm9105():
    return 'ret9105' 

@action('ctrl_act9106')
def ctrl_nm9106():
    return 'ret9106' 

@action('ctrl_act9107')
def ctrl_nm9107():
    return 'ret9107' 

@action('ctrl_act9108')
def ctrl_nm9108():
    return 'ret9108' 

@action('ctrl_act9109')
def ctrl_nm9109():
    return 'ret9109' 

@action('ctrl_act9110')
def ctrl_nm9110():
    return 'ret9110' 

@action('ctrl_act9111')
def ctrl_nm9111():
    return 'ret9111' 

@action('ctrl_act9112')
def ctrl_nm9112():
    return 'ret9112' 

@action('ctrl_act9113')
def ctrl_nm9113():
    return 'ret9113' 

@action('ctrl_act9114')
def ctrl_nm9114():
    return 'ret9114' 

@action('ctrl_act9115')
def ctrl_nm9115():
    return 'ret9115' 

@action('ctrl_act9116')
def ctrl_nm9116():
    return 'ret9116' 

@action('ctrl_act9117')
def ctrl_nm9117():
    return 'ret9117' 

@action('ctrl_act9118')
def ctrl_nm9118():
    return 'ret9118' 

@action('ctrl_act9119')
def ctrl_nm9119():
    return 'ret9119' 

@action('ctrl_act9120')
def ctrl_nm9120():
    return 'ret9120' 

@action('ctrl_act9121')
def ctrl_nm9121():
    return 'ret9121' 

@action('ctrl_act9122')
def ctrl_nm9122():
    return 'ret9122' 

@action('ctrl_act9123')
def ctrl_nm9123():
    return 'ret9123' 

@action('ctrl_act9124')
def ctrl_nm9124():
    return 'ret9124' 

@action('ctrl_act9125')
def ctrl_nm9125():
    return 'ret9125' 

@action('ctrl_act9126')
def ctrl_nm9126():
    return 'ret9126' 

@action('ctrl_act9127')
def ctrl_nm9127():
    return 'ret9127' 

@action('ctrl_act9128')
def ctrl_nm9128():
    return 'ret9128' 

@action('ctrl_act9129')
def ctrl_nm9129():
    return 'ret9129' 

@action('ctrl_act9130')
def ctrl_nm9130():
    return 'ret9130' 

@action('ctrl_act9131')
def ctrl_nm9131():
    return 'ret9131' 

@action('ctrl_act9132')
def ctrl_nm9132():
    return 'ret9132' 

@action('ctrl_act9133')
def ctrl_nm9133():
    return 'ret9133' 

@action('ctrl_act9134')
def ctrl_nm9134():
    return 'ret9134' 

@action('ctrl_act9135')
def ctrl_nm9135():
    return 'ret9135' 

@action('ctrl_act9136')
def ctrl_nm9136():
    return 'ret9136' 

@action('ctrl_act9137')
def ctrl_nm9137():
    return 'ret9137' 

@action('ctrl_act9138')
def ctrl_nm9138():
    return 'ret9138' 

@action('ctrl_act9139')
def ctrl_nm9139():
    return 'ret9139' 

@action('ctrl_act9140')
def ctrl_nm9140():
    return 'ret9140' 

@action('ctrl_act9141')
def ctrl_nm9141():
    return 'ret9141' 

@action('ctrl_act9142')
def ctrl_nm9142():
    return 'ret9142' 

@action('ctrl_act9143')
def ctrl_nm9143():
    return 'ret9143' 

@action('ctrl_act9144')
def ctrl_nm9144():
    return 'ret9144' 

@action('ctrl_act9145')
def ctrl_nm9145():
    return 'ret9145' 

@action('ctrl_act9146')
def ctrl_nm9146():
    return 'ret9146' 

@action('ctrl_act9147')
def ctrl_nm9147():
    return 'ret9147' 

@action('ctrl_act9148')
def ctrl_nm9148():
    return 'ret9148' 

@action('ctrl_act9149')
def ctrl_nm9149():
    return 'ret9149' 

@action('ctrl_act9150')
def ctrl_nm9150():
    return 'ret9150' 

@action('ctrl_act9151')
def ctrl_nm9151():
    return 'ret9151' 

@action('ctrl_act9152')
def ctrl_nm9152():
    return 'ret9152' 

@action('ctrl_act9153')
def ctrl_nm9153():
    return 'ret9153' 

@action('ctrl_act9154')
def ctrl_nm9154():
    return 'ret9154' 

@action('ctrl_act9155')
def ctrl_nm9155():
    return 'ret9155' 

@action('ctrl_act9156')
def ctrl_nm9156():
    return 'ret9156' 

@action('ctrl_act9157')
def ctrl_nm9157():
    return 'ret9157' 

@action('ctrl_act9158')
def ctrl_nm9158():
    return 'ret9158' 

@action('ctrl_act9159')
def ctrl_nm9159():
    return 'ret9159' 

@action('ctrl_act9160')
def ctrl_nm9160():
    return 'ret9160' 

@action('ctrl_act9161')
def ctrl_nm9161():
    return 'ret9161' 

@action('ctrl_act9162')
def ctrl_nm9162():
    return 'ret9162' 

@action('ctrl_act9163')
def ctrl_nm9163():
    return 'ret9163' 

@action('ctrl_act9164')
def ctrl_nm9164():
    return 'ret9164' 

@action('ctrl_act9165')
def ctrl_nm9165():
    return 'ret9165' 

@action('ctrl_act9166')
def ctrl_nm9166():
    return 'ret9166' 

@action('ctrl_act9167')
def ctrl_nm9167():
    return 'ret9167' 

@action('ctrl_act9168')
def ctrl_nm9168():
    return 'ret9168' 

@action('ctrl_act9169')
def ctrl_nm9169():
    return 'ret9169' 

@action('ctrl_act9170')
def ctrl_nm9170():
    return 'ret9170' 

@action('ctrl_act9171')
def ctrl_nm9171():
    return 'ret9171' 

@action('ctrl_act9172')
def ctrl_nm9172():
    return 'ret9172' 

@action('ctrl_act9173')
def ctrl_nm9173():
    return 'ret9173' 

@action('ctrl_act9174')
def ctrl_nm9174():
    return 'ret9174' 

@action('ctrl_act9175')
def ctrl_nm9175():
    return 'ret9175' 

@action('ctrl_act9176')
def ctrl_nm9176():
    return 'ret9176' 

@action('ctrl_act9177')
def ctrl_nm9177():
    return 'ret9177' 

@action('ctrl_act9178')
def ctrl_nm9178():
    return 'ret9178' 

@action('ctrl_act9179')
def ctrl_nm9179():
    return 'ret9179' 

@action('ctrl_act9180')
def ctrl_nm9180():
    return 'ret9180' 

@action('ctrl_act9181')
def ctrl_nm9181():
    return 'ret9181' 

@action('ctrl_act9182')
def ctrl_nm9182():
    return 'ret9182' 

@action('ctrl_act9183')
def ctrl_nm9183():
    return 'ret9183' 

@action('ctrl_act9184')
def ctrl_nm9184():
    return 'ret9184' 

@action('ctrl_act9185')
def ctrl_nm9185():
    return 'ret9185' 

@action('ctrl_act9186')
def ctrl_nm9186():
    return 'ret9186' 

@action('ctrl_act9187')
def ctrl_nm9187():
    return 'ret9187' 

@action('ctrl_act9188')
def ctrl_nm9188():
    return 'ret9188' 

@action('ctrl_act9189')
def ctrl_nm9189():
    return 'ret9189' 

@action('ctrl_act9190')
def ctrl_nm9190():
    return 'ret9190' 

@action('ctrl_act9191')
def ctrl_nm9191():
    return 'ret9191' 

@action('ctrl_act9192')
def ctrl_nm9192():
    return 'ret9192' 

@action('ctrl_act9193')
def ctrl_nm9193():
    return 'ret9193' 

@action('ctrl_act9194')
def ctrl_nm9194():
    return 'ret9194' 

@action('ctrl_act9195')
def ctrl_nm9195():
    return 'ret9195' 

@action('ctrl_act9196')
def ctrl_nm9196():
    return 'ret9196' 

@action('ctrl_act9197')
def ctrl_nm9197():
    return 'ret9197' 

@action('ctrl_act9198')
def ctrl_nm9198():
    return 'ret9198' 

@action('ctrl_act9199')
def ctrl_nm9199():
    return 'ret9199' 

@action('ctrl_act9200')
def ctrl_nm9200():
    return 'ret9200' 

@action('ctrl_act9201')
def ctrl_nm9201():
    return 'ret9201' 

@action('ctrl_act9202')
def ctrl_nm9202():
    return 'ret9202' 

@action('ctrl_act9203')
def ctrl_nm9203():
    return 'ret9203' 

@action('ctrl_act9204')
def ctrl_nm9204():
    return 'ret9204' 

@action('ctrl_act9205')
def ctrl_nm9205():
    return 'ret9205' 

@action('ctrl_act9206')
def ctrl_nm9206():
    return 'ret9206' 

@action('ctrl_act9207')
def ctrl_nm9207():
    return 'ret9207' 

@action('ctrl_act9208')
def ctrl_nm9208():
    return 'ret9208' 

@action('ctrl_act9209')
def ctrl_nm9209():
    return 'ret9209' 

@action('ctrl_act9210')
def ctrl_nm9210():
    return 'ret9210' 

@action('ctrl_act9211')
def ctrl_nm9211():
    return 'ret9211' 

@action('ctrl_act9212')
def ctrl_nm9212():
    return 'ret9212' 

@action('ctrl_act9213')
def ctrl_nm9213():
    return 'ret9213' 

@action('ctrl_act9214')
def ctrl_nm9214():
    return 'ret9214' 

@action('ctrl_act9215')
def ctrl_nm9215():
    return 'ret9215' 

@action('ctrl_act9216')
def ctrl_nm9216():
    return 'ret9216' 

@action('ctrl_act9217')
def ctrl_nm9217():
    return 'ret9217' 

@action('ctrl_act9218')
def ctrl_nm9218():
    return 'ret9218' 

@action('ctrl_act9219')
def ctrl_nm9219():
    return 'ret9219' 

@action('ctrl_act9220')
def ctrl_nm9220():
    return 'ret9220' 

@action('ctrl_act9221')
def ctrl_nm9221():
    return 'ret9221' 

@action('ctrl_act9222')
def ctrl_nm9222():
    return 'ret9222' 

@action('ctrl_act9223')
def ctrl_nm9223():
    return 'ret9223' 

@action('ctrl_act9224')
def ctrl_nm9224():
    return 'ret9224' 

@action('ctrl_act9225')
def ctrl_nm9225():
    return 'ret9225' 

@action('ctrl_act9226')
def ctrl_nm9226():
    return 'ret9226' 

@action('ctrl_act9227')
def ctrl_nm9227():
    return 'ret9227' 

@action('ctrl_act9228')
def ctrl_nm9228():
    return 'ret9228' 

@action('ctrl_act9229')
def ctrl_nm9229():
    return 'ret9229' 

@action('ctrl_act9230')
def ctrl_nm9230():
    return 'ret9230' 

@action('ctrl_act9231')
def ctrl_nm9231():
    return 'ret9231' 

@action('ctrl_act9232')
def ctrl_nm9232():
    return 'ret9232' 

@action('ctrl_act9233')
def ctrl_nm9233():
    return 'ret9233' 

@action('ctrl_act9234')
def ctrl_nm9234():
    return 'ret9234' 

@action('ctrl_act9235')
def ctrl_nm9235():
    return 'ret9235' 

@action('ctrl_act9236')
def ctrl_nm9236():
    return 'ret9236' 

@action('ctrl_act9237')
def ctrl_nm9237():
    return 'ret9237' 

@action('ctrl_act9238')
def ctrl_nm9238():
    return 'ret9238' 

@action('ctrl_act9239')
def ctrl_nm9239():
    return 'ret9239' 

@action('ctrl_act9240')
def ctrl_nm9240():
    return 'ret9240' 

@action('ctrl_act9241')
def ctrl_nm9241():
    return 'ret9241' 

@action('ctrl_act9242')
def ctrl_nm9242():
    return 'ret9242' 

@action('ctrl_act9243')
def ctrl_nm9243():
    return 'ret9243' 

@action('ctrl_act9244')
def ctrl_nm9244():
    return 'ret9244' 

@action('ctrl_act9245')
def ctrl_nm9245():
    return 'ret9245' 

@action('ctrl_act9246')
def ctrl_nm9246():
    return 'ret9246' 

@action('ctrl_act9247')
def ctrl_nm9247():
    return 'ret9247' 

@action('ctrl_act9248')
def ctrl_nm9248():
    return 'ret9248' 

@action('ctrl_act9249')
def ctrl_nm9249():
    return 'ret9249' 

@action('ctrl_act9250')
def ctrl_nm9250():
    return 'ret9250' 

@action('ctrl_act9251')
def ctrl_nm9251():
    return 'ret9251' 

@action('ctrl_act9252')
def ctrl_nm9252():
    return 'ret9252' 

@action('ctrl_act9253')
def ctrl_nm9253():
    return 'ret9253' 

@action('ctrl_act9254')
def ctrl_nm9254():
    return 'ret9254' 

@action('ctrl_act9255')
def ctrl_nm9255():
    return 'ret9255' 

@action('ctrl_act9256')
def ctrl_nm9256():
    return 'ret9256' 

@action('ctrl_act9257')
def ctrl_nm9257():
    return 'ret9257' 

@action('ctrl_act9258')
def ctrl_nm9258():
    return 'ret9258' 

@action('ctrl_act9259')
def ctrl_nm9259():
    return 'ret9259' 

@action('ctrl_act9260')
def ctrl_nm9260():
    return 'ret9260' 

@action('ctrl_act9261')
def ctrl_nm9261():
    return 'ret9261' 

@action('ctrl_act9262')
def ctrl_nm9262():
    return 'ret9262' 

@action('ctrl_act9263')
def ctrl_nm9263():
    return 'ret9263' 

@action('ctrl_act9264')
def ctrl_nm9264():
    return 'ret9264' 

@action('ctrl_act9265')
def ctrl_nm9265():
    return 'ret9265' 

@action('ctrl_act9266')
def ctrl_nm9266():
    return 'ret9266' 

@action('ctrl_act9267')
def ctrl_nm9267():
    return 'ret9267' 

@action('ctrl_act9268')
def ctrl_nm9268():
    return 'ret9268' 

@action('ctrl_act9269')
def ctrl_nm9269():
    return 'ret9269' 

@action('ctrl_act9270')
def ctrl_nm9270():
    return 'ret9270' 

@action('ctrl_act9271')
def ctrl_nm9271():
    return 'ret9271' 

@action('ctrl_act9272')
def ctrl_nm9272():
    return 'ret9272' 

@action('ctrl_act9273')
def ctrl_nm9273():
    return 'ret9273' 

@action('ctrl_act9274')
def ctrl_nm9274():
    return 'ret9274' 

@action('ctrl_act9275')
def ctrl_nm9275():
    return 'ret9275' 

@action('ctrl_act9276')
def ctrl_nm9276():
    return 'ret9276' 

@action('ctrl_act9277')
def ctrl_nm9277():
    return 'ret9277' 

@action('ctrl_act9278')
def ctrl_nm9278():
    return 'ret9278' 

@action('ctrl_act9279')
def ctrl_nm9279():
    return 'ret9279' 

@action('ctrl_act9280')
def ctrl_nm9280():
    return 'ret9280' 

@action('ctrl_act9281')
def ctrl_nm9281():
    return 'ret9281' 

@action('ctrl_act9282')
def ctrl_nm9282():
    return 'ret9282' 

@action('ctrl_act9283')
def ctrl_nm9283():
    return 'ret9283' 

@action('ctrl_act9284')
def ctrl_nm9284():
    return 'ret9284' 

@action('ctrl_act9285')
def ctrl_nm9285():
    return 'ret9285' 

@action('ctrl_act9286')
def ctrl_nm9286():
    return 'ret9286' 

@action('ctrl_act9287')
def ctrl_nm9287():
    return 'ret9287' 

@action('ctrl_act9288')
def ctrl_nm9288():
    return 'ret9288' 

@action('ctrl_act9289')
def ctrl_nm9289():
    return 'ret9289' 

@action('ctrl_act9290')
def ctrl_nm9290():
    return 'ret9290' 

@action('ctrl_act9291')
def ctrl_nm9291():
    return 'ret9291' 

@action('ctrl_act9292')
def ctrl_nm9292():
    return 'ret9292' 

@action('ctrl_act9293')
def ctrl_nm9293():
    return 'ret9293' 

@action('ctrl_act9294')
def ctrl_nm9294():
    return 'ret9294' 

@action('ctrl_act9295')
def ctrl_nm9295():
    return 'ret9295' 

@action('ctrl_act9296')
def ctrl_nm9296():
    return 'ret9296' 

@action('ctrl_act9297')
def ctrl_nm9297():
    return 'ret9297' 

@action('ctrl_act9298')
def ctrl_nm9298():
    return 'ret9298' 

@action('ctrl_act9299')
def ctrl_nm9299():
    return 'ret9299' 

@action('ctrl_act9300')
def ctrl_nm9300():
    return 'ret9300' 

@action('ctrl_act9301')
def ctrl_nm9301():
    return 'ret9301' 

@action('ctrl_act9302')
def ctrl_nm9302():
    return 'ret9302' 

@action('ctrl_act9303')
def ctrl_nm9303():
    return 'ret9303' 

@action('ctrl_act9304')
def ctrl_nm9304():
    return 'ret9304' 

@action('ctrl_act9305')
def ctrl_nm9305():
    return 'ret9305' 

@action('ctrl_act9306')
def ctrl_nm9306():
    return 'ret9306' 

@action('ctrl_act9307')
def ctrl_nm9307():
    return 'ret9307' 

@action('ctrl_act9308')
def ctrl_nm9308():
    return 'ret9308' 

@action('ctrl_act9309')
def ctrl_nm9309():
    return 'ret9309' 

@action('ctrl_act9310')
def ctrl_nm9310():
    return 'ret9310' 

@action('ctrl_act9311')
def ctrl_nm9311():
    return 'ret9311' 

@action('ctrl_act9312')
def ctrl_nm9312():
    return 'ret9312' 

@action('ctrl_act9313')
def ctrl_nm9313():
    return 'ret9313' 

@action('ctrl_act9314')
def ctrl_nm9314():
    return 'ret9314' 

@action('ctrl_act9315')
def ctrl_nm9315():
    return 'ret9315' 

@action('ctrl_act9316')
def ctrl_nm9316():
    return 'ret9316' 

@action('ctrl_act9317')
def ctrl_nm9317():
    return 'ret9317' 

@action('ctrl_act9318')
def ctrl_nm9318():
    return 'ret9318' 

@action('ctrl_act9319')
def ctrl_nm9319():
    return 'ret9319' 

@action('ctrl_act9320')
def ctrl_nm9320():
    return 'ret9320' 

@action('ctrl_act9321')
def ctrl_nm9321():
    return 'ret9321' 

@action('ctrl_act9322')
def ctrl_nm9322():
    return 'ret9322' 

@action('ctrl_act9323')
def ctrl_nm9323():
    return 'ret9323' 

@action('ctrl_act9324')
def ctrl_nm9324():
    return 'ret9324' 

@action('ctrl_act9325')
def ctrl_nm9325():
    return 'ret9325' 

@action('ctrl_act9326')
def ctrl_nm9326():
    return 'ret9326' 

@action('ctrl_act9327')
def ctrl_nm9327():
    return 'ret9327' 

@action('ctrl_act9328')
def ctrl_nm9328():
    return 'ret9328' 

@action('ctrl_act9329')
def ctrl_nm9329():
    return 'ret9329' 

@action('ctrl_act9330')
def ctrl_nm9330():
    return 'ret9330' 

@action('ctrl_act9331')
def ctrl_nm9331():
    return 'ret9331' 

@action('ctrl_act9332')
def ctrl_nm9332():
    return 'ret9332' 

@action('ctrl_act9333')
def ctrl_nm9333():
    return 'ret9333' 

@action('ctrl_act9334')
def ctrl_nm9334():
    return 'ret9334' 

@action('ctrl_act9335')
def ctrl_nm9335():
    return 'ret9335' 

@action('ctrl_act9336')
def ctrl_nm9336():
    return 'ret9336' 

@action('ctrl_act9337')
def ctrl_nm9337():
    return 'ret9337' 

@action('ctrl_act9338')
def ctrl_nm9338():
    return 'ret9338' 

@action('ctrl_act9339')
def ctrl_nm9339():
    return 'ret9339' 

@action('ctrl_act9340')
def ctrl_nm9340():
    return 'ret9340' 

@action('ctrl_act9341')
def ctrl_nm9341():
    return 'ret9341' 

@action('ctrl_act9342')
def ctrl_nm9342():
    return 'ret9342' 

@action('ctrl_act9343')
def ctrl_nm9343():
    return 'ret9343' 

@action('ctrl_act9344')
def ctrl_nm9344():
    return 'ret9344' 

@action('ctrl_act9345')
def ctrl_nm9345():
    return 'ret9345' 

@action('ctrl_act9346')
def ctrl_nm9346():
    return 'ret9346' 

@action('ctrl_act9347')
def ctrl_nm9347():
    return 'ret9347' 

@action('ctrl_act9348')
def ctrl_nm9348():
    return 'ret9348' 

@action('ctrl_act9349')
def ctrl_nm9349():
    return 'ret9349' 

@action('ctrl_act9350')
def ctrl_nm9350():
    return 'ret9350' 

@action('ctrl_act9351')
def ctrl_nm9351():
    return 'ret9351' 

@action('ctrl_act9352')
def ctrl_nm9352():
    return 'ret9352' 

@action('ctrl_act9353')
def ctrl_nm9353():
    return 'ret9353' 

@action('ctrl_act9354')
def ctrl_nm9354():
    return 'ret9354' 

@action('ctrl_act9355')
def ctrl_nm9355():
    return 'ret9355' 

@action('ctrl_act9356')
def ctrl_nm9356():
    return 'ret9356' 

@action('ctrl_act9357')
def ctrl_nm9357():
    return 'ret9357' 

@action('ctrl_act9358')
def ctrl_nm9358():
    return 'ret9358' 

@action('ctrl_act9359')
def ctrl_nm9359():
    return 'ret9359' 

@action('ctrl_act9360')
def ctrl_nm9360():
    return 'ret9360' 

@action('ctrl_act9361')
def ctrl_nm9361():
    return 'ret9361' 

@action('ctrl_act9362')
def ctrl_nm9362():
    return 'ret9362' 

@action('ctrl_act9363')
def ctrl_nm9363():
    return 'ret9363' 

@action('ctrl_act9364')
def ctrl_nm9364():
    return 'ret9364' 

@action('ctrl_act9365')
def ctrl_nm9365():
    return 'ret9365' 

@action('ctrl_act9366')
def ctrl_nm9366():
    return 'ret9366' 

@action('ctrl_act9367')
def ctrl_nm9367():
    return 'ret9367' 

@action('ctrl_act9368')
def ctrl_nm9368():
    return 'ret9368' 

@action('ctrl_act9369')
def ctrl_nm9369():
    return 'ret9369' 

@action('ctrl_act9370')
def ctrl_nm9370():
    return 'ret9370' 

@action('ctrl_act9371')
def ctrl_nm9371():
    return 'ret9371' 

@action('ctrl_act9372')
def ctrl_nm9372():
    return 'ret9372' 

@action('ctrl_act9373')
def ctrl_nm9373():
    return 'ret9373' 

@action('ctrl_act9374')
def ctrl_nm9374():
    return 'ret9374' 

@action('ctrl_act9375')
def ctrl_nm9375():
    return 'ret9375' 

@action('ctrl_act9376')
def ctrl_nm9376():
    return 'ret9376' 

@action('ctrl_act9377')
def ctrl_nm9377():
    return 'ret9377' 

@action('ctrl_act9378')
def ctrl_nm9378():
    return 'ret9378' 

@action('ctrl_act9379')
def ctrl_nm9379():
    return 'ret9379' 

@action('ctrl_act9380')
def ctrl_nm9380():
    return 'ret9380' 

@action('ctrl_act9381')
def ctrl_nm9381():
    return 'ret9381' 

@action('ctrl_act9382')
def ctrl_nm9382():
    return 'ret9382' 

@action('ctrl_act9383')
def ctrl_nm9383():
    return 'ret9383' 

@action('ctrl_act9384')
def ctrl_nm9384():
    return 'ret9384' 

@action('ctrl_act9385')
def ctrl_nm9385():
    return 'ret9385' 

@action('ctrl_act9386')
def ctrl_nm9386():
    return 'ret9386' 

@action('ctrl_act9387')
def ctrl_nm9387():
    return 'ret9387' 

@action('ctrl_act9388')
def ctrl_nm9388():
    return 'ret9388' 

@action('ctrl_act9389')
def ctrl_nm9389():
    return 'ret9389' 

@action('ctrl_act9390')
def ctrl_nm9390():
    return 'ret9390' 

@action('ctrl_act9391')
def ctrl_nm9391():
    return 'ret9391' 

@action('ctrl_act9392')
def ctrl_nm9392():
    return 'ret9392' 

@action('ctrl_act9393')
def ctrl_nm9393():
    return 'ret9393' 

@action('ctrl_act9394')
def ctrl_nm9394():
    return 'ret9394' 

@action('ctrl_act9395')
def ctrl_nm9395():
    return 'ret9395' 

@action('ctrl_act9396')
def ctrl_nm9396():
    return 'ret9396' 

@action('ctrl_act9397')
def ctrl_nm9397():
    return 'ret9397' 

@action('ctrl_act9398')
def ctrl_nm9398():
    return 'ret9398' 

@action('ctrl_act9399')
def ctrl_nm9399():
    return 'ret9399' 

@action('ctrl_act9400')
def ctrl_nm9400():
    return 'ret9400' 

@action('ctrl_act9401')
def ctrl_nm9401():
    return 'ret9401' 

@action('ctrl_act9402')
def ctrl_nm9402():
    return 'ret9402' 

@action('ctrl_act9403')
def ctrl_nm9403():
    return 'ret9403' 

@action('ctrl_act9404')
def ctrl_nm9404():
    return 'ret9404' 

@action('ctrl_act9405')
def ctrl_nm9405():
    return 'ret9405' 

@action('ctrl_act9406')
def ctrl_nm9406():
    return 'ret9406' 

@action('ctrl_act9407')
def ctrl_nm9407():
    return 'ret9407' 

@action('ctrl_act9408')
def ctrl_nm9408():
    return 'ret9408' 

@action('ctrl_act9409')
def ctrl_nm9409():
    return 'ret9409' 

@action('ctrl_act9410')
def ctrl_nm9410():
    return 'ret9410' 

@action('ctrl_act9411')
def ctrl_nm9411():
    return 'ret9411' 

@action('ctrl_act9412')
def ctrl_nm9412():
    return 'ret9412' 

@action('ctrl_act9413')
def ctrl_nm9413():
    return 'ret9413' 

@action('ctrl_act9414')
def ctrl_nm9414():
    return 'ret9414' 

@action('ctrl_act9415')
def ctrl_nm9415():
    return 'ret9415' 

@action('ctrl_act9416')
def ctrl_nm9416():
    return 'ret9416' 

@action('ctrl_act9417')
def ctrl_nm9417():
    return 'ret9417' 

@action('ctrl_act9418')
def ctrl_nm9418():
    return 'ret9418' 

@action('ctrl_act9419')
def ctrl_nm9419():
    return 'ret9419' 

@action('ctrl_act9420')
def ctrl_nm9420():
    return 'ret9420' 

@action('ctrl_act9421')
def ctrl_nm9421():
    return 'ret9421' 

@action('ctrl_act9422')
def ctrl_nm9422():
    return 'ret9422' 

@action('ctrl_act9423')
def ctrl_nm9423():
    return 'ret9423' 

@action('ctrl_act9424')
def ctrl_nm9424():
    return 'ret9424' 

@action('ctrl_act9425')
def ctrl_nm9425():
    return 'ret9425' 

@action('ctrl_act9426')
def ctrl_nm9426():
    return 'ret9426' 

@action('ctrl_act9427')
def ctrl_nm9427():
    return 'ret9427' 

@action('ctrl_act9428')
def ctrl_nm9428():
    return 'ret9428' 

@action('ctrl_act9429')
def ctrl_nm9429():
    return 'ret9429' 

@action('ctrl_act9430')
def ctrl_nm9430():
    return 'ret9430' 

@action('ctrl_act9431')
def ctrl_nm9431():
    return 'ret9431' 

@action('ctrl_act9432')
def ctrl_nm9432():
    return 'ret9432' 

@action('ctrl_act9433')
def ctrl_nm9433():
    return 'ret9433' 

@action('ctrl_act9434')
def ctrl_nm9434():
    return 'ret9434' 

@action('ctrl_act9435')
def ctrl_nm9435():
    return 'ret9435' 

@action('ctrl_act9436')
def ctrl_nm9436():
    return 'ret9436' 

@action('ctrl_act9437')
def ctrl_nm9437():
    return 'ret9437' 

@action('ctrl_act9438')
def ctrl_nm9438():
    return 'ret9438' 

@action('ctrl_act9439')
def ctrl_nm9439():
    return 'ret9439' 

@action('ctrl_act9440')
def ctrl_nm9440():
    return 'ret9440' 

@action('ctrl_act9441')
def ctrl_nm9441():
    return 'ret9441' 

@action('ctrl_act9442')
def ctrl_nm9442():
    return 'ret9442' 

@action('ctrl_act9443')
def ctrl_nm9443():
    return 'ret9443' 

@action('ctrl_act9444')
def ctrl_nm9444():
    return 'ret9444' 

@action('ctrl_act9445')
def ctrl_nm9445():
    return 'ret9445' 

@action('ctrl_act9446')
def ctrl_nm9446():
    return 'ret9446' 

@action('ctrl_act9447')
def ctrl_nm9447():
    return 'ret9447' 

@action('ctrl_act9448')
def ctrl_nm9448():
    return 'ret9448' 

@action('ctrl_act9449')
def ctrl_nm9449():
    return 'ret9449' 

@action('ctrl_act9450')
def ctrl_nm9450():
    return 'ret9450' 

@action('ctrl_act9451')
def ctrl_nm9451():
    return 'ret9451' 

@action('ctrl_act9452')
def ctrl_nm9452():
    return 'ret9452' 

@action('ctrl_act9453')
def ctrl_nm9453():
    return 'ret9453' 

@action('ctrl_act9454')
def ctrl_nm9454():
    return 'ret9454' 

@action('ctrl_act9455')
def ctrl_nm9455():
    return 'ret9455' 

@action('ctrl_act9456')
def ctrl_nm9456():
    return 'ret9456' 

@action('ctrl_act9457')
def ctrl_nm9457():
    return 'ret9457' 

@action('ctrl_act9458')
def ctrl_nm9458():
    return 'ret9458' 

@action('ctrl_act9459')
def ctrl_nm9459():
    return 'ret9459' 

@action('ctrl_act9460')
def ctrl_nm9460():
    return 'ret9460' 

@action('ctrl_act9461')
def ctrl_nm9461():
    return 'ret9461' 

@action('ctrl_act9462')
def ctrl_nm9462():
    return 'ret9462' 

@action('ctrl_act9463')
def ctrl_nm9463():
    return 'ret9463' 

@action('ctrl_act9464')
def ctrl_nm9464():
    return 'ret9464' 

@action('ctrl_act9465')
def ctrl_nm9465():
    return 'ret9465' 

@action('ctrl_act9466')
def ctrl_nm9466():
    return 'ret9466' 

@action('ctrl_act9467')
def ctrl_nm9467():
    return 'ret9467' 

@action('ctrl_act9468')
def ctrl_nm9468():
    return 'ret9468' 

@action('ctrl_act9469')
def ctrl_nm9469():
    return 'ret9469' 

@action('ctrl_act9470')
def ctrl_nm9470():
    return 'ret9470' 

@action('ctrl_act9471')
def ctrl_nm9471():
    return 'ret9471' 

@action('ctrl_act9472')
def ctrl_nm9472():
    return 'ret9472' 

@action('ctrl_act9473')
def ctrl_nm9473():
    return 'ret9473' 

@action('ctrl_act9474')
def ctrl_nm9474():
    return 'ret9474' 

@action('ctrl_act9475')
def ctrl_nm9475():
    return 'ret9475' 

@action('ctrl_act9476')
def ctrl_nm9476():
    return 'ret9476' 

@action('ctrl_act9477')
def ctrl_nm9477():
    return 'ret9477' 

@action('ctrl_act9478')
def ctrl_nm9478():
    return 'ret9478' 

@action('ctrl_act9479')
def ctrl_nm9479():
    return 'ret9479' 

@action('ctrl_act9480')
def ctrl_nm9480():
    return 'ret9480' 

@action('ctrl_act9481')
def ctrl_nm9481():
    return 'ret9481' 

@action('ctrl_act9482')
def ctrl_nm9482():
    return 'ret9482' 

@action('ctrl_act9483')
def ctrl_nm9483():
    return 'ret9483' 

@action('ctrl_act9484')
def ctrl_nm9484():
    return 'ret9484' 

@action('ctrl_act9485')
def ctrl_nm9485():
    return 'ret9485' 

@action('ctrl_act9486')
def ctrl_nm9486():
    return 'ret9486' 

@action('ctrl_act9487')
def ctrl_nm9487():
    return 'ret9487' 

@action('ctrl_act9488')
def ctrl_nm9488():
    return 'ret9488' 

@action('ctrl_act9489')
def ctrl_nm9489():
    return 'ret9489' 

@action('ctrl_act9490')
def ctrl_nm9490():
    return 'ret9490' 

@action('ctrl_act9491')
def ctrl_nm9491():
    return 'ret9491' 

@action('ctrl_act9492')
def ctrl_nm9492():
    return 'ret9492' 

@action('ctrl_act9493')
def ctrl_nm9493():
    return 'ret9493' 

@action('ctrl_act9494')
def ctrl_nm9494():
    return 'ret9494' 

@action('ctrl_act9495')
def ctrl_nm9495():
    return 'ret9495' 

@action('ctrl_act9496')
def ctrl_nm9496():
    return 'ret9496' 

@action('ctrl_act9497')
def ctrl_nm9497():
    return 'ret9497' 

@action('ctrl_act9498')
def ctrl_nm9498():
    return 'ret9498' 

@action('ctrl_act9499')
def ctrl_nm9499():
    return 'ret9499' 

@action('ctrl_act9500')
def ctrl_nm9500():
    return 'ret9500' 

@action('ctrl_act9501')
def ctrl_nm9501():
    return 'ret9501' 

@action('ctrl_act9502')
def ctrl_nm9502():
    return 'ret9502' 

@action('ctrl_act9503')
def ctrl_nm9503():
    return 'ret9503' 

@action('ctrl_act9504')
def ctrl_nm9504():
    return 'ret9504' 

@action('ctrl_act9505')
def ctrl_nm9505():
    return 'ret9505' 

@action('ctrl_act9506')
def ctrl_nm9506():
    return 'ret9506' 

@action('ctrl_act9507')
def ctrl_nm9507():
    return 'ret9507' 

@action('ctrl_act9508')
def ctrl_nm9508():
    return 'ret9508' 

@action('ctrl_act9509')
def ctrl_nm9509():
    return 'ret9509' 

@action('ctrl_act9510')
def ctrl_nm9510():
    return 'ret9510' 

@action('ctrl_act9511')
def ctrl_nm9511():
    return 'ret9511' 

@action('ctrl_act9512')
def ctrl_nm9512():
    return 'ret9512' 

@action('ctrl_act9513')
def ctrl_nm9513():
    return 'ret9513' 

@action('ctrl_act9514')
def ctrl_nm9514():
    return 'ret9514' 

@action('ctrl_act9515')
def ctrl_nm9515():
    return 'ret9515' 

@action('ctrl_act9516')
def ctrl_nm9516():
    return 'ret9516' 

@action('ctrl_act9517')
def ctrl_nm9517():
    return 'ret9517' 

@action('ctrl_act9518')
def ctrl_nm9518():
    return 'ret9518' 

@action('ctrl_act9519')
def ctrl_nm9519():
    return 'ret9519' 

@action('ctrl_act9520')
def ctrl_nm9520():
    return 'ret9520' 

@action('ctrl_act9521')
def ctrl_nm9521():
    return 'ret9521' 

@action('ctrl_act9522')
def ctrl_nm9522():
    return 'ret9522' 

@action('ctrl_act9523')
def ctrl_nm9523():
    return 'ret9523' 

@action('ctrl_act9524')
def ctrl_nm9524():
    return 'ret9524' 

@action('ctrl_act9525')
def ctrl_nm9525():
    return 'ret9525' 

@action('ctrl_act9526')
def ctrl_nm9526():
    return 'ret9526' 

@action('ctrl_act9527')
def ctrl_nm9527():
    return 'ret9527' 

@action('ctrl_act9528')
def ctrl_nm9528():
    return 'ret9528' 

@action('ctrl_act9529')
def ctrl_nm9529():
    return 'ret9529' 

@action('ctrl_act9530')
def ctrl_nm9530():
    return 'ret9530' 

@action('ctrl_act9531')
def ctrl_nm9531():
    return 'ret9531' 

@action('ctrl_act9532')
def ctrl_nm9532():
    return 'ret9532' 

@action('ctrl_act9533')
def ctrl_nm9533():
    return 'ret9533' 

@action('ctrl_act9534')
def ctrl_nm9534():
    return 'ret9534' 

@action('ctrl_act9535')
def ctrl_nm9535():
    return 'ret9535' 

@action('ctrl_act9536')
def ctrl_nm9536():
    return 'ret9536' 

@action('ctrl_act9537')
def ctrl_nm9537():
    return 'ret9537' 

@action('ctrl_act9538')
def ctrl_nm9538():
    return 'ret9538' 

@action('ctrl_act9539')
def ctrl_nm9539():
    return 'ret9539' 

@action('ctrl_act9540')
def ctrl_nm9540():
    return 'ret9540' 

@action('ctrl_act9541')
def ctrl_nm9541():
    return 'ret9541' 

@action('ctrl_act9542')
def ctrl_nm9542():
    return 'ret9542' 

@action('ctrl_act9543')
def ctrl_nm9543():
    return 'ret9543' 

@action('ctrl_act9544')
def ctrl_nm9544():
    return 'ret9544' 

@action('ctrl_act9545')
def ctrl_nm9545():
    return 'ret9545' 

@action('ctrl_act9546')
def ctrl_nm9546():
    return 'ret9546' 

@action('ctrl_act9547')
def ctrl_nm9547():
    return 'ret9547' 

@action('ctrl_act9548')
def ctrl_nm9548():
    return 'ret9548' 

@action('ctrl_act9549')
def ctrl_nm9549():
    return 'ret9549' 

@action('ctrl_act9550')
def ctrl_nm9550():
    return 'ret9550' 

@action('ctrl_act9551')
def ctrl_nm9551():
    return 'ret9551' 

@action('ctrl_act9552')
def ctrl_nm9552():
    return 'ret9552' 

@action('ctrl_act9553')
def ctrl_nm9553():
    return 'ret9553' 

@action('ctrl_act9554')
def ctrl_nm9554():
    return 'ret9554' 

@action('ctrl_act9555')
def ctrl_nm9555():
    return 'ret9555' 

@action('ctrl_act9556')
def ctrl_nm9556():
    return 'ret9556' 

@action('ctrl_act9557')
def ctrl_nm9557():
    return 'ret9557' 

@action('ctrl_act9558')
def ctrl_nm9558():
    return 'ret9558' 

@action('ctrl_act9559')
def ctrl_nm9559():
    return 'ret9559' 

@action('ctrl_act9560')
def ctrl_nm9560():
    return 'ret9560' 

@action('ctrl_act9561')
def ctrl_nm9561():
    return 'ret9561' 

@action('ctrl_act9562')
def ctrl_nm9562():
    return 'ret9562' 

@action('ctrl_act9563')
def ctrl_nm9563():
    return 'ret9563' 

@action('ctrl_act9564')
def ctrl_nm9564():
    return 'ret9564' 

@action('ctrl_act9565')
def ctrl_nm9565():
    return 'ret9565' 

@action('ctrl_act9566')
def ctrl_nm9566():
    return 'ret9566' 

@action('ctrl_act9567')
def ctrl_nm9567():
    return 'ret9567' 

@action('ctrl_act9568')
def ctrl_nm9568():
    return 'ret9568' 

@action('ctrl_act9569')
def ctrl_nm9569():
    return 'ret9569' 

@action('ctrl_act9570')
def ctrl_nm9570():
    return 'ret9570' 

@action('ctrl_act9571')
def ctrl_nm9571():
    return 'ret9571' 

@action('ctrl_act9572')
def ctrl_nm9572():
    return 'ret9572' 

@action('ctrl_act9573')
def ctrl_nm9573():
    return 'ret9573' 

@action('ctrl_act9574')
def ctrl_nm9574():
    return 'ret9574' 

@action('ctrl_act9575')
def ctrl_nm9575():
    return 'ret9575' 

@action('ctrl_act9576')
def ctrl_nm9576():
    return 'ret9576' 

@action('ctrl_act9577')
def ctrl_nm9577():
    return 'ret9577' 

@action('ctrl_act9578')
def ctrl_nm9578():
    return 'ret9578' 

@action('ctrl_act9579')
def ctrl_nm9579():
    return 'ret9579' 

@action('ctrl_act9580')
def ctrl_nm9580():
    return 'ret9580' 

@action('ctrl_act9581')
def ctrl_nm9581():
    return 'ret9581' 

@action('ctrl_act9582')
def ctrl_nm9582():
    return 'ret9582' 

@action('ctrl_act9583')
def ctrl_nm9583():
    return 'ret9583' 

@action('ctrl_act9584')
def ctrl_nm9584():
    return 'ret9584' 

@action('ctrl_act9585')
def ctrl_nm9585():
    return 'ret9585' 

@action('ctrl_act9586')
def ctrl_nm9586():
    return 'ret9586' 

@action('ctrl_act9587')
def ctrl_nm9587():
    return 'ret9587' 

@action('ctrl_act9588')
def ctrl_nm9588():
    return 'ret9588' 

@action('ctrl_act9589')
def ctrl_nm9589():
    return 'ret9589' 

@action('ctrl_act9590')
def ctrl_nm9590():
    return 'ret9590' 

@action('ctrl_act9591')
def ctrl_nm9591():
    return 'ret9591' 

@action('ctrl_act9592')
def ctrl_nm9592():
    return 'ret9592' 

@action('ctrl_act9593')
def ctrl_nm9593():
    return 'ret9593' 

@action('ctrl_act9594')
def ctrl_nm9594():
    return 'ret9594' 

@action('ctrl_act9595')
def ctrl_nm9595():
    return 'ret9595' 

@action('ctrl_act9596')
def ctrl_nm9596():
    return 'ret9596' 

@action('ctrl_act9597')
def ctrl_nm9597():
    return 'ret9597' 

@action('ctrl_act9598')
def ctrl_nm9598():
    return 'ret9598' 

@action('ctrl_act9599')
def ctrl_nm9599():
    return 'ret9599' 

@action('ctrl_act9600')
def ctrl_nm9600():
    return 'ret9600' 

@action('ctrl_act9601')
def ctrl_nm9601():
    return 'ret9601' 

@action('ctrl_act9602')
def ctrl_nm9602():
    return 'ret9602' 

@action('ctrl_act9603')
def ctrl_nm9603():
    return 'ret9603' 

@action('ctrl_act9604')
def ctrl_nm9604():
    return 'ret9604' 

@action('ctrl_act9605')
def ctrl_nm9605():
    return 'ret9605' 

@action('ctrl_act9606')
def ctrl_nm9606():
    return 'ret9606' 

@action('ctrl_act9607')
def ctrl_nm9607():
    return 'ret9607' 

@action('ctrl_act9608')
def ctrl_nm9608():
    return 'ret9608' 

@action('ctrl_act9609')
def ctrl_nm9609():
    return 'ret9609' 

@action('ctrl_act9610')
def ctrl_nm9610():
    return 'ret9610' 

@action('ctrl_act9611')
def ctrl_nm9611():
    return 'ret9611' 

@action('ctrl_act9612')
def ctrl_nm9612():
    return 'ret9612' 

@action('ctrl_act9613')
def ctrl_nm9613():
    return 'ret9613' 

@action('ctrl_act9614')
def ctrl_nm9614():
    return 'ret9614' 

@action('ctrl_act9615')
def ctrl_nm9615():
    return 'ret9615' 

@action('ctrl_act9616')
def ctrl_nm9616():
    return 'ret9616' 

@action('ctrl_act9617')
def ctrl_nm9617():
    return 'ret9617' 

@action('ctrl_act9618')
def ctrl_nm9618():
    return 'ret9618' 

@action('ctrl_act9619')
def ctrl_nm9619():
    return 'ret9619' 

@action('ctrl_act9620')
def ctrl_nm9620():
    return 'ret9620' 

@action('ctrl_act9621')
def ctrl_nm9621():
    return 'ret9621' 

@action('ctrl_act9622')
def ctrl_nm9622():
    return 'ret9622' 

@action('ctrl_act9623')
def ctrl_nm9623():
    return 'ret9623' 

@action('ctrl_act9624')
def ctrl_nm9624():
    return 'ret9624' 

@action('ctrl_act9625')
def ctrl_nm9625():
    return 'ret9625' 

@action('ctrl_act9626')
def ctrl_nm9626():
    return 'ret9626' 

@action('ctrl_act9627')
def ctrl_nm9627():
    return 'ret9627' 

@action('ctrl_act9628')
def ctrl_nm9628():
    return 'ret9628' 

@action('ctrl_act9629')
def ctrl_nm9629():
    return 'ret9629' 

@action('ctrl_act9630')
def ctrl_nm9630():
    return 'ret9630' 

@action('ctrl_act9631')
def ctrl_nm9631():
    return 'ret9631' 

@action('ctrl_act9632')
def ctrl_nm9632():
    return 'ret9632' 

@action('ctrl_act9633')
def ctrl_nm9633():
    return 'ret9633' 

@action('ctrl_act9634')
def ctrl_nm9634():
    return 'ret9634' 

@action('ctrl_act9635')
def ctrl_nm9635():
    return 'ret9635' 

@action('ctrl_act9636')
def ctrl_nm9636():
    return 'ret9636' 

@action('ctrl_act9637')
def ctrl_nm9637():
    return 'ret9637' 

@action('ctrl_act9638')
def ctrl_nm9638():
    return 'ret9638' 

@action('ctrl_act9639')
def ctrl_nm9639():
    return 'ret9639' 

@action('ctrl_act9640')
def ctrl_nm9640():
    return 'ret9640' 

@action('ctrl_act9641')
def ctrl_nm9641():
    return 'ret9641' 

@action('ctrl_act9642')
def ctrl_nm9642():
    return 'ret9642' 

@action('ctrl_act9643')
def ctrl_nm9643():
    return 'ret9643' 

@action('ctrl_act9644')
def ctrl_nm9644():
    return 'ret9644' 

@action('ctrl_act9645')
def ctrl_nm9645():
    return 'ret9645' 

@action('ctrl_act9646')
def ctrl_nm9646():
    return 'ret9646' 

@action('ctrl_act9647')
def ctrl_nm9647():
    return 'ret9647' 

@action('ctrl_act9648')
def ctrl_nm9648():
    return 'ret9648' 

@action('ctrl_act9649')
def ctrl_nm9649():
    return 'ret9649' 

@action('ctrl_act9650')
def ctrl_nm9650():
    return 'ret9650' 

@action('ctrl_act9651')
def ctrl_nm9651():
    return 'ret9651' 

@action('ctrl_act9652')
def ctrl_nm9652():
    return 'ret9652' 

@action('ctrl_act9653')
def ctrl_nm9653():
    return 'ret9653' 

@action('ctrl_act9654')
def ctrl_nm9654():
    return 'ret9654' 

@action('ctrl_act9655')
def ctrl_nm9655():
    return 'ret9655' 

@action('ctrl_act9656')
def ctrl_nm9656():
    return 'ret9656' 

@action('ctrl_act9657')
def ctrl_nm9657():
    return 'ret9657' 

@action('ctrl_act9658')
def ctrl_nm9658():
    return 'ret9658' 

@action('ctrl_act9659')
def ctrl_nm9659():
    return 'ret9659' 

@action('ctrl_act9660')
def ctrl_nm9660():
    return 'ret9660' 

@action('ctrl_act9661')
def ctrl_nm9661():
    return 'ret9661' 

@action('ctrl_act9662')
def ctrl_nm9662():
    return 'ret9662' 

@action('ctrl_act9663')
def ctrl_nm9663():
    return 'ret9663' 

@action('ctrl_act9664')
def ctrl_nm9664():
    return 'ret9664' 

@action('ctrl_act9665')
def ctrl_nm9665():
    return 'ret9665' 

@action('ctrl_act9666')
def ctrl_nm9666():
    return 'ret9666' 

@action('ctrl_act9667')
def ctrl_nm9667():
    return 'ret9667' 

@action('ctrl_act9668')
def ctrl_nm9668():
    return 'ret9668' 

@action('ctrl_act9669')
def ctrl_nm9669():
    return 'ret9669' 

@action('ctrl_act9670')
def ctrl_nm9670():
    return 'ret9670' 

@action('ctrl_act9671')
def ctrl_nm9671():
    return 'ret9671' 

@action('ctrl_act9672')
def ctrl_nm9672():
    return 'ret9672' 

@action('ctrl_act9673')
def ctrl_nm9673():
    return 'ret9673' 

@action('ctrl_act9674')
def ctrl_nm9674():
    return 'ret9674' 

@action('ctrl_act9675')
def ctrl_nm9675():
    return 'ret9675' 

@action('ctrl_act9676')
def ctrl_nm9676():
    return 'ret9676' 

@action('ctrl_act9677')
def ctrl_nm9677():
    return 'ret9677' 

@action('ctrl_act9678')
def ctrl_nm9678():
    return 'ret9678' 

@action('ctrl_act9679')
def ctrl_nm9679():
    return 'ret9679' 

@action('ctrl_act9680')
def ctrl_nm9680():
    return 'ret9680' 

@action('ctrl_act9681')
def ctrl_nm9681():
    return 'ret9681' 

@action('ctrl_act9682')
def ctrl_nm9682():
    return 'ret9682' 

@action('ctrl_act9683')
def ctrl_nm9683():
    return 'ret9683' 

@action('ctrl_act9684')
def ctrl_nm9684():
    return 'ret9684' 

@action('ctrl_act9685')
def ctrl_nm9685():
    return 'ret9685' 

@action('ctrl_act9686')
def ctrl_nm9686():
    return 'ret9686' 

@action('ctrl_act9687')
def ctrl_nm9687():
    return 'ret9687' 

@action('ctrl_act9688')
def ctrl_nm9688():
    return 'ret9688' 

@action('ctrl_act9689')
def ctrl_nm9689():
    return 'ret9689' 

@action('ctrl_act9690')
def ctrl_nm9690():
    return 'ret9690' 

@action('ctrl_act9691')
def ctrl_nm9691():
    return 'ret9691' 

@action('ctrl_act9692')
def ctrl_nm9692():
    return 'ret9692' 

@action('ctrl_act9693')
def ctrl_nm9693():
    return 'ret9693' 

@action('ctrl_act9694')
def ctrl_nm9694():
    return 'ret9694' 

@action('ctrl_act9695')
def ctrl_nm9695():
    return 'ret9695' 

@action('ctrl_act9696')
def ctrl_nm9696():
    return 'ret9696' 

@action('ctrl_act9697')
def ctrl_nm9697():
    return 'ret9697' 

@action('ctrl_act9698')
def ctrl_nm9698():
    return 'ret9698' 

@action('ctrl_act9699')
def ctrl_nm9699():
    return 'ret9699' 

@action('ctrl_act9700')
def ctrl_nm9700():
    return 'ret9700' 

@action('ctrl_act9701')
def ctrl_nm9701():
    return 'ret9701' 

@action('ctrl_act9702')
def ctrl_nm9702():
    return 'ret9702' 

@action('ctrl_act9703')
def ctrl_nm9703():
    return 'ret9703' 

@action('ctrl_act9704')
def ctrl_nm9704():
    return 'ret9704' 

@action('ctrl_act9705')
def ctrl_nm9705():
    return 'ret9705' 

@action('ctrl_act9706')
def ctrl_nm9706():
    return 'ret9706' 

@action('ctrl_act9707')
def ctrl_nm9707():
    return 'ret9707' 

@action('ctrl_act9708')
def ctrl_nm9708():
    return 'ret9708' 

@action('ctrl_act9709')
def ctrl_nm9709():
    return 'ret9709' 

@action('ctrl_act9710')
def ctrl_nm9710():
    return 'ret9710' 

@action('ctrl_act9711')
def ctrl_nm9711():
    return 'ret9711' 

@action('ctrl_act9712')
def ctrl_nm9712():
    return 'ret9712' 

@action('ctrl_act9713')
def ctrl_nm9713():
    return 'ret9713' 

@action('ctrl_act9714')
def ctrl_nm9714():
    return 'ret9714' 

@action('ctrl_act9715')
def ctrl_nm9715():
    return 'ret9715' 

@action('ctrl_act9716')
def ctrl_nm9716():
    return 'ret9716' 

@action('ctrl_act9717')
def ctrl_nm9717():
    return 'ret9717' 

@action('ctrl_act9718')
def ctrl_nm9718():
    return 'ret9718' 

@action('ctrl_act9719')
def ctrl_nm9719():
    return 'ret9719' 

@action('ctrl_act9720')
def ctrl_nm9720():
    return 'ret9720' 

@action('ctrl_act9721')
def ctrl_nm9721():
    return 'ret9721' 

@action('ctrl_act9722')
def ctrl_nm9722():
    return 'ret9722' 

@action('ctrl_act9723')
def ctrl_nm9723():
    return 'ret9723' 

@action('ctrl_act9724')
def ctrl_nm9724():
    return 'ret9724' 

@action('ctrl_act9725')
def ctrl_nm9725():
    return 'ret9725' 

@action('ctrl_act9726')
def ctrl_nm9726():
    return 'ret9726' 

@action('ctrl_act9727')
def ctrl_nm9727():
    return 'ret9727' 

@action('ctrl_act9728')
def ctrl_nm9728():
    return 'ret9728' 

@action('ctrl_act9729')
def ctrl_nm9729():
    return 'ret9729' 

@action('ctrl_act9730')
def ctrl_nm9730():
    return 'ret9730' 

@action('ctrl_act9731')
def ctrl_nm9731():
    return 'ret9731' 

@action('ctrl_act9732')
def ctrl_nm9732():
    return 'ret9732' 

@action('ctrl_act9733')
def ctrl_nm9733():
    return 'ret9733' 

@action('ctrl_act9734')
def ctrl_nm9734():
    return 'ret9734' 

@action('ctrl_act9735')
def ctrl_nm9735():
    return 'ret9735' 

@action('ctrl_act9736')
def ctrl_nm9736():
    return 'ret9736' 

@action('ctrl_act9737')
def ctrl_nm9737():
    return 'ret9737' 

@action('ctrl_act9738')
def ctrl_nm9738():
    return 'ret9738' 

@action('ctrl_act9739')
def ctrl_nm9739():
    return 'ret9739' 

@action('ctrl_act9740')
def ctrl_nm9740():
    return 'ret9740' 

@action('ctrl_act9741')
def ctrl_nm9741():
    return 'ret9741' 

@action('ctrl_act9742')
def ctrl_nm9742():
    return 'ret9742' 

@action('ctrl_act9743')
def ctrl_nm9743():
    return 'ret9743' 

@action('ctrl_act9744')
def ctrl_nm9744():
    return 'ret9744' 

@action('ctrl_act9745')
def ctrl_nm9745():
    return 'ret9745' 

@action('ctrl_act9746')
def ctrl_nm9746():
    return 'ret9746' 

@action('ctrl_act9747')
def ctrl_nm9747():
    return 'ret9747' 

@action('ctrl_act9748')
def ctrl_nm9748():
    return 'ret9748' 

@action('ctrl_act9749')
def ctrl_nm9749():
    return 'ret9749' 

@action('ctrl_act9750')
def ctrl_nm9750():
    return 'ret9750' 

@action('ctrl_act9751')
def ctrl_nm9751():
    return 'ret9751' 

@action('ctrl_act9752')
def ctrl_nm9752():
    return 'ret9752' 

@action('ctrl_act9753')
def ctrl_nm9753():
    return 'ret9753' 

@action('ctrl_act9754')
def ctrl_nm9754():
    return 'ret9754' 

@action('ctrl_act9755')
def ctrl_nm9755():
    return 'ret9755' 

@action('ctrl_act9756')
def ctrl_nm9756():
    return 'ret9756' 

@action('ctrl_act9757')
def ctrl_nm9757():
    return 'ret9757' 

@action('ctrl_act9758')
def ctrl_nm9758():
    return 'ret9758' 

@action('ctrl_act9759')
def ctrl_nm9759():
    return 'ret9759' 

@action('ctrl_act9760')
def ctrl_nm9760():
    return 'ret9760' 

@action('ctrl_act9761')
def ctrl_nm9761():
    return 'ret9761' 

@action('ctrl_act9762')
def ctrl_nm9762():
    return 'ret9762' 

@action('ctrl_act9763')
def ctrl_nm9763():
    return 'ret9763' 

@action('ctrl_act9764')
def ctrl_nm9764():
    return 'ret9764' 

@action('ctrl_act9765')
def ctrl_nm9765():
    return 'ret9765' 

@action('ctrl_act9766')
def ctrl_nm9766():
    return 'ret9766' 

@action('ctrl_act9767')
def ctrl_nm9767():
    return 'ret9767' 

@action('ctrl_act9768')
def ctrl_nm9768():
    return 'ret9768' 

@action('ctrl_act9769')
def ctrl_nm9769():
    return 'ret9769' 

@action('ctrl_act9770')
def ctrl_nm9770():
    return 'ret9770' 

@action('ctrl_act9771')
def ctrl_nm9771():
    return 'ret9771' 

@action('ctrl_act9772')
def ctrl_nm9772():
    return 'ret9772' 

@action('ctrl_act9773')
def ctrl_nm9773():
    return 'ret9773' 

@action('ctrl_act9774')
def ctrl_nm9774():
    return 'ret9774' 

@action('ctrl_act9775')
def ctrl_nm9775():
    return 'ret9775' 

@action('ctrl_act9776')
def ctrl_nm9776():
    return 'ret9776' 

@action('ctrl_act9777')
def ctrl_nm9777():
    return 'ret9777' 

@action('ctrl_act9778')
def ctrl_nm9778():
    return 'ret9778' 

@action('ctrl_act9779')
def ctrl_nm9779():
    return 'ret9779' 

@action('ctrl_act9780')
def ctrl_nm9780():
    return 'ret9780' 

@action('ctrl_act9781')
def ctrl_nm9781():
    return 'ret9781' 

@action('ctrl_act9782')
def ctrl_nm9782():
    return 'ret9782' 

@action('ctrl_act9783')
def ctrl_nm9783():
    return 'ret9783' 

@action('ctrl_act9784')
def ctrl_nm9784():
    return 'ret9784' 

@action('ctrl_act9785')
def ctrl_nm9785():
    return 'ret9785' 

@action('ctrl_act9786')
def ctrl_nm9786():
    return 'ret9786' 

@action('ctrl_act9787')
def ctrl_nm9787():
    return 'ret9787' 

@action('ctrl_act9788')
def ctrl_nm9788():
    return 'ret9788' 

@action('ctrl_act9789')
def ctrl_nm9789():
    return 'ret9789' 

@action('ctrl_act9790')
def ctrl_nm9790():
    return 'ret9790' 

@action('ctrl_act9791')
def ctrl_nm9791():
    return 'ret9791' 

@action('ctrl_act9792')
def ctrl_nm9792():
    return 'ret9792' 

@action('ctrl_act9793')
def ctrl_nm9793():
    return 'ret9793' 

@action('ctrl_act9794')
def ctrl_nm9794():
    return 'ret9794' 

@action('ctrl_act9795')
def ctrl_nm9795():
    return 'ret9795' 

@action('ctrl_act9796')
def ctrl_nm9796():
    return 'ret9796' 

@action('ctrl_act9797')
def ctrl_nm9797():
    return 'ret9797' 

@action('ctrl_act9798')
def ctrl_nm9798():
    return 'ret9798' 

@action('ctrl_act9799')
def ctrl_nm9799():
    return 'ret9799' 

@action('ctrl_act9800')
def ctrl_nm9800():
    return 'ret9800' 

@action('ctrl_act9801')
def ctrl_nm9801():
    return 'ret9801' 

@action('ctrl_act9802')
def ctrl_nm9802():
    return 'ret9802' 

@action('ctrl_act9803')
def ctrl_nm9803():
    return 'ret9803' 

@action('ctrl_act9804')
def ctrl_nm9804():
    return 'ret9804' 

@action('ctrl_act9805')
def ctrl_nm9805():
    return 'ret9805' 

@action('ctrl_act9806')
def ctrl_nm9806():
    return 'ret9806' 

@action('ctrl_act9807')
def ctrl_nm9807():
    return 'ret9807' 

@action('ctrl_act9808')
def ctrl_nm9808():
    return 'ret9808' 

@action('ctrl_act9809')
def ctrl_nm9809():
    return 'ret9809' 

@action('ctrl_act9810')
def ctrl_nm9810():
    return 'ret9810' 

@action('ctrl_act9811')
def ctrl_nm9811():
    return 'ret9811' 

@action('ctrl_act9812')
def ctrl_nm9812():
    return 'ret9812' 

@action('ctrl_act9813')
def ctrl_nm9813():
    return 'ret9813' 

@action('ctrl_act9814')
def ctrl_nm9814():
    return 'ret9814' 

@action('ctrl_act9815')
def ctrl_nm9815():
    return 'ret9815' 

@action('ctrl_act9816')
def ctrl_nm9816():
    return 'ret9816' 

@action('ctrl_act9817')
def ctrl_nm9817():
    return 'ret9817' 

@action('ctrl_act9818')
def ctrl_nm9818():
    return 'ret9818' 

@action('ctrl_act9819')
def ctrl_nm9819():
    return 'ret9819' 

@action('ctrl_act9820')
def ctrl_nm9820():
    return 'ret9820' 

@action('ctrl_act9821')
def ctrl_nm9821():
    return 'ret9821' 

@action('ctrl_act9822')
def ctrl_nm9822():
    return 'ret9822' 

@action('ctrl_act9823')
def ctrl_nm9823():
    return 'ret9823' 

@action('ctrl_act9824')
def ctrl_nm9824():
    return 'ret9824' 

@action('ctrl_act9825')
def ctrl_nm9825():
    return 'ret9825' 

@action('ctrl_act9826')
def ctrl_nm9826():
    return 'ret9826' 

@action('ctrl_act9827')
def ctrl_nm9827():
    return 'ret9827' 

@action('ctrl_act9828')
def ctrl_nm9828():
    return 'ret9828' 

@action('ctrl_act9829')
def ctrl_nm9829():
    return 'ret9829' 

@action('ctrl_act9830')
def ctrl_nm9830():
    return 'ret9830' 

@action('ctrl_act9831')
def ctrl_nm9831():
    return 'ret9831' 

@action('ctrl_act9832')
def ctrl_nm9832():
    return 'ret9832' 

@action('ctrl_act9833')
def ctrl_nm9833():
    return 'ret9833' 

@action('ctrl_act9834')
def ctrl_nm9834():
    return 'ret9834' 

@action('ctrl_act9835')
def ctrl_nm9835():
    return 'ret9835' 

@action('ctrl_act9836')
def ctrl_nm9836():
    return 'ret9836' 

@action('ctrl_act9837')
def ctrl_nm9837():
    return 'ret9837' 

@action('ctrl_act9838')
def ctrl_nm9838():
    return 'ret9838' 

@action('ctrl_act9839')
def ctrl_nm9839():
    return 'ret9839' 

@action('ctrl_act9840')
def ctrl_nm9840():
    return 'ret9840' 

@action('ctrl_act9841')
def ctrl_nm9841():
    return 'ret9841' 

@action('ctrl_act9842')
def ctrl_nm9842():
    return 'ret9842' 

@action('ctrl_act9843')
def ctrl_nm9843():
    return 'ret9843' 

@action('ctrl_act9844')
def ctrl_nm9844():
    return 'ret9844' 

@action('ctrl_act9845')
def ctrl_nm9845():
    return 'ret9845' 

@action('ctrl_act9846')
def ctrl_nm9846():
    return 'ret9846' 

@action('ctrl_act9847')
def ctrl_nm9847():
    return 'ret9847' 

@action('ctrl_act9848')
def ctrl_nm9848():
    return 'ret9848' 

@action('ctrl_act9849')
def ctrl_nm9849():
    return 'ret9849' 

@action('ctrl_act9850')
def ctrl_nm9850():
    return 'ret9850' 

@action('ctrl_act9851')
def ctrl_nm9851():
    return 'ret9851' 

@action('ctrl_act9852')
def ctrl_nm9852():
    return 'ret9852' 

@action('ctrl_act9853')
def ctrl_nm9853():
    return 'ret9853' 

@action('ctrl_act9854')
def ctrl_nm9854():
    return 'ret9854' 

@action('ctrl_act9855')
def ctrl_nm9855():
    return 'ret9855' 

@action('ctrl_act9856')
def ctrl_nm9856():
    return 'ret9856' 

@action('ctrl_act9857')
def ctrl_nm9857():
    return 'ret9857' 

@action('ctrl_act9858')
def ctrl_nm9858():
    return 'ret9858' 

@action('ctrl_act9859')
def ctrl_nm9859():
    return 'ret9859' 

@action('ctrl_act9860')
def ctrl_nm9860():
    return 'ret9860' 

@action('ctrl_act9861')
def ctrl_nm9861():
    return 'ret9861' 

@action('ctrl_act9862')
def ctrl_nm9862():
    return 'ret9862' 

@action('ctrl_act9863')
def ctrl_nm9863():
    return 'ret9863' 

@action('ctrl_act9864')
def ctrl_nm9864():
    return 'ret9864' 

@action('ctrl_act9865')
def ctrl_nm9865():
    return 'ret9865' 

@action('ctrl_act9866')
def ctrl_nm9866():
    return 'ret9866' 

@action('ctrl_act9867')
def ctrl_nm9867():
    return 'ret9867' 

@action('ctrl_act9868')
def ctrl_nm9868():
    return 'ret9868' 

@action('ctrl_act9869')
def ctrl_nm9869():
    return 'ret9869' 

@action('ctrl_act9870')
def ctrl_nm9870():
    return 'ret9870' 

@action('ctrl_act9871')
def ctrl_nm9871():
    return 'ret9871' 

@action('ctrl_act9872')
def ctrl_nm9872():
    return 'ret9872' 

@action('ctrl_act9873')
def ctrl_nm9873():
    return 'ret9873' 

@action('ctrl_act9874')
def ctrl_nm9874():
    return 'ret9874' 

@action('ctrl_act9875')
def ctrl_nm9875():
    return 'ret9875' 

@action('ctrl_act9876')
def ctrl_nm9876():
    return 'ret9876' 

@action('ctrl_act9877')
def ctrl_nm9877():
    return 'ret9877' 

@action('ctrl_act9878')
def ctrl_nm9878():
    return 'ret9878' 

@action('ctrl_act9879')
def ctrl_nm9879():
    return 'ret9879' 

@action('ctrl_act9880')
def ctrl_nm9880():
    return 'ret9880' 

@action('ctrl_act9881')
def ctrl_nm9881():
    return 'ret9881' 

@action('ctrl_act9882')
def ctrl_nm9882():
    return 'ret9882' 

@action('ctrl_act9883')
def ctrl_nm9883():
    return 'ret9883' 

@action('ctrl_act9884')
def ctrl_nm9884():
    return 'ret9884' 

@action('ctrl_act9885')
def ctrl_nm9885():
    return 'ret9885' 

@action('ctrl_act9886')
def ctrl_nm9886():
    return 'ret9886' 

@action('ctrl_act9887')
def ctrl_nm9887():
    return 'ret9887' 

@action('ctrl_act9888')
def ctrl_nm9888():
    return 'ret9888' 

@action('ctrl_act9889')
def ctrl_nm9889():
    return 'ret9889' 

@action('ctrl_act9890')
def ctrl_nm9890():
    return 'ret9890' 

@action('ctrl_act9891')
def ctrl_nm9891():
    return 'ret9891' 

@action('ctrl_act9892')
def ctrl_nm9892():
    return 'ret9892' 

@action('ctrl_act9893')
def ctrl_nm9893():
    return 'ret9893' 

@action('ctrl_act9894')
def ctrl_nm9894():
    return 'ret9894' 

@action('ctrl_act9895')
def ctrl_nm9895():
    return 'ret9895' 

@action('ctrl_act9896')
def ctrl_nm9896():
    return 'ret9896' 

@action('ctrl_act9897')
def ctrl_nm9897():
    return 'ret9897' 

@action('ctrl_act9898')
def ctrl_nm9898():
    return 'ret9898' 

@action('ctrl_act9899')
def ctrl_nm9899():
    return 'ret9899' 

@action('ctrl_act9900')
def ctrl_nm9900():
    return 'ret9900' 

@action('ctrl_act9901')
def ctrl_nm9901():
    return 'ret9901' 

@action('ctrl_act9902')
def ctrl_nm9902():
    return 'ret9902' 

@action('ctrl_act9903')
def ctrl_nm9903():
    return 'ret9903' 

@action('ctrl_act9904')
def ctrl_nm9904():
    return 'ret9904' 

@action('ctrl_act9905')
def ctrl_nm9905():
    return 'ret9905' 

@action('ctrl_act9906')
def ctrl_nm9906():
    return 'ret9906' 

@action('ctrl_act9907')
def ctrl_nm9907():
    return 'ret9907' 

@action('ctrl_act9908')
def ctrl_nm9908():
    return 'ret9908' 

@action('ctrl_act9909')
def ctrl_nm9909():
    return 'ret9909' 

@action('ctrl_act9910')
def ctrl_nm9910():
    return 'ret9910' 

@action('ctrl_act9911')
def ctrl_nm9911():
    return 'ret9911' 

@action('ctrl_act9912')
def ctrl_nm9912():
    return 'ret9912' 

@action('ctrl_act9913')
def ctrl_nm9913():
    return 'ret9913' 

@action('ctrl_act9914')
def ctrl_nm9914():
    return 'ret9914' 

@action('ctrl_act9915')
def ctrl_nm9915():
    return 'ret9915' 

@action('ctrl_act9916')
def ctrl_nm9916():
    return 'ret9916' 

@action('ctrl_act9917')
def ctrl_nm9917():
    return 'ret9917' 

@action('ctrl_act9918')
def ctrl_nm9918():
    return 'ret9918' 

@action('ctrl_act9919')
def ctrl_nm9919():
    return 'ret9919' 

@action('ctrl_act9920')
def ctrl_nm9920():
    return 'ret9920' 

@action('ctrl_act9921')
def ctrl_nm9921():
    return 'ret9921' 

@action('ctrl_act9922')
def ctrl_nm9922():
    return 'ret9922' 

@action('ctrl_act9923')
def ctrl_nm9923():
    return 'ret9923' 

@action('ctrl_act9924')
def ctrl_nm9924():
    return 'ret9924' 

@action('ctrl_act9925')
def ctrl_nm9925():
    return 'ret9925' 

@action('ctrl_act9926')
def ctrl_nm9926():
    return 'ret9926' 

@action('ctrl_act9927')
def ctrl_nm9927():
    return 'ret9927' 

@action('ctrl_act9928')
def ctrl_nm9928():
    return 'ret9928' 

@action('ctrl_act9929')
def ctrl_nm9929():
    return 'ret9929' 

@action('ctrl_act9930')
def ctrl_nm9930():
    return 'ret9930' 

@action('ctrl_act9931')
def ctrl_nm9931():
    return 'ret9931' 

@action('ctrl_act9932')
def ctrl_nm9932():
    return 'ret9932' 

@action('ctrl_act9933')
def ctrl_nm9933():
    return 'ret9933' 

@action('ctrl_act9934')
def ctrl_nm9934():
    return 'ret9934' 

@action('ctrl_act9935')
def ctrl_nm9935():
    return 'ret9935' 

@action('ctrl_act9936')
def ctrl_nm9936():
    return 'ret9936' 

@action('ctrl_act9937')
def ctrl_nm9937():
    return 'ret9937' 

@action('ctrl_act9938')
def ctrl_nm9938():
    return 'ret9938' 

@action('ctrl_act9939')
def ctrl_nm9939():
    return 'ret9939' 

@action('ctrl_act9940')
def ctrl_nm9940():
    return 'ret9940' 

@action('ctrl_act9941')
def ctrl_nm9941():
    return 'ret9941' 

@action('ctrl_act9942')
def ctrl_nm9942():
    return 'ret9942' 

@action('ctrl_act9943')
def ctrl_nm9943():
    return 'ret9943' 

@action('ctrl_act9944')
def ctrl_nm9944():
    return 'ret9944' 

@action('ctrl_act9945')
def ctrl_nm9945():
    return 'ret9945' 

@action('ctrl_act9946')
def ctrl_nm9946():
    return 'ret9946' 

@action('ctrl_act9947')
def ctrl_nm9947():
    return 'ret9947' 

@action('ctrl_act9948')
def ctrl_nm9948():
    return 'ret9948' 

@action('ctrl_act9949')
def ctrl_nm9949():
    return 'ret9949' 

@action('ctrl_act9950')
def ctrl_nm9950():
    return 'ret9950' 

@action('ctrl_act9951')
def ctrl_nm9951():
    return 'ret9951' 

@action('ctrl_act9952')
def ctrl_nm9952():
    return 'ret9952' 

@action('ctrl_act9953')
def ctrl_nm9953():
    return 'ret9953' 

@action('ctrl_act9954')
def ctrl_nm9954():
    return 'ret9954' 

@action('ctrl_act9955')
def ctrl_nm9955():
    return 'ret9955' 

@action('ctrl_act9956')
def ctrl_nm9956():
    return 'ret9956' 

@action('ctrl_act9957')
def ctrl_nm9957():
    return 'ret9957' 

@action('ctrl_act9958')
def ctrl_nm9958():
    return 'ret9958' 

@action('ctrl_act9959')
def ctrl_nm9959():
    return 'ret9959' 

@action('ctrl_act9960')
def ctrl_nm9960():
    return 'ret9960' 

@action('ctrl_act9961')
def ctrl_nm9961():
    return 'ret9961' 

@action('ctrl_act9962')
def ctrl_nm9962():
    return 'ret9962' 

@action('ctrl_act9963')
def ctrl_nm9963():
    return 'ret9963' 

@action('ctrl_act9964')
def ctrl_nm9964():
    return 'ret9964' 

@action('ctrl_act9965')
def ctrl_nm9965():
    return 'ret9965' 

@action('ctrl_act9966')
def ctrl_nm9966():
    return 'ret9966' 

@action('ctrl_act9967')
def ctrl_nm9967():
    return 'ret9967' 

@action('ctrl_act9968')
def ctrl_nm9968():
    return 'ret9968' 

@action('ctrl_act9969')
def ctrl_nm9969():
    return 'ret9969' 

@action('ctrl_act9970')
def ctrl_nm9970():
    return 'ret9970' 

@action('ctrl_act9971')
def ctrl_nm9971():
    return 'ret9971' 

@action('ctrl_act9972')
def ctrl_nm9972():
    return 'ret9972' 

@action('ctrl_act9973')
def ctrl_nm9973():
    return 'ret9973' 

@action('ctrl_act9974')
def ctrl_nm9974():
    return 'ret9974' 

@action('ctrl_act9975')
def ctrl_nm9975():
    return 'ret9975' 

@action('ctrl_act9976')
def ctrl_nm9976():
    return 'ret9976' 

@action('ctrl_act9977')
def ctrl_nm9977():
    return 'ret9977' 

@action('ctrl_act9978')
def ctrl_nm9978():
    return 'ret9978' 

@action('ctrl_act9979')
def ctrl_nm9979():
    return 'ret9979' 

@action('ctrl_act9980')
def ctrl_nm9980():
    return 'ret9980' 

@action('ctrl_act9981')
def ctrl_nm9981():
    return 'ret9981' 

@action('ctrl_act9982')
def ctrl_nm9982():
    return 'ret9982' 

@action('ctrl_act9983')
def ctrl_nm9983():
    return 'ret9983' 

@action('ctrl_act9984')
def ctrl_nm9984():
    return 'ret9984' 

@action('ctrl_act9985')
def ctrl_nm9985():
    return 'ret9985' 

@action('ctrl_act9986')
def ctrl_nm9986():
    return 'ret9986' 

@action('ctrl_act9987')
def ctrl_nm9987():
    return 'ret9987' 

@action('ctrl_act9988')
def ctrl_nm9988():
    return 'ret9988' 

@action('ctrl_act9989')
def ctrl_nm9989():
    return 'ret9989' 

@action('ctrl_act9990')
def ctrl_nm9990():
    return 'ret9990' 

@action('ctrl_act9991')
def ctrl_nm9991():
    return 'ret9991' 

@action('ctrl_act9992')
def ctrl_nm9992():
    return 'ret9992' 

@action('ctrl_act9993')
def ctrl_nm9993():
    return 'ret9993' 

@action('ctrl_act9994')
def ctrl_nm9994():
    return 'ret9994' 

@action('ctrl_act9995')
def ctrl_nm9995():
    return 'ret9995' 

@action('ctrl_act9996')
def ctrl_nm9996():
    return 'ret9996' 

@action('ctrl_act9997')
def ctrl_nm9997():
    return 'ret9997' 

@action('ctrl_act9998')
def ctrl_nm9998():
    return 'ret9998' 

@action('ctrl_act9999')
def ctrl_nm9999():
    return 'ret9999' 
