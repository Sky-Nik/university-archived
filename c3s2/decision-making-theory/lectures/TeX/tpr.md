{% include mathjax %}

## ВСТУП

Сподіваємось ніхто не буде заперечувати проти такого визначення:
"життя &mdash; це процес прийняття рішень". Рішення приймають політики,
військові, виробники, споживачі, продавці, покупці, водії, пішоходи
("йти чи не йти на червоне світло"), дорослі ("що робити з дітьми"), діти
("що робити з іграшкою"), рішення приймають навіть студенти ("йти чи
не йти на лекцію, а якщо йти, то що робити &mdash; слухати лектора, розмовляти з сусідом). Рішення приймаються колективні (вибори президента),
індивідуальні (за якого кандидата голосувати), стратегічні ("куди піти
вчитися"), тактичні ("брати чи не брати з собою парасольку"), миттєві
(воротар &mdash; "у який кут стрибати"), розтягнуті в часі та просторі, важливі (з погляду цивілізації, партії, окремого індивіда), несуттєві ("яку програму по телевізору дивитися") і т. п. Рішення приймаються на основі
знань, досвіду, інтуїтивно, за допомогою випадкового механізму, за
підказкою інших, за бажанням, за необхідністю. У багатьох практично
цікавих випадках основним моментом є саме метод (алгоритм) прийняття рішення, а вже потім вивчення властивостей прийнятого рішення. Більше того, у деяких випадках апріорне задання властивостей
шуканого рішення (у вигляді аксіом) призводить до його неіснування
або до неможливості його знаходження заданою процедурою.

Хоча вивченням окремих задач прийняття рішень людство займалось давно, теорія прийняття рішень як наукова дисципліна сформувалось у другій половині ХХ ст., що пов'язано, у першу чергу, з розвитком обчислювальної техніки й інформатики.

Термін "прийняття рішень" зустрічається в багатьох дисциплінах,
прийняття рішень є одним з основних напрямів прикладної математики. Моделі та методи теорії прийняття рішень знайшли широке застосування, у першу чергу, в економіці, військовій справі, політиці,
медицині. Історично теорія прийняття рішень виокремилась із наукового напряму, відомого під назвою "дослідження операцій". У свою
чергу, теорія прийняття рішень стимулювала розвиток нового наукового напряму "штучний інтелект".

Таким чином, із погляду навчального плану напряму "прикладна
математика та інформатика" теорія прийняття рішень є проміжною
ланкою між дисциплінами "дослідження операцій" ("методи оптимізації") та "штучний інтелект" ("проектування баз знань").

# Розділ 1. БАЗОВІ ОСНОВИ ПРИЙНЯТТЯ РІШЕНЬ

Якщо дотримуватись класифікації проблем прийняття рішень
американських учених Г. Саймона й А. Н'юєлла [11], то типові задачі дослідження операцій відносяться до добре структурованих
або кількісно сформульованих. У таких проблемах суттєві залежності відомі настільки добре, що можуть бути вираженими в числах
або символах, які у підсумку отримують чисельні оцінки. Вивчення
реальної ситуації, що моделюється, може вимагати великого обсягу
часу. Необхідна інформація може мати високу вартість, але за наявності засобів і високої кваліфікації дослідників є всі можливості
знайти адекватне кількісне описання проблеми, критерій якості та
кількісні зв'язки між змінними.

По-іншому складається справа у слабо структурованих проблемах.
Тут частина інформації, що необхідна для повного й однозначного визначення вимог до розв'язку, принципово відсутня. Дослідник, як правило, може визначити основні змінні, встановити зв'язок між ними,
тобто побудувати модель, що адекватно описує ситуацію. Але при цьому залежності між критеріями взагалі не можуть бути визначеними на
основі об'єктивної інформації, що мається в дослідника.

Більше того, існують проблеми, у яких відомий лише перелік основних параметрів, але кількісні зв'язки встановити між ними неможливо.
У таких випадках структура, що розуміється як сукупність зв'язків між
параметрами, невизначена і проблема називається неструктурованою.

Будемо вважати, що _структуровані_ (добре структуровані) задачі
відносяться до предмета дослідження операцій, _слабо структуровані_
&mdash; до компетенції прийняття рішень, _неструктуровані_ &mdash; до штучного
інтелекту.

### &sect;1. Загальна задача прийняття рішень

Схему прийняття рішень можна описати в такому вигляді:

1. Визначення мети (цілі) та засобів її досягнення
2. Побудова варіантів досягнення мети (множини альтернатив)
3. Формування множини наслідків (оцінка альтернатив)
4. Визначення принципу порівняння альтернатив (визначення принципу оптимальності)
5. Структурування множини альтернатив:
	- розбиття на класи (кластеризація);
	- упорядкування;
	- вибір кращої (кращих).

Загалом кожен блок 1&ndash;5 наведеної схеми ("загальної задачі прийняття рішень" &mdash; ЗЗПР) потребує конкретизації та певної формалізації.
Задача із заданою множиною альтернатив $$\Omega$$ і принципом оптимальності ОП називається загальною задачею оптимізації, зміст якої полягає у виділенні множини "кращих" альтернатив ОП($$\Omega$$), зокрема, якщо
принцип оптимальності задається скалярною функцією вибору на $$\Omega$$,
то маємо звичайну _оптимізаційну задачу_ (наприклад, лінійного програмування). Якщо принцип оптимальності задається множиною
_критеріальних функцій_, то маємо задачу _багатокритеріальної оптимізації_. Задача з відомою множиною альтернатив $$\Omega$$ і явно заданим
принципом оптимальності називається _задачею вибору_.

У процесі розв'язання загальної задачі прийняття рішень, як правило, беруть участь три групи осіб: _особи, що приймають рішення_
(ОПР), _експерти_ (Е) та _консультанти_ (К).

ОПР називають людину (або колективний орган такий, як науковий
заклад, Верховна рада), що має (формує) ціль, яка слугує мотивом постановки задачі та пошуку її розв'язання. ОПР визначає також, які засоби є допустимими (недопустимими) для досягнення мети.

_Експерт_ &mdash; це спеціаліст у своїй галузі, що володіє інформацією про
задачу, але не несе прямої відповідальності за результати її розв'язання. Експерти допомагають ОПР на всіх стадіях постановки й розв'язання ЗПР.

_Аналітиками_ (консультантами, дослідниками) називають спеціалістів із теорії прийняття рішень. Вони розробляють модель (математичну, інформаційну) задачі прийняття рішень (ЗПР), процедури прийняття рішень, організовують роботу ОПР і експертів.

У найпростіших ситуаціях ОПР може виступати одним у трьох ролях, у більш складних &mdash; ОПР може поєднувати функції аналітика, звертаючись до спеціалістів із вузьким профілем для вирішення часткових проблем. У загальному випадку ОПР (наприклад, президент або
профільний комітет Верховної Ради) залучає до вирішення державних
проблем аналітиків &mdash;консультантів, які, у свою чергу, звертаються до
експертів. ОПР &mdash; головнокомандуючий має колективного консультанта &mdash; Генеральний штаб, який, у свою чергу, організовує роботу експертів &mdash; спеціалістів з озброєння, хімічного й біологічного захисту, політологів, метеорологів тощо.

У практичних (прикладних) задачах прийняття рішень формалізація
кожного кроку процесу прийняття рішень (поданих на рис. 1.1.1) пов'язана з певними, іноді дуже складними, проблемами. У першу чергу, постає проблема визначення мети та засобів її досягнення. Можна ставити
апріорі недосяжні або навіть абсурдні чи злочинні цілі ("моя мета &mdash; пробігти стометрівку за п'ять секунд", "наша мета &mdash; комунізм", "наша мета &mdash;
чистота раси" і т. д.). Можна використовувати нецивілізовані, навіть
злочинні, методи досягнення цілком досяжної мети ("мета &mdash; стати
президентом", "стати багатим", "отримати п'ятірку на іспиті" і т. д.).

Але зараз не про це. Нас цікавить формалізація ЗЗПР, її описання
на мові математики з метою моделювання практичних ситуацій прийняття рішень. І якщо математична модель призведе до факту неіснування розв'язку поставленої задачі, наша мета буде досягнутою.
Припустимо тепер, що мета й методи її досягнення визначені. Постає
проблема побудови множини альтернатив &mdash; варіантів дій, направлених на досягнення мети. Тут, у першу чергу, виникає проблема побудови "повного списку" альтернатив. Можлива ситуація, коли не включення певної альтернативи призведе до неможливості розв'язання задачі або до її "неякісного" розв'язання. Так, не включення до економічної системи колишнього СРСР ринкових механізмів призвело до деградації суспільства й розпаду СРСР.

Не менш складною є проблема оцінки альтернатив &mdash; "до чого приведе та чи інша вибрана дія". Як правило, оцінки альтернатив мають
суб'єктивний характер, вони отримуються на основі обробки експертної інформації. Навіть якщо можна оцінювати альтернативи за допомогою "об'єктивних" процедур (наприклад, вимірювати вагу товару, відстань між населеними пунктами), постає проблема визначення
всіх або хоча б "найважливіших" аспектів оцінки кожної альтернативи. Тут також неврахування навіть одного аспекту в оцінці варіантів
дії може призвести до катастрофічних наслідків (згадаймо Чорнобильську катастрофу &mdash; неврахування ризику аварії при будівництві
АЕС привело до трагічних результатів).

Остання принципова складність (але не остання за значенням) &mdash; вибір принципу порівняння альтернатив і на його основі &mdash; принципу оптимальності. Якщо на попередньому етапі визначені числові оцінки
альтернатив, то вибір принципу оптимальності зводиться до вибору
критерію (критеріїв) оптимізації, який максимально відповідає меті
ЗЗПР. Так, якщо для тренера футбольної команди мета &mdash; перемога у
наступному матчі, то за принцип оптимальності може слугувати такий
критерій: "Перемагає та команда, яка виконує за матч більшу сумарну
кількість успішних тактично-технічних елементів" (передач м'яча, відборів, ударів по воротах і т. д.). Такий принцип не раз висловлював
В. Лобановський. Як правило, визначення (побудова, прийняття) принципу оптимальності відбувається у декілька етапів. Так, якщо мета
ЗЗПР описується декількома числовими критеріями (і, отже, маємо задачу багатокритеріальної оптимізації), необхідно визначити &mdash; на основі
якого "глобального" принципу оптимальності будуть порівнюватись (і
вибиратись кращі) альтернативи.

Проблеми реалізації останнього блоку схеми пов'язані, у першу чергу, із математичними труднощами розв'язання задач, що виникають.
Тут і велика розмірність, і проблеми існування розв'язку, і збіжність
процедур його побудови і т. д.

Розглянемо приклади змістовної інтерпретації блоків ЗЗПР.

1. **Визначення мети та засобів.** Розглянемо такі приклади.
	1. Християнська доктрина визначає мету земного існування людини як "спасіння душі". 
		Засоби &mdash; будь-які, що не суперечать заповідям
		"Нового заповіту" (не вбивай; не гнівайся на ближнього; не чини перелюбу; не клянись, але виконуй клятви свої перед Господом; не протився
		злому, і коли вдарить тебе, хто у праву щоку твою, &mdash; підстав йому й іншу; любіть і ворогів своїх; про милостиню; про піст; складайте собі скарби на небі; покладайте на Бога надію свою; не судіть своїх ближніх ("Не
		суди, але викривай"); ходіть дорогою вузькою; стережіться фальшивих
		пророків; чиніть волю отця вашого небесного; не будуйте на піску).

	2. Сучасна гуманістична доктрина визначає ціль життя людини як "самореалізацію"
		(Е. Фромм) [44]. Засоби досягнення цієї мети
		визначаються, перш за все, "Декларацією прав людини", у якій на
		першому місці, безумовно, стоїть християнський принцип "не убий"
		("право на життя"). Інші біблійні принципи не є категоричними імперативами. Із принципом "Не вбивай" тісно пов'язана проблема
		смертної кари. Якщо мета &mdash; "справедливість за будь-яку ціну" (зокрема, "око за око, зуб за зуб"), то смертна кара допустима. Але, якщо дещо переформулювати проблему смертної кари &mdash; чи згодні ви,
		щоб разом із шістьма злочинцями був страчений один невинний
		(а саме така статистика хибних смертних вироків за останні 150 років у Європі й Америці), то принцип "справедливість за будь-яку
		ціну" стає зовсім не очевидним.

	3. Видатний філософ ХХ ст. Микола Бердяєв визначав мету
		життя людини не як "спасіння", а як "творче сходження", засіб &mdash;
		"свобода" [13].

	4. "Хто ж вони, справжні філософи? Ті, хто метою мають істину"
		(Платон).

		"Життя перестає прив'язувати до себе щойно зникає мета"
		(І. Павлов).
		
		"Минуле і сучасне &mdash; наші засоби, тільки майбутнє &mdash; наша мета"
		(Блез Паскаль).
		
		"Мета влади &mdash; влада" (Дж. Оруел).

	5. Мета &mdash; вилікувати хворого. Засоби &mdash; усе те, що надається системою охорони 
		здоров'я.

	6. Мета &mdash; побудувати літак. Засоби &mdash; 300 млн грн. на початок
		2010 р.

	7. Мета &mdash; виграти футбольний матч, засоби у тренера &mdash; сформувати команду на 
		даний матч із наявних 25 футболістів.

	8. Мета &mdash; "щастя всього людства". Цю мету висували й висувають
		філософи, політики, пророки, авантюристи. І якщо з метою все зрозуміло (про формалізацію терміна "щастя" тепер не йдеться &mdash; на Всесвітньому економічному форумі в Давосі в січні 2006 р. один із семінарів мав назву "Щастя &mdash; це&hellip;"), то із засобами її досягнення набагато
		складніше. Згадаймо хоча б Ф. Достоєвського &mdash; "щастя всього людства
		не варте однієї сльозинки дитини"; Мао Цзедуна &mdash; "заради перемоги
		соціалізму можна пожертвувати половиною людства"; Ф. Ніцше &mdash; "хочеш бути щасливим &mdash; не мрій".

		Доцільно тут згадати і слова: "Політики &mdash; це люди, найбільш нерозбірливі в засобах (досягнення мети)". Сучасна історія, на жаль,
		повністю підтверджує цей вислів. Прикладів тут безліч, і читач легко
		може їх навести. Ми ж лише процитуємо слова Максима Горького
		про те, що "Леніну, як вождю, притаманна для цієї ролі необхідність
		у відсутності моралі" і слова Мітчела Канора (розробника "Lotus"),
		який називає Білла Гейтса "найуспішнішим і яскравим представником тих, хто грає на стратегії &mdash; перемога за будь-яку ціну". А взагалі
		проблема "мета &mdash; засоби" стара як світ. Ми ж приєднуємось до думки, що історичний досвід показує, що відмова від вимог моралі є
		завжди програшною стратегією.

	9. Мета &mdash; отримання максимального задоволення від життя (про
		формалізацію поняття задоволення див. вище у Е. Фромма). Засоби
		студента &mdash; 50 грн (на початок 2009 р.).

	10. Мета викладача &mdash; навчити студента своєму предмету, засоби
		викладання &mdash; "цікаво, зрозуміло і &hellip; весело" (принцип видатного вченого і педагога ХХ ст. академіка &mdash; фізика П. Капіци).

	Загальний підхід до поняття мети був розвинутий на початку
	40-х рр. ХХ ст., у першу чергу, Н. Вінером, який писав, що термін "цілеспрямоване" означає, що дія або поведінка допускає тлумачення як
	направлені на досягнення деякої мети, тобто деякого кінцевого стану,
	при якому об'єкт вступає у певний зв'язок у просторі або часі з деякими іншими об'єктами або подіями. Із філософськими аспектами в
	об'єктивізації поняття мети можна ознайомитись у роботі [11].
	
	Розглянемо основні типи цілей і способи їхньої формалізації, що застосовуються при прийнятті рішень.
	
	_"Якісна" ціль_ характеризується тим, що будь-який результат або повністю задовольняє ці цілі або повністю не задовольняє, причому результати, що задовольняють ці цілі нерозрізненні між собою точно так
	як нерозрізнені між собою й результати, що не задовольняють ці цілі.
	Наприклад, ціль &mdash; стати чемпіоном. І якщо ціль досягнуто, то немає
	значення, як її досягнуто &mdash; наполегливим тренуванням, підкупом суддів, знищенням конкурентів тощо. Якісну ціль можна формалізувати у
	вигляді деякої підмножини $$A$$ множини всіх можливих результатів, де
	будь-який результат $$a \in A$$ задовольняє цій цілі, а будь-який результат
	$$a \notin A$$ не задовольняє їй. Множина $$A$$ при цьому називається цільовою
	підмножиною. Так, якщо ціль "зайняти призове місце", то цільова
	множина $$A$$ &mdash; перші три місця з усіх можливих.
	
	Якісну ціль (її можна назвати якісною "чіткою" ціллю) можна узагальнити так. Нехай кожному результату а відповідає "ступінь" виконання цілі $$0 \le \mu(a) \le 1$$. Зокрема, якщо ціль чітка, то $$\mu(a) = 1$$, якщо $$a \in A$$; $$\mu(a) = 0$$, якщо $$a \notin A$$. Так, нехай у останньому прикладі
	$$\mu(\text{І місце}) = 1, \mu(\text{II}) = 0.9, \mu(\text{III}) = 0.7$$ і "нечітка" цільова множина $$A$$ визначається умовою: $$\mu(a) \ge 0.7$$. Зазначимо, що значення функції $$\mu(a)$$
	(функція "належності" &mdash; див. Розділ 7 "Прийняття рішень в умовах нечіткої інформації") не є оцінкою результату $$a$$, а лише "ступінь" його
	належності до цільової множини $$A$$ (можливо "націлюватись" на І місце недоцільно з погляду прикладання надмірних зусиль).

	_"Кількісна" ціль_ є результатом вибору на множині результатів, що
	описуються кількісно, за допомогою деякої дійснозначної функції
	$$f: A \to E^1$$. Задача прийняття рішень у цьому випадку зводиться до
	знаходження оптимуму (максимуму чи мінімуму) функції $$f$$ на множині $$A$$. Зазначимо, якщо "якісну чітку" ціль формально можна звести до
	"кількісної" (поклавши, наприклад, $$f(a) = 1$$, $$a \in A$$; $$f(a) = 0$$, $$a \notin A$$), то
	ЗПР з "якісною нечіткою" ціллю вимагають додаткової інформації до
	своєї формалізації.

	Якщо цільова функція є векторною, тобто кожен результат описується набором чисел, що характеризують його "вартість", "ефективність", "надійність", то маємо задачу багатокритеріальної оптимізації.

	Зазначимо, якщо ціль задано з допомогою скалярної цільової функції
	$$f$$, то можна визначити пов'язану з цією ціллю перевагу серед результатів: із двох результатів кращим буде той, якому відповідає більше (менше) значення цільової функції (при рівних значеннях цільової функції
	говорять про байдужність результатів). Назвемо таку перевагу перевагою, що пов'язана з цільовою функцією $$f$$. Але можна говорити про перевагу й без наявності цільової функції, задаючи множину пар результатів, для яких перший результат у парі є кращим за другий (або не гіршим). Останнє означає, що на декартовому добутку результатів $$A \times A$$
	задане деяке бінарне відношення. За заданим бінарним відношенням у
	загальному випадку неможливо побудувати цільову функцію, пов'язану
	з ним. Відомі достатні умови (властивості), яким повинно задовольняти
	бінарне відношення для того, щоб існувала цільова функція, пов'язана з
	ним (див. Розділ 2 "Основи теорії корисності"). Отже, задання переваг у
	вигляді бінарного відношення на множині результатів є більш загальною
	формою формалізації цілі. З іншого боку, на практиці дуже часто відношення переваги задається саме бінарним порівнянням &mdash; про це говорить і народна мудрість "Усе пізнається у порівнянні".

2. **Побудова множини варіантів дій і їхніх наслідків.** Формально
	блоки 2 і 3 схеми ЗЗПР є незалежними, але змістовно зв'язаними (для
	чого розглядати альтернативи, які не можна принципово оцінити?).
	Тому на прикладах розглянемо їх сумісно. У блоці 2 альтернативи будуються на основі евристичних, неформальних процедур; у блоці 3 на
	основі формально-математичних, експертних процедур здійснюється
	оцінювання їхніх наслідків.

	Розглянемо основні типи залежностей між альтернативами та наслідками.

	Найпростіший тип залежності &mdash; _детермінований_, коли кожна альтернатива приводить до єдиного наслідку. При цьому між альтернативами та наслідками існує функціональна залежність і такі ЗПР називаються _ЗПР в умовах визначеності_. Наявність функціональної залежності приводить до того, що ЗПР достатньо описувати лише у термінах цілі й альтернатив.

	Найчастіше вибрана альтернатива може привести до множини наслідків. Такий тип залежності називається _недетермінованим_. При
	цьому між альтернативами та наслідками не існує функціональної залежності й такі ЗПР називаються _ЗПР в умовах невизначеності_. Невизначеність є проявом впливу на наслідок зовнішнього середовища, як ще кажуть &mdash; природи. Якщо при цьому задано розподіл станів природи, то маємо ЗПР в умовах ризику. Якщо невизначеність є проявом
	впливу на наслідок інших ОПР, які мають свої цілі, то така задача називається _ЗПР в умовах конфлікту_.

	Інколи, як множини альтернатив (наслідків), так і зв'язок між ними
	є _нечіткими_. При цьому між альтернативами й наслідками також не
	існує функціональної залежності і такі ЗПР називаються _ЗПР в умовах
	нечіткої інформації_. Нечіткість, як правило, є проявом суб'єктивності
	ОПР, експертів та аналітиків, які формулюють ЗПР.

	Пропонуємо читачеві (як завдання на самостійну роботу) побудувати множину варіантів для досягнення мети в умовах визначених засобів для наведених вище прикладів.

	Детальніше проаналізуємо проблему 1.9 &mdash; "Отримати максимальне
	задоволення за 50 грн". Можливі дії: $$a_1$$ &mdash; піти в кіно; $$a_2$$ &mdash; піти на дискотеку; $$a_3$$ &mdash; придбати книгу; $$a_4$$ &mdash; залишитись вдома і т. д.
	Цілком можливо, що два різні індивіди оцінять альтернативи (наслідки вибраних дій) так: $$a_1$$ &mdash; 5 балів, $$a_2$$ &mdash; 4, $$a_3$$ &mdash; 2, $$a_4$$ &mdash; 1 (екстраверт, кінолюб); $$a_1$$ &mdash; 2, $$a_2$$ &mdash; 1, $$a_3$$ &mdash; 5, $$a_4$$ &mdash; 3 (інтраверт, бібліофіл).
	У цій задачі зв'язок між альтернативами й наслідками є детермінованим, ЗПР достатньо описувати лише у термінах цілі й альтернатив.

	Зв'язок між альтернативами та наслідками найчастіше є недетермінованим, залежним від "станів природи".

	Так, збираючись зранку на заняття, залежно від станів природи $$y_1$$&ndash;$$y_4$$ (тепло &mdash; сонячно, тепло &mdash; дощ, холодно &mdash; сонячно, холодно &mdash; дощ),
	студент повинен вибрати одну з альтернатив $$a_1$$&ndash;$$a_4$$ (іти в одному костюмі, взяти парасольку, одягнути плащ, пальто). Оцінки альтернатив
	(за п'ятибальною шкалою) внесемо у таблицю:

	&nbsp;  | $$y_1$$ | $$y_2$$ | $$y_3$$ | $$y_4$$
	------- | ------- | ------- | ------- | -------
	$$a_1$$ |    5    |    2    |    2    |    1   
	$$a_1$$ |    3    |    5    |    3    |    3   
	$$a_1$$ |    2    |    3    |    2    |    3   
	$$a_1$$ |    2    |    4    |    5    |    4   

	Якщо в прикладі 1.1.6 замовником промисловості виступає уряд,
	то альтернативами можуть бути конструкторські бюро й літакобудівні
	заводи України (Київ, Харків), Росії тощо. Обираючи меню, ОПР оцінює комплексний обід за трьома критеріями: за п'ятибальною шкалою &mdash; вартість ($$f_1$$ &mdash; мінімізувати), калорійність ($$f_2$$ &mdash; максимізувати
	або мінімізувати), смакові якості ($$f_3$$ &mdash; максимізувати). Крім того, нехай оцінки за переліченими критеріями залежать від стану "природи"
	(у якого з трьох постачальників було закуплено продукти), причому
	відомі ймовірності реалізації станів (із імовірністю $$1/4$$ товари було
	закуплено у І або ІІ постачальника, із імовірністю $$1/2$$ &mdash; у ІІІ). Нехай
	також ОПР вибирає альтернативи за допомогою деякого випадкового
	механізму, зумовленого тим, що двічі на тиждень доцільно вибирати
	пісну дієту (альтернатива $$a_3$$ &mdash; салат з капусти, овочевий суп, каша,
	компот), двічі &mdash; рибну ($$a_2$$ &mdash; салат з огірків, борщ, риба, сік) і тричі &mdash;
	м'ясну ($$a_1$$ &mdash; салат з капусти, солянка, котлети, компот). Тоді оцінки
	наслідків можна описати наступною таблицею ($$q$$ &mdash; імовірнісний розподіл станів
	природи, $$р$$ &mdash; розподіл альтернатив):

	<table>
		<thead>
			<tr>
				<th> </th> <th colspan="3"> $$y_1$$ </th> <th colspan="3"> $$y_2$$ </th> <th colspan="3"> $$y_3$$ </th> <th> $$p$$ </th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td> </td> <td> $$f_1$$ </td> <td> $$f_2$$ </td> <td> $$f_3$$ </td> <td> $$f_1$$ </td> <td> $$f_2$$ </td> <td> $$f_3$$ </td> <td> $$f_1$$ </td> <td> $$f_2$$ </td> <td> $$f_3$$ </td> <td> </td>
			</tr>
			<tr>
				<td> $$a_1$$ </td> <td> $$4$$ </td> <td> $$5$$ </td> <td> $$4$$ </td> <td> $$3$$ </td> <td> $$5$$ </td> <td> $$3$$ </td> <td> $$2$$ </td> <td> $$4$$ </td> <td> $$2$$ </td> <td> $$2/7$$ </td>
			</tr>
			<tr>
				<td> $$a_2$$ </td> <td> $$3$$ </td> <td> $$4$$ </td> <td> $$4$$ </td> <td> $$2$$ </td> <td> $$4$$ </td> <td> $$3$$ </td> <td> $$2$$ </td> <td> $$4$$ </td> <td> $$3$$ </td> <td> $$2/7$$ </td>
			</tr>
			<tr>
				<td> $$a_2$$ </td> <td> $$2$$ </td> <td> $$3$$ </td> <td> $$3$$ </td> <td> $$1$$ </td> <td> $$3$$ </td> <td> $$2$$ </td> <td> $$1$$ </td> <td> $$2$$ </td> <td> $$1$$ </td> <td> $$3/7$$ </td>
			</tr>
			<tr>
				<td> $$q$$ </td> <td colspan="3"> $$1/4$$ </td> <td colspan="3"> $$1/4$$ </td> <td colspan="3"> $$1/2$$ </td> <td> </td>
			</tr>
		</tbody>
	</table>
	
	