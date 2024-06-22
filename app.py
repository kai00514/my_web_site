from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        'name': '藤島海',
        'title': 'AsFilm株式会社代表',
        'affiliation': 'AIエンジニア',
        'description': '2021年 東京工業大学 情報理工学院 知能情報コース卒業後, 同大学院 同コースにて修士課程修了. 修士課程では主に人間の意思決定プロセスをモデル化することでより自然な人間とAIのインタラクションの実現を目指す研究に従事. 学部時代には, 機械学習を用いた自動作曲や, 深層学習を用いた画像生成の研究に取り組む. 2020年イーロン大学サマーリサーチプログラムに参加. 学業と並行して, サービス開発にも携わり, 2018年よりAIスタートアップにてエンジニア/リサーチャーとしてインターン, 2020年12月よりソニーイノベーション人材育成制度にて研究を実施. 2022年 Forbes Japan 30 Under 30に選出. 第3回日本オープンイノベーション大賞 選抜認定証, WSDM2022 Best Paper Runner-up Award, 東京工業大学学長賞, 等を受賞.',
        'education': [
            'コンピューターサイエンス専攻 博士課程, 2021-',
            '東京工業大学 情報理工学院, 2016-2021'
        ],
        'interests': [
            'ヒューマンAIインタラクション',
            '機械学習',
            '音楽情報科学'
        ]
    }
    
    news = [
        'Forbes Japan 30 Under 30 2022に選出されました。',
        '2023年8月14日にKDD2022にて発表を行いました。学生に対するチュートリアルを行いました。',
        '2023年7月18日に第3回夏季学校に 先輩生として登壇しました。',
        '2023年4月8日に情報処理学会全国大会2023にて、3件発表を行いました。',
        '情報処理学会第85回全国大会にて、学生奨励賞を受賞しました。',
        '情報システムのトップ国際会議RecSys2022にて、査読付き論文・デモ論文それぞれ1本を発表しました。',
        '2021年8月8日に、「絵じゃんけんのための画像生成AI」(Amazon)を公開しました。',
        '東京工業大学のOSAに認定され、2021年3月31日に表彰されました。',
        '東京工業大学学長賞(修士課程の学業成績優秀者)を受賞しました。',
        '第3回日本オープンイノベーション大賞 選抜認定証を受賞しました (2021年2月)。',
        '2020年12月3日に開催された第四回共創イノベーションシンポジウムにて登壇しました。',
        '2020年10月9日に博報堂賞2位(Recsys2020)にて受賞しました。'
    ]
    
    talks = [
        {
            'title': 'Workshop Tutorial at CONSEQUENCES, RecSys2022',
            'description': 'CONSEQUENCES Workshop RecSys2022 "Tutorial on Causal-Based Preference Elicitation"',
            'date': 'Sep 22, 2022',
            'location': 'Seattle, WA, USA'
        },
        {
            'title': 'Counterfactual Tutorial at KDD2022',
            'description': 'KDD2022 Tutorial on Counterfactual Machine Learning',
            'date': 'Aug 14, 2022 - Aug 18, 2022',
            'location': 'Washington, DC, USA'
        },
        {
            'title': 'Counterfactual Tutorial at RecSys2021',
            'description': 'RecSys2021 Tutorial on Counterfactual Evaluation and Learning',
            'date': 'Sep 28, 2021',
            'location': 'Amsterdam, Netherlands (Virtual)'
        }
    ]
    
    return render_template('index.html', profile=profile, news=news, talks=talks)

if __name__ == '__main__':
    app.run(debug=True)