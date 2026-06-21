--The Winged Dragon of Ra - Deformation Mode
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()

	--Cannot be Normal Summoned/Set
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_SINGLE)
	e0:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e0:SetCode(EFFECT_SPSUMMON_CONDITION)
	c:RegisterEffect(e0)

	--Special Summon itself from hand or Deck
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_SPSUMMON_PROC)
	e3:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e3:SetRange(LOCATION_HAND+LOCATION_DECK)
	e3:SetCondition(s.spcon)
	e3:SetOperation(s.spop)
	e3:SetValue(SUMMON_TYPE_SPECIAL)
	c:RegisterEffect(e3)

	--Summon "The Winged Dragon of Ra" and send "Immortal Phoenix"
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,1))
	e4:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_TOGRAVE)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e4:SetCode(EVENT_TO_GRAVE)
	e4:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DELAY)
	e4:SetCondition(s.rapcon)
	e4:SetTarget(s.raptg)
	e4:SetOperation(s.rapop)
	c:RegisterEffect(e4)
end

--Condition to check "The Winged Dragon of Ra - Sphere Mode" is on the field
function s.filter(c)
	return c:IsFaceup() and c:IsCode(10000080) and c:IsAbleToGraveAsCost()  -- "The Winged Dragon of Ra - Sphere Mode" ID
end

function s.spcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp,c)
	local g=Duel.SelectMatchingCard(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
	Duel.SendtoGrave(g,REASON_COST)
	-- If the card was an opponent's, restrict the attack
	if g:GetFirst():IsControler(1-tp) then
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_CANNOT_ATTACK)
		e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE+EFFECT_FLAG_OATH)
		e1:SetReset(RESET_EVENT+RESET_TOFIELD+RESET_PHASE+PHASE_END)
		c:RegisterEffect(e1)
	end
end

--Condition to check if sent to the GY by opponent's card
function s.rapcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsPreviousControler(tp) and rp==1-tp
		and e:GetHandler():IsReason(REASON_EFFECT+REASON_BATTLE)
end

--Target: Special Summon "The Winged Dragon of Ra" and send "Immortal Phoenix" to the GY
function s.raptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.rafilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,e,tp) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND+LOCATION_DECK)
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,nil,1,tp,LOCATION_DECK)
end

function s.rafilter(c,e,tp)
	return c:IsCode(10000010) and c:IsCanBeSpecialSummoned(e,0,tp,true,true)  -- "The Winged Dragon of Ra" ID
end

function s.phoenixfilter(c)
	return c:IsCode(10000090)  -- "The Winged Dragon of Ra - Immortal Phoenix" ID
end

function s.rapop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.rafilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,1,nil,e,tp)
	local tc=g:GetFirst()
	if tc and Duel.SpecialSummon(tc,0,tp,tp,true,true,POS_FACEUP)~=0 then
		tc:CompleteProcedure()
		Duel.BreakEffect()  -- Ensure this effect happens after the summon
		local phoenix=Duel.SelectMatchingCard(tp,s.phoenixfilter,tp,LOCATION_DECK,0,1,1,nil)
		if phoenix:GetCount()>0 then
			Duel.SendtoGrave(phoenix,REASON_EFFECT)
		end
	end
end
