from sklearn.feature_extraction.text import CountVectorizer

text=[
    "Uh, summa-lumma, dooma-lumma, you assumin' I'm a human What I gotta do to get it through to you I'm superhuman?",

"Innovative and I'm made of rubber so that anything You say is ricochetin' off of me, and it'll glue to you",

"and I'm devastating, more than ever demonstrating How to give a motherfuckin' audience a feeling like it's levitating Never fading,",

"and I know the haters are forever waiting For the day that they can say I fell off, they'll be celebrating",

"Cause I know the way to get 'em motivated I make elevating music, you make elevator music"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

print("结果:")
print(X.toarray())

