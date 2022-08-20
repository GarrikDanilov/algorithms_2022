"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# О(1) - константная
def authorization_const(users, login, password):
    if users.get(login):                                                                        # О(1) - константная
        user = users.get(login)                                                                 # О(1) - константная
        if user['password'] == password:                                                        # О(1) - константная
            return 'Авторизация пройдена' if user['state'] else 'Активируйте учетную запись'    # О(1) - константная
        else:
            return 'Неверный пароль'                                                            # О(1) - константная
    return 'Неверный логин'                                                                     # О(1) - константная


# O(N) - линейная
def authorization_lin(users, login, password):
    for logins, info in users.items():                                                            # O(N) - линейная
        if logins == login:                                                                       # О(1) - константная
            if info['password'] == password:                                                      # О(1) - константная
                return 'Авторизация пройдена' if info['state'] else 'Активируйте учетную запись'  # О(1) - константная
            else:
                return 'Неверный пароль'                                                          # О(1) - константная
    return 'Неверный логин'                                                                       # О(1) - константная


if __name__ == '__main__':
    users = {'user_1': {'password': 123, 'state': False}, 'user_2': {'password': 456, 'state': True},
             'user_3': {'password': 789, 'state': True}}

    print('Константная сложность:')
    print(authorization_const(users, 'user_1', 123))
    print(authorization_const(users, 'user_2', 222))
    print(authorization_const(users, 'user_3', 789))
    print('\n')

    print('Линейная сложность:')
    print(authorization_lin(users, 'user_1', 123))
    print(authorization_lin(users, 'user_2', 222))
    print(authorization_lin(users, 'user_3', 789))
