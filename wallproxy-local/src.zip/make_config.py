# -*- coding: utf-8 -*-
from __future__ import with_statement

PUBLIC_APPIDS = '''
freegoagent001|freegoagent002|freegoagent003|freegoagent004|freegoagent005|freegoagent006|freegoagent007|freegoagent008|freegoagent009|freegoagent010|freegoagent011|freegoagent012|freegoagent013|freegoagent014|freegoagent015|freegoagent016|freegoagent017|freegoagent018|freegoagent019|freegoagent020|freegoagent021|freegoagent022|freegoagent023|freegoagent024|freegoagent025|freegoagent026|freegoagent027|freegoagent028|freegoagent029|freegoagent030|freegoagent031|freegoagent032|freegoagent033|freegoagent034|freegoagent035|freegoagent036|freegoagent037|freegoagent038|freegoagent039|freegoagent040|freegoagent041|freegoagent042|freegoagent043|freegoagent044|freegoagent045|freegoagent046|freegoagent047|freegoagent048|freegoagent049|freegoagent050|freegoagent051|freegoagent052|freegoagent053|freegoagent054|freegoagent055|freegoagent056|freegoagent057|freegoagent058|freegoagent059|freegoagent060|freegoagent061|freegoagent062|freegoagent063|freegoagent064|freegoagent065|freegoagent066|freegoagent067|freegoagent068|freegoagent069|freegoagent070|freegoagent071|freegoagent072|freegoagent073|freegoagent074|freegoagent075|freegoagent076|freegoagent077|freegoagent078|freegoagent079|freegoagent080|freegoagent081|freegoagent082|freegoagent083|freegoagent084|freegoagent085|freegoagent086|freegoagent087|freegoagent088|freegoagent089|freegoagent090|freegoagent091|freegoagent092|freegoagent093|freegoagent094|freegoagent095|freegoagent096|freegoagent097|freegoagent098|freegoagent099|freegoagent100|freegoagent101|freegoagent102|freegoagent103|freegoagent104|freegoagent105|freegoagent106|freegoagent107|freegoagent108|freegoagent109|freegoagent110|freegoagent121|freegoagent122|freegoagent124|freegoagent125|freegoagent126|freegoagent127|freegoagent128|freegoagent129|freegoagent130|freegoagent131|freegoagent132|freegoagent133|freegoagent134|freegoagent135|freegoagent136|freegoagent137|freegoagent138|freegoagent139|freegoagent140|freegoagent141|freegoagent142|freegoagent143|freegoagent144|freegoagent145|freegoagent146|freegoagent147|freegoagent148|freegoagent149|freegoagent150|freegoagent151|freegoagent152|freegoagent153|freegoagent154|freegoagent155|freegoagent156|freegoagent157|freegoagent158|freegoagent159|freegoagent160|freegoagent161|freegoagent162|freegoagent163|freegoagent164|freegoagent165|freegoagent166|freegoagent167|freegoagent168|freegoagent169|freegoagent170|freegoagent171|freegoagent172|freegoagent173|freegoagent174|freegoagent175|freegoagent176|freegoagent177|freegoagent178|freegoagent179|freegoagent180|freegoagent181|freegoagent182|freegoagent183|freegoagent184|freegoagent185|freegoagent186|freegoagent187|freegoagent188|freegoagent189|freegoagent190|freegoagent191|freegoagent192|freegoagent193|freegoagent194|freegoagent195|freegoagent196|freegoagent197|freegoagent198|freegoagent199|freegoagent200|freegoagent201|freegoagent202|freegoagent203|freegoagent204|freegoagent205|freegoagent206|freegoagent207|freegoagent208|freegoagent209|freegoagent210|freegoagent211|freegoagent212|freegoagent213|freegoagent214|freegoagent215|freegoagent216|freegoagent217|freegoagent218|freegoagent219|freegoagent220|freegoagent221|freegoagent222|freegoagent223|freegoagent224|freegoagent225|freegoagent226|freegoagent227|freegoagent228|freegoagent229|freegoagent230|freegoagent231|freegoagent232|freegoagent233|freegoagent234|freegoagent235|freegoagent236|freegoagent237|freegoagent238|freegoagent239|freegoagent240|freegoagent241|freegoagent242|freegoagent243|freegoagent244|freegoagent245|freegoagent246|freegoagent247|freegoagent248|freegoagent249|freegoagent250|freegoagent251|freegoagent252|freegoagent253|freegoagent254|freegoagent255|freegoagent256|freegoagent257|freegoagent258|freegoagent259|freegoagent260|freegoagent261|freegoagent262|freegoagent263|freegoagent264|freegoagent265|freegoagent266|freegoagent267|freegoagent268|freegoagent269|freegoagent270|freegoagent271|freegoagent272|freegoagent273|freegoagent274|freegoagent275|freegoagent276|freegoagent277|freegoagent278|freegoagent279|freegoagent280|freegoagent281|freegoagent282|freegoagent283|freegoagent284|freegoagent285|freegoagent286|freegoagent287|freegoagent288|freegoagent289|freegoagent290|freegoagent291|freegoagent292|freegoagent293|freegoagent294|freegoagent295|freegoagent296|freegoagent297|freegoagent298|freegoagent299|freegoagent300|freegoagent301|freegoagent302|freegoagent303|freegoagent304|freegoagent305|freegoagent306|freegoagent307|freegoagent308|freegoagent309|freegoagent310|freegoagent311|freegoagent312|freegoagent313|freegoagent314|freegoagent315|freegoagent316|freegoagent317|freegoagent318|freegoagent319|freegoagent320|freegoagent321|freegoagent322|freegoagent323|freegoagent324|freegoagent325|freegoagent326|freegoagent327|freegoagent328|freegoagent329|freegoagent330|freegoagent331|freegoagent332|freegoagent333|freegoagent334|freegoagent335|freegoagent336|freegoagent337|freegoagent338|freegoagent339|freegoagent340|freegoagent341|freegoagent342|freegoagent343|freegoagent344|freegoagent345|freegoagent346|freegoagent347|freegoagent348|freegoagent349|freegoagent350|freegoagent351|freegoagent352|freegoagent353|freegoagent354|freegoagent355|freegoagent356|freegoagent357|freegoagent358|freegoagent359|freegoagent360|freegoagent361|freegoagent362|freegoagent363|freegoagent364|freegoagent365|freegoagent366|freegoagent367|freegoagent368|freegoagent369|freegoagent370|freegoagent371|freegoagent372|freegoagent373|freegoagent374|freegoagent375|freegoagent376|freegoagent377|freegoagent378|freegoagent379|freegoagent380|freegoagent381|freegoagent382|freegoagent383|freegoagent384|freegoagent385|freegoagent386|freegoagent387|freegoagent388|freegoagent389|freegoagent390|freegoagent391|freegoagent392|freegoagent393|freegoagent394|freegoagent395|freegoagent396|freegoagent397|freegoagent398|freegoagent399|freegoagent400|freegoagent401|freegoagent402|freegoagent403|freegoagent404|freegoagent405|freegoagent406|freegoagent407|freegoagent408|freegoagent409|freegoagent410|freegoagent411|freegoagent412|freegoagent413|freegoagent414|freegoagent415|freegoagent416|freegoagent417|freegoagent418|freegoagent419|freegoagent420|freegoagent421|freegoagent422|freegoagent423|freegoagent424|freegoagent425|freegoagent426|freegoagent427|freegoagent428|freegoagent429|freegoagent430|freegoagent431|freegoagent432|freegoagent433|freegoagent434|freegoagent435|freegoagent436|freegoagent437|freegoagent438|freegoagent439|freegoagent440|freegoagent441|freegoagent442|freegoagent443|freegoagent444|freegoagent445|freegoagent446|freegoagent447|freegoagent448|freegoagent449|freegoagent450|freegoagent451|freegoagent452|freegoagent453|freegoagent454|freegoagent455|freegoagent456|freegoagent457|freegoagent458|freegoagent459|freegoagent460|freegoagent461|freegoagent462|freegoagent463|freegoagent464|freegoagent465|freegoagent466|freegoagent467|freegoagent468|freegoagent469|freegoagent470|freegoagent471|freegoagent472|freegoagent473|freegoagent474|freegoagent475|freegoagent476|freegoagent477|freegoagent478|freegoagent479|freegoagent480|freegoagent481|freegoagent482|freegoagent483|freegoagent484|freegoagent485|freegoagent486|freegoagent487|freegoagent488|freegoagent489|freegoagent490|freegoagent491|freegoagent492|freegoagent493|freegoagent494|freegoagent495|freegoagent496|freegoagent497|freegoagent498|freegoagent499|freegoagent500|freegoagent501|freegoagent502|freegoagent503|freegoagent504|freegoagent505|freegoagent506|freegoagent507|freegoagent508|freegoagent509|freegoagent510|freegoagent511|freegoagent512|freegoagent513|freegoagent514|freegoagent515|freegoagent516|freegoagent517|freegoagent518|freegoagent519|freegoagent520|freegoagent521|freegoagent522|freegoagent523|freegoagent524|freegoagent525|freegoagent526|freegoagent527|freegoagent528|freegoagent529|freegoagent530|freegoagent531|freegoagent532|freegoagent533|freegoagent534|freegoagent535|freegoagent536|freegoagent537|freegoagent538|freegoagent539|freegoagent540|freegoagent541|freegoagent542|freegoagent543|freegoagent544|freegoagent545|freegoagent546|freegoagent547|freegoagent548|freegoagent549|freegoagent550|freegoagent551|freegoagent552|freegoagent553|freegoagent554|freegoagent555|freegoagent556|freegoagent557|freegoagent558|freegoagent559|freegoagent560|freegoagent561|freegoagent562|freegoagent563|freegoagent564|freegoagent565|freegoagent566|freegoagent567|freegoagent568|freegoagent569|freegoagent570|freegoagent571|freegoagent572|freegoagent573|freegoagent574|freegoagent575|freegoagent576|freegoagent577|freegoagent578|freegoagent579|freegoagent580|freegoagent581|freegoagent582|freegoagent583|freegoagent584|freegoagent585|freegoagent586|freegoagent587|freegoagent588|freegoagent589|freegoagent590|freegoagent591|freegoagent592|freegoagent593|freegoagent594|freegoagent595|freegoagent596|freegoagent597|freegoagent598|freegoagent599|freegoagent600|freegoagent601|freegoagent602|freegoagent603|freegoagent604|freegoagent605|freegoagent606|freegoagent607|freegoagent608|freegoagent609|freegoagent610|freegoagent611|freegoagent612|freegoagent613|freegoagent614|freegoagent615|freegoagent616|freegoagent617|freegoagent618|freegoagent619|freegoagent620|freegoagent621|freegoagent622|freegoagent623|freegoagent624|freegoagent625|freegoagent626|freegoagent627|freegoagent628|freegoagent629|freegoagent630|freegoagent631|freegoagent632|freegoagent633|freegoagent634|freegoagent635|freegoagent636|freegoagent637|freegoagent638|freegoagent639|freegoagent640|freegoagent641|freegoagent642|freegoagent643|freegoagent644|freegoagent645|freegoagent646|freegoagent647|freegoagent648|freegoagent649|freegoagent650|freegoagent651|freegoagent652|freegoagent653|freegoagent654|freegoagent655|freegoagent656|freegoagent657|freegoagent658|freegoagent659|freegoagent660|freegoagent661|freegoagent662|freegoagent663|freegoagent664|freegoagent665|freegoagent666|freegoagent667|freegoagent668|freegoagent669|freegoagent670|freegoagent671|freegoagent672|freegoagent673|freegoagent674|freegoagent675|freegoagent676|freegoagent677|freegoagent678|freegoagent679|freegoagent680|freegoagent681|freegoagent682|freegoagent683|freegoagent684|freegoagent685|freegoagent686|freegoagent687|freegoagent688|freegoagent689|freegoagent690|freegoagent691|freegoagent692|freegoagent693|freegoagent694|freegoagent695|freegoagent696|freegoagent697|freegoagent698|freegoagent699|freegoagent700|freegoagent701|freegoagent702|freegoagent703|freegoagent704|freegoagent705|freegoagent706|freegoagent707|freegoagent708|freegoagent709|freegoagent710|freegoagent711|freegoagent712|freegoagent713|freegoagent714|freegoagent715|freegoagent716|freegoagent717|freegoagent718|freegoagent719|freegoagent720|freegoagent721|freegoagent722|freegoagent723|freegoagent724|freegoagent725|freegoagent726|freegoagent727|freegoagent728|freegoagent729|freegoagent730|freegoagent731|freegoagent732|freegoagent733|freegoagent734|freegoagent735|freegoagent736|freegoagent737|freegoagent738|freegoagent739|freegoagent740|freegoagent741|freegoagent742|freegoagent743|freegoagent744|freegoagent745|freegoagent746|freegoagent747|freegoagent748|freegoagent749|freegoagent750|freegoagent751|freegoagent752|freegoagent753|freegoagent754|freegoagent755|freegoagent756|freegoagent757|freegoagent758|freegoagent759|freegoagent760|freegoagent761|freegoagent762|freegoagent763|freegoagent764|freegoagent765|freegoagent766|freegoagent767|freegoagent768|freegoagent769|freegoagent770|freegoagent771|freegoagent772|freegoagent773|freegoagent774|freegoagent775|freegoagent776|freegoagent777|freegoagent778|freegoagent779|freegoagent780|freegoagent781|freegoagent782|freegoagent783|freegoagent784|freegoagent785|freegoagent786|freegoagent787|freegoagent788|freegoagent789|freegoagent790|freegoagent791|freegoagent792|freegoagent793|freegoagent794|freegoagent795|freegoagent796|freegoagent797|freegoagent798|freegoagent799|freegoagent800|freegoagent801|freegoagent802|freegoagent803|freegoagent804|freegoagent805|freegoagent806|freegoagent807|freegoagent808|freegoagent809|freegoagent810|freegoagent811|freegoagent812|freegoagent813|freegoagent814|freegoagent815|freegoagent817|freegoagent818|freegoagent819|freegoagent820|freegoagent821|freegoagent822|freegoagent823|freegoagent824|freegoagent825|freegoagent826|freegoagent827|freegoagent828|freegoagent829|freegoagent830|freegoagent831|freegoagent832|freegoagent833|freegoagent834|freegoagent835|freegoagent836|freegoagent837|freegoagent838|freegoagent839|freegoagent840|freegoagent841|freegoagent842|freegoagent843|freegoagent844|freegoagent845|freegoagent846|freegoagent847|freegoagent848|freegoagent849|freegoagent850|freegoagent851|freegoagent852|freegoagent853|freegoagent854|freegoagent855|freegoagent856|freegoagent857|freegoagent858|freegoagent859|freegoagent860|freegoagent861|freegoagent862|freegoagent863|freegoagent864|freegoagent865|freegoagent866|freegoagent867|freegoagent868|freegoagent869|freegoagent870|freegoagent871|freegoagent872|freegoagent873|freegoagent874|freegoagent875|freegoagent876|freegoagent877|freegoagent878|freegoagent879|freegoagent880|freegoagent881|freegoagent882|freegoagent883|freegoagent884|freegoagent885|freegoagent886|freegoagent887|freegoagent888|freegoagent889|freegoagent890|freegoagent891|freegoagent892|freegoagent893|freegoagent894|freegoagent895|freegoagent896|freegoagent897|freegoagent898|freegoagent899|freegoagent900|freegoagent901|freegoagent902|freegoagent903|freegoagent904|freegoagent905|freegoagent906|freegoagent907|freegoagent908|freegoagent909|freegoagent910|freegoagent911|freegoagent912|freegoagent913|freegoagent914|freegoagent915|freegoagent917|freegoagent918|freegoagent919|freegoagent920|freegoagent921|freegoagent922|freegoagent923|freegoagent924|freegoagent925|freegoagent926|freegoagent927|freegoagent928|freegoagent929|freegoagent930|freegoagent931|freegoagent932|freegoagent933|freegoagent934|freegoagent935|freegoagent936|freegoagent937|freegoagent938|freegoagent939|freegoagent940|freegoagent941|freegoagent942|freegoagent943|freegoagent944|freegoagent945|freegoagent946|freegoagent947|freegoagent948|freegoagent949|freegoagent950|freegoagent951|freegoagent952|freegoagent953|freegoagent954|freegoagent955|freegoagent956|freegoagent957|freegoagent958|freegoagent959|freegoagent960|freegoagent961|freegoagent962|freegoagent963|freegoagent964|freegoagent965|freegoagent966|freegoagent967|freegoagent968|freegoagent969|freegoagent970|freegoagent971|freegoagent972|freegoagent973|freegoagent974|freegoagent975|freegoagent976|freegoagent977|freegoagent978|freegoagent979|freegoagent980|freegoagent981|freegoagent982|freegoagent983|freegoagent984|freegoagent985|freegoagent986|freegoagent987|freegoagent988|freegoagent989|freegoagent990|freegoagent991|freegoagent992|freegoagent993|freegoagent994|freegoagent995|freegoagent996|freegoagent997|freegoagent998|freegoagent999|fgabootstrap001|fgabootstrap002|fgabootstrap003|fgabootstrap004|fgabootstrap005|fgabootstrap006|fgabootstrap007|fgabootstrap008|fgabootstrap009|fgabootstrap010|fgaupdate001|fgaupdate002|fgaupdate003|fgaupdate004|fgaupdate005|fgaupdate006|fgaupdate007|fgaupdate008|fgaupdate009|fgaupdate010|fganr001|fganr002|gfanqiang000-0|gfanqiang000-1|gfanqiang000-2|gfanqiang000-3|gfanqiang000-4|gfanqiang000-5|gfanqiang000-6|gfanqiang000-7|gfanqiang000-8|gfanqiang000-9|gfanqiang001-0|gfanqiang001-1|gfanqiang001-2|gfanqiang001-3|gfanqiang001-4|gfanqiang001-5|gfanqiang001-6|gfanqiang001-7|gfanqiang001-8|gfanqiang001-9|gfanqiang002-0|gfanqiang002-1|gfanqiang002-2|gfanqiang002-3|gfanqiang002-4|gfanqiang002-5|gfanqiang002-6|gfanqiang002-7|gfanqiang002-8|gfanqiang002-9|gfanqiang003-0|gfanqiang003-1|gfanqiang003-2|gfanqiang003-3|gfanqiang003-4|gfanqiang003-5|gfanqiang003-6|gfanqiang003-7|gfanqiang003-8|gfanqiang003-9|gfanqiang004-0|gfanqiang004-1|gfanqiang004-2|gfanqiang004-3|gfanqiang004-4|gfanqiang004-5|gfanqiang004-6|gfanqiang004-7|gfanqiang004-8|gfanqiang004-9|gfanqiang005-0|gfanqiang005-1|gfanqiang005-2|gfanqiang005-3|gfanqiang005-4|gfanqiang005-5|gfanqiang005-6|gfanqiang005-7|gfanqiang005-8|gfanqiang005-9|gfanqiang006-0|gfanqiang006-1|gfanqiang006-2|gfanqiang006-3|gfanqiang006-4|gfanqiang006-5|gfanqiang006-6|gfanqiang006-7|gfanqiang006-8|gfanqiang006-9|gfanqiang007-0|gfanqiang007-1|gfanqiang007-2|gfanqiang007-3|gfanqiang007-4|gfanqiang007-5|gfanqiang007-6|gfanqiang007-7|gfanqiang007-8|gfanqiang007-9|gfanqiang008-0|gfanqiang008-1|gfanqiang008-2|gfanqiang008-3|gfanqiang008-4|gfanqiang008-5|gfanqiang008-6|gfanqiang008-7|gfanqiang008-8|gfanqiang008-9|gfanqiang009-0|gfanqiang009-1|gfanqiang009-2|gfanqiang009-3|gfanqiang009-4|gfanqiang009-5|gfanqiang009-6|gfanqiang009-7|gfanqiang009-8|gfanqiang009-9|gfanqiang010-0|gfanqiang010-1|gfanqiang010-2|gfanqiang010-3|gfanqiang010-4|gfanqiang010-5|gfanqiang010-6|gfanqiang010-7|gfanqiang010-8|gfanqiang010-9|gfanqiang011-0|gfanqiang011-1|gfanqiang011-2|gfanqiang011-3|gfanqiang011-4|gfanqiang011-5|gfanqiang011-6|gfanqiang011-7|gfanqiang011-8|gfanqiang011-9|gfanqiang012-0|gfanqiang012-1|gfanqiang012-2|gfanqiang012-3|gfanqiang012-4|gfanqiang012-5|gfanqiang012-6|gfanqiang012-7|gfanqiang012-8|gfanqiang012-9|gfanqiang013-0|gfanqiang013-1|gfanqiang013-2|gfanqiang013-3|gfanqiang013-4|gfanqiang013-5|gfanqiang013-6|gfanqiang013-7|gfanqiang013-8|gfanqiang013-9|gfanqiang014-0|gfanqiang014-1|gfanqiang014-2|gfanqiang014-3|gfanqiang014-4|gfanqiang014-5|gfanqiang014-6|gfanqiang014-7|gfanqiang014-8|gfanqiang014-9|gfanqiang015-0|gfanqiang015-1|gfanqiang015-2|gfanqiang015-3|gfanqiang015-4|gfanqiang015-5|gfanqiang015-6|gfanqiang015-7|gfanqiang015-8|gfanqiang015-9|gfanqiang016-0|gfanqiang016-1|gfanqiang016-2|gfanqiang016-3|gfanqiang016-4|gfanqiang016-5|gfanqiang016-6|gfanqiang016-7|gfanqiang016-8|gfanqiang016-9|gfanqiang017-0|gfanqiang017-1|gfanqiang017-2|gfanqiang017-3|gfanqiang017-4|gfanqiang017-5|gfanqiang017-6|gfanqiang017-7|gfanqiang017-8|gfanqiang017-9|gfanqiang018-0|gfanqiang018-1|gfanqiang018-2|gfanqiang018-3|gfanqiang018-4|gfanqiang018-5|gfanqiang018-6|gfanqiang018-7|gfanqiang018-8|gfanqiang018-9|gfanqiang019-0|gfanqiang019-1|gfanqiang019-2|gfanqiang019-3|gfanqiang019-4|gfanqiang019-5|gfanqiang019-6|gfanqiang019-7|gfanqiang019-8|gfanqiang019-9|gfanqiang020-0|gfanqiang020-1|gfanqiang020-2|gfanqiang020-3|gfanqiang020-4|gfanqiang020-5|gfanqiang020-6|gfanqiang020-7|gfanqiang020-8|gfanqiang020-9|gfanqiang021-0|gfanqiang021-1|gfanqiang021-2|gfanqiang021-3|gfanqiang021-4|gfanqiang021-5|gfanqiang021-6|gfanqiang021-7|gfanqiang021-8|gfanqiang021-9|gfanqiang022-0|gfanqiang022-1|gfanqiang022-2|gfanqiang022-3|gfanqiang022-4|gfanqiang022-5|gfanqiang022-6|gfanqiang022-7|gfanqiang022-8|gfanqiang022-9|gfanqiang023-0|gfanqiang023-1|gfanqiang023-2|gfanqiang023-3|gfanqiang023-4|gfanqiang023-5|gfanqiang023-6|gfanqiang023-7|gfanqiang023-8|gfanqiang023-9|gfanqiang024-0|gfanqiang024-1|gfanqiang024-2|gfanqiang024-3|gfanqiang024-4|gfanqiang024-5|gfanqiang024-6|gfanqiang024-7|gfanqiang024-8|gfanqiang024-9|gfanqiang025-0|gfanqiang025-1|gfanqiang025-2|gfanqiang025-3|gfanqiang025-4|gfanqiang025-5|gfanqiang025-6|gfanqiang025-7|gfanqiang025-8|gfanqiang025-9|gfanqiang026-0|gfanqiang026-1|gfanqiang026-2|gfanqiang026-3|gfanqiang026-4|gfanqiang026-5|gfanqiang026-6|gfanqiang026-7|gfanqiang026-8|gfanqiang026-9|gfanqiang027-0|gfanqiang027-1|gfanqiang027-2|gfanqiang027-3|gfanqiang027-4|gfanqiang027-5|gfanqiang027-6|gfanqiang027-7|gfanqiang027-8|gfanqiang027-9|gfanqiang028-0|gfanqiang028-1|gfanqiang028-2|gfanqiang028-3|gfanqiang028-4|gfanqiang028-5|gfanqiang028-6|gfanqiang028-7|gfanqiang028-8|gfanqiang028-9|gfanqiang029-0|gfanqiang029-1|gfanqiang029-2|gfanqiang029-3|gfanqiang029-4|gfanqiang029-5|gfanqiang029-6|gfanqiang029-7|gfanqiang029-8|gfanqiang029-9|gfanqiang030-0|gfanqiang030-1|gfanqiang030-2|gfanqiang030-3|gfanqiang030-4|gfanqiang030-5|gfanqiang030-6|gfanqiang030-7|gfanqiang030-8|gfanqiang030-9|gfanqiang031-0|gfanqiang031-1|gfanqiang031-2|gfanqiang031-3|gfanqiang031-4|gfanqiang031-5|gfanqiang031-6|gfanqiang031-7|gfanqiang031-8|gfanqiang031-9|gfanqiang032-0|gfanqiang032-1|gfanqiang032-2|gfanqiang032-3|gfanqiang032-4|gfanqiang032-5|gfanqiang032-6|gfanqiang032-7|gfanqiang032-8|gfanqiang032-9|gfanqiang033-0|gfanqiang033-1|gfanqiang033-2|gfanqiang033-3|gfanqiang033-4|gfanqiang033-5|gfanqiang033-6|gfanqiang033-7|gfanqiang033-8|gfanqiang033-9|gfanqiang034-0|gfanqiang034-1|gfanqiang034-2|gfanqiang034-3|gfanqiang034-4|gfanqiang034-5|gfanqiang034-6|gfanqiang034-7|gfanqiang034-8|gfanqiang034-9|gfanqiang035-0|gfanqiang035-1|gfanqiang035-2|gfanqiang035-3|gfanqiang035-4|gfanqiang035-5|gfanqiang035-6|gfanqiang035-7|gfanqiang035-8|gfanqiang035-9|gfanqiang036-0|gfanqiang036-1|gfanqiang036-2|gfanqiang036-3|gfanqiang036-4|gfanqiang036-5|gfanqiang036-6|gfanqiang036-7|gfanqiang036-8|gfanqiang036-9
'''

