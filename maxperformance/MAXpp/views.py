from django.shortcuts import render
import requests


def index(request):
    return render(request, 'MAXpp/index.html')


def auth_view(request):
    username = request.POST['username']
    if username.replace(" ", "") != "":
        return scores_view(request, username)
    else:
        return render(request, 'MAXpp/index.html', {'error_message': "Please input a username"})


def scores_view(request, username):
    u = requests.get(
        "https://osu.ppy.sh/api/get_user_best?k=c454ff459212656188160c05723e971579d18dcd&m=3&limit=50&u=" + username)
    score_data = u.json()
    nums = []
    mapid_list = []
    dt_list = []
    title_list = []
    diff_list = []
    star_list = []
    bpm_list = []
    time_list = []
    min_list = []
    sec_list = []
    listr300 = []
    list300 = []
    list200 = []
    list100 = []
    list50 = []
    list0 = []
    list_acc = []
    list_pp = []
    total_pp = 0

    for i in score_data:
        mapid_list.append(i['beatmap_id'])

        mods = bin(int(i['enabled_mods']))[2:]
        if len(mods) >= 7:
            if mods[-7] == '1':
                dt_list.append("+DT")
            else:
                dt_list.append("")
        else:
            dt_list.append("")

        listr300.append(int(i['countgeki']))
        list300.append(int(i['count300']))
        list200.append(int(i['countkatu']))
        list100.append(int(i['count100']))
        list50.append(int(i['count50']))
        list0.append(int(i['countmiss']))

        totalnotes = int(i['countgeki']) + int(i['count300']) + int(i['countkatu']) + int(i['count100']) + int(
            i['count50']) + int(i['countmiss'])
        list_acc.append("%.2f" % round(
            (int(i['countgeki']) * 16 + int(i['count300']) * 15 + int(i['countkatu']) * 10 + int(
                i['count100']) * 5 + int(
                i['count50']) * 2) / totalnotes * (100 / 16),
            2))

    for id in mapid_list:
        v = requests.get(
            "https://osu.ppy.sh/api/get_beatmaps?k=c454ff459212656188160c05723e971579d18dcd&b=" + id)
        map_data = v.json()

        for i in map_data:
            title_list.append(i['title'])
        diff_list.append(i['version'])
        star_list.append("%.2f" % round(float(i['difficultyrating']), 2))
        bpm_list.append(int(float(i['bpm'])))
        time_list.append(int(i['hit_length']))

    for i in range(0, len(star_list), 1):
        if dt_list[i] == "+DT":
            star_list[i] = "%.2f" % round(float(star_list[i]) * 1.38, 2)
            bpm_list[i] = int(bpm_list[i] * 1.5)
            time_list[i] = int(time_list[i] * 2 / 3)

        min_list.append(time_list[i] // 60)
        if len(str(time_list[i] % 60)) == 1:
            sec_list.append('0' + str(time_list[i] % 60))
        else:
            sec_list.append(str(time_list[i] % 60))

        stars = int(float(star_list[i]))
        maxpp = 20
        while stars > 1:
            maxpp *= (2 - stars / 10 + 0.2)
            stars -= 1
        stars = int(float(star_list[i]))
        maxpp = int(maxpp * ((2 - stars / 10 + 0.1) ** (float(star_list[i]) - stars)))
        pp = int(maxpp / (1.5 ** ((100 - float(list_acc[i])) / 10)))
        list_pp.append(pp)

    temp = list_pp[:]
    factor = 1
    for i in range(0, len(temp), 1):
        index = temp.index(max(temp))
        nums.append(index)
        temp[index] = -1
        total_pp = total_pp + list_pp[i] * factor
        factor = factor * 0.95
    total_pp = int(total_pp)
    return render(request, 'MAXpp/scores.html',
                  {'listr300': listr300, 'list300': list300, 'list200': list200, 'list100': list100,
                   'list50': list50, 'list0': list0, 'nums': nums, 'title_list': title_list,
                   'diff_list': diff_list, 'star_list': star_list, 'bpm_list': bpm_list, 'min_list': min_list,
                   'sec_list': sec_list, 'list_acc': list_acc, 'list_pp': list_pp, 'total_pp': total_pp,
                   'dt_list': dt_list, 'username': username})
