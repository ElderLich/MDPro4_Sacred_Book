--Awakening of the Demon God

local s,id,o=GetID()
function s.initial_effect(c)
 
	aux.AddCodeList(c,130000640)	

	--Activate
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_DECKDES)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCountLimit(1,id+EFFECT_COUNT_CODE_OATH)
	e1:SetTarget(s.target)
	e1:SetOperation(s.activate)
	c:RegisterEffect(e1)

	--spsummon
	local e2=Effect.CreateEffect(c)
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_IGNITION)
	e2:SetRange(LOCATION_GRAVE)
	e2:SetCountLimit(1,id)
	e2:SetCondition(aux.exccon)
	e2:SetCost(s.spcost)
	e2:SetTarget(s.sptg)
	e2:SetOperation(s.spop)
	c:RegisterEffect(e2)
end

function s.filter(c,e,tp)
	if not c:IsCode(130000620) or bit.band(c:GetType(),0x81)~=0x81
		or not c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_RITUAL,tp,false,true) then return false end
	return Duel.IsExistingMatchingCard(s.matfilter1,tp,LOCATION_HAND,0,1,c,tp,c)
end

function s.matfilter1(c,tp,rc)
	return c:IsLevelBelow(7) and c:IsAttribute(ATTRIBUTE_DARK) and c:IsAbleToGrave() and c:IsCanBeRitualMaterial(rc)
		and Duel.IsExistingMatchingCard(s.matfilter2,tp,LOCATION_DECK,0,1,c,c:GetLevel(),c:GetAttribute(),rc)
end

function s.matfilter2(c,lv,att,rc)
	return ((c:IsAttribute(ATTRIBUTE_DARK) and att==ATTRIBUTE_DARK) or (c:IsAttribute(ATTRIBUTE_DARK) and att==ATTRIBUTE_DARK))
		and c:IsLevel(8-lv) and c:IsAbleToGrave() and c:IsCanBeRitualMaterial(rc)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_HAND+LOCATION_GRAVE,0,1,nil,e,tp)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND+LOCATION_GRAVE)
end

function s.check(g)
	return g:GetClassCount(Card.GetLocation)==#g and g:GetSum(Card.GetLevel)==8
end

function s.mfilter(c,rc)
	return c:IsLevelBelow(7) and c:IsAttribute(ATTRIBUTE_DARK) and c:IsAbleToGrave() and c:IsCanBeRitualMaterial(rc)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	::cancel::
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local rg=Duel.SelectMatchingCard(tp,aux.NecroValleyFilter(s.filter),tp,LOCATION_HAND+LOCATION_GRAVE,0,1,1,nil,e,tp)
	local rc=rg:GetFirst()
	if rc then
		local mg=Duel.GetMatchingGroup(s.mfilter,tp,LOCATION_DECK+LOCATION_HAND,0,nil,rc)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
		local mat=mg:SelectSubGroup(tp,s.check,true,2,2)
		if not mat then goto cancel end
		rc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)
		Duel.BreakEffect()
		Duel.SpecialSummon(rc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
		rc:CompleteProcedure()
	end
end

function s.cfilter(c,att)
	return c:IsAttribute(att) and c:IsAbleToRemoveAsCost()
end

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToRemoveAsCost()
		and Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_GRAVE,0,2,nil,ATTRIBUTE_DARK) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local g=Duel.SelectMatchingCard(tp,s.cfilter,tp,LOCATION_GRAVE,0,2,2,nil,ATTRIBUTE_DARK)
	g:AddCard(e:GetHandler())
	Duel.Remove(g,POS_FACEUP,REASON_COST)
end

function s.spfilter(c,e,tp)
	return c:IsCode(130000620) and c:IsType(TYPE_RITUAL) and c:IsCanBeSpecialSummoned(e,0,tp,true,false)
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_HAND,0,1,nil,e,tp) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_HAND,0,1,1,nil,e,tp)
	if g:GetCount()>0 then
		Duel.SpecialSummon(g,0,tp,tp,true,false,POS_FACEUP)
	end
end