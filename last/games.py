def my_function(): #menu
    if grfuhdfihgiihrg == 0:
        basic.clear_screen()
        spaceinvad()
    elif grfuhdfihgiihrg == 1:
        basic.clear_screen()
        chutedebrique()
    elif grfuhdfihgiihrg == 2:
        basic.clear_screen()
        flappy()
    elif grfuhdfihgiihrg == 3:
        basic.clear_screen()
        chutedevoiture()
    elif grfuhdfihgiihrg == 4:
        basic.clear_screen()
        pongsolo()
          
    elif grfuhdfihgiihrg == 5:
        basic.clear_screen()
        badapple()
    elif grfuhdfihgiihrg == 6 :
        basic.clear_screen()
        trex()
    elif grfuhdfihgiihrg == 7 :
        basic.clear_screen()
        superman64()
    elif grfuhdfihgiihrg == 8 :
        basic.clear_screen()
        superman62()
bitcommander.on_event(BCPins.GREEN, BCEvents.DOWN, my_function)


def on_event_red_down(): #permet de retourner au menu
    control.reset()
bitcommander.on_event(BCPins.RED, BCEvents.DOWN, on_event_red_down)

def on_button_pressed_a(): #deplace le menu vers la gauche
    global grfuhdfihgiihrg
    if grfuhdfihgiihrg == 0:
        grfuhdfihgiihrg = 8
        basic.show_string("" + str((grfuhdfihgiihrg)))
    else:
        grfuhdfihgiihrg += -1
        basic.show_string("" + str((grfuhdfihgiihrg)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b(): #permet de deplacer le menu vers la droite
    global grfuhdfihgiihrg
    if grfuhdfihgiihrg == 8:
        grfuhdfihgiihrg = 0
        basic.show_string("" + str((grfuhdfihgiihrg)))
    else:
        grfuhdfihgiihrg += 1
        basic.show_string("" + str((grfuhdfihgiihrg)))
input.on_button_pressed(Button.B, on_button_pressed_b)

grfuhdfihgiihrg = 0
grfuhdfihgiihrg = 0
basic.show_string("" + str((grfuhdfihgiihrg)))

def on_forever():
    pass
basic.forever(on_forever)



def badapple(): #def qui va lancer le clip de bad apple
    music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.show_string("BAD APPLE")
    vs = "0:q,tc,tc,n76p,1aebk:2,1g5d,18y74:2,ab6kg,e8,g:2,55la8,sg:2,zk,w,3,74,2,1ekg:2,1962o:3,1s,4zsoy:5,4zz0g,2,8,1s:2,74:9,1s,2:2,8:2,74:7,74,8:5,1u:7,1s:2,2:3,8:2,2,20,18y68:2,1eki:2,1kz:2,2hzlw,2t58,sh:2,so,74:4,18y68:2,2t4w:a,18y68,74:3,1,1:2,w0:2,w,pa8,w:3,35s:2,w:6,35s:4,pa8:2,w,sg,3k,35s,74,35s,2hwcg,8,3d0:2,3t:3,2hwcg,18z2c,3lly:2,mh4w,1g5c:2,mh5a,5xoi,3imk,8mli,4w7:3,2hwcg:2,2t4w,2hwcg,35s,2t4w:2,3k:2,35s:5,35s:3,3k:2,2t4w:8,2ups:2,3k:5,1kw,1kw,1vgu8,2img0,jwctb:7,586tc,abq4g,1vpxc,cmfhc,55eyx,t7,9zojp,bdag,5gni8,ckav4,1x8g0,5b2c0,9ea4,41w,sm:2,2,1kw:2,1kw:4,2t8g,35s,4zsow,7hp1c,55eyo,pa8,5m9s0:2,39c,w,1ekg0,1fdw,1k,1k,3p,3r6,e8,1ts,3k,1ls,35s,1kw,b28,35s,6bk:3,2t4w:2,2t4w,35s:7,2t4w,2t4w:9,35s:f,35s,2t4w,2t4w:2,1kw:2,2t4w:2,1gxs:3,35s:2,35s:3,g,so,1eyo:6,1ekg:d,1ekg:l,4,1ekg:2,eg,sk,34:2,1kw,23up,mh4w:2,18zs1,18y68,mh34:2,pa8,35s,39c:3,3k:2,39c,35s,2ups,3o,4xs0,1xj44,1vf9c:8,2t4w,2tr0,i31lv,4gu0w,2t4w:3,2hwcg:2,18y68,18y68:2,18y68:2,18y80,2,1g5e,47r4,2t4w,1kw,6bk:2,74:3,5m9s,8,5mgw:2,6bk,8,6bk,6bk:2,8,74,5slc:3,4zsow:2,4zsow:3,5mgw,4,32q0:3,2hwcg:3,2hwcg:3,1kw,1kw:5,1kw:2,2t4y,9kw,35s,1s,4,4,1s,3k,2t6q:2,4e0y,2t8g:2,2we8:2,3o,2t8k,2t4w,3k,2t8g:3,4:3,74,74,39c,2zgg:2,6bk,4,5m9w,1enls:2,2t4w,18y68,2we9,18yzo,pac,mk90,3k:4,2t4w:4,74:2,74:3,2t4w,74,18zsw,76,1in4,1ekh,okxs,2tc0,8feo:2,5mgw,1mq,1ekg,49j6,2t4w,5m9s,2,74,5mbp,4,37k,mkbk,sg0,1agp0,5q8,3if5,74,mio4,3qv42,1hs0,18ydc,18z7k,2hxj4,d1c,d1c:2,74:6,cu8:2,cn4,w:2,f4:3,2o:2,sg,sg:2,w,1f0g:3,2hwcg:2,1aj28,9hc,1hq8,36p,1,2hy0w,4,136,2e8,q138,tc,1lt,18y68:2,6bo:6,1ekh,18y6b,191fk,vx34,1eld,8x0js,5qi9w,3rjsw,mh34,8,ao,3d0,3k,2t4w:2,2hzi8:3,18y68,18y68:2,2hwcg,35s,2t4w,5c,jz3jt,2:2,aq:4,6f8,6bk,5mdg,5m9u,2,1u,9s,w,6,8,a,5m9t,5m9t,35s:2,35s:2,35s:9,2t8g,2t8g:4,3k,3k:2,6bk,6bk:6,2kphc,2hwg0:2,2jh8k,1l4w,8y,2hwci:i,6bk,6bk:4,5m9s:8,5m9s:3,2:3,1kw,1mo:2,1ekg,4u8,sg,pa8:2,2t4w,mh34:2,1w4jo,mh34,1ycn4,1gch,1g8w,52le,q3l:9,5j4:2,35s:2,36p,2r,3o,zu,rfg,w8h,n9g8,1grc,191xc,k3m,neys,32xx:7,w,74,74:2,2hzi8,2i2o0:3,3k,78,e8,74:3,74,hs,3r7hc,heo,1s2q,1z4,5tz4,74,5uyo,cn4,iyo,cn4,2hwcg,dfk:2,8,8,zk,2hwjk,co0,w:7,1s,2,8y:2,1s:3,cw0,sg:4,w,w:5,g,8w:2,g:6,cn4,sg,dfk,1mhd,85m,jz56n,1kw:3,6bk,1kw,19ngg:4,b8qo,dht,1ekg,dfs,pa8,83k2,18y68,18y6o,ysch,18y6i:2,bxts,duo,g8c8w:4,5j4,6bk,cn4:5,9hc,w,cn5:2,mhwh,mh37,1t,mh34,4,mh38,eo4,18y68,1s,pa8,12gw:2,2hwcg,3quio,e8,1s,1mo,4si,2t6s:2,191c0,2tc4,74:2,mh34,mh34,18y68,2wao,4:2,6bk,6bk,18y68,1,1brb5,1o1s,2jaww,2i2o0,1ekg,1ekg,2wow:2,1r7k,4,1f5s,o1zc,o26g:2,1lc,1kw,2hwcg:2,1kw:3,1lk:3,d8g,4fhxk,2hwlh,5ssqr,1b3nm,qv4,4zthc,2dd,2njts,1ff4,1f1d,g,5mog,2hwcg,2iamk,5b2vg,a2hs0,eze2w,b8jk,cn4,cn4,5b18g:2,9zlds:2,4zsow,9zlds,4zsow:3,d1g,b8k0:3,35s,3k,2t4w:3,4zsow,4zsow,2t4w,bbsw,40,cqs,5b1q8,4zssg,b8jk,3o:2,a2eki,f277k:2,5c,4zsow:2,d1e,b8k0,2:3,39c,2t4w,2,4zsoy:2,4zsow,2t8g,35s,g,bl6o,cn4,em8:2,4zsow,1kw,6,6:2,4zsow:2,e8,d1c,505qo,bl6o,2t4w:2,4zssg:2,35s,4zsox,37k:2,4zsox,e1u8:2,505q8,cqo,505c0:2,4zsow,9zlhc,6bq,9zll2,5m9s,a57nk:2,6,5m9s,9zle0:3,g,g,g,368,b8k0,d1c,35s:2,35s:6,3k,2t4w:2,2t8g:3,5m9s,5m9s,1kw,6bk:4,6bk,1kw:4,3k:6,b28,7wg,1s:5,74:2,2t4w:2,2t4w,2ibr4,2i8zk:2,2wao,6ci,7i1om,50hzc:2,g:2,pa8,5yww,6bk,5m9u,1,7wg,6bk,9zmkg:2,26nuo,mh34,19auw,1eyw,517gi,4zspd,1kw,9zm6g,e80,2nw1s:2,5nuo:9,1kw:2,w0:2,g,5n28:4,8,2,360,2f4,gvls,1rlw,1brb5,1heeg,neiq,2t4w:2,5181t,14,84veo,1brb4,1viis,mha8,5m9s,194hs,1g76:2,n6dd,tc:4,2ksqs:4,4,4:3,3k:2,35s:6,2t4w:4,2t4w:3,2t4w:a,3k,35s,1s,2t4w,37k:2,1s,2t6o,4,1mo,2hwe8,1kw:2,4:g,39k,2t8o,2t4w:4,8iko,32m8,3d0,39c,2t4w,5ssk,2l0lo,4h6o,1af9g,25ib,mh41,x:4,sg:2,sg:2,w,1kw,1t,w:2,3,2t4w,4sg,3q:e,8,8:3,74:2,2hwcg:2,74:r,2hwcg:4,2hwe8:m,2hwcg,5mbk,6bk:2,1g5c,7wg:2,5m9s,5m9s,68qv4,6bk,1kw:2,74,1s,pa8,a33t6,aycxs,2kq9s,a0b28,pzi8,376m2,2hwcy,3t,3k,g:l,bl6w,g,5gtu0,cn4:2,e8,a5kao,5m9s,cn4:4,5m9s,55ez4,4zsow:2,6bk,5m9s,4zz0g,55eys,e8,3k,35s,2ubk,2ilmq,1aedc:2,mhxc,paa,sh,xpmo,vls,9znr4,am39s,sg,70uo,4zsox,69gyo,18y68,sw,pa8,3k,f4,dfk,io:8,1,18y68,68qv4,35s:a,35s:2,4zssg,4zsp0,2t4w,50hz4,pa8,7j4so,cnc,1ls,coao,18zr4,2o,3k,9zlj4,by82,am39w,1l3k,qvb8,8feq,gydk,paa:2,9zmkk,20,18zrc,1eo0,3r4,2kphc,6bk,6ozl,w:4,pa8:3,1en4,si,w,1lt:j,35s:2,35s:4,1ekg:i,1ekg:9,35s:4,35s:4,1ekg,1s,1:2,1ls,q2q,5m9s:2,pa8,tc,1,2hwcg,e1og:2,9zlds,18y68,5m9s,1ekg,4zsow,mh34:2,3if4,2i9e8,bl6o,b8y8,1l3c,1ekg0,5sso,39g:3,2t4w:f,pa8:4,mh34:c,35s,2,1s:3,35s:4,1s:4,8,1g75,7k,lc,1l3l,5ob4,g,36aa,35s,5m9w,6bs,74,cn6,es,5c,1s,4qy,1g5c,47pc,pa80,3k,sn8,194i8,1gy0,2kwgw,55im9,6xi,ab6ko,g:g,4:5,h:2,4,k:4,1,1:2,3k,h:3,w,g,35t,10,e9:2,1kw,ec,1kw,4,3d0,4,8,g,ao,5yww,5m9s,6bl,q2o,6bs,6bl,g:2,cn5,2wht,3k,sg,6io,2hwcg:2,cnl,23up,2hxxc,2t4w,b8pc,bc5e,5zbc,6bqkg,1dawy,4zz2c,d1iq0,ckkd4,h85w,505c0,b8jk,eebk,b8jk:2,2t4w,b8jk,47pg,1erk,7q96o,2u14,740,6bk,1g5c,775u,3wgsw,d1vo,2t4w,1w85d,h3qy,1ssg,vx2c,3t,1ekg,2gy,5078,23uo,sw,blkw,a1qv7,9zy20,h1c0,4zsow,ec,4zsow,9b1c,39e,2hwjk,zl,2:2,2hwjk:2,74,8,1o8w,348w,2,32tg,1bri8,74x,1w656,1eq2,n78i,w,1t,e,dt,369:3,35s:2,35s:3,1kw,2zgo,1erk,2nima,6fzr8,68rnl,ay3hc,693wg,740g:2,70u8:3,5pfk,1bxmw,6io,2i2o4,5srm,w,fml9c,bl7l,dv4,duo,fl,h:2,4qo,6bs,2tc0,70w4,55n0i,93j8h,bg9og,o8ow,6frps,1kw,2dc,24n4,5648w,5m9u0,1zrpc,3r0u8,1ekg,6bk:3,1ekg,1kw:2,1s,2hwjk,74,2t4w,2,1kw,35s,1l0,1qa,1eki,2,1hs0,35u:2,w:4,sh,1ls,1,16o,b8jk,ab6yo,bf9c,ezksg,2zgg,e1vk,5yww,2t4w,58hog:2,2t4w,74,2t50:2,1kw,75u,cn4:2,w,1s,2t4x,w,mh35:2,2:2,5rw1s,2hwcg,4zsp4,55f60,1eku8,mvb4,1feo,8,9zmzk,18y6m,18y7e,24oi,1f29,b9q8,16o,co0,3kw,e8,e8:2,4:6,4,4:3,35s,35s,3k,4:2,4,4,3o,2t4w:2,2xvm,1hvo:6,2t8g:2,4,4,2t8g:4,3k:6,2t4w,5slc,4,6bk,5mh4,e8:2,bocg,9zle8,aatxc,505cg,8lq8:2,8,8fes,55fd4,2ns3s,1em8,1mq:3,a,94,1s,6,2jax2,2t4w,1kw:2,18zr8,25fl,1adk0,nvpe,qw0,n75s,pb5,x,x:3,36o:2,3k:5,8,74:2,6bk,5m9s:7,1,1:8,2,2:5,2,1s,1kw:12,5179c:2,2wg0,4,6bk,4,4:7,6bk,1s,2hwcg,2hwcg,5fa4u,h874:2,sg,4qo,iyo:7,3k,7wg,2t4w:4,2t8g:5,dfk:4,2t8g,70w0,phc,b8xs,3quio,5p4i8,c,7wg:2,am2rk,3pje,18y68,2jbxd,23uo,mh3c,2t4w,18y6c:b,2t4w:7,4,2t50,4:f,2hwcg:2,4:3,1ekg,1kw,1kw,18zr4,4qo,sg,2hwci,n800,6bk,9hc:2,6bk:2,6bk,6bk:3,5m9s,6bk,5slc:2,3yc,2l8xw,b9d1,ba6a,1akua,6rs3,mh3c,3k,2t54,4,2np6o,1ekg,18y6c,u68,2m4u8,1w4jk,35s:2,mh6o:2,2t4w:3,2t4w,2t50:2,35s,35s:a,2t4w:3,2,3m:2,3m,1s,6,2t4w,90:2,2t6o,2t50,78,3eo,2zgo:2,9kw,6m8,6bk,2t4w:2,8:2,1s,2,1s:2,1s:5,1ekg:3,8,7c,1u,1ekg,d1c:2,6bk,6bk,cn4,2:3,5ma2,k42k,bllc:3,26ar,52wf:7,5m9s,k4gs,bllc:3,25lz,ao9v:8,6c8,e5ck,cnk,6iw,9zlds,ssn4,71mp,f4:4,e8:2,1ekg0:4,8:2,8y,1kw:3,1ty,8,3m,chhts,7g,5b1mo,35sg,b8ki,9zlm0,cv8,7k,d1d,4zt34,6f4,52p34,9vk,5yx8,2hwci,35s,1g5c,2hxc2,1ok,3k:4,1:4,1:6,2t4w,18y68:2,6bk:6,74,3l,5,3k:3,74,c:2,1,n7yg,35t,4,18y80,1ekg,36q,mh6p,pds,a2fb8,a2eis,6,3m:3,5m9s:2,5pfk,35s:2,35s,39c,3k,2,2,1t,35s:4,w:2,2de:3,n7a9,4wzo,1vgw0,a,1acqo,74:2,2hwcg,2hwci,8:2,6pu:2,8,2i9e0,2hwcg:2,1apdu,1ekg8:2,7c:4,1ekg:3,1ekg,2t4w,1kw:i,1ekg:4,1ekg,1s,1ekg:2,1ekg:2,4zvuo,1ekg,phc,2tc0,5mh4,5mh4,vls,5pmo,4zsxs,2hwcg,2:7,1s:4,so,so,5mh6,7b4,4zvvs,74,74,1,1ekg:2,517cw,40,ahips,jdc,35s8,e8,9zllc,bl6o,qyw,es,u8,2hzj6,1:6,39c:j,35s:2,4:7,2wao,2t4y:2,35s,35w:5,3k:7,1ekg:2,3k:3,18y68,1kw,74:2,3k:3,8,4,1s:6,mh34,phc:2,pa8,9,18y68,pb4,pds,q4g,1ekg:2,4,3b4,1ekg,3k02,1jb4,mh35,2o,sg:2,2wcg,1kw,39c:2,1u,2:2,1s,1s:2,35s,37k,35s:2,37k,35s,2,2,2t4w:2,2t4w,2t4w,3o,3k:3,4,2hwg0,3k:3,2hwck,2hwe8,2,1s:2,2hwcg,1kw,5c,2jayo,2jays,1hq8,1ekg:2,47ts,2zgg,2we8,3k,6f4,405,opom,4qp:2,35s:2,1ls,q49s,25gg,4zsow,1g5c,590jn,5ter,74w,5pfk,5m9s,40w,4wz,3n:4,q4g,1ww8w,2k4xs,5p2ww,6ed4w,5m9s,35s:5,2t4w:7,2kphc,35s,2t5n,35w,3xg,311c,dfo,2nim8,dchs,3k,4zsow,9zlds,1vf9c:3,4,4,4,4,2hwcg,2hwcg:5,cn4,co0,w:3,b8jk,b9c0,sg:6,sg,4zthc,5beag,14,1ekgw,18ykg,6bk:2,7c:2,eebk,4zsow:3,2hwcg:3,2t4w:2,3quio,1kjcw,2t4w,32m8:2,b8jk,fsw:2,7k:3,pa8,sg0,4zsow:2,35w,2hzls:3,1hdmo,1s,1ekg,18y68,2hwcg,1kw:2,1elc,2o:2,1kw:6,8,1s:2,8,4sg,1s,1l4,1ekg,47pc:2,35s,2t8g:2,3k,8:2,m88,35s,2hwci,6bo,2hxz4,4e0w,cn4,2r,6bk,24n4:2,x,sg0,6bk,4qo,w,74w,3b4,74,18y74,18ykg,pa8,37vuo,t8g,9ig,1kx,4g2,8,2hwci,vls,2hwu9,mh34,pa80,18ykh,uxs,2hwe8,mhog,1ekg,g2,mh3k,mp0g,n38x,191c0,xq1c,5n28:2,5m9s,bxts,b8k0,w:2,6,fgbk:2,1kw,4vk,2hwcg,2hwcg:2,1kw:4,1t,d1s:5,2hwcg,1s:3,1s,5m9s,9he:4,4zsow:7,1:4,4zsow:2,35s:3,6bk,1,5m9s:3,18y68,1em8,5nxg,2t85c:3,5n28,pa80,pa8,hhc1u,2jnk0,4zsow,18ykg,g,tc,pa8,mh35:4,g:2,e8,cn4,b8qo,f56v4:2,6bk:2,5m9s:2,4zsow:7,4,4:4,35s,35s:3,2t4w,2t4w:6,2t4w:2,2wao,35s:2,39c:3,8w,4,bbi,80a,3o:2,3y,a:2,f8,fl,l,e:2,3u:7,a:2,a:3,35s:r,2t4w:d,5mh4:2,74:5,5m9s,8,2,1s:2,1g5c,2wap,w,q2o,1g5c,mh4w,n75v,x,1:3,6fzuy:4,1ekg:2,1ekg,aye5t:3,18y68:3,1hq8,1s0:2,3k,18ydc:2,3k,35s,1ekg,74,nf35,4zz7k,2qi2o,35s,6bk,bev4,55la8,1aeeb,b8jk:2,9zlds:4,b8jk:4,2ksqs:2,2kphc:3,2kphc,2t4w:3,2t4w,2kphc:3,2t4w:d,9zlds,1,36o,2i8zk,2wao0,1,w,5m9s,5mao,9zlds,4zsow,3qulk,1ex2,1ad1c,1enns,pacw,a0e9t,1enls:2,3y8,5m9s,658g:2,3czk,564oy,35s,2nio4,9zldt,7c,1acqo,7wg,24g0,tx74,bew0,58g5e,cn41x,bwf89,74,otg0,7ebk,bgo0,f81j7,2nio4,3s9ak,2i490,oyz4,ib8g,f28sj,2niro,5mbk,3s9ak,36psk,7ebk,bf36,hpwat,5mbk,3s9ak,35b10,1s74,i9nk,f27b7,2nio4,5mbk,3s9ak,miog,3rqj0,dmo,1r7mw:2,f0sub,3k,2t4w,2hwck:3,2kphc,e80:3,fsw,3y8,55lhk,u8,w,2o,1kw:7,1s,w,1kw:3,1s:2,1hq8,57414,f0g,n6dc,38i2s:2,1anuq,2t4w,q0bl,2t5o,lg,2t8g,35s,9zy2s,5b18g,65n4,aatz4,4zsow,8w,2t52:2,20,5m9s,6bk:2,6,35s,35s,35s,5m9s,7hp34,194q3,azua8:s,"
    lastChar = 0
    for char in range(len(vs)):
        now2 = input.running_time()
        if vs[char] != ",":
            continue
        frameString2 = vs.substr(lastChar, char - lastChar)
        lastChar = char + 1
        fSSplit2 = frameString2.split(":")
        count2 = 1
        frame2 = int(fSSplit2.get(0), 36)
        if len(fSSplit2) > 1:
            count2 = int(fSSplit2.get(1), 36)
        for bit in range(25):
            x2 = bit % 5
            y2 = Math.floor(bit / 5)
            if frame2 & 1:
                led.toggle(4 - x2, 4 - y2)
            frame2 = frame2 >> 1
        # si quelq'un lit, ça, vrm merci infiniment a reddit ! j'ai commencer a faire ça frame par frame, et j'ai vrm cru die...
        
        basic.pause(((1000 / 15.97) * count2) - (input.running_time() - now2))
EnposY1 = 0
EnposX1 = 0
EnpoxY = 0
EnposX = 0
posY = 0
posX = 0
lancement1 = 0
lancement = 0
verif = 0
verif = 0
def chutedebrique(): #jeu ou l'on doit esuqiver des obstacle qui tombe du ciel
    EnposY1 = 0
    EnposX1 = 0
    EnpoxY = 0
    EnposX = 0
    posY = 0
    posX = 0
    lancement1 = 0
    lancement = 0
    verif = 0
    verif = 0
    def on_button_pressed_a(): #deplace le joeur vers la gauche
        global posX, posY
        if verif == 0:
            led.unplot(posX, posY)
            posX += -1
            if posX < 0:
                posX += 1
            posY += 0
            led.plot(posX, posY)
    input.on_button_pressed(Button.A, on_button_pressed_a)

    def on_button_pressed_b(): #depalce le joueur vers la droite
        global posX, posY
        if verif == 0:
            led.unplot(posX, posY)
            posX += 1
            if posX > 4:
                posX += -1
            posY += 0
            led.plot(posX, posY)
    input.on_button_pressed(Button.B, on_button_pressed_b)


    if verif == 0:
        lancement = 0
        lancement1 = 0
        lancement += 1
        posX = 2
        posY = 4
        led.plot(posX, posY)

    def on_forever(): #ecran de fin
        global verif
        if posX == EnposX and posY == EnpoxY:
            verif = 1
            basic.clear_screen()
            for index in range(4):
                basic.show_leds("""
                    . . # . .
                    . # # # .
                    # . # . #
                    . . # . .
                    . # . # .
                    """)
                basic.pause(100)
                basic.show_leds("""
                    . . # . .
                    . # # . .
                    # # . # #
                    . # . . .
                    . # # . .
                    """)
                basic.pause(100)
    basic.forever(on_forever)

    def on_forever2(): #lance un ennemi
        global lancement, EnposX, EnpoxY
        if verif == 0:
            if lancement == 1 or lancement == 3:
                if lancement == 1:
                    lancement += 2
                    EnposX = randint(0, 5)
                    EnpoxY = 0
                    for index2 in range(5):
                        led.plot(EnposX, EnpoxY)
                        basic.pause(100)
                        led.unplot(EnposX, EnpoxY)
                        EnpoxY += 1
                        led.plot(EnposX, EnpoxY)
                    lancement = 1
    basic.forever(on_forever2)

    def on_forever3():#lance un autre ennemi
        global lancement1, EnposX1, EnposY1, EnpoxY
        basic.pause(200)
        if verif == 0:
            if lancement1 == 1 or lancement1 == 3:
                if lancement1 == 1:
                    lancement1 += 2
                    EnposX1 = randint(0, 5)
                    EnposY1 = 0
                    for index3 in range(5):
                        led.plot(EnposX1, EnposY1)
                        basic.pause(100)
                        led.unplot(EnposX1, EnposY1)
                        EnpoxY += 1
                        led.plot(EnposX1, EnposY1)
                    lancement1 = 1
    basic.forever(on_forever3)

def chutedevoiture(): #jeu de voiture
    EnposY1 = 0
    EnposX1 = 0
    EnpoxY = 0
    EnposX = 0
    posY = 0
    posX = 0
    lancement1 = 0
    lancement = 0
    verif = 0
    def on_button_pressed_a(): #deplace le joueur vers la gauche
        global posX, posY
        if verif == 0:
            led.unplot(posX, posY)
            posX += -2
            if posX < 0:
                posX += 2
            posY += 0
            led.plot(posX, posY)
    input.on_button_pressed(Button.A, on_button_pressed_a)

    def on_button_pressed_b(): #deplace le joueur vers la droite
        global posX, posY
        if verif == 0:
            led.unplot(posX, posY)
            posX += 2
            if posX > 4:
                posX += -2
            posY += 0
            led.plot(posX, posY)
    input.on_button_pressed(Button.B, on_button_pressed_b)


    basic.show_leds("""
        . # . # .
        . # . # .
        . # . # .
        . # . # .
        . # . # .
        """)
    verif = 0
    if verif == 0:
        lancement = 0
        lancement1 = 0
        lancement += 1
        posX = 2
        posY = 4
        led.plot(posX, posY)

    def on_forever(): #ecran de fin
        global verif
        if posX == EnposX and posY == EnpoxY:
            verif = 1
            basic.clear_screen()
            for index in range(4):
                basic.show_leds("""
                    . . # . .
                    . # # # .
                    # . # . #
                    . . # . .
                    . # . # .
                    """)
                basic.pause(100)
                basic.show_leds("""
                    . . # . .
                    . # # . .
                    # # . # #
                    . # . . .
                    . # # . .
                    """)
                basic.pause(100)
    basic.forever(on_forever)

    def on_forever2(): #lance un ennemi
        global lancement, EnposX, EnpoxY
        if verif == 0:
            if lancement == 1 or lancement == 3:
                if lancement == 1:
                    lancement += 2
                    EnposX = randint(0, 5)
                    if EnposX == 0 or EnposX == 2 or EnposX == 4:
                        EnpoxY = 0
                        for index2 in range(5):
                            led.plot(EnposX, EnpoxY)
                            basic.pause(100)
                            led.unplot(EnposX, EnpoxY)
                            EnpoxY += 1
                            led.plot(EnposX, EnpoxY)
                    lancement = 1
    basic.forever(on_forever2)

    def on_forever3(): #lance un ennemi
        global lancement1, EnposX1, EnposY1, EnpoxY
        basic.pause(200)
        if verif == 0:
            if lancement1 == 1 or lancement1 == 3:
                if lancement1 == 1:
                    lancement1 += 2
                    EnposX1 = randint(0, 5)
                    if EnposX1 == 0 or EnposX1 == 2 or EnposX1 == 4:
                        EnposY1 = 0
                        for index3 in range(5):
                            led.plot(EnposX1, EnposY1)
                            basic.pause(100)
                            led.unplot(EnposX1, EnposY1)
                            EnpoxY += 1
                            led.plot(EnposX1, EnposY1)
                    lancement1 = 1
    basic.forever(on_forever3)
bar_x = 0
point = 0
interval = 0
interval_step = 0
ball_x = 0
ball_y = 0
ball_dx = 0
ball_dy = 0
in_game = False
def pongsolo(): #jeu du pong
    bar_x = 0
    point = 0
    interval = 0
    interval_step = 0
    ball_x = 0
    ball_y = 0
    ball_dx = 0
    ball_dy = 0
    in_game = False


    def on_button_pressed_a(): #deplace la barre vers la gauche
        global bar_x
        if bar_x > 0:
            led.unplot(bar_x + 1, 4)
            bar_x = bar_x - 1
            led.plot(bar_x, 4)
    input.on_button_pressed(Button.A, on_button_pressed_a)



    def on_button_pressed_b(): #deplace la barre vers la droite
        global bar_x
        if bar_x < 3:
            led.unplot(bar_x, 4)
            bar_x = bar_x + 1
            led.plot(bar_x + 1, 4)
    input.on_button_pressed(Button.B, on_button_pressed_b)

    def on_forever(): #definit les mouvement de la balle
        global point, interval, interval_step, ball_x, ball_y, ball_dx, ball_dy, bar_x, in_game
        point = 0
        interval = 500
        interval_step = 10
        ball_x = 3
        ball_y = 4
        ball_dx = -1
        ball_dy = -1
        bar_x = 0
        led.plot(ball_x, ball_y)
        led.plot(bar_x, 4)
        led.plot(bar_x + 1, 4)
        in_game = True
        while in_game:
            if ball_x + ball_dx > 4:
                ball_dx = ball_dx * -1
            elif ball_x + ball_dx < 0:
                ball_dx = ball_dx * -1
            if ball_y + ball_dy < 0:
                ball_dy = ball_dy * -1
            elif ball_y + ball_dy > 3:
                if led.point(ball_x + ball_dx, ball_y + ball_dy):
                    ball_dy = ball_dy * -1
                    point = point + 1
                    if interval - interval_step >= 0:
                        interval = interval - interval_step
                else:
                    in_game = False
            if in_game:
                led.plot(ball_x + ball_dx, ball_y + ball_dy)
                led.unplot(ball_x, ball_y)
                ball_x = ball_x + ball_dx
                ball_y = ball_y + ball_dy
                basic.pause(interval)
            else:
                game.set_score(point)
                game.game_over()
    basic.forever(on_forever)

Enemy2: game.LedSprite = None
Enemy: game.LedSprite = None
shoot: game.LedSprite = None



def spaceinvad(): #space invaders
    player: game.LedSprite = None
    player = game.create_sprite(2, 4)
    shoot: game.LedSprite = None
    def on_button_pressed_a(): #deplace le joueur vers la gauche
        player.move(-1)
    input.on_button_pressed(Button.A, on_button_pressed_a)

    def on_button_pressed_ab(): #permet de tirer
        global shoot
        shoot = game.create_sprite(player.get(LedSpriteProperty.X),
            player.get(LedSpriteProperty.Y))
        for index in range(4):
            shoot.change(LedSpriteProperty.Y, -1)
            basic.pause(10)
            if Enemy.is_touching(shoot):
                Enemy.delete()
                game.add_score(1)
            if Enemy2.is_touching(shoot):
                Enemy2.delete()
                game.add_score(1)
        shoot.delete()
        basic.pause(500)
    input.on_button_pressed(Button.AB, on_button_pressed_ab)

    def on_button_pressed_b(): #deplace le joeur vers la droite
        player.move(1)
    input.on_button_pressed(Button.B, on_button_pressed_b)

    
    
    
    

    def on_forever():#crée 1 des ennemis
        global Enemy
        Enemy = game.create_sprite(randint(0, 4), 1)
        for index2 in range(5):
            Enemy.change(LedSpriteProperty.Y, 1)
            basic.pause(300)
        basic.pause(10)
        Enemy.delete()
    basic.forever(on_forever)

    def on_forever2():#crée 1 des ennemis
        global Enemy2
        Enemy2 = game.create_sprite(randint(0, 4), 0)
        for index3 in range(5):
            Enemy2.change(LedSpriteProperty.Y, 1)
            basic.pause(300)
        basic.pause(10)
        Enemy2.delete()
    basic.forever(on_forever2)

    def on_forever3(): #verifie si le joueur est mort
        if Enemy.is_touching(player):
            player.delete()
            game.game_over()
        if Enemy2.is_touching(player):
            player.delete()
            game.game_over()
    basic.forever(on_forever3)
hole_size2 = 0
ticks = 0
obstacles: List[game.LedSprite] = []
index = 0
ticks2 = 0
emptyObstacleY2 = 0
emptyObstacleY = randint(0, 3)
hole_size = randint(1, 2)
def flappy(): #flappy bird
    global hole_size2
    
    def on_button_pressed_a(): #fait tomber le joueur
        zozio.change(LedSpriteProperty.Y, 1)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    
    
    def on_button_pressed_b(): #fait "sauter" le joueur
        zozio.change(LedSpriteProperty.Y, -1)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    
    hole_size2 = 1
    zozio = game.create_sprite(0, 2)
    
    
    def on_forever(): #fait tomber automatiquement le joueur
        zozio.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
    basic.forever(on_forever)
    
    
    def on_forever2(): #va crée les obstacles
        global emptyObstacleY2, hole_size2, ticks2
        while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
            obstacles.remove_at(0).delete()
        for obstacle2 in obstacles:
            obstacle2.change(LedSpriteProperty.X, -1)
        if ticks2 % 3 == 0:
            emptyObstacleY2 = randint(0, 3)
            hole_size2 = randint(1, 2)
            for index2 in range(5):
                if not (emptyObstacleY2 <= index2 and index2 < emptyObstacleY2 + hole_size2):
                    obstacles.append(game.create_sprite(4, index2))
        for obstacle3 in obstacles:
            if obstacle3.get(LedSpriteProperty.X) == zozio.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == zozio.get(LedSpriteProperty.Y):
                game.game_over()
        ticks2 += 1
        basic.pause(1000)
    basic.forever(on_forever2)
    
_this = 0

obstacle_group_4: game.LedSprite = None

obstacle_group_3: game.LedSprite = None
obstacle_group_2: game.LedSprite = None
_this = 0
obstacle_group_1: game.LedSprite = None

def trex(): #le jeu du T-Rex de google
    def on_button_pressed_a(): #fait sauter le trex d'une case
        player_sprite_1.move(1)
        player_sprite_2.move(1)
        basic.pause(820)
        player_sprite_1.move(-1)
        player_sprite_2.move(-1)
    input.on_button_pressed(Button.A, on_button_pressed_a)

    def on_button_pressed_ab(): #fait sauter le Trex de 2 cases
        player_sprite_1.move(2)
        player_sprite_2.move(2)
        basic.pause(650)
        player_sprite_1.move(-1)
        player_sprite_2.move(-1)
        basic.pause(320)
        player_sprite_1.move(-1)
        player_sprite_2.move(-1)
    input.on_button_pressed(Button.AB, on_button_pressed_ab)

    def on_button_pressed_b(): #fait le trex se baisser
        player_sprite_1.move(-1)
        basic.pause(820)
        player_sprite_1.move(1)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    obstacle_group_4: game.LedSprite = None

    obstacle_group_3: game.LedSprite = None
    obstacle_group_2: game.LedSprite = None
    _this = 0
    obstacle_group_1: game.LedSprite = None

    player_sprite_1 = game.create_sprite(0, 3)
    player_sprite_2 = game.create_sprite(0, 4)
    player_sprite_1.turn(Direction.LEFT, 90)
    player_sprite_2.turn(Direction.LEFT, 90)
    game.set_life(3)

    def on_forever(): #crée le 1er obstacle
        global obstacle_group_1, _this
        obstacle_group_1 = game.create_sprite(4, randint(0, 4))
        for index in range(5):
            basic.pause(500)
            obstacle_group_1.move(-1)
        obstacle_group_1.delete()
        _this += 1
        basic.pause(randint(0, 3) * 500)
    basic.forever(on_forever)

    def on_forever2():#crée le 2eme obstacle
        global obstacle_group_2, _this
        
        obstacle_group_2 = game.create_sprite(4, randint(0, 4))
        for index2 in range(5):
            basic.pause(500)
            obstacle_group_2.move(-1)
        obstacle_group_2.delete()
        _this += 1
        basic.pause(randint(0, 3) * 500)
    basic.forever(on_forever2)

    def on_forever3(): #verifie si le joueur ne prend pas de degat
        
        if player_sprite_1.is_touching(obstacle_group_2) or player_sprite_2.is_touching(obstacle_group_2) or (player_sprite_1.is_touching(obstacle_group_1) or player_sprite_2.is_touching(obstacle_group_1)):
            game.remove_life(1)
            basic.pause(500)
    basic.forever(on_forever3)

    def on_forever4():#crée le 3eme obstacle
        global obstacle_group_3
        if 10 < _this:
            obstacle_group_3 = game.create_sprite(4, randint(0, 4))
            for index3 in range(5):
                basic.pause(500)
                obstacle_group_3.move(-1)
            obstacle_group_3.delete()
            basic.pause(randint(0, 3) * 500)
    basic.forever(on_forever4)

    def on_forever5(): #crée le 4eme et dernier obstacle
        global obstacle_group_4
        if 20 < _this:
            obstacle_group_4 = game.create_sprite(4, randint(0, 4))
            for index4 in range(5):
                basic.pause(500)
                obstacle_group_4.move(-1)
            obstacle_group_4.delete()
            basic.pause(randint(0, 3) * 500)
    basic.forever(on_forever5)
hole_size2 = 0
ticks = 0
index = 0
ticks2 = 0
emptyObstacleY2 = 0
emptyObstacleY = randint(0, 3)
hole_size = randint(1, 2)
def superman64(): #superman64
    global hole_size2
    
    def on_button_pressed_a(): #fait descendre le joueur
        super.change(LedSpriteProperty.Y, 1)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    
    
    def on_button_pressed_b(): #fait monter le joueur
        super.change(LedSpriteProperty.Y, -1)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    
    hole_size2 = 1
    super = game.create_sprite(0, 2)
    
    

    
    
    def on_forever2(): #va crée les obstacles
        global emptyObstacleY2, hole_size2, ticks2
        while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
            obstacles.remove_at(0).delete()
        for obstacle2 in obstacles:
            obstacle2.change(LedSpriteProperty.X, -1)
        if ticks2 % 3 == 0:
            emptyObstacleY2 = randint(0, 3)
            hole_size2 = 1
            for index2 in range(5):
                if not (emptyObstacleY2 <= index2 and index2 < emptyObstacleY2 + hole_size2):
                    obstacles.append(game.create_sprite(4, index2))
        for obstacle3 in obstacles:
            if obstacle3.get(LedSpriteProperty.X) == super.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == super.get(LedSpriteProperty.Y):
                game.game_over()
        ticks2 += 1
        basic.pause(400)
    basic.forever(on_forever2)

hole_size2 = 0
ticks = 0

index = 0
ticks2 = 0
emptyObstacleY2 = 0
emptyObstacleY = randint(0, 3)
hole_size = randint(1, 2)
def superman62(): #superman64 mais les murs ne sont pas en kriptonite
    global hole_size2
    
    def on_button_pressed_a(): #fait descendre le joueur
        super.change(LedSpriteProperty.Y, 1)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    
    
    def on_button_pressed_b(): #fait monter le joueur
        super.change(LedSpriteProperty.Y, -1)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    
    hole_size2 = 1
    super = game.create_sprite(0, 2)
    
    

    
    
    def on_forever2(): #va crée les obstacles
        global emptyObstacleY2, hole_size2, ticks2
        while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
            obstacles.remove_at(0).delete()
        for obstacle2 in obstacles:
            obstacle2.change(LedSpriteProperty.X, -1)
        if ticks2 % 3 == 0:
            emptyObstacleY2 = randint(0, 3)
            hole_size2 = 1
            for index2 in range(5):
                if not (emptyObstacleY2 <= index2 and index2 < emptyObstacleY2 + hole_size2):
                    obstacles.append(game.create_sprite(4, index2))

        ticks2 += 1
        basic.pause(400)
    basic.forever(on_forever2)
