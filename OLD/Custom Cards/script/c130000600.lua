--Kurimajin

local s,id,o=GetID()
function s.initial_effect(c)

	aux.AddCodeList(c,130000640)

	--①: Add 1 Dark and 1 Rituall Spell
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_TOHAND)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e1:SetCode(EVENT_ATTACK_ANNOUNCE)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.condition)
	e1:SetCost(s.cost)
	e1:SetTarget(s.target)
	e1:SetOperation(s.operation)
	c:RegisterEffect(e1)

	--②: Ritual Material
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_EXTRA_RITUAL_MATERIAL)
	e2:SetValue(s.mtval)
	c:RegisterEffect(e2)
end

-- Condition: When an opponent's monster declares an attack
function s.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetAttacker():GetControler()~=tp
end

-- Cost: Send this card from hand to the GY
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToGraveAsCost() end
	Duel.SendtoGrave(e:GetHandler(),REASON_COST)
end

-- Filter for Dark monsters (excluding "Kurimajin")
function s.filter(c)
	return c:IsAttribute(ATTRIBUTE_DARK) and not c:IsCode(id) and c:IsAbleToHand()
end

-- Filter for Ritual Spell Cards
function s.thfilter(c)
	return c:IsType(TYPE_RITUAL) and c:IsType(TYPE_SPELL) and c:IsAbleToHand()
end

-- Target: Select 1 Dark monster and 1 Ritual Spell in your GY
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return false end
	if chk==0 then 
		return Duel.IsExistingTarget(s.filter,tp,LOCATION_GRAVE,0,1,nil)
			and Duel.IsExistingTarget(s.thfilter,tp,LOCATION_GRAVE,0,1,nil) 
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g1=Duel.SelectTarget(tp,s.filter,tp,LOCATION_GRAVE,0,1,1,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g2=Duel.SelectTarget(tp,s.thfilter,tp,LOCATION_GRAVE,0,1,1,nil)
	g1:Merge(g2)
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,g1,2,0,0)
end

-- Operation: Add selected cards to hand
function s.operation(e,tp,eg,ep,ev,re,r,rp)
	local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
	if tg then
		local sg=tg:Filter(Card.IsRelateToEffect,nil,e)
		if #sg>0 then
			Duel.SendtoHand(sg,nil,REASON_EFFECT)
		end
	end
end

function s.mtval(e,c)
	return c:IsSetCard(0xfa3)
end