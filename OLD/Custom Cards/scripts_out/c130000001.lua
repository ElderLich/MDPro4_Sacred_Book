--Obelisk the Tormentor - Crusher

local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	--summon with 3 tribute
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,7))
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_LIMIT_SUMMON_PROC)
	e1:SetCondition(s.ttcon)
	e1:SetOperation(s.ttop)
	e1:SetValue(SUMMON_TYPE_ADVANCE)
	c:RegisterEffect(e1)
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_LIMIT_SET_PROC)
	e2:SetCondition(s.setcon)
	c:RegisterEffect(e2)
	--summon
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_SINGLE)
	e3:SetCode(EFFECT_CANNOT_DISABLE_SUMMON)
	e3:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	c:RegisterEffect(e3)
	--summon success
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
	e4:SetCode(EVENT_SUMMON_SUCCESS)
	e4:SetOperation(s.sumsuc)
	c:RegisterEffect(e4)
	-- Normal Summon with 3 Tributes or without Tributing if the opponent controls 3 or more monsters
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,1))
	e5:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e5:SetType(EFFECT_TYPE_SINGLE)
	e5:SetCode(EFFECT_LIMIT_SUMMON_PROC)
	e5:SetRange(LOCATION_HAND)
	e5:SetCondition(s.ntcon)
	e5:SetOperation(s.ntop)
	e5:SetValue(SUMMON_TYPE_ADVANCE)
	c:RegisterEffect(e5)
	-- Special Summon God Tokens
	local e6=Effect.CreateEffect(c)
	e6:SetDescription(aux.Stringid(id,0))
	e6:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_TOKEN)
	e6:SetType(EFFECT_TYPE_IGNITION)
	e6:SetRange(LOCATION_MZONE)
	e6:SetCountLimit(1,id)
	e6:SetTarget(s.tktg)
	e6:SetOperation(s.tkop)
	c:RegisterEffect(e6)
	-- Special Summon Obelisk the Tormentor
	local e7=Effect.CreateEffect(c)
	e7:SetDescription(aux.Stringid(id,2))
	e7:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_SEARCH+CATEGORY_TOHAND)
	e7:SetType(EFFECT_TYPE_IGNITION)
	e7:SetRange(LOCATION_MZONE)
	e7:SetCost(s.spcost)
	e7:SetTarget(s.sptg)
	e7:SetOperation(s.spop)
	c:RegisterEffect(e7)
end

function s.ttcon(e,c,minc)
	if c==nil then return true end
	return minc<=3 and Duel.CheckTribute(c,3)
end

function s.ttop(e,tp,eg,ep,ev,re,r,rp,c)
	local g=Duel.SelectTribute(tp,c,3,3)
	c:SetMaterial(g)
	Duel.Release(g,REASON_SUMMON+REASON_MATERIAL)
end

function s.setcon(e,c,minc)
	if not c then return true end
	return false
end

function s.sumsuc(e,tp,eg,ep,ev,re,r,rp)
	Duel.SetChainLimitTillChainEnd(aux.FALSE)
end

-- Normal Summon condition without Tributing

function s.ntcon(e,c,minc)
	if c==nil then return true end
	local _,max=c:GetTributeRequirement()
	return max>0 and Duel.GetLocationCount(c:GetControler(),LOCATION_MZONE)>0 and Duel.GetFieldGroupCount(c:GetControler(),0,LOCATION_MZONE)>2 
end

function s.ntop(e,tp,eg,ep,ev,re,r,rp,c,minc)
	if minc==0 then return end
	local mg=Duel.SelectTribute(tp,c,3,3)
	c:SetMaterial(mg)
	Duel.Release(mg,REASON_SUMMON+REASON_MATERIAL)
end

-- Special Summon God Tokens

function s.tktg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_TOKEN,nil,2,tp,0)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,2,tp,0)
end

function s.tkop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
	if ft>1 and Duel.IsPlayerAffectedByEffect(tp,59822133) then ft=1 end
	if ft<2 then return end 
	if Duel.IsPlayerCanSpecialSummonMonster(tp,130000002,0,TYPES_TOKEN,0,0,1,RACE_FAIRY,ATTRIBUTE_DARK) then
	for i=1,2 do
	local token=Duel.CreateToken(tp,130000002) --This is the Code for the God Tokens
		Duel.SpecialSummonStep(token,0,tp,tp,false,false,POS_FACEUP)
		--Cannot be used as fusion material 
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
		e1:SetCode(EFFECT_CANNOT_BE_FUSION_MATERIAL)
		e1:SetValue(1)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
		token:RegisterEffect(e1,true)
		--Cannot be used as synchro material 
		local e2=e1:Clone()
		e2:SetCode(EFFECT_CANNOT_BE_SYNCHRO_MATERIAL)
		token:RegisterEffect(e2,true)
		--Cannot be used as link material 
		local e3=e1:Clone()
		e3:SetCode(EFFECT_CANNOT_BE_LINK_MATERIAL)
		token:RegisterEffect(e3,true)
		end
	Duel.SpecialSummonComplete()
	end
end

-- Special Summon Obelisk the Tormentor

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsReleasable() end
	Duel.Release(e:GetHandler(),REASON_COST)
end

function s.spfilter(c,e,tp)
	return c:IsCode(10000000) and c:IsCanBeSpecialSummoned(e,0,tp,true,false)
end

function s.thfilter(c)
	return c:IsAbleToHand() and c:IsSetCard(0xfaa) and not c:IsCode(10000000)
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0 
	and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_HAND|LOCATION_DECK,0,1,nil,e,tp) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND|LOCATION_DECK)
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local sc=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_HAND|LOCATION_DECK,0,1,1,nil,e,tp):GetFirst()
	if sc and Duel.SpecialSummon(sc,0,tp,tp,false,false,POS_FACEUP)>0 then
	sc:CompleteProcedure()
	local g2=Duel.GetMatchingGroup(s.thfilter,tp,LOCATION_DECK,0,nil)
		if #g2>0 and Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
		Duel.BreakEffect()
		local sg=g2:Select(tp,1,1,nil)
		Duel.SendtoHand(sg,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,sg)
	end
		sc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
		local ObeliskTGVEffect=EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F --we create a variable for the effect for Obelisk Activation when sent to GV
		local effs={sc:GetCardEffect()}
			if not effs then return false end
			for _, eff in ipairs(effs) do
			if (eff:GetType()&ObeliskTGVEffect)>0 then
				eff:SetCondition(aux.AND(s.obeliskeffcon,eff:GetCondition())) --i dont know how i can explain, but like we remove the condition for the Obelisk to not to send to GV During End Phase
			end
		end
	end
end

function s.obeliskeffcon(e,tp,eg,ep,ev,re,r,rp)
	return not e:GetHandler():HasFlagEffect(id)
end