import ConfigParser, os, re, urlparse, os.path as ospath, random
from cStringIO import StringIO

rulefiles = lambda v:[v.replace(r'\n','\n') if v.startswith('string://') else v for v in v.split('|')]

class Common(object):
    v = '''def %s(self, *a):
    try:
        return self.CONFIG.%s(*a[:-1])
    except:
        return a[-1]
'''
    for k in ('get', 'getint', 'getfloat', 'getboolean', 'items', 'remove_option'):
        exec(v % (k, k))
    del k, v

    def parse_pac_config(self):
        v = self.get('pac', 'py_default', '') or 'FORWARD'
        self.PY_DEFAULT = (v.split('|') * 3)[:3]
        if self.PAC_FILE:
            v = self.get('pac', 'default', '') or self._PAC_DEFAULT
            self.PAC_DEFAULT = (v.split('|') * 3)[:3]
        else:
            self.PAC_DEFAULT = self.PY_DEFAULT
        def get_rule_cfg(key, default):
            PAC_RULELIST = v = self.get('pac', key, default)
            if v.startswith('!'):
                if self.PAC_FILE:
                    v = self.items(v.lstrip('!').strip(), ())
                    v = [(rulefiles(v),k.upper()) for k,v in v if k and v]
                else:
                    v = self.items('py_'+v.lstrip('!').strip(), ())
                    sp = {'FORBID':'False', 'WEB':'None'}
                    v = [(rulefiles(v),sp.get(k.upper()) or k.upper()) for k,v in v if k and v]
                PAC_RULELIST = v
            elif v:
                TARGET_PAC = self.TARGET_PAAS
                if self.PAC_FILE:
                    TARGET_PAC = self.TARGET_LISTEN
                    if not TARGET_PAC:
                        TARGET_PAC = '*:*'
                    elif ':' not in TARGET_PAC:
                        TARGET_PAC = '*:' + TARGET_PAC
                    TARGET_PAC = 'PROXY %s;DIRECT' % TARGET_PAC
                PAC_RULELIST = [(rulefiles(v), TARGET_PAC)]
            return PAC_RULELIST
        self.PAC_RULELIST = get_rule_cfg('rulelist', '')
        self.PAC_IPLIST = get_rule_cfg('iplist', '')

    def __init__(self, INPUT):
        ConfigParser.RawConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
        CONFIG = self.CONFIG = ConfigParser.ConfigParser()
        try:
            CONFIG.read(INPUT)
        except ConfigParser.MissingSectionHeaderError:
            with open(INPUT, 'rb') as fp: v = fp.read()
            v = v[v.find('['):]
            try:
                with open(INPUT, 'wb') as fp: fp.write(v)
            except IOError:
                pass
            CONFIG.readfp(StringIO(v), INPUT)

        self.LISTEN_IP          = self.get('listen', 'ip', '127.0.0.1')
        self.LISTEN_PORT        = self.getint('listen', 'port', 8086)
        self.USERNAME           = self.get('listen', 'username', None)
        self.WEB_USERNAME       = self.get('listen', 'web_username', 'admin')
        self.WEB_PASSWORD       = self.get('listen', 'web_password', 'admin')
        self.WEB_AUTHLOCAL      = self.getboolean('listen', 'web_authlocal', False)
        if self.USERNAME is not None:
            self.PASSWORD       = self.get('listen', 'password', '')
            self.BASIC_AUTH     = self.getboolean('listen', 'basic_auth', True)
            self.DISABLE_SOCKS4 = self.getboolean('listen', 'disable_socks4', False)
            self.DISABLE_SOCKS5 = self.getboolean('listen', 'disable_socks5', False)
        self.CERT_WILDCARD      = self.getboolean('listen', 'cert_wildcard', True)
        self.TASKS_DELAY        = self.getint('listen', 'tasks_delay', 0)

        self.FETCH_KEEPALIVE    = self.getboolean('urlfetch', 'keep_alive', True)
        self.FETCH_TIMEOUT      = self.getfloat('urlfetch', 'timeout', -1)
        self.FORWARD_TIMEOUT    = self.getfloat('urlfetch', 'fwd_timeout', -1)
        self.FETCH_ARGS = v = {}
        k = self.getfloat('urlfetch', 'gae_timeout', -1)
        if k >= 0: v['timeout'] = k or None
        k = self.getint('urlfetch', 'gae_crlf', 0)
        if k > 0: v['crlf'] = k
        self.DEBUG_LEVEL        = self.getint('urlfetch', 'debug', -1)

        GAE_PROFILE = 'gae'; self.GAE_HANDLER = False
        self.GAE_ENABLE         = self.getboolean('gae', 'enable', CONFIG.has_section('gae'))
        if self.GAE_ENABLE:
            self.GAE_LISTEN     = self.get('gae', 'listen', '8087')
            if self.LISTEN_PORT == 8087 and self.GAE_LISTEN == '8087':
                self.LISTEN_PORT = 8086
            v = self.get('gae', 'appid', '').replace('.appspot.com', '')
            if not v or v == 'appid1|appid2':
                self.GAE_APPIDS = v = re.sub(r'\s+', '', PUBLIC_APPIDS).split('|')
                random.shuffle(v)
            else:
                self.GAE_APPIDS = v.split('|')
            self.GAE_PASSWORD   = self.get('gae', 'password', '')
            self.GAE_PATH       = self.get('gae', 'path', '/fetch.py')
            GAE_PROFILE         = self.get('gae', 'profile', GAE_PROFILE)
            self.GAE_MAXTHREADS = self.getint('gae', 'max_threads', 0)
            v = self.getint('gae', 'fetch_mode', 0)
            self.GAE_FETCHMOD   = 0 if v <= 0 else (2 if v >= 2 else 1)
            self.GAE_PROXY      = self.get('gae', 'proxy', 'default')
            self.GAE_HANDLER    = self.GAE_LISTEN and self.getboolean('gae', 'find_handler', True)

        self.PAAS_ENABLE        = self.getboolean('paas', 'enable', CONFIG.has_section('paas'))
        if self.PAAS_ENABLE:
            self.PAAS_LISTEN        = self.get('paas', 'listen', '')
            self.PAAS_PASSWORD      = self.get('paas', 'password', '')
            self.PAAS_FETCHSERVER   = CONFIG.get('paas', 'fetchserver').split('|')
            self.PAAS_PROXY         = self.get('paas', 'proxy', 'default')

        self.SOCKS5_ENABLE      = self.getboolean('socks5', 'enable', CONFIG.has_section('socks5'))
        if self.SOCKS5_ENABLE:
            self.SOCKS5_LISTEN      = self.get('socks5', 'listen', '')
            self.SOCKS5_PASSWORD    = self.get('socks5', 'password', '')
            self.SOCKS5_FETCHSERVER = CONFIG.get('socks5', 'fetchserver')
            self.SOCKS5_PROXY       = self.get('socks5', 'proxy', 'default')

        OLD_PLUGIN = []
        d = {'gaeproxy':'OGAE', 'forold':'OOLD', 'goagent':'OGA', 'simple':'OSP', 'simple2':'OSP2'}
        for k in d:
            if self.getboolean(k, 'enable', CONFIG.has_section(k)):
                url = self.get(k, 'url', '')
                if url: url = url.split('|')
                else:
                    url = self.get(k, 'appid', '')
                    if not url: continue
                    url = ['https://%s.appspot.com/%s.py' % (i,k) for i in url.split('|')]
                crypto = (self.get(k, 'crypto', '') + '|'*20).split('|')
                key = self.get(k, 'password', '').decode('string-escape')
                key = (key + ('|'+key)*20).split('|')
                proxy = [v.split(',') if ',' in v else v for v in (self.get(k, 'proxy', 'default')+'|'*20).split('|')]
                configs = []
                for url,crypto,key,proxy in zip(url,crypto,key,proxy):
                    config = {'url':url, 'key':key}
                    if crypto: config['crypto'] = crypto
                    if proxy == 'none':
                        config['proxy'] = None
                    elif proxy:
                        config['proxy'] = proxy
                    configs.append(config)
                for v in ('max_threads', 'range0', 'range'):
                    configs[0][v] = self.getint(k, v, 0)
                OLD_PLUGIN.append((d[k], k, configs, self.get(k, 'listen', '')))
        self.OLD_PLUGIN = OLD_PLUGIN or False

        self.TARGET_PAAS        = self.GAE_ENABLE and 'GAE' or self.PAAS_ENABLE and 'PAAS' or self.SOCKS5_ENABLE and 'SOCKS5' or self.OLD_PLUGIN and self.OLD_PLUGIN[0][0]
        self.TARGET_LISTEN = self.GAE_ENABLE and self.GAE_LISTEN or self.PAAS_ENABLE and self.PAAS_LISTEN or self.SOCKS5_ENABLE and self.SOCKS5_LISTEN or self.OLD_PLUGIN and self.OLD_PLUGIN[0][3]

        v = self.getint('proxy', 'enable', 0)
        self._PAC_DEFAULT = 'DIRECT'; self.GLOBAL_PROXY = None
        if v > 0:
            PROXIES = []
            for i in xrange(1,v+1):
                v = self.get('proxy', 'proxy%d'%i, '')
                if not v: break
                PROXIES.append(v)
            if not PROXIES:
                PROXY_HOST      = CONFIG.get('proxy', 'host')
                PROXY_PORT      = CONFIG.getint('proxy', 'port')
                PROXY_USERNAME  = self.get('proxy', 'username', '')
                PROXY_PASSWROD  = self.get('proxy', 'password', '')
                self._PAC_DEFAULT= 'PROXY %s:%s;DIRECT' % (PROXY_HOST, PROXY_PORT)
                if PROXY_USERNAME:
                    PROXY_HOST = '%s:%s@%s' % (PROXY_USERNAME, PROXY_PASSWROD, PROXY_HOST)
                PROXIES.append('http://%s:%s' % (PROXY_HOST, PROXY_PORT))
            self.GLOBAL_PROXY   = PROXIES[0] if len(PROXIES) == 1 else tuple(PROXIES)

        self.HTTPS_TARGET = {}
        if self.getboolean('forward', 'enable', CONFIG.has_section('forward')):
            self.remove_option('forward', 'enable', '')
            for k,v in self.items('forward', ()):
                self.HTTPS_TARGET[k.upper()] = '(%s)'%v if '"' in v or "'" in v else repr(v)

        self.PAC_ENABLE = self.getboolean('pac', 'enable', True)
        v = self.getint('pac', 'https_mode', 2)
        self.PAC_HTTPSMODE = 0 if v <= 0 else (2 if v >= 2 else 1)
        v = self.get('pac', 'file', '').replace('goagent', 'proxy')
        self.PAC_FILE = v and v.split('|')
        self.parse_pac_config()

        self.GOOGLE_MODE        = self.get(GAE_PROFILE, 'mode', 'http')
        v = self.get(GAE_PROFILE, 'hosts', '')
        self.GOOGLE_HOSTS       = ' '.join(v and tuple(v.split('|')) or ())
        v = self.get(GAE_PROFILE, 'sites', '')
        self.GOOGLE_SITES       = v and tuple(v.split('|')) or ()
        v = self.get(GAE_PROFILE, 'forcehttps', ''); v = v and v.split('|') or ()
        GOOGLE_FORCEHTTPS = [(i if '/' in i else ('http://%s/'%('*'+i if i.startswith('.') else i))) for i in v]
        v = self.get(GAE_PROFILE, 'noforcehttps', ''); v = v and v.split('|') or ()
        GOOGLE_FORCEHTTPS.extend(['@@%s'%(i if '/' in i else ('http://%s/'%('*'+i if i.startswith('.') else i))) for i in v])
        self.GOOGLE_FORCEHTTPS = ' \n '.join(GOOGLE_FORCEHTTPS)
        v = self.get(GAE_PROFILE, 'withgae', '')
        GOOGLE_WITHGAE          = v and tuple(v.split('|')) or ()
        self.TRUE_HTTPS = self.TARGET_PAAS and self.get(GAE_PROFILE, 'truehttps', '').replace('|', ' ').strip()
        self.NOTRUE_HTTPS = self.TRUE_HTTPS and self.get(GAE_PROFILE, 'notruehttps', '').replace('|', ' ').strip()

        self.FETCHMAX_LOCAL     = self.getint('fetchmax', 'local', 3)
        self.FETCHMAX_SERVER    = self.getint('fetchmax', 'server', 0)

        self.AUTORANGE_ENABLE   = self.getboolean('autorange', 'enable', False)
        def get_rules(opt, key, d=''):
            v = self.get(opt, key, d)
            if v.startswith('!'):
                v = v.lstrip('!').strip()
                return v and rulefiles(v)
            else:
                return v.replace(r'\n', '\n').strip()
        self.AUTORANGE_RULES = get_rules('autorange', 'rules')
        v = self.get('autorange', 'hosts', ''); v = v and v.split('|') or ()
        v = ' \n '.join([(i if '/' in i else ('||%s'%i.lstrip('.') if i.startswith('.') else 'http*://%s/'%i)) for i in v])
        if isinstance(self.AUTORANGE_RULES, list):
            self.AUTORANGE_RULES.append('string://' + v)
        elif v:
            self.AUTORANGE_RULES = ' \n '.join((v, self.AUTORANGE_RULES))
        self.AUTORANGE_MAXSIZE  = self.getint('autorange', 'maxsize', 1000000)
        self.AUTORANGE_WAITSIZE = self.getint('autorange', 'waitsize', 500000)
        self.AUTORANGE_BUFSIZE  = self.getint('autorange', 'bufsize', 8192)

        assert self.AUTORANGE_BUFSIZE <= self.AUTORANGE_WAITSIZE <= self.AUTORANGE_MAXSIZE

        self.REMOTE_DNS = self.DNS_RESOLVE = self.CRLF_RULES = self.HOSTS_RULES = ''; self.HOSTS = {}
        if self.getboolean('hosts', 'enable', CONFIG.has_section('hosts')):
            self.REMOTE_DNS = v = self.get('hosts', 'dns', '')
            if v: self.REMOTE_DNS = v if ',' in v else repr(v)
            self.DNS_RESOLVE = self.get('hosts', 'resolve', '').replace('|', ' ').strip()
            self.HOSTS_CRLF = self.getint('hosts', 'crlf', 0)
            self.CRLF_RULES = self.HOSTS_CRLF > 0 and get_rules('hosts', 'crlf_rules')
            self.HOSTS_RULES = self.TARGET_PAAS and get_rules('hosts', 'rules')
            for v in ('enable', 'rules', 'crlf', 'crlf_rules', 'dns', 'resolve'):
                self.remove_option('hosts', v, '')
            for k,v in self.items('hosts', ()):
                if v.startswith('profile:'):
                    v = self.get(GAE_PROFILE, v[8:], '')
                else:
                    m = re.match(r'\[(\w+)\](\w+)', v)
                    if m:
                        v = v.replace(m.group(0), self.get(m.group(1), m.group(2), ''))
                v = v.replace('|', ' ').strip()
                if k and v: self.HOSTS[k] = v

        self.THIRD_APPS = []
        if self.getboolean('third', 'enable', CONFIG.has_section('third')):
            self.remove_option('third', 'enable', '')
            self.THIRD_APPS = [(k,v if v[0] in ('"',"'") else repr(v)) for k,v in self.items('third', ()) if v]

        self.USERAGENT_STRING   = self.getboolean('useragent', 'enable', True) and self.get('useragent', 'string', '')
        self.USERAGENT_MATCH    = self.USERAGENT_STRING and self.get('useragent', 'match', '')
        self.USERAGENT_RULES    = self.USERAGENT_MATCH and get_rules('useragent', 'rules')
        self.FALLBACK_RULES     = self.TARGET_PAAS and get_rules('urlfetch', 'nofallback',
            r'/^https?:\/\/(?:[\w-]+|127(?:\.\d+){3}|10(?:\.\d+){3}|192\.168(?:\.\d+){2}|172\.[1-3]\d(?:\.\d+){2}|\[.+?\])(?::\d+)?\//')

        self.AUTORANGE_RULES    = (self.GAE_ENABLE or self.OLD_PLUGIN) and self.AUTORANGE_ENABLE and self.AUTORANGE_RULES
        self.PAC_ENABLE         = (self.PAC_RULELIST or self.PAC_IPLIST) and self.PAC_ENABLE and 'PAC_ENABLE'
        self.GOOGLE_WITHGAE     = False
        if self.TARGET_PAAS and self.GOOGLE_SITES and not self.GLOBAL_PROXY:
            self.GOOGLE_WITHGAE = ' \n '.join([(i if '/' in i else '||%s'%i.lstrip('.')) for i in GOOGLE_WITHGAE])
            v = ' \n '.join(['||%s'%i.lstrip('.') for i in self.GOOGLE_SITES])
            if isinstance(self.HOSTS_RULES, basestring):
                self.HOSTS_RULES = ' \n '.join((self.HOSTS_RULES, v))
            else:
                self.HOSTS_RULES.append('string://' + v)
        self.NEED_PAC           = self.GOOGLE_FORCEHTTPS or self.USERAGENT_RULES or self.FALLBACK_RULES or self.AUTORANGE_RULES or self.CRLF_RULES or self.HOSTS_RULES or self.GOOGLE_WITHGAE or self.PAC_ENABLE


