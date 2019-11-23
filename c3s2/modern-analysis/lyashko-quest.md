{% include mathjax %}

## 2. Теореми Веєрштраса

### На компакті

> **Теорема**: Неперервна функція на компакті (1) обмежена і (2) досягає своїх екстремумів.

_Доведення_:

1. Доведемо, що функція $$f(x)$$ обмежена зверху на проміжку $$[a, b]$$ (обмеженість знизу доводиться аналогічно).

	Припустимо супротивне, тобто припустимо, що $$f(x)$$ не є обмеженою на проміжку $$K$$.

	Тоді для будь-якого натурального числа $$n$$ ($$n = 1, 2, \ldots$$) знайдеться хоча б одна точка $$x_n$$ з $$K$$ така, що $$f(x_n) > n$$ (інакше $$f(x)$$ була б обмежена зверху на $$K$$).

	Таким чином, існує послідовність точок $$\{x_n\}$$ з $$K$$ така, що відповідна їй послідовність значень функції $$\{f(x_n)\}$$ є нескінченно великою. В силу теореми Больцано-Вейєрштрасса, з послідовності $$\{x_n\}$$ можна виділити підпослідовність, яка збігається до точки $$c$$, що належить $$K$$. Позначимо цю послідовність символом $$\{x_{n_k}\}$$ ($$k = 1, 2, \ldots$$). В силу неперервності функції $$f(x)$$ у точці $$c$$ відповідна підпослідовність значень функції $$\{f(x_{n_k})\}$$ повинна збігатися до $$f(c)$$. Але це неможливо, оскільки підпослідовність $$\{f(x_{n_k})\}$$, яку виділено з послідовності $$\{f(x_n)\}$$, сама є нескінченно великою. Отже, наше припущення про необмеженість хибне.

	Теорему доведено. $$\square$$

