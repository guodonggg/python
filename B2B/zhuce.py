from pickle import FALSE, TRUE
import time,os,datetime
from openpyxl import load_workbook
from os import listdir
from os.path import join
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# 第一项是ID，第二项是classname
infos = [
    ['帐号',('txt_name','u-username','','','','','','mp','username','loginrepwd','login','sUID','UID','tname','tbx_son','txtUName','tb_UserName','login','TxtUserName','txt_1_User_Name','txtLoginId','membername','rLogName','TUname','ctl00_ContentPlaceHolder1_txtname','loginid2','J_UserName','txtname','BaseTextBox1','account','loginid','usernameiii045w','musername','LoginID','txtAccout','loginId','txtloginNames','tbUserName','users-username','txtUid','registerUser','mask_body_item_username','user','txtRegUserName','domain','mydomain','login_username','fhyddddmll5','y','uname','corpdomain','domainNameUrl0','txtUserName','txt_domain','memberId','tbUserName','Domains','company_login_id','cuser','User','txtUserName','user_name','userName','logUserName','userNamein','username','Account','nick','loginName','UserName','accountLogin_UserName')],
    ['密码',('newpsw1','','','','','','pass2','qpassword','PasswordRepeat','rpwd','sPWD','CheckPWD','PWD','pwdconfirm','reg_password','Txt_Cnl_User_PwdD','Txt_Cnl_User_Pwd','txtReUPwd','txtUPwd','passwordagain','tb_UserConfirmPassword','tb_UserPassword','RePassword','u_pass2','u_pass','cpasswd','npasswd','passwd_ack','passw','txtConfirmPwd','_txt_Password','again_password','txtTwoPwd','qiyepwd2','qiyepwd1','Password1','rPwd','rPwd2','rPwd1','ConfirmUserPsw','UserPsw','TUpwd2','TUpwd','confirmPassword','pass1','surePwd','affirmPassword1','password1','passwordConfirm','contentZone_corpName','cpwd','J_Password','J_RePassword','txtpwd','txtpwdtwo','regpwdconfirm','regpwd','PassWord1','confirm_password','conpassword','mpwd','mpwd1','txtPass','','userPW','conpassword','textfield3','password_register','post[cpassword]','psd1','psd2','passwd1','','js_register_password','js_register_password_confirm','userpwd','userpwd_repeat','new_password','qr_password','password3','UserPass','ConfPass','txtpwdfirst','txtpwdsecond','passwd2','passwd12','tbPassword1','tbPassword2','userpassword','sUserPassword','users-loginpwd','users-repassword','txtPwd','shopPwd','registerPassword','registerDbPass','mask_body_item_password','mask_body_item_newpassword','re_password','password','passwd','txtRegUserPwd','txtRegUserPwdConfirm','pass','PassWord','company_password','company_repassword','','pwd','ConfirmPassWord','confirmPass','repasswd','u-password','m1','m2','m','password1','password222','login_password','confirmPwd','userpass','UserPassword','ConfirmUserPassword','userpass2','pwd1','pwd2','userpsw','confirm_userpsw','tbPassword1','tbPassword2','user_password0','Password','txtPassword','txtPassword','ReUserPassword','txtRePassword','BaseTextBox2','BaseTextBox3','rpassword','verifypass','lg-password','RePwd','Pwd','txtPwd1','txtPwd2','repassword','cpassword','QrPassword','rePassword','ConfirmPassword','accountLogin_Password','ctl00_ContentPlaceHolder1_txtrepassword','ctl00_ContentPlaceHolder1_txtpassword','newpsw2','txt_password','txt_repwd','user_password','userPassword','mpassword','logPassword','comfirmLogPassword','phpassword','password_confirmation','passwordin','secpasswordin','password2','Password2','pwdRepeat','confirm','txtPassword1')],
    ['公司名称',('inputgs3','','','','','','','question','cue_problex','Txt_com_name','txtCName','companyNname','rz_Name','bname','linkModeInfo_ModeTitle','TxtCompanyName','txt_MemberCompCName','qiyename','CompanyName','lblsName','TTitle','rComName','TComName','gsmc','cShopTitle','ctl00_ContentPlaceHolder1_txtcompany','corpName','txtcompany','BaseTextBox15','erqeredsaasagsss','amt','com_name','CompName','data[gongsimingcheng]','companynameakm','Comane','compfname','txtCompany','txtNewCorpName','txtCorpName','userCorpName','UserCode1','compName','shopName','compname','js_register_company','txtCompanyName','CusTitle','Qymc','quesion','regBCompany','tbCorpName','usershopname','users-company','company','ComName','brandName','ctl00_Middle_OptimizerTitle','ctl00_Middle_Corpname','company_enterprise_name','Answers','cptitle','OfficeName','SeoCompanyName','COM','txtRegCompany','comname','qymc','EnterpriseShortName','EnterpriseName','companyname','corpname','txtCompanyName','tbCorpName','Corpname','txtComName','cxljdzj_name','rz_coname1','textwebname','txtcompanyname','company_name','txt_cname','comName','company','comNamein','Company','companyName','CompanyName','coname','com_pany','input_text w260')],
    ['公司简称',('shortname','','','','chesursse_key','Txt_Cnl_Answer','t13name_70','short_name','corpShortName','projectName','companyShortName','shop_url','compabb','Answer','firstname','answer','regACompany','company_nickname','Imcomabb','','Title','pwdAnswer','Abbreviation','FirmName','txtCompanyShortName_new','shortcompany','ShortName')],
    ['手机',('inputdh3','','','','','apply_mobile','reg_username','phonetxt','txtUTel','Moble','rz_Tel','b_mobile','b_tel','linkModeInfo_Telephone','txt_MemberMobile','mphone','contactphone','rHandset','TMobile','headerPhone','userEmail1','cAppMobile','contentZone_txtMobile','ctl00_ContentPlaceHolder1_txtmobile','BaseTextBox14','user_mobile','ContentPlaceHolder1_txtPhone','mobile[]','StandbyPhone','sj3','PwdConfirm','TelePhone','userMobil','loginphone','safeMobile','lastname3','lastname','js_register_account_phone','tel3','loginMobile','regMobile','regphone','qyphone','realltel','tbMobile','realltol','users-mobile','txtPhone','partnerPhone','mask_body_item_phonenum','re_username','company_phone','company_mobile','company_tel','MobilePhone','OfficeTel','IMMobile','mobileNo','loginphone','pmphone','dh','telphone','EnterpriseMobileNo','MobileNo','tbMobile','Phone','mobilecheck','BaseTextBox4','Cellularphone','telNum','txt_compMobile','txtmobile','RegisterPhone','phoneNum','txtMobile','txtWeiXin','phnumber','lg-cellphone','txt_mobile','mob','mobile','userMobile','phonenum','Mobile','shouji','mobilein','telephone','phone','wechatCode')],
    ['微信号',('msn','','','','','','','txtsWxh','weixinId','weixi','data[weixinhao]','txtPostId','lastname2','wxtxt','wx','ctl00_Middle_WX','company_msn','wechat','weixin')],
    ['邮箱',('inputdle3','','','','apply_email','EmailAddress','Txt_Cnl_User_Name','txtUEmail','us_Email','tb_email','t13060_V90','b_email','linkModeInfo_EMail','showInfo_Email','_txt__Email','txtsEmail','TUEmail','cAppMail','femail','emailValue2','J_Email','email','BaseTextBox7','ContentPlaceHolder1_txtEmail','data[email]','StandbyEmail3','StandbyEmail2','StandbyEmail1','memail','EMail','userSafetyMail','userMail','com_email','js_register_email','regEmail','user_email','tbEmail','useremail','users-email','mail','me','ctl00_Middle_Email','company_email','OfficeEmail','txtRegUserEmail','dfyhg6','email_txt','EnterpriseMail','lkemail','tbEmail','UserEmail','company_email','txtCompanyEmail','txtEMail1','Email','txt_mail','mail','userEmail','txt_email','ctl00_ContentPlaceHolder1_txtemail','RegisterEmail','txtEmail','contact_email')],
    ['QQ',('txt_qq','','','','','','','','txtUQQ','tb_qq','Qqonline','rz_QQ','b_qq','linkModeInfo_QQ','QQhaoma','mqq','Qq','rQQNum','TUQQ','Text1','cAppQq','linkManQQ1','contentZone_txtQQ','ctl00_ContentPlaceHolder1_txtqq','qqnum','user_qq','userQQ','qq0','com_qq','lastname1','ctl00_Middle_QQ','company_qq','tm','text_qq','qq','QQ','txtQQ','LinkQQNum','tbQQ','Oicq')],
    ['阿里旺旺',('wangwang','ali','AliTalk','','','','')],
    ['固定电话',('fax','','','','','','apply_tel','corpFax','corpTel','mtel','TFax','TPhone','cAppTel','user_telephone','data[lianxidianhua]','txtTelephone','userTel','post[telephone]','com_phone')],
    ['区号',('phonearea','','','','','','','','tel2','t_1','tel_2','tb_tel2','txt_MemberTel_City','txtsFaxQu','txtsPhoneQu','telqu','contentZone_txtPhoneArea','BaseTextBox9','area','TelPrefix','telnumber22','areacode','TelCode','PhoneArea','quhao','Phonearea','ctl00_Middle_AreaCode','textphone2','phone2','Phone_area','txtAreaCode','txt_compTelDdd','cotelq')],
    ['电话',('phonenum','','','','','','','','','','t_2','tel_3','us_Phone','tb_tel3','showInfo_MobilePhone','showInfo_Telephone','txt_MemberTel','txtsFax','txtsPhone','teltext','contentZone_txtPhone','BaseTextBox10','telnumber32','telnumber','mmobil','Tel','PhoneNumber','Phonenumber','ctl00_Middle_Telephone','tel','textphone3','phone3','Phone_number','txtTelPhone','txt_compTelphone','cotel')],
    ['网址',('txt_website','','','companypage','webSite','txtUWeb','tb_courl','Compweb','rz_Web','companyWebsite','site','contact_www','linkModeInfo_CompanyUrl','txtHomepage','comweb','webHref','txtsSite','TUrl','txtCompanyURL','CorpUrl','contentZone_txtURL','qy_www','website','txtUrl','url','txtwebsite','txtCompanyNet','Href','homepage','ctl00_Middle_Url','company_homepage','WebUrl','Imurl','wangzi','web','EnterpriseNetUrl','tbCorpUrl','Web','txtWebSite','MobileWebSite','Site','website','cxljdzj_collection','coweb','comHomepage','web_site','weburl','txtWebsite','ctl00_ManageContent_txtUrl','companyWeb','comHomepage')],
    ['联系人',('inputlxr3','','','','','contacter','loginpwd','truenametxt','txtTName','tb_realname','ConnPerson','companyLinkMan','linkname','b_link_man','TxtPersonName','_txt__Linkman','PersonName','txtName','contactname','Corporate','TAppRen','rRealName','TLxRen','memberName','txtRealName','xingming','headerName','contacts','rel_name','cRegName','cAppName','contactname','contentZone_txtFirstName','ctl00_ContentPlaceHolder1_txtname','fullname','BaseTextBox5','user_rname','linkMan','Applicant','Linkman','first_name','lxr','contact3jjz','mName','mtruename','txtContact','txtNickName','real_name','userCorpLinker','trueName','applayUser','your_name','com_linkman','js_register_name','usefactory-name','link_man','regname','cname','txttruename','txtLinkMan','regContacts','tbContactUser','reallname','users-realname','realName','txtDelegateMan','FirstName','linkMan','nickname','compellation','company_compellation','','company_linkman','attn','OfficeLinkman','txtRegRealName','Somane2','name-txt','EnterpriseLinkMan','linkuser','tbContactUser','name','txtPersonName','linkman','RealName','txtTrueName','Name','txt_uname','realname','lianxiren','truename','Connecter','contactName','contact','PersonToContact','con_name','Contact')],
    ['联系人身份证号',('cred_card','','','','number','txtsfz','IDCardNo','txtIDCard','sfzNumber','idcardnum','rcard','card','identityCode','idcard','company_identity_card','identity_card','decodeIdNo')],
    ['部门',('con_depart','','','departname','apply_part','contentZone_txtDepartName','','department','txtDepartment','txtMyDept','tbBumen0','tbBumen3','tbBumen1','bm','tbBumen4','title','userDept')],
    ['职位',('con_duty','','','','','','','apply_position','duty','txtUHeadShip','HeaderShip','headship','txtZhiwei','b_position','txtMemberCJobTitle','Department','txtsDuty','TZhiWei','txtPosition','linkManWork','contentZone_txtJobTitle','ctl00_ContentPlaceHolder1_txtjob','BaseTextBox6','mpost','txtMyPosition','job','post[career]','tbZhiwei3','txtJobName','tbZhiwei0','Position','txtRegPosition','zhiw','duty','zw','txtPartment','colxrzw','position','txtJobTitle','userDuty','Job','career','jobtitle')],
    ['法人',('legalman','','','','','','','','','legal_name','businessLicenseLegalPerson','corowner','tb_leader','zz_delegate','comp_owner','txtlegalper','b_legalperson','txtCorporation','legalperson','txtsCorporation','TFaRen','legalPerson','txtCompanyCorporate','legalRepres','LegalPerson','person','cLegal','principal','contentZone_lawPerson','legal','CompBoss','apply_name','company_legal_person','txtLawMan','corpn','legalRepresentative','lessName','LegalRepresentative','Frdb','company_legal_person_compellation','frdb','RegisteredMan','faren','artifical','tbLegalPerson','Commissary','textname','txtAttLegalPerson','cofr','txtcontact','RegName','Man','legalRepresentative','ctl00_ManageContent_LegalPerson','ctl00_ManageContent_txtPrincipal','owner','artificialPerson','txtCorporateName','Legal','faren_name','legalRepresentative')],
    ['法人身份证号',('faren_license','','','','','','','','','tb_idcard','card_id','identity','ctl00_Middle_txtCertificateNo_2','company_legal_person_identity_card','textsfz','id_card','IDCardNumber','sfzNub','ctl00_ManageContent_IdNumber')],
    ['品牌名称',('Brand','abbrName','','','corbrand','txtCBrand','brand_name','txtNameplate','pingpai','brandname','contentZone_txtTrademark','Brands','pinpai1','p_z_Z_BrandName','ppmc','txtWorkBreed','txtBrand','pZzBrandName','pp','EnterpriseMasterBreed','tbBrand','comTradeMarks','pinpai','ctl00_ManageContent_BradWord','comTradeMarks','brand','txt_bname','txtRegisterLogo1','txtMainBrand1','')],
    ['注册号',('txt_icnum','','','','','','','bl_id','businessLicenseNo','tb_regnum','zz_number','b_licence_code','reg_id','shuiwuhao','SCreditCode','txtZhizhaoNum','TRegNum','yyzzNumber','CreditCode','Industrial_num','cRegNo','registerCode','companycode','company_card_id','taxnumber2','taxnumber','icnumber2','regNum','licenseCode','yyzz_no','registerNum','code','creditCode','bh','ctl00_Middle_txtCertificateNo_1','company_business_license','RegisteredNO','text_xydm','RegistrationNumber','BusinessLicenseNumber','txtAttRegNum','zhhm','textyyCode','txtJiGouCode','ctl00_ManageContent_RegNum','RegNo','license_number','gongshanghao','corpnum','regcode','registerNumber','txtLicence','licenseNo')],
    ['注册金额',('txt_capital','','registered_capital','Txt_com_money','capitalsum','tb_currency','build_capital','zz_money','txtRegister','b_reg_capital','txtregCapital','txtsRegiSum','TRegPrice','registeredCapital','txtCompanyCapital','cRegMoney','contentZone_txtFund','txtRegMoney','txtFoundMoney','regCapital','ComType','ziben','RegisteredCapital','txtRegisterMoney','RegMoney','zijin','EnterpriseRegMoney','Capital','txtAttRegisteredCapital','fund','zhucezijin','fund','reg_capital','capital','ctl00_ManageContent_RegCapital','txtRegFund','')],
    ['成立时间',('txt_date','','','','','cp_start','establishment_date','txt_Filregisterdate','tb_BuildDate','build_year','zz_date','comp_year','b_create_time','txtExistence','txtsFoundTime','TNjTime','TRegTime','registeredTime','txtCompanyEstablished','AnnualSurvey','J-xl','cCheck','cRegDate','first_year','contentZone_txtFoundTime','Establish','clnf','txtFoundDate','postfromtime','licenseBDate','builddate','yyqx_date_1','p_z_Z_EstablishedYear','txtRegisterTime','pZzEstablishedYear','AnnualSurveyTime','AnnualYear','RegistrationDate','comadddate','foundedTime','buildtime','tbYear','Begindate','ComBulidTime','codate','ctl00_ManageContent_RegDate','setuptime','txt_create','txtCreateTime','regyear','ctl00_ManageContent_InspectionTime')],
    ['营业期限',('manageTime','','','','TBusTime','cValidPeriod','ctl00_ManageContent_BizTerm')],
    ['登记机关',('organ','registerOrgan','','','','','registration_authority','zz_organ','TDjCom','RegistrationAuthority','cRegAuthority','authority','jiguan','registrationAuthority','AwardOrg','txtAttRegPart','ctl00_ManageContent_RegOrg')],
    ['公司地址',('inputxxdz3','','','','addresstxt','txtUAddr','us_Address','tb_regadress','tb_address','rz_add','companyJydz','zz_addr','bus_addr','txtStreet','b_street','linkModeInfo_Address','showInfo_Address','txtregAddress','txtMemberCAddress','businessAddress','detailaddress','CompaniesRegistry','txtsStreet','TRegAddress','TAddress','registeredAddress','txtCompanyStreet','txtCompanyDealinAddr','txtCompanyRegAddr','RegisterAddress','minute','cRegAddr','CorpAddress','citys','contentZone_txtAddress1','ctl00_ContentPlaceHolder1_txtWorkAddrOther','ctl00_ContentPlaceHolder1_txtBideAddrOther','schcate_k','adress98','BaseTextBox16','add2','street_ddr','registerAddr','add','txtDiZhi','regaddress3','mailaddress','txtMainArea','userCorpAddr','addr','business_address','factoryAddress','regaddress','dizhi','lastname4','registerAddress','p_z_Z_BizPlace','p_z_Z_FoundedPlace','txtaddr','regAddress','realladdress','txtDetailAddress','ctl00_Middle_Address','company_address','pZzFoundedPlace','OfficeAddress','RegPlace','txtRegAddress','complace','address','EnterpriseAddress','tbContactAddr','tbBizAddr','tbRegAddr','coaddress','comAddress','txtaddress','ctl00_ManageContent_RegAddress','ctl00_ManageContent_txtAddress','daddress','Addr','txt_addr','address','Address','registerPlace','manageArea','txtAddress')],
    ['邮政编码',('txtPostCode','','','txtUPost','tb_postcode','txtPostalcode','txtsDak','TZip','txtCompanyPostalcode','ZipCode','user_mailcode','Zip','userCorpZip','Post','txtPostNumber','ctl00_Middle_Postcode','company_zip','OfficePostCode','post','postcode','postCode','Postcode','zip','comZip','postalcode','zipcode','coyb','comZip','ctl00_ManageContent_txtZipCode')],
    ['省',('majorMarket','CorpMark','contentZone_txtMainMarket','PrimaryMarket','txtMarket','Mart','comy')],
    ['市',('jingyingdd','','','','','','comp_raddr','txtManageaddr','companyAddress','bizplace','contentZone_txtRunSite','contentZone_txtRegisterAddress','txtMainMarket','txtPrimaryMarket','MajorMarkets','txt_src','company_city','pZzBizPlace','TheWork','SalesAddr','ctl00_ManageContent_txtRegAddr')],
    ['区',('','','','','')],
    ['行业分类',('mainV','adjust_text','','','','','')],
    ['主营产品',('inputzyxm3','','','','','','','scope','pre_function','tb_bizscope','Product','mainBiz','rz_prod','zz_bound','txtMainProduct','b_product','showInfo_MainProducts','Product_For_Sell','TBusFanWei','TComProduct','businessMarket','memberDescription','txtCompanyProduct','BusinessScope','mainBusiness','cBusiness','contentZone_txtIntroProduce','contentZone_txtSaleKeywords','contentZone_enCorpName','BaseTextBox17','businessScope','js_register_business','PrimaryProducts','txtCompanyServices','doarea','MainProduct','classname','txtServiceArea','txtKeyword','userMainProduct','mainProductText','ComProcurement','mainProduct','products','com_mainpro','txtBusiness','userproduct','ctl00_Middle_OptimizerDescription','ctl00_Middle_OptimizerKeywords','Business','cpserve','zypro','MainBusiness','product','tbMainBuyProduct','tbMainSellProduct','mainproduct','shop_name','txtAttBusiness','ProKeys','txtComProduct','cocg','coyw','txtMainBusiness','business','ctl00_ManageContent_BizScope','SalesMarket','jingyingfanwei','sell','zhuyingchanpin','mproduct','MainProducts','sale','txtMainProduct1','txtCompanyKeyword')],
    ['关键字1',('txt_product1','','','','tbx_zhuying1','mainbuy','mainpro','productionService_0','no_validate','ctl00_Middle_KeyWord1','txtsServing1','TComPKey1','cg','cp','Text2','business-t','gjc4','gjc1','zhuying1','Zycp_1','productname','productname1','Keywords','sproduct1','majorProduct_0','zycp1')],
    ['关键字2',('txt_product2','','','','','','tbx_zhuying2','MainProd0','productionService_1','ctl00_Middle_KeyWord2','txtsServing2','TComPKey2','wordInput','cp1','gjc5','gjc2','Zycp_2','productname2','sproduct2','majorProduct_1','zycp2')],
    ['关键字3',('txt_product3','','','','','','','tbx_zhuying3','productionService_2','ctl00_Middle_KeyWord3','txtsServing3','TComPKey3','cp2','gjc3','Zycp_3','productname3','sproduct3','majorProduct_2','zycp3')],
    ['企业类型',('','','','','TComType','companyIndustries','ctl00_ManageContent_EnterType')],
    ['月产量',('monthOutput','','','','monthpros','monthlyOutput','productioncapacity','contentZone_txtMoonOutput','MonthlyOutput','txtMonthlyOutput','p_z_Z_ProductionCapacity','ProMonth')],
    ['雇佣人数',('txtEmployeeNum','','','','','','txtResearchNumber','ComPersons','size','Tap','ctl00_ManageContent_DeviceNum')],
    ['年营业额',('txtTurnover','','','','','','b_turnover','turnover','Turnover','Export','tbMonthlyCapacity','sales','ComYearSales','yye')],
    ['厂房面积',('warehouseArea','','','shopsize','factorySize','contentZone_txtArea','CompArea','txtFactoryArea','p_z_Z_FactorySize','PlantArea','tbFactroySize','Area','warehouseArea','workshopArea','changfang','ctl00_ManageContent_txtFactorySize')],
    ['公司简介',('qianming','','express','comintroduction','searchintroduce','txtCIntro','companyAbout','comp_desc','b_intro','txtIntro','comjj','txtsIntroduction','TDes','about','profile','body','certinfo','info','brief','Memo','Intro','companyabout','discription','operation','txtDetail','digest','introduce','textarea','introduction','proserver','lastname7','company_detail','AboutUS','ManageRange','content','jianjie','intro','introduce_short','tbNote','instroduce','Description','introduce','coms','txtintroduce','manageBound','txt_abstract','txtCompanyDesc','descript','ctl00_ManageContent_txtMemo','shorCoutTextarea','jieshao','About','description','corp_introduct','corpintro')],
    ['客户群体',('primaryCustomers','','','','','','keycustoms','comp_cust','txtClient','majorCustomer','keyclients','contentZone_txtMainClient','PrimaryClient','','txtMainGuest','','p_z_Z_KeyClients','MajorCustomers','pZzKeyClients','ctl00_ManageContent_txtKeyClients','kehuqun','tbCliensKey','Client','cokh','Customer')],
]
class jisu():
    def __init__(self,browser):
        self.browser = browser
        self.user = 'jiemeidq'
        self.userinfo = 'd:\\python\\b2b\\info\\%s\\user2.txt' % (self.user)
        self.content = 'd:\\python\\b2b\\info\\%s\\content.txt' % (self.user)
    def getUser(self):
        userInfo = {}
        with open(self.userinfo,'r',encoding='utf-8') as t:
            lines = t.read().splitlines()
        for i in lines :
            s = i.split(':',1)
            userInfo[s[0]] = s[1]
        try:
            with open(self.content,'r',encoding='utf-8') as t:
                lines = t.read()
            userInfo['公司简介'] = lines
        except:
            pass
        return userInfo

    def get_input(self):
        inp = self.browser.find_elements(By.XPATH,'//input')
        textarea = self.browser.find_elements(By.XPATH,'//textarea')
        inpub = []
        for i in inp:
            types = i.get_attribute('type')
            if i.get_attribute('id') and (types != 'hidden'):
            #if i.get_attribute('id') and (types == 'text' or types == 'password'):
                inpub.append(i.get_attribute('id'))
                continue
            if i.get_attribute('name') and (types != 'hidden'):
            #if i.get_attribute('name') and (types == 'text' or types == 'password'):
                inpub.append(i.get_attribute('name'))
                continue
            if i.get_attribute('class') and (types != 'hidden'):
            #if i.get_attribute('class') and (types == 'text' or types == 'password'):
                inpub.append(i.get_attribute('class'))
        for t in textarea:
            if t.get_attribute('id'):
                inpub.append(t.get_attribute('id'))
                continue
            if t.get_attribute('name'):
                inpub.append(t.get_attribute('name'))
                continue
            if t.get_attribute('class'):
                inpub.append(t.get_attribute('class'))
        return set(sorted(inpub))

    def set_input(self,ele,content):
        print('%s-%s'%(ele,content))
        try:
            self.browser.find_element(By.ID,ele).clear()
            self.browser.find_element(By.ID,ele).send_keys(content)
            time.sleep(0.1)
            return True
        except:
            pass
        try:
            self.browser.find_element(By.NAME,ele).clear()
            self.browser.find_element(By.NAME,ele).send_keys(content)
            time.sleep(0.1)
            return True
        except:
            pass
        try:
            self.browser.find_element(By.CLASS_NAME,ele).clear()
            self.browser.find_element(By.CLASS_NAME,ele).send_keys(content)
            time.sleep(0.1)
            return True
        except:
            return False



if __name__ == '__main__':
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome(options=options)
    try:
        browser.switch_to.window(browser.window_handles[0])
        print(browser.current_url)
    except:
        pass
    fabu = jisu(browser)
    userInfo = fabu.getUser()
    einput = fabu.get_input()
    print(datetime.datetime.now())
    time.sleep(1)
    for einp in einput:
        for info in infos:
            if einp in info[1]:
                fabu.set_input(einp,userInfo[info[0]])
                break
    print(datetime.datetime.now())