def tob(s, enc='utf-8'):
    return s.encode(enc) if isinstance(s, unicode) else bytes(s)
def touni(s, enc='utf-8', err='strict'):
    return s.decode(enc, err) if isinstance(s, str) else unicode(s)

class SimpleTemplate(object):
    """SimpleTemplate from bottle"""
    blocks = ('if', 'elif', 'else', 'try', 'except', 'finally', 'for', 'while',
              'with', 'def', 'class')
    dedent_blocks = ('elif', 'else', 'except', 'finally')
    re_pytokens = re.compile(r'''
            (''(?!')|""(?!")|'{6}|"{6}    # Empty strings (all 4 types)
             |'(?:[^\\']|\\.)+?'          # Single quotes (')
             |"(?:[^\\"]|\\.)+?"          # Double quotes (")
             |'{3}(?:[^\\]|\\.|\n)+?'{3}  # Triple-quoted strings (')
             |"{3}(?:[^\\]|\\.|\n)+?"{3}  # Triple-quoted strings (")
             |\#.*                        # Comments
            )''', re.VERBOSE)

    def __init__(self, source, encoding='utf-8'):
        self.source = source
        self.encoding = encoding
        self._str = lambda x: touni(repr(x), encoding)
        self._escape = lambda x: touni(x, encoding)

    @classmethod
    def split_comment(cls, code):
        """ Removes comments (#...) from python code. """
        if '#' not in code: return code
        #: Remove comments only (leave quoted strings as they are)
        subf = lambda m: '' if m.group(0)[0]=='#' else m.group(0)
        return re.sub(cls.re_pytokens, subf, code)

    @property
    def co(self):
        # print self.code
        return compile(self.code, '<string>', 'exec')

    @property
    def code(self):
        stack = [] # Current Code indentation
        lineno = 0 # Current line of code
        ptrbuffer = [] # Buffer for printable strings and token tuple instances
        codebuffer = [] # Buffer for generated python code
        multiline = dedent = oneline = False
        template = self.source

        def yield_tokens(line):
            for i, part in enumerate(re.split(r'\{\{(.*?)\}\}', line)):
                if i % 2:
                    if part.startswith('!'): yield 'RAW', part[1:]
                    else: yield 'CMD', part
                else: yield 'TXT', part

        def flush(): # Flush the ptrbuffer
            if not ptrbuffer: return
            cline = ''
            for line in ptrbuffer:
                for token, value in line:
                    if token == 'TXT': cline += repr(value)
                    elif token == 'RAW': cline += '_str(%s)' % value
                    elif token == 'CMD': cline += '_escape(%s)' % value
                    cline +=  ', '
                cline = cline[:-2] + '\\\n'
            cline = cline[:-2]
            if cline[:-1].endswith('\\\\\\\\\\n'):
                cline = cline[:-7] + cline[-1] # 'nobr\\\\\n' --> 'nobr'
            cline = '_printlist([' + cline + '])'
            del ptrbuffer[:] # Do this before calling code() again
            code(cline)

        def code(stmt):
            for line in stmt.splitlines():
                codebuffer.append('  ' * len(stack) + line.strip())

        for line in template.splitlines(True):
            lineno += 1
            line = touni(line, self.encoding)
            sline = line.lstrip()
            if lineno <= 2:
                m = re.match(r"%\s*#.*coding[:=]\s*([-\w.]+)", sline)
                if m: self.encoding = m.group(1)
                if m: line = line.replace('coding','coding (removed)')
            if sline and sline[0] == '%' and sline[:2] != '%%':
                line = line.split('%',1)[1].lstrip() # Full line following the %
                cline = self.split_comment(line).strip()
                cmd = re.split(r'[^a-zA-Z0-9_]', cline)[0]
                flush() # You are actually reading this? Good luck, it's a mess :)
                if cmd in self.blocks or multiline:
                    cmd = multiline or cmd
                    dedent = cmd in self.dedent_blocks # "else:"
                    if dedent and not oneline and not multiline:
                        cmd = stack.pop()
                    code(line)
                    oneline = not cline.endswith(':') # "if 1: pass"
                    multiline = cmd if cline.endswith('\\') else False
                    if not oneline and not multiline:
                        stack.append(cmd)
                elif cmd == 'end' and stack:
                    code('#end(%s) %s' % (stack.pop(), line.strip()[3:]))
                else:
                    code(line)
            else: # Line starting with text (not '%') or '%%' (escaped)
                if line.strip().startswith('%%'):
                    line = line.replace('%%', '%', 1)
                ptrbuffer.append(yield_tokens(line))
        flush()
        return '\n'.join(codebuffer) + '\n'

    def execute(self, _stdout, *args, **kwargs):
        for dictarg in args: kwargs.update(dictarg)
        env = {}
        env.update({'_stdout': _stdout, '_printlist': _stdout.extend,
               '_str': self._str, '_escape': self._escape, 'get': env.get,
               'setdefault': env.setdefault, 'defined': env.__contains__})
        env.update(kwargs)
        eval(self.co, env)
        return env

    def render(self, *args, **kwargs):
        """ Render the template using keyword arguments as local variables. """
        for dictarg in args: kwargs.update(dictarg)
        stdout = []
        self.execute(stdout, kwargs)
        return ''.join(stdout)