2. Доведемо, що функція $$f(x)$$ неперервна на $$K$$ досягає своєї точної верхньої межі $$M$$ (досягнення точної нижньої межі доводиться аналогічно).

	Припустимо супротивне, тобто припустимо, що функція $$f(x)$$ не приймає значення точної верхньої межі у будь-якій точці $$K$$. Тоді для всіх точок $$K$$ нерівність $$f(x) < M$$ є правильною, і ми можемо розглянути на $$K$$ скрізь додатну функцію

	\begin{equation}
		F(x) = \frac{1}{M - f(x)}.
	\end{equation}

	Оскільки знаменник $$M - f(x)$$ не обертається в нуль та неперервний на $$K$$, то за теоремою про неперевність частки неперервних функцій, функція $$F(x)$$ також неперервна на $$K$$. У цьому разі, згідно з першою частиною теореми Веєйрштраса, функція $$F(x)$$ обмежена на $$K$$, тобто знайдеться таке додатне число $$B$$, що для будь-якого $$x$$ з $$K$$ справедлива нерівність:

	\begin{equation}
		F(x) = \frac{1}{M - f(x)} \le B.
	\end{equation}

	Її можна переписати (враховуючи що $$M - f(x) > 0$$ у такому вигляді:

	\begin{equation}
		f(x) \le M - \frac{1}{B}
	\end{equation}

	Це співвідношення правильне для будь-яких точок $$x$$ з $$K$$. Воно суперечить тому, що $$M$$ є точною верхньою межею (найменшою з усіх верхніх меж) функції $$f(x)$$ на $$K$$. Отже, отримана суперечність доводить хибність нашого припущення.

	Теорему доведено. $$\square$$

### Теореми Вейєрштраса у Банахових просторах

Нехай $$\rho$$ &mdash; метрика в метричному просторі $$B$$, тобто $$\rho : B \times B \to \RR$$:

1. для будь-яких $$x, y$$: $$\rho(x, y) \ge 0$$, $$\rho(x, y) = 0 \iff x = y$$.

2. $$\rho(x, y) = \rho(y, x)$$.

3. $$\rho(x, z) + \rho(z, y) \ge \rho(x, y)$$.

> **Означення 1**. Функціонал $$f$$ називається $$\rho$$-напівнеперервним знизу, якщо $$\Lim_{x \to \infty} \rho(x_n, x) \to 0 \implies \Lim_{x \to \infty}f(x_n) \ge f(x)$$.

> **Означення 2.** Множина $$X$$ з метричного простору $$B$$ називається $$\rho$$-компактною, якщо з довільної послідовності точок $$\{x_n\} \subset X$$ можна обрати підпослідовність збіжну до $$x \in X$$.

> **Теорема 1.** Якщо функція $$f$$ є визначеною, скінченною, $$\rho$$-напівнеперервною знизу на $$\rho$$-компактній множині $$X$$, то $$f$$ досягає на $$X$$ свого мінімального значення. Тобто існує $$x \in X: f(x) = \Inf_{y \in X} f(x)$$.

Нехай тепер $$E$$ &mdash; банахів простір.

> **Означення 3.** Послідовність $$\{x_n\} \subset E$$ називається слабко збіжною до елемента $$x \in E$$, якщо для будь-якого лінійного неперервного функціоналу $$F$$: $$F(x_n) \to F(x)$$.

> **Означення 4.** Функціонал $$f$$ називається слабконапівнеперервним знизу, якщо з того що $$x_n \to x$$ випливає, що $$\Lim_{n \to \infty} f(x_n) \ge f(x)$$.

> **Означення 5.** Множина $$X$$ з банахового простору $$E$$ називається слабкокомпактною, якщо з довільної послідовності точок $$\{x_n\} \subset X$$ можна обрати підпослідовність, що слабко збігається до деякої $$x \in X$$.

> **Теорема 2.** Якщо функція $$f$$ визначена, скінченна, слабконапівнеперервна знизу на слабкокомпактній множині $$X$$, то $$f$$ досягає на $$X$$ свого мінімального значення.

## 3. Необхідні умови екстремуму. Опуклість функцій

### Необхідні умови екстремуму

> **Теорема Ферма** (_необхідна умова екстремуму_): Нехай дійсна функція $$f$$ визначена в околі деякої точки $$x_0$$ і має в цій точці похідну. Тоді якщо в цій точці $$f$$ має екстремум то $$f'(x_0) = 0$$.

Геометрично це означає, що дотична до графіка функції $$f$$ в точці $$(x_0, f(x_0))$$ паралельна до осі абсцис $$Ox$$.

> **Теорема 2** (_сильніше необхідна умова екстремуму_): Нехай дійсна функція $$f$$ визначена в околі деякої точки $$x_0$$ і має в цій точці кілька похідних. Тоді якщо в цій точці $$f$$ має екстремум то перша ненульова похідна &mdash; парного степеню, причому якщо вона від'ємна то екстремум &mdash; максимум, а якщо додатна то мінімум.

> **Теорема 3**: $$X^\star = \{x^\star \in X: \Min_{x \in X} \langle f'(x^\star), x - x^\star \rangle = 0\}$$.

### Опуклість функцій

> **Означення:** _Опукла функція_ &mdash; функція, яка визначена на опуклій множині лінійного простору, і задовольняє нерівності
>
> \begin{equation}
> f(\lambda x + (1-\lambda) y) \le \lambda f(x) + (1-\lambda) f(y)
> \end{equation}
>
> при всіх $$\lambda \in [0, 1]$$.

> **Означення:** _Строго опукла функція_ &mdash; функція, яка визначена на опуклій множині лінійного простору, і задовольняє нерівності
>
> \begin{equation}
> f(\lambda x + (1-\lambda) y) < \lambda f(x) + (1-\lambda) f(y)
> \end{equation}
>
> при всіх $$\lambda \in (0, 1)$$.

> **Означення:** _Сильно опукла з параметром $$m > 0$$ функція_ &mdash; диференційовна функція, яка визначена на опуклій множині лінійного простору, і задовольняє нерівності
>
> \begin{equation}
> \langle \nabla f(x) - \nabla f(y), x - y \rangle \ge m \|x - y\|^2.
> \end{equation}

Увігнутість/угнутість визначається аналогічно, але всі нерівності в інший бік.

[Назад на головну](README.md)