--Nameless Pharaoh
local s,id=GetID()
function s.initial_effect(c)
	--①: Treated as 3 Tributes for Divine-Beast
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_ADD_EXTRA_TRIBUTE)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetTargetRange(LOCATION_MZONE,0)
	e1:SetValue(s.trival)
	c:RegisterEffect(e1)

	--②: Add or Special Summon Slifer/Obelisk/Ra or support card
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,0))
	e2:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH+CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetCode(EVENT_SUMMON_SUCCESS)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCountLimit(1,id)
	e2:SetTarget(s.effect2tg)
	e2:SetOperation(s.effect2op)
	c:RegisterEffect(e2)
	local e3=e2:Clone()
	e3:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e3)

	--③: Quick Tribute Summon Level 10 ?/4000 DEF monster from hand
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,1))
	e4:SetCategory(CATEGORY_SUMMON)
	e4:SetType(EFFECT_TYPE_QUICK_O)
	e4:SetCode(EVENT_FREE_CHAIN)
	e4:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_MAIN_END)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCountLimit(1,{id,1})
	e4:SetCondition(s.effect3con)
	e4:SetTarget(s.effect3tg)
	e4:SetOperation(s.effect3op)
	c:RegisterEffect(e4)
end

--①: Treated as 3 Tributes for Divine-Beast
function s.trival(e,c)
	return c:IsRace(RACE_DIVINE) and c:IsSummonType(SUMMON_TYPE_ADVANCE) and 3
end

--②: Filter - Egyptian God cards and cards that mention them
function s.egyptian_filter(c)
	return (c:IsCode(10000000,10000010,10000020)
		or c:ListsCode(10000000) or c:ListsCode(10000010) or c:ListsCode(10000020))
end
function s.except_self(c)
	return not c:IsCode(id)
end
function s.hand_ss_filter(c,e,tp)
	return c:IsCode(10000000,10000020) and c:IsCanBeSpecialSummoned(e,0,tp,true,false)
end

function s.effect2tg(e,tp,eg,ep,ev,re,r,rp,chk)
	local can_add = Duel.IsExistingMatchingCard(function(c)
		return s.egyptian_filter(c) and s.except_self(c) and c:IsAbleToHand()
	end,tp,LOCATION_DECK+LOCATION_GRAVE,0,1,nil)
	local can_ss = Duel.IsExistingMatchingCard(s.hand_ss_filter,tp,LOCATION_HAND,0,1,nil,e,tp)
	if chk==0 then return can_add or can_ss end

	local options = {}
	if can_add then table.insert(options,{true,aux.Stringid(id,2),1}) end
	if can_ss then table.insert(options,{true,aux.Stringid(id,3),2}) end
	local choice = Auxiliary.SelectFromOptions(tp,table.unpack(options))
	e:SetLabel(choice)

	if choice==1 then
		Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK+LOCATION_GRAVE)
	elseif choice==2 then
		Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND)
	end
end

function s.effect2op(e,tp,eg,ep,ev,re,r,rp)
	local op=e:GetLabel()
	if op==1 then
		local g=Duel.SelectMatchingCard(tp,function(c)
			return s.egyptian_filter(c) and s.except_self(c) and c:IsAbleToHand()
		end,tp,LOCATION_DECK+LOCATION_GRAVE,0,1,1,nil)
		if #g>0 then
			Duel.SendtoHand(g,nil,REASON_EFFECT)
			Duel.ConfirmCards(1-tp,g)
		end
	elseif op==2 then
		local g=Duel.SelectMatchingCard(tp,s.hand_ss_filter,tp,LOCATION_HAND,0,1,1,nil,e,tp)
		if #g>0 then
			Duel.SpecialSummon(g,0,tp,tp,true,false,POS_FACEUP)
		end
	end
end

--③: Quick Tribute Summon Level 10 ?/4000 DEF monster from hand
function s.effect3con(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsMainPhase()
end
function s.effect3filter(c)
	local def=c:GetDefense()
	return c:IsLevel(10) and (def==4000 or def<0) and c:IsSummonable(true,nil)
end
function s.effect3tg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.effect3filter,tp,LOCATION_HAND,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_SUMMON,nil,1,0,0)
end
function s.effect3op(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SUMMON)
	local g=Duel.SelectMatchingCard(tp,s.effect3filter,tp,LOCATION_HAND,0,1,1,nil)
	local tc=g:GetFirst()
	if tc then
		Duel.Summon(tp,tc,true,nil)
	end
end
