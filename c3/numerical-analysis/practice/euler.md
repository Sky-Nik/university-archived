{% include mathjax %}

### Задача

> Явним методом Ейлера виконати $$2$$ кроки $$h = 0.05$$, $$\frac{\diff u}{\diff x} = x^2 + u$$, $$u(1) = 1$$.

### Розв'язок

Нагадаємо, що метод Ейлера має вигляд $$y_{i + 1} = y_i + h \cdot f(x_i, y_i)$$.

початкові значення зрозуміло які, $$x_0 = 0$$, $$y_0 = u_0 = u(0) = 1$$.

Тобто маємо

\begin{equation}
	\begin{aligned}
		y_1 &= y_0 + h \cdot f(x_0, y_0) = \newline
		&= 1 + 0.05 \cdot f(0, 1) = 1.05
	\end{aligned}
\end{equation}

Далі

\begin{equation}
	\begin{aligned}
		y_2 &= y_1 + h \cdot f(x_1, y_1) = \newline
		&= 1.05 + 0.05 \cdot f(0.05, 1.05) = \newline
		&= 1.05 + 0.05 \cdot (0.05^2 + 1.05) = \newline
		&= 1.05 + 0.052625 = 1.102625
	\end{aligned}
\end{equation}

[Назад до задач](README.md)

[Назад на головну](../README.md)