template = r"""# -*- coding: utf-8 -*-
# 是否使用ini作为配置文件，0不使用
ini_config = {{MTIME}}
# 监听ip
listen_ip = '{{LISTEN_IP}}'
# 监听端口
listen_port = {{LISTEN_PORT}}
# 是否使用通配符证书
cert_wildcard = {{int(CERT_WILDCARD)}}
# 更新PAC时也许还没联网，等待tasks_delay秒后才开始更新
tasks_delay = {{!TASKS_DELAY}}
# WEB界面是否对本机也要求认证
web_authlocal = {{int(WEB_AUTHLOCAL)}}
# 登录WEB界面的用户名
web_username = {{!WEB_USERNAME}}
# 登录WEB界面的密码
web_password = {{!WEB_PASSWORD}}
# 全局代理
global_proxy = {{!GLOBAL_PROXY}}
# URLFetch参数
fetch_keepalive = {{int(FETCH_KEEPALIVE)}}
%if FETCH_TIMEOUT >= 0:
fetch_timeout = {{!FETCH_TIMEOUT or None}}
%end
%if FORWARD_TIMEOUT >= 0:
forward_timeout = {{!FORWARD_TIMEOUT or None}}
%end
%if DEBUG_LEVEL >= 0:
debuglevel = {{!DEBUG_LEVEL}}
%end
check_update = 0

def config():
    Forward, set_dns, set_resolve, set_hosts, check_auth, redirect_https = import_from('util')
%for k,v in HTTPS_TARGET.iteritems():
    {{k}} = Forward({{v}})
%HTTPS_TARGET[k] = k
%end
    RAW_FORWARD = FORWARD = Forward()
%if REMOTE_DNS:
    set_dns({{REMOTE_DNS}})
%end
%if DNS_RESOLVE:
    set_resolve({{!DNS_RESOLVE}})
%end
    google_sites = {{!GOOGLE_SITES}}
    google_hosts = {{!GOOGLE_HOSTS}}
    set_hosts(google_sites, google_hosts)
%for k,v in HOSTS.iteritems():
%if k and v:
    set_hosts({{!k}}, {{repr(v) if v != GOOGLE_HOSTS else 'google_hosts'}})
%end
%end

    from plugins import misc; misc = install('misc', misc)
    PAGE = misc.Page('page.html')
%HTTPS_TARGET.update({'FORWARD':'FORWARD', 'RAW_FORWARD':'RAW_FORWARD', 'False':'False', 'None':'None','PAGE':'None'})
%if TARGET_PAAS:

    from plugins import paas; paas = install('paas', paas)
%end #TARGET_PAAS
%if GAE_ENABLE:
%HTTPS_TARGET['GAE'] = 'None'
    GAE = paas.GAE(appids={{!GAE_APPIDS}}\\
%if GAE_LISTEN:
, listen={{!GAE_LISTEN}}\\
%end
%if GAE_PASSWORD:
, password={{!GAE_PASSWORD}}\\
%end
%if GAE_PATH:
, path={{!GAE_PATH}}\\
%end
%if GOOGLE_MODE == 'https':
, scheme='https'\\
%end
%if GAE_PROXY != 'default':
, proxy={{!GAE_PROXY}}\\
%end
, hosts=google_hosts\\
%if AUTORANGE_MAXSIZE and AUTORANGE_MAXSIZE != 1000000:
, maxsize={{!AUTORANGE_MAXSIZE}}\\
%end
%if AUTORANGE_WAITSIZE and AUTORANGE_WAITSIZE != 500000:
, waitsize={{!AUTORANGE_WAITSIZE}}\\
%end
%if AUTORANGE_BUFSIZE and AUTORANGE_BUFSIZE != 8192:
, bufsize={{!AUTORANGE_BUFSIZE}}\\
%end
%if FETCHMAX_LOCAL and FETCHMAX_LOCAL != 3:
, local_times={{!FETCHMAX_LOCAL}}\\
%end
%if FETCHMAX_SERVER and FETCHMAX_SERVER != 3:
, server_times={{!FETCHMAX_SERVER}}\\
%end
%if GAE_MAXTHREADS:
, max_threads={{!GAE_MAXTHREADS}}\\
%end
%if GAE_FETCHMOD:
, fetch_mode={{!GAE_FETCHMOD}}\\
%end
%if FETCH_ARGS:
, fetch_args={{!FETCH_ARGS}}\\
%end
)
%end #GAE_ENABLE
%if PAAS_ENABLE:
%HTTPS_TARGET['PAAS'] = 'None'
%for i,k in enumerate(PAAS_FETCHSERVER):
    PAAS{{i+1 if len(PAAS_FETCHSERVER) > 1 else ''}} = paas.PAAS(url={{!k}}\\
%if PAAS_LISTEN and i == 0:
, listen={{!PAAS_LISTEN}}\\
%end
%if PAAS_PASSWORD:
, password={{!PAAS_PASSWORD}}\\
%end
%if PAAS_PROXY != 'default':
, proxy={{!PAAS_PROXY}}\\
%end
%if FETCH_ARGS:
, fetch_args={{!FETCH_ARGS}}\\
%end
)
%end
%if len(PAAS_FETCHSERVER) > 1:
%k = ['PAAS%d'%i for i in xrange(1, len(PAAS_FETCHSERVER)+1)]
%HTTPS_TARGET.update(dict.fromkeys(k,'None'))
    PAASS = ({{', '.join(k)}})
    from random import choice
    PAAS = lambda req: choice(PAASS)(req)
    server = paas.data.get('PAAS_server')
    if server:
        def find_handler(req):
            if req.proxy_type.endswith('http'):
                return PAAS
        server.find_handler = find_handler
%end
%end #PAAS_ENABLE
%if SOCKS5_ENABLE:
%HTTPS_TARGET['SOCKS5'] = 'SOCKS5'
    SOCKS5 = paas.SOCKS5(url={{!SOCKS5_FETCHSERVER}}\\
%if SOCKS5_LISTEN:
, listen={{!SOCKS5_LISTEN}}\\
%end
%if SOCKS5_PASSWORD:
, password={{!SOCKS5_PASSWORD}}\\
%end
%if SOCKS5_PROXY != 'default':
, proxy={{!SOCKS5_PROXY}}\\
%end
)
%end #SOCKS5_ENABLE
%if OLD_PLUGIN:
    from old import old; old = install('old', old)
%for n,k,c,p in OLD_PLUGIN:
    {{n}} = old.{{k}}({{!c}}, {{!p}})
%HTTPS_TARGET[n] = 'None'
%end
%end #OLD_PLUGIN
%if NEED_PAC:

    PacFile, RuleList, HostList = import_from('pac')
%end #NEED_PAC
%if GOOGLE_FORCEHTTPS:
    forcehttps_sites = RuleList({{!GOOGLE_FORCEHTTPS}})
%end
%if AUTORANGE_RULES:
    autorange_rules = RuleList({{!AUTORANGE_RULES}})
%if GAE_ENABLE:
    _GAE = GAE; GAE = lambda req: _GAE(req, autorange_rules.match(req.url, req.proxy_host[0]))
%end
%if OLD_PLUGIN:
%for n,k,c,p in OLD_PLUGIN:
    _{{n}} = {{n}}; {{n}} = lambda req: _{{n}}(req, autorange_rules.match(req.url, req.proxy_host[0]))
%end
%end #OLD_PLUGIN
%end
%if USERAGENT_RULES:
    import re; useragent_match = re.compile({{!USERAGENT_MATCH}}).search
    useragent_rules = RuleList({{!USERAGENT_RULES}})
%end
%if GOOGLE_WITHGAE:
    withgae_sites = RuleList({{!GOOGLE_WITHGAE}})
%end #GOOGLE_WITHGAE
%if TRUE_HTTPS:
%if NOTRUE_HTTPS:
    notruehttps_sites = HostList({{!NOTRUE_HTTPS}})
%end
    truehttps_sites = HostList({{!TRUE_HTTPS}})
%end #TRUE_HTTPS
%if CRLF_RULES:
    crlf_rules = RuleList({{!CRLF_RULES}})
%end #CRLF_RULES
%if HOSTS_RULES:
    hosts_rules = RuleList({{!HOSTS_RULES}})
%end #HOSTS_RULES
%if TARGET_PAAS:
    _HttpsFallback = ({{TARGET_PAAS}},)
%if FALLBACK_RULES:
    nofallback_rules = RuleList({{!FALLBACK_RULES}})
    def FORWARD(req):
        if req.proxy_type.endswith('http'):
            if nofallback_rules.match(req.url, req.proxy_host[0]):
                return RAW_FORWARD(req)
            return RAW_FORWARD(req, {{TARGET_PAAS}})
        url = build_fake_url(req.proxy_type, req.proxy_host)
        if nofallback_rules.match(url, req.proxy_host[0]):
            return RAW_FORWARD(req)
        return RAW_FORWARD(req, _HttpsFallback)
%else:
    def FORWARD(req):
        if req.proxy_type.endswith('http'):
            return RAW_FORWARD(req, {{TARGET_PAAS}})
        return RAW_FORWARD(req, _HttpsFallback)
%end
%end
%PY_DEFAULT = (([v for v in PY_DEFAULT if v in HTTPS_TARGET] or ['FORWARD']) * 3)[:3]
%if PAC_ENABLE:
%if PAC_FILE:
%NEED_PAC = NEED_PAC != 'PAC_ENABLE'

    rulelist = (
%for k,v in PAC_RULELIST:
        ({{!k}}, {{!v}}),
%end #PAC_RULELIST
    )
    iplist = (
%for k,v in PAC_IPLIST:
        ({{!k}}, {{!v}}),
%end #PAC_IPLIST
    )
    PacFile(rulelist, iplist, {{!PAC_FILE}}, {{!PAC_DEFAULT}})
%else:
%PAC_DEFAULT = PY_DEFAULT
%PAC_RULELIST = [(k,v) for k,v in PAC_RULELIST if v in HTTPS_TARGET]
%PAC_IPLIST = [(k,v) for k,v in PAC_IPLIST if v in HTTPS_TARGET]
%PAC_ENABLE = PAC_RULELIST or PAC_IPLIST
%NEED_PAC = NEED_PAC != 'PAC_ENABLE' or PAC_ENABLE
%if PAC_RULELIST:

    rulelist = (
%for k,v in PAC_RULELIST:
        (RuleList({{!k}}), {{v}}),
%end #PAC_RULELIST
    )
%if PAC_HTTPSMODE == 2:
    httpslist = (
%for i,k in enumerate(PAC_RULELIST):
        (rulelist[{{i}}][0], {{HTTPS_TARGET[k[1]]}}),
%end #PAC_RULELIST
    )
    unparse_netloc = import_from('utils')
    def build_fake_url(type, host):
        if type == 'https': port = 443
        elif host[1] % 1000 == 443: type, port = 'https', 443
        else: type, port = 'http', 80
        return '%s://%s/' % (type, unparse_netloc(host, port))
%end #PAC_HTTPSMODE
%end #PAC_RULELIST
%if PAC_IPLIST:
    IpList, makeIpFinder = import_from('pac')
    iplist = (
%for k,v in PAC_IPLIST:
        (IpList({{!k}}), {{v}}),
%end #PAC_IPLIST
    )
    findHttpProxyByIpList = makeIpFinder(iplist, [{{', '.join(PAC_DEFAULT)}}])
    findHttpsProxyByIpList = makeIpFinder(iplist, [{{', '.join([HTTPS_TARGET[v] for v in PAC_DEFAULT])}}])
%end #PAC_IPLIST
%end #PAC_FILE
%end #PAC_ENABLE
%if THIRD_APPS:

    from plugins import third; third = install('third', third)
%for k,v in THIRD_APPS:
    third.run({{v}}) #{{k}}
%end
%end

%if USERNAME:
    auth_checker = check_auth({{!USERNAME}}, {{!PASSWORD}}\\
%if DISABLE_SOCKS4:
, socks4=False\\
%end
%if DISABLE_SOCKS5 and not SOCKS5_ENABLE:
, socks5=False\\
%end
%if BASIC_AUTH:
, digest=False\\
%end
)
%end #USERNAME
%if GAE_ENABLE:
%if GAE_HANDLER:
%if USERNAME:
    @auth_checker
%end
    def find_gae_handler(req):
        proxy_type = req.proxy_type
        host, port = req.proxy_host
        if proxy_type.endswith('http'):
            url = req.url
%if USERAGENT_RULES:
            if useragent_match(req.headers.get('User-Agent','')) and useragent_rules.match(url, host):
                req.headers['User-Agent'] = {{!USERAGENT_STRING}}
%end
%if GOOGLE_WITHGAE:
            if withgae_sites.match(url, host):
                return GAE
%end
%if GOOGLE_FORCEHTTPS:
            needhttps = req.scheme == 'http' and forcehttps_sites.match(url, host) and req.content_length == 0
            if needhttps and getattr(req, '_r', '') != url:
                req._r = url
                return redirect_https
%end
%if CRLF_RULES:
            if crlf_rules.match(url, host):
                req.crlf = {{HOSTS_CRLF}}
                return FORWARD
%end
%if HOSTS_RULES:
            if \\
%if GOOGLE_FORCEHTTPS:
not needhttps and \\
%end
hosts_rules.match(url, host):
                return FORWARD
%end
            return GAE
%if TRUE_HTTPS:
%if NOTRUE_HTTPS:
        if notruehttps_sites.match(host): return
%end
        if truehttps_sites.match(host): return FORWARD
%end
%else:
    def find_gae_handler(req):
        if req.proxy_type.endswith('http'): return GAE
%end #GAE_HANDLER
    paas.data['GAE_server'].find_handler = find_gae_handler

%end #GAE_ENABLE
%if USERNAME:
    @auth_checker
%end
    def find_proxy_handler(req):
%if TARGET_PAAS or NEED_PAC:
        proxy_type = req.proxy_type
        host, port = req.proxy_host
        if proxy_type.endswith('http'):
            url = req.url
%if USERAGENT_RULES:
            if useragent_match(req.headers.get('User-Agent','')) and useragent_rules.match(url, host):
                req.headers['User-Agent'] = {{!USERAGENT_STRING}}
%end
%if GOOGLE_WITHGAE:
            if withgae_sites.match(url, host):
                return {{TARGET_PAAS}}
%end
%if GOOGLE_FORCEHTTPS:
            needhttps = req.scheme == 'http' and forcehttps_sites.match(url, host) and req.content_length == 0
            if needhttps and getattr(req, '_r', '') != url:
                req._r = url
                return redirect_https
%end
%if CRLF_RULES:
            if crlf_rules.match(url, host):
                req.crlf = {{HOSTS_CRLF}}
                return FORWARD
%end
%if HOSTS_RULES:
            if \\
%if GOOGLE_FORCEHTTPS:
not needhttps and \\
%end
hosts_rules.match(url, host):
                return FORWARD
%end
%if PAC_ENABLE and not PAC_FILE:
%if PAC_RULELIST:
            for rule,target in rulelist:
                if rule.match(url, host):
                    return target
%end
%if PAC_IPLIST:
            return findHttpProxyByIpList(host)
%else:
            return {{PY_DEFAULT[0]}}
%end
%elif TARGET_PAAS:
            return {{TARGET_PAAS}}
%else:
            return FORWARD
%end
%if TRUE_HTTPS:
%if NOTRUE_HTTPS:
        if notruehttps_sites.match(host): return
%end
        if truehttps_sites.match(host): return FORWARD
%end
%if PAC_ENABLE and not PAC_FILE and PAC_HTTPSMODE == 2:
%if PAC_RULELIST:
        url = build_fake_url(proxy_type, (host, port))
        for rule,target in httpslist:
            if rule.match(url, host):
                return target
%end
%if PAC_IPLIST:
        return findHttpsProxyByIpList(host)
%else:
        return {{HTTPS_TARGET[PY_DEFAULT[0]]}}
%end
%elif PAC_HTTPSMODE == 0:
        return {{HTTPS_TARGET[PY_DEFAULT[0]]}}
%end
%else:
        return FORWARD
%end
    return find_proxy_handler
"""

def make_config(INPUT=None, OUTPUT=None):
    if not (INPUT and OUTPUT):
        if INPUT:
            OUTPUT = ospath.join(ospath.dirname(INPUT), 'config.py')
        elif OUTPUT:
            INPUT = ospath.join(ospath.dirname(OUTPUT), 'proxy.ini')
        else:
            if '__loader__' in globals() and __loader__:
                DIR = ospath.dirname(__loader__.archive)
            else:
                DIR = ospath.dirname(__file__)
            INPUT = ospath.join(DIR, 'proxy.ini')
            OUTPUT = ospath.join(DIR, 'config.py')
    config = Common(INPUT).__dict__
    # from pprint import pprint
    # pprint(config)
    config['MTIME'] = int(os.stat(INPUT).st_mtime)
    code = SimpleTemplate(template).render(**config)
    # print code
    return tob(code), OUTPUT

if __name__ == '__main__':
    code, OUTPUT = make_config()
    with open(OUTPUT, 'wb') as fp:
        fp.write(code)
