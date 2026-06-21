--Egyptian God Divine Trinity
local s,id=GetID()

function s.initial_effect(c)
	c:EnableReviveLimit()

	--========================
	-- Contact Fusion Procedure
	--========================
	aux.AddFusionProcMix(c,true,true,10000020,10000010,10000000)
	aux.AddContactFusionProcedure(c,s.contactfilter,LOCATION_MZONE+LOCATION_GRAVE,0,s.contactop)

	--========================
	--SP Summon condition
	--========================

	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_SINGLE)
	e0:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e0:SetCode(EFFECT_SPSUMMON_CONDITION)
	e0:SetValue(s.splimit)
	c:RegisterEffect(e0)

	--========================
	-- Unaffected by other cards' effects
	--========================
	--local e1=Effect.CreateEffect(c)
	--e1:SetType(EFFECT_TYPE_SINGLE)
	--e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	--e1:SetRange(LOCATION_MZONE)
	--e1:SetCode(EFFECT_IMMUNE_EFFECT)
	--e1:SetValue(s.efilter)
	--c:RegisterEffect(e1)

	--========================
	-- Gains 1000 ATK/DEF for each card in hand
	--========================
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_UPDATE_ATTACK)
	e2:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetValue(s.atkdefval)
	c:RegisterEffect(e2)
	local e3=e2:Clone()
	e3:SetCode(EFFECT_UPDATE_DEFENSE)
	c:RegisterEffect(e3)

	--========================
	-- Optional: Destroy all other monsters and burn
	--========================
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,0))
	e4:SetCategory(CATEGORY_DESTROY+CATEGORY_DAMAGE)
	e4:SetType(EFFECT_TYPE_IGNITION)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCountLimit(1)
	e4:SetTarget(s.destg)
	e4:SetOperation(s.desop)
	c:RegisterEffect(e4)

	--========================
	-- Revival on Leaving the Field (Optional, Delayed, with Unique Check)
	--========================
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,1))
	e5:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e5:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e5:SetCode(EVENT_LEAVE_FIELD)
	e5:SetProperty(EFFECT_FLAG_DELAY)
	e5:SetCondition(s.revcon)
	e5:SetTarget(s.revtg)
	e5:SetOperation(s.revop)
	c:RegisterEffect(e5)
end

--========================
-- SP Summon Condition
--========================

function s.splimit(e,se,sp,st)
	return e:GetHandler():GetLocation()~=LOCATION_EXTRA
end

--========================
-- Contact Fusion Helpers
--========================

function s.contactfilter(c)
	return c:IsCode(10000020,10000010,10000000) and c:IsAbleToRemoveAsCost()
end

function s.contactop(g)
	Duel.Remove(g,POS_FACEUP,REASON_COST)
end

--========================
-- Effect Immunity
--========================

function s.efilter(e,te)
	return te:GetOwner()~=e:GetOwner()
end

--========================
-- ATK/DEF Scaling
--========================

function s.atkdefval(e,c)
	return Duel.GetFieldGroupCount(c:GetControler(),LOCATION_HAND,0)*1000
end

--========================
-- Destroy & Burn
--========================

function s.destg(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,e:GetHandler())
	if chk==0 then return #g>0 end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,#g,0,0)
	Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,#g*1000)
end

function s.desop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,e:GetHandler())
	local ct=Duel.Destroy(g,REASON_EFFECT)
	if ct>0 then
		Duel.Damage(1-tp,ct*1000,REASON_EFFECT)
	end
end

--========================
-- Revival Effect
--========================

function s.revcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsPreviousControler(tp)
end

function s.revfilter(c,e,tp)
	return c:IsCode(10000020,10000010,10000000)
		and c:IsCanBeSpecialSummoned(e,0,tp,true,true)
end

function s.revtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<3 then return false end
		local g=Duel.GetMatchingGroup(s.revfilter,tp,LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,nil,e,tp)
		return g:GetClassCount(Card.GetCode)>=3
			and g:IsExists(Card.IsCode,1,nil,10000020) -- Slifer
			and g:IsExists(Card.IsCode,1,nil,10000010) -- Ra
			and g:IsExists(Card.IsCode,1,nil,10000000) -- Obelisk
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,3,tp,LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED)
end

function s.revop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<3 then return end
	local loc=LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED
	local g=Duel.GetMatchingGroup(aux.NecroValleyFilter(s.revfilter),tp,loc,0,nil,e,tp)
	local codes = {10000020, 10000010, 10000000} -- Slifer, Ra, Obelisk

	for _,code in ipairs(codes) do
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then break end
		local sg=g:Filter(Card.IsCode,nil,code)
		local tc=sg:GetFirst()
		if tc then
			Duel.SpecialSummonStep(tc,0,tp,tp,true,true,POS_FACEUP)
		end
	end
	Duel.SpecialSummonComplete()
end